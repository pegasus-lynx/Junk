#ifndef MATRIX_H
#define MATRIX_H


class Matrix {
    private:
        int rows;
        int cols;

        vector<vector<int> > mat;

    public:

        // Constructor
        Matrix(int n);
        Matrix(int r, int c);
        Matrix(int r, int c, int x);

        // Other Functions
        void print();
        void set(int x);
        int getCols();
        int getRows();

        // Operators
        Matrix operator+(const Matrix&);
        Matrix operator-(const Matrix&);
        Matrix operator*(const Matrix&);
        Matrix& operator=(const Matrix&);
        bool operator==(const Matrix&);

        Matrix expo(const Matrix&, int power);        

};

#endif