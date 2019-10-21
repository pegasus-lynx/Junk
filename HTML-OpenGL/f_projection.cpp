#include<GL/glut.h>
#include<bits/stdc++..h>
#include "matrix.h" 

using namespace std;

void init(void)
 {
    glClearColor (1.0, 1.0, 1.0, 1.0);
    // glOrtho(-454.0, 454.0, -250.0, 250.0, -250.0, 250.0); 
     // Set the no. of Co-ordinates along X & Y axes and their gappings
    glEnable(GL_DEPTH_TEST);
 // To Render the surfaces Properly according to their depths
 }

int main(int argc, char **argv){
    
    cout<<"Projections :\n1. Parallel\n2. Perspective\nEnter the choice : "
    int c; cin>>c;

    if(c==1){

    }
    else if(c==2){

    }
    else{
        cout<<"Invalid Choice";
        return 0;
    }

    glutInit(&argc, argv);
    glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH );
    glutWindowSize(2000,2000);
    glutInitWindowPosition(0,0);
    glutCreateWindow("Projections");

    init();

    glutDisplyFunc(display);
    glutMainLoop();

    return 0;
}