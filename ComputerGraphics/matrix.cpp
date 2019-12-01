#include "macros.h"
#include "matrix.h"

using namespace std;

Matrix::Matrix(int n){
    this->rows = n;
    this->cols = n;

    this->mat.resize(n);
    rep(i,0,n) this->mat[i].resize(n);
    
    this->mat.set(0);
}

Matrix::Matrix(int r,int c){
    this->rows = r;
    this->cols = c;

    this->mat.resize(r);
    rep(i,0,r) this->mat[i].resize(c);

    this->mat.set(0);
}

Matrix::Matrix(int r,int c,int x){
    this->Matrix(r,c);
    this->mat.set(x);
}

void Matrix::getCols(){
    return this->cols;
}

vois Matrix::getRows(){
    return this->rows;
}

void Matrix::set(int x){
    rep(i,0,this->rows){
        rep(j,0,this->cols) this->mat[i][j]=x;
    }
}

void Matrix::print(){
    cout<<"Matrix:\n"
    rep(i,0,r){
        rep(j,0,c)  cout<<this->mat[i][j]<<" ";
        cout<<"\n";
    }
}

Matrix Matrix::operator+(const Matrix& sec){
    Matrix res(this->rows, this->cols);
    rep(i,0,this->rows){
        rep(j,0,this->cols){
            res.mat[i][j]=this->val[i][j]+sec.val[i][j];
        }
    }
    return res;
}

Matrix Matrix::operator-(const Matrix& sec){
    Matrix res(this->rows, this->cols);
    rep(i,0,this->rows){
        rep(j,0,this->cols){
            res.mat[i][j]=this->val[i][j]-sec.val[i][j];
        }
    }
    return res;
}

Matrix Matrix::operator*(const Matrix& sec){
    Matrix res(this->rows, sec.getCols());
    
    int r=this->rows;
    int c=sec.cols;
    int p=this->cols;
    rep(i,0,r)
        rep(j,0,c)
            rep(k,0,p) res.mat[i][j] += this->mat[i][k] * sec.mat[k][j];

    return res;
}

Matrix& Matrix::operator=(const Matrix& sec){

    rep(i,0,this->rows){
        rep(j,0,this->cols){
            if(this->mat[i][j] != sec[i][j]) return false;
        }
    }

    return true;
}

class matrix{
public:

    matrix& operator=(const matrix& b){
        val=b.val;
        n=b.n;
        return *this;
    }
    
    matrix mul(int a){
        matrix ans(this->n);
        rep(i,0,this->n){
            rep(j,0,this->n){
                ans.val[i][j]=a*this->val[i][j];
            }
        }
        return ans;
    }
};
matrix::matrix(int x){
    n=x;
    val.resize(x);
    rep(i,0,x){
        val[i].resize(x);
    }
}
matrix matrix::operator+(const matrix& b) const{
    matrix ans(b.n);
    rep(i,0,b.n){
        rep(j,0,b.n){
            ans.val[i][j]=this->val[i][j]+b.val[i][j];
        }
    }
    return ans;
}
matrix matrix::operator-(const matrix& b) const{
    matrix ans(b.n);
    rep(i,0,b.n){
        rep(j,0,b.n){
            ans.val[i][j]=this->val[i][j]-b.val[i][j];
        }
    }
    return ans;
}
matrix matrix::operator*(const matrix& b) const{
    matrix ans(b.n);
    rep(i,0,b.n){
        rep(j,0,b.n){
            rep(k,0,b.n){
                ans.val[i][j]=(ans.val[i][j]+1LL*this->val[i][k]*b.val[k][j])%hell;
            }
        }
    }
    return ans;            
}
matrix identity(int N=2){
    matrix ans(N);
    rep(i,0,N){
        ans.val[i][i]=1;
    }
    return ans;
}
matrix matexpo(matrix a, int n){
    if(n==0){
        return identity(a.n);
    }
    if(n==1) return a;
    matrix x=matexpo(a,n/2);
    matrix r=x*x;
    if(n&1) r=r*a;
    return r;
}
void solve(){
    int n,k;
    cin>>n>>k;
    matrix mat(n);
    rep(i,0,n){
        rep(j,0,n){
            cin>>mat.val[i][j];
        }
    }
    