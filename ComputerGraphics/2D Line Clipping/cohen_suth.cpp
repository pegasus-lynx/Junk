#include<bits/stdc++.h>
#include<GL/glut.h>

using namespace std;

float x_min, y_min, x_max, y_max;
float ex1, ex2, ey1, ey2;

int getCode(float x, float y){
    int c=0;
    if(x < x_min) c |= 1;
    if(x > x_max) c |= 2;
    if(y < y_min) c |= 4;
    if(y > y_max) c |= 8;
    return c;
}

void display();

void keyPress(unsigned char key, int x, int y){
    switch(key){
        case 'c':
            break;
        case 'l':
            cout<<"Enter the line coordinates (ex1,ey1,ex2,ey2) : ";
            cin>>ex1>>ey1>>ex2>>ey2;
            glutPostRedisplay();
            break;
        case 'w':
            cout<<"Enter the clipping window dimensions ( x_min, y_min, x_max, y_max ) : ";
            cin>>x_min>>y_min>>x_max>>y_max;
            glutPostRedisplay();
            break;
    }
}

void cohenLine(float x1, float y1, float x2, float y2){

    int c1,c2;
    c1 = getCode(x1,y1);
    c2 = getCode(x2,y2);

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
       y=y_max;
       x=xi+ 1.0/m*(y_max-yi);
    }
    else
      if((c & 4)>0) {
          y=y_min;
          x=xi+1.0/m*(y_min-yi);
      }
      else
       if((c & 2)>0) {
           x=x_max;
           y=yi+m*(x_max-xi);
       }
       else
       if((c & 1)>0) {
           x=x_min;
           y=yi+m*(x_min-xi);
       }

       if(c==c1) {
           ex1=x;
           ey1=y;
           c1=getCode(ex1,ey1);
       }

       if(c==c2) {
           ex2=x;
           ey2=y;
           c2=getCode(ex2,ey2);
       }
}

 display();
}

void plotClipWindow(){
    glColor3f(0.0,0.0,1.0);
    glBegin(GL_LINE_LOOP);
        glVertex2i(x_min,y_min);
        glVertex2i(x_min,y_max);
        glVertex2i(x_max,y_max);
        glVertex2i(x_max,y_min);
    glEnd();
}

void plotLine(){
    glColor3f(1.0,0.0,0.0);
    glBegin(GL_LINES);
        glVertex2i(ex1,ey1);
        glVertex2i(ex2,ey2);
    glEnd();    
}

void display(){
    glClear(GL_COLOR_BUFFER_BIT);
    plotClipWindow();
    plotLine();
    glFlush();
}

void init() {
    glClearColor(1.0,1.0,1.0,1.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(-300,300,-300,300);    
}

void createWin(int argc,char** argv, char* name,int mode, int x, int y, int h,int w){
    glutInit(&argc,argv);
    glutInitDisplayMode(mode);
    glutInitWindowSize(w,h);
    glutInitWindowPosition(x,y);
    glutCreateWindow(name);
}

int main(int argc,char** argv) {

    cout<<"Enter the clipping window dimensions ( x_min, y_min, x_max, y_max ) : ";
    cin>>x_min>>y_min>>x_max>>y_max;

    cout<<"Enter the line coordinates (ex1,ey1,ex2,ey2) : ";
    cin>>ex1>>ey1>>ex2>>ey2;

    // Creating Window 
    int mode = GLUT_SINGLE|GLUT_RGB;
    createWin(argc,argv,"Line Clipping", mode, 100, 100, 500, 500);

    // Specifying Display and KeyBoard Callbacks
    glutDisplayFunc(display);
    glutKeyboardFunc(keyPress);

    // Initializing and Entering Main Loop
    init();
    glutMainLoop();

    return 0;
}