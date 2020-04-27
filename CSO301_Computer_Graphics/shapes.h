#ifndef SHAPES_H
#define SHAPES_H

class Point{
    private:
        pair<int> pos;

    public:
        pair<int> getPos();
        int getX();
        int getY();

        void plot();

}

class Line{
    private:
        Point stPoint, endPoint;
};

class Arc{
    private:
        Point stPoint, endPoint;
}

class Circle{
    private:
        Point center;
        double radius;
};

class Polygon{
    private:
        int n_vt;
        vector<Point> vertices;
};

class Triangle : public Polygon {
    
};

class Isoceles : public Triangle{

};

class Equilateral : public Triangle{

};

class Quadrilateral : public Polygon {

};

class Parallelogram : public Quadrilateral {

};

class Rhombus : public Parallelogram {

};

class Trapezium : public Quadrilateral {

};

class Rectangle : public Parallelogram {

};

#endif