#include "macros.h"
#include "glutil.h"
#include "glshape.h"

// void help(){
//     cout<<"Commands :\n"
//     cout<<"\t"<<"help : Lists all the command in this program\n";
//     cout<<"\t"<<"new `line_name` [coordinates ( xa, ya, xb, yb )] ( line --new a 1.2 1.3 6.7 9.9 ) :  Creates a line instance \n";
//     cout<<"\t"<<"use `line_name` `algo_code` [ 1-Parametric, 2-DDA, 3-Bresenham ] : Chooses which algo to use for line generation\n"
//     cout<<"\t"<<"plot `line_name` : Lists all the command in this program\n";
//     cout<<"\t"<<"clear : Clears the window\n"
// }

// void parse(string inp){

// }

Line l;

void DDALine(){
    
    Point d(l.endPoint.X - l.stPoint.X, l.endPoint.Y - l.stPoint.Y);
    int steps = max(d.X,d.Y);
    Point temp = l.stPoint;

    // Steps == 0
    if(steps == 0){
        temp.X = l.stPoint.X;
        temp.Y = l.stPoint.Y;
        temp.plot();
        return ;
    }

    // Line Parallel to x-axis
    if(d.X==0){
        temp.Y = min(l.stPoint.Y, l.endPoint.Y);
        rep(i,0,steps){
            temp.plot();
            temp.Y+=1;
        }

        return ;
    }

    // Line Parallel to y-axis
    if(d.Y==0){
        temp.X = min(l.stPoint.X, l.endPoint.X);
        rep(i,0,steps){
            temp.plot();
            temp.X+=1;
        }

        return ;
    }

    if(steps == d.X){
        temp = (l.stPoint.X<l.endPoint.X?l.stPoint:l.endPoint);
        d.Y = ((double)d.Y)/steps;
        d.X = 1;

        rep(i,0,steps){
            temp.plot();
            temp.Y += d.Y; 
        }
    }
    else{
        temp = (l.stPoint.Y<l.endPoint.Y?l.stPoint:l.endPoint);
        d.X = ((double)d.X)/steps;
        d.Y = 1;

        rep(i,0,steps){
            temp.plot();
            temp.X += d.X; 
        }
    }
}

void BresenhamLine(){
    Point abs_d(abs(l.endPoint.X - l.stPoint.X), abs(l.endPoint.Y - l.stPoint.Y));
    Point d(l.endPoint.X - l.stPoint.X, l.endPoint.Y - l.stPoint.Y);

    if(abs_d.X >= abs_d.Y){
    
        int p = 2*abs_d.Y-abs_d.X;
        int dy2 = 2*abs_d.Y;
        int dydx2 = 2 * (abs_d.Y - abs_d.X);
        int x,y,xEnd;

        if(l.stPoint.X > l.endPoint.X){
            x = l.endPoint.X;
            y = l.endPoint.Y;
            xEnd = l.stPoint.X;
        }
        else{
            x = l.stPoint.X;
            y = l.stPoint.Y;
            xEnd = l.endPoint.X;
        }

        Point temp(x,y);
        
        temp.plot();
        
        while(temp.X<xEnd){
            temp.X++;
            if(p<0){
                p += dy2;
            }    
            else{
                temp.Y++;
                p += dydx2;
            }
            temp.plot();
        }
    }

}

void displayMode(int mode) {
    glClear(GL_COLOR_BUFFER_BIT);
    switch(mode){
        case 1:
            glutDisplayFunc(DDALineFunc);
            break;
        case 2:
            glutDisplayFunc(BresenhamLineFunc);
            break;
    }
    glFlush();
}

int main(int argc, char** argv){
    cout<<"Line Generation Algorithms :\n";

    cout<<"Enter the coordinates : ";
    cin>>l.stPoint.X>>l.stPoint.Y>>l.endPoint.X>>l.endPoint.Y;

    int mode;
    cout<<"Enter the algorithm to be used [ 1. DDA Line, 2. Bresenham Line] : ";
    cin>>mode;

    initGL();
    createWin(argc,argv,"Line", GLUT_SINGLE | GLUT_RGB, 100, 100, 500, 500);
    
    displayMode(mode);
    glutMainLoop();

    return 0;
}