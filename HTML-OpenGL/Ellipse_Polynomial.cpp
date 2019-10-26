#include<bits/stdc++.h>
#include<GL/glut.h>
using namespace std;
// $ g++ gl.cpp -o gl -lGL -lGLU -lglut- To compile //
int h,k;
float a,b;
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

void polynomial()
{
    glClear(GL_COLOR_BUFFER_BIT);
	setPixel(h,k);
	for(int i=0 ; i<=a ; i+=1)
	{ 
		float J = sqrt(1 - (i*i)/(a*a))*b;
		int j = (int)(J);
		setPixel(h+i,k+j);
		setPixel(h-i,k+j);
		setPixel(h-i,k-j);
		setPixel(h+i,k-j);
	}
    glFlush();
}
int main(int argc,char ** argv)
{
    cout<<"Enter the center of ellipse :\n";
    cin>>h>>k;
    cout<<"Enter the parameters a & b:\n";
    cin>>a>>b;
    glutInit(&argc, argv);
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize (500,500);
    glutInitWindowPosition (100, 150);
    glutCreateWindow ("Ellipse : Polynomial Method ");
    Init();
    glutDisplayFunc(polynomial);
    glutMainLoop();
    return 0;
}
