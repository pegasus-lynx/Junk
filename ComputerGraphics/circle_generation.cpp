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

Circle c;
Point oct[8];

void plotOct(Point& p){
    oct[0].X = c.center.X + p.X, oct[0].Y = c.center.Y + p.Y;
    oct[1].X = c.center.X + p.Y, oct[1].Y = c.center.Y + p.X;
    oct[2].X = c.center.X + p.X, oct[2].Y = c.center.Y - p.Y;
    oct[3].X = c.center.X + p.Y, oct[3].Y = c.center.Y - p.X;
    oct[4].X = c.center.X - p.X, oct[4].Y = c.center.Y + p.Y;
    oct[5].X = c.center.X - p.Y, oct[5].Y = c.center.Y + p.X;
    oct[6].X = c.center.X - p.X, oct[6].Y = c.center.Y - p.Y;
    oct[7].X = c.center.X - p.Y, oct[7].Y = c.center.Y - p.X;

    rep(i,0,8) oct[i].plot();
}

void CirclePolynomial(){
    Point tu(c.center.X - c.radius, c.center.Y);
    Point tl(c.center.X - c.radius, c.center.Y);

    tu.plot();
    tl.plot();

    rep(i, c.center.X-c.radius, c.center.X+c.radius){
        tl.X = tu.X = tl.X+1;
        tu.Y += sqrt(pow(c.radius,2) - pow(tu.X,2));
        tl.Y -= sqrt(pow(c.radius,2) - pow(tl.X,2));
        tl.plot();
        tu.plot();
    }
}

void CircleBresenham(){
    Point temp(0,c.radius);
    int d = 3 - 2*c.radius;
    while(temp.X<=temp.Y){
        plotOct(temp);
        if(d<0){
            d += 4*temp.X + 6;
        }
        else{
            d += 4*(temp.X-temp.Y) + 10;
            temp.Y--;
        }
        temp.X++;
    }
}

void CircleMidPoint(){
    Point temp(0,c.radius);
    plotOct();
    
    int p = (double)5/4 - c.radius;
    
    while(temp.X<temp.Y){
        temp.X++;
        if(p<0){
            p += 2*temp.X + 1;
        }
        else{
            temp.Y--;
            p += 2*(temp.X-temp.Y)+1;
        }
        plotOct();
    }
}

void CircleParametric(){
    double theta = 0;
    double del = 0.01;

    Point temp(c.center.X + c.radius*cos(theta),c.center.Y + c.radius*sin(theta));

    while(theta<2*PI){
        temp.plot();
        theta += delta;
        temp.X = c.center.X + c.radius*cos(theta);
        temp.Y = c.center.Y + c.radius*sin(theta);
    }
}

void displayMode(int mode) {
    glClear(GL_COLOR_BUFFER_BIT);
    switch(mode){
        case 1:
            glutDisplayFunc(CircleParametric);
            break;
        case 2:
            glutDisplayFunc(CircleBresenham);
            break;
        case 3:
            glutDisplayFunc(CircleMidPoint);
            break;
        case 4:
            glutDisplayFunc(CirclePolynomial);
            break;
    }
    glFlush();
}

int main(int argc, char** argv){
    cout<<"Circle Generation Algorithms :\n";

    cout<<"Enter the center of the circle : ";
    cin>>c.center.X>>c.center.Y;

    int mode;
    cout<<"Enter the algorithm to be used [ 1. Parametric, 2. Bresenham, 3. Mid Point, 4. Polynomial] : ";
    cin>>mode;

    initGL();
    createWin(argc,argv,"Line", GLUT_SINGLE | GLUT_RGB, 100, 100, 500, 500);
    
    displayMode(mode);
    glutMainLoop();

    return 0;
}