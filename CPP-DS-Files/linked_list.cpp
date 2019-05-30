#include<bits/stdc++.h>

using namespace std;

// This is a simple implementation of Linked List (int) data structure through class.

class Node {
    private:
        int data;
        Node* next;

    public:
    // Constructors
        Node() {
            data = INT_MIN;
            next = NULL;    
        }

        Node(int x) {
            data = x;
            next = NULL;
        }

        // Copy constructor
        Node(Node &n){
            this->data = n.getData();
            this->next = n.getNext();
        } 

    // Data access ans setter methods
        int getData() {
            return data;
        }

        bool checkData(int x) {
            return x==data;
        }

        Node* getNext(){
            return next;
        }

        bool isEnd(){
            if(next==NULL) return true;
            return false;
        }

        void setData(int x){
            data = x;
        }

        void setNext(Node* ptr){
            next = ptr;
        }

    // Other
        void print(){
            cout<<data;
        }

};

class LinkedList {
    private:
        Node* head;

    public:
        void insertFront(int data) {
            Node* c = new Node(data);
            c->setNext(head);
            head = c;
        }

        void insertEnd(int data) {
            Node* c=head;
            while(c->getNext()!=NULL) c = c->getNext();
            Node* n = new Node(data);
            c->setNext(n);
        }

        void insertAfter(Node* p,int data) {
            Node* c = new Node(data);
            c->setNext(p->getNext());
            p->setNext(c);
        }

        void remFirstValue(int data) {
            Node *c=head,*p=NULL;
            while(!c->checkData(data) && !c->isEnd()){
                p = c; 
                c = c->getNext();
            }
            if(c->checkData(data)){
                if(c==head)
                    head = c->getNext();
                else 
                    p->setNext(c->getNext());

                free(c);
                return ;
            }
        }

        void remAllValue(int data) {
            Node *c=head,*p;
            while(!c->isEnd()){
                if(c->checkData(data)){
                    if(c==head)
                        head = c->getNext();
                    else
                        p->setNext(c->getNext());
                    free(c);
                    c=p;
                }
                c = c->getNext();
            }
            if(c->checkData(data)){
                if(c==head){
                    head = NULL;
                }
                else{
                    p->setNext(NULL);
                }
                free(c);
            }
        }

        void remPosition(int pos) {
            Node *c=head,*p;
            int k=0;
            while(k<pos){
                p=c;
                c=c->getNext();
            }
            p->setNext(c->getNext());
            free(c);
        }

        int  length() {
            int l=0;
            Node* c=head;
            if(c=NULL) return 0;
            while(!c->isEnd()){
                l++;
                c = c->getNext();
            } 
            return l+1;
        }
        
        bool search(int data) {
            Node* c=head;
            
            if(c==NULL) return false;

            while(!c->isEnd()){
                if(c->checkData(data)) return true;
            }
            if(c->checkData(data)) return true;

            return false;
        }

        int  getNth(int n) {
            Node* c=head;
            int k=1;
            while(k<n){
                k++;
                c=c->getNext();
            }
            return c.getData();
        }

        int  freqOfValue(int data) {
            int freq=0;
            Node* c=head;
            while(!c->isEnd()){
                if(c->checkData(data)) freq++;
                c=c->getNext();
            }
            if(c->checkData(data)) freq++;
            return freq;
        }

        void reverse() {
            Node* c=head,*p=NULL,*t;
            while(!c->isEnd()){
                t=c->getNext();
                c->setNext(p);
                p=c;
                c=t;
            }
            c->setNext(p);
            head = c;
        }
        
        void sortQuick() {}

        // Others :: 
        bool isLoop() {return 0;}

};


int main(){
    LinkedList l;
    l.insertFront(2);
    l.insertFront(3);
    return 0;
}