#include<bits/stdc++.h>
#include<GL/glut.h>
using namespace std;
// $ g++ gl.cpp -o gl -lGL -lGLU -lglut- To compile //
int xc,yc,x,y,r;
void setPixel(int x,int y)
{
    glBegin(GL_POINTS);
    glVertex2i(x,y);
    glEnd();
}
void Init()
{
    glClearColor(1.0,1.0,1.0,0); //clear color-black
    glColor3f(0.0,0.0,0.0); //fill color-white
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(0 , 500 , 0 , 500);
}
void circlePlotPoints()
{
    setPixel(xc+x,yc+y);
    setPixel(xc+x,yc-y);
    setPixel(xc+y,yc-x);
    setPixel(xc-y,yc-x);
    setPixel(xc-x,yc-y);
    setPixel(xc-x,yc+y);
    setPixel(xc-y,yc+x);
    setPixel(xc+y,yc+x);
}
void bresenham()
{
    glClear (GL_COLOR_BUFFER_BIT);
    x = 0;
    y = r;
    int d = 3 - 2*r;
    while(x<=y)
    {
        // setPixel(x,y);
        circlePlotPoints();
        if(d<0)
            d += 4*x + 6;
        else
        {
            d += 4*(x-y) + 10;
            y--;
        }
        x++;
    }
    glFlush();
}
int main(int argc,char ** argv)
{
    cout<<"Enter the center of circle :\n";
    cin>>xc>>yc;
    cout<<"Enter the radius of circle :\n";
    cin>>r;
    glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize (500, 500);
    glutInitWindowPosition (700, 700);
    glutCreateWindow ("Bresenham's method for circle generation");
    Init();
    glutDisplayFunc(bresenham);
    glutMainLoop();
    return 0;
}
