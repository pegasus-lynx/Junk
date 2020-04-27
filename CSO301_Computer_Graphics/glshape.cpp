#include "macros.h"
#include "glshape.h"
#include <GL/glut.h>

using namespace std;

Color::Color(){
    r = g = b = 0;
    a = 1;
}

Color::Color(float red,float green,float blue,float alpha=1.0){
    r = red; g = green; b = blue; a = alpha;
}

void Primitive::setCol(Color color){
    this->color = color;
}

void Primitive::setCol(float red,float green,float blue,float alpha=1.0){
    this->color.r = red; 
    this->color.g = green; 
    this->color.b = blue; 
    this->color.a = alpha; 
}

float* Color::vec(){
    float colorVars[4];
    colorVars[0] = r;
    colorVars[1] = g;
    colorVars[2] = b;
    colorVars[3] = a;
    return colorVars;
}

Point::Point(){
    pos = {0.0,0.0};
    color = Color();
}

Point::Point(double x,double y){
    pos = {x,y};
    color = Color();
}

double* Point::getPos(){
    double position[2] = {this->pos.first, this->pos.second};
    return position;
}

void Point::plot(){
    glColor4d(color.r,color.g,color.b,color.a);
    glBegin(GL_POINTS);
        glVertex2d(pos.first, pos.second);
    glEnd();
}

Line::Line(){
    stPoint = Point();
    endPoint = Point(); 
    color = Color();  
}

Line::Line(Point&a , Point&b ){
    stPoint = a;
    endPoint = b;
    color = Color();  
}

Line::Line(double xa,double ya,double xb,double yb){
    stPoint = Point(xa,ya);
    endPoint = Point(xb,yb);
    color = Color();  
}

void Line::plot(){
    glColor4d(color.r,color.g,color.b,color.a);
    glBegin(GL_LINE);
        glVertex2d(stPoint.pos.X,stPoint.pos.Y);
        glVertex2d(endPoint.pos.X,endPoint.pos.Y);
    glEnd();
}

Circle::Circle(){
    center = Point();
    radius = 0;
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

Circle::Circle(double rad, double xc, double yc){
    center = Point(xc,yc);
    radius = rad;
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

Circle::Circle(double rad, Point& center){
    this->center = center;
    radius = rad;
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

//  Complete plot circle function
void Circle::plot(){
    glColor4d(color.r,color.g,color.b,color.a);
    // glBegin(GL_CIR)
}

Polygon::Polygon(){
    n_vt = 0;
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

Polygon::Polygon(int n){
    n_vt = n;
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

Polygon::Polygon(vector<Point>& pts){
    n_vt = pts.size();
    vertices = pts;
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

Polygon::Polygon(vector<pair<double, double> >& vec){
    n_vt = vec.size();
    rep(i,0,n_vt) vertices.pb(Point(vec[i].X, vec[i].Y));
    color = Color();
    fillColor = Color(0.7,0.7,0.7);
}

void Polygon::plot(){
    glColor4d(color.r,color.g,color.b,color.a);
    glBegin(GL_LINE_LOOP);
        rep(i,0,vertices.size()){
            glVertex2d(vertices[i].pos.X,vertices[i].pos.Y);
        }
    glEnd();
}
