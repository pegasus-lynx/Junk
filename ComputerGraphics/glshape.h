#ifndef GLSHAPE_H
#define GLSHAPE_H



// Structs to hold informations about the primitives :
class Color{
    public:
        float r, g, b, a;

        Color();
        Color(float red,float green,float blue,float alpha=1.0);
        float* vec();
};

class Primitive{
    public:
        Color color;

        void setCol(Color color);
        void setCol(float red,float green,float blue,float alpha=1.0);

        void plot();
};

class Closed : public Primitive{
    public:
        Color fillColor;

        void setFillCol(Color color);
        void setFillCol(float red,float green,float blue,float alpha=1.0);
        void plot();
};

class Point : public Primitive{
    public:
        pair<double,double> pos;

        Point();
        Point(double x,double y);
        double* getPos();
        void plot();
};

class Line : public Primitive{
    public:
        Point stPoint, endPoint;

        Line();
        Line(Point& a, Point& b);
        Line(double xa,double ya,double xb,double yb);
        void plot();
        
};

class Circle : public Closed{
    public:
        Point center;
        double radius;

        Circle();
        Circle(double rad, double xc, double yc);
        Circle(double rad, Point& center);
        void plot();
};

class Polygon : public Closed{
    public:
        int n_vt;
        vector<Point> vertices;

        Polygon();
        Polygon(int n);
        Polygon(vector<Point>& pts);
        Polygon(vector<pair<double, double> >& vec);
        void plot();
};

#endif