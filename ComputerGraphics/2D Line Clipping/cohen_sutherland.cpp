#include<bits/stdc++.h>
#include<GL/glut.h>

void display();
using namespace std;

float xmin,ymin,xmax,ymax;
float xd1,yd1,xd2,yd2;

int code(float x,float y) {
    int c=0;
    if(y>ymax)c=8;
    if(y<ymin)c=4;
    if(x>xmax)c=c|2;
    if(x<xmin)c=c|1;
    return c;
}

void cohen_Line(float x1,float y1,float x2,float y2) {
    int c1=code(x1,y1);
    int c2=code(x2,y2);
    float m=(y2-y1)/(x2-x1);
    while((c1|c2)>0) {
        if((c1 & c2)>0) {
           exit(0);
        }

    float xi=x1;float yi=y1;
    int c=c1;
    if(c==0) {
         c=c2;
         xi=x2;
         yi=y2;
    }
    float x,y;
    if((c & 8)>0) {
       y=ymax;
       x=xi+ 1.0/m*(ymax-yi);
    }
    else
      if((c & 4)>0) {
          y=ymin;
          x=xi+1.0/m*(ymin-yi);
      }
      else
       if((c & 2)>0) {
           x=xmax;
           y=yi+m*(xmax-xi);
       }
       else
       if((c & 1)>0) {
           x=xmin;
           y=yi+m*(xmin-xi);
       }

       if(c==c1) {
           xd1=x;
           yd1=y;
           c1=code(xd1,yd1);
       }

       if(c==c2) {
           xd2=x;
           yd2=y;
           c2=code(xd2,yd2);
       }
}

 display();
}

void mykey(unsigned char key,int x,int y)
{
    if(key=='c') {  
        cohen_Line(xd1,yd1,xd2,yd2);
        glFlush();
    }
}

void plotClipWindow(){
    glColor3f(0.0,0.0,1.0);
    glBegin(GL_LINE_LOOP);
    glVertex2i(xmin,ymin);
    glVertex2i(xmin,ymax);
    glVertex2i(xmax,ymax);
    glVertex2i(xmax,ymin);
    glEnd();
}

void display() {

    glClear(GL_COLOR_BUFFER_BIT);
    
    plotClipWindow();

    glColor3f(1.0,0.0,0.0);
    glBegin(GL_LINES);
    glVertex2i(xd1,yd1);
    glVertex2i(xd2,yd2);
    glEnd();
    glFlush();
}

void init() {
    glClearColor(1.0,1.0,1.0,1.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(-300,300,-300,300);
}

void createWin(int argc,char** argv, string name,int mode, int x, int y, int h,int w){
    glutInit(&argc,argv);
    glutInitDisplayMode(mode);
    glutInitWindowSize(w,h);
    glutInitWindowPosition(x,y);
    glutCreateWindow(name);
}


int main(int argc,char** argv) {

    cout<<"Enter the clipping window dimensions ( x_min, y_min, x_max, y_max ) : ";
    cin>>xmin>>ymin>>xmax>>ymax;

    // Creating Window 
    int mode = GLUT_SINGLE|GLUT_RGB;
    createWin(argc,argv,"Line Clipping", mode, 100, 100, 500, 500);

    // Specifying Display and KeyBoard Callbacks
    glutDisplayFunc(display);
    glutKeyboardFunc(mykey);

    // Initializing and Entering Main Loop
    init();
    glutMainLoop();

    return 0;
}