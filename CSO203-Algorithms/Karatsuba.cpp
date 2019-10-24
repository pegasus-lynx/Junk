#include <iostream>
#include <string>
using namespace std;

class Multiply
{
    public:
        string p,q;
        void initialise(string p,string q)
        {
            this->p=p;
            this->q=q;
        }
        
        int sameLength(string &x, string &y)
        {
            int l1=x.length();
            int l2=y.length();
            string tm="";
            if(l1<l2)
            {
                while(l1!=l2)
                {
                    tm=tm+'0';
                    l1++;
                }
            }
            x = tm+x;
            tm="";
            while(l1!=l2)
            {
                tm=tm+'0';
                l2++;
            }
            y=tm+y;
            return(l1);
        }
        
        string binarySum(string x,string y)
        {
            string s;
            int n=sameLength(x,y);
            int c=0,f,m;
            string tm="";
            while(n--)
            {
                f=(x[n]-'0');
                m=(y[n]-'0');
                s=char((f^m^c)+'0')+s;
                c=(f&m || m&c || c&f);
            }
            if(c)
                s='1'+s;
            return(s);
        }
        
        int binaryMultiply(string x,string y)
        {
            int n = sameLength(x, y); 
            if (n == 0) return 0; 
            if (n == 1) return ((x[0]-'0')*(y[0]-'0')); 
  
            int fh = n/2;    
            int sh = (n-fh); 
  
            string xl = x.substr(0, fh); 
            string xr = x.substr(fh, sh);
  
            string yl = y.substr(0, fh); 
            string yr = y.substr(fh, sh); 
  
            int P1 = binaryMultiply(xl, yl); 
            int P2 = binaryMultiply(xr, yr); 
            int P3 = binaryMultiply(binarySum(xl, xr), binarySum(yl, yr)); 
  
            return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2; 
        }
};

int main()
{
    Multiply obj;    // Declaring class obj
    string s1,s2;
    cout<<"Enter 1st Binary Number : ";
    cin>>s1;
    cout<<"Enter 2nd Binary Number : ";
    cin>>s2;
    cout<<"Multiplied Result (in Decimal) : ";
    obj.initialise(s1,s2);
    cout<<obj.binaryMultiply(obj.p,obj.q);    // Calling the function 
}
