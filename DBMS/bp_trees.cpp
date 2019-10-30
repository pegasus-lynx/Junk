#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define endl "\n";
#define all(a) (a).begin(),(a).end()
#define lb lower_bound
#define bs binary_search

using namespace std;

class Node {
    public:
        bool leaf;
        int n;
        vector<int> data;
        vector<Node*> ptrs;

        Node(int order, bool isLeaf){
            leaf = isLeaf;
            n = order;
        }

        void add(int x,Node* p){
            int pos = lb(all(data),x)-data.begin();

            data.pb(x);
            ptrs.pb(p);

            int t;
            Node* temp;

            rep(i,pos,data.size()){
                t = data[i];
                data[i] = x;
                x = t;
            }

            rep(i,pos+1,ptrs.size()){
                temp = ptrs[i];
                ptrs[i] = p;
                p = temp;
            }

        }

        void print(){
            cout<<"isLeaf : "<<leaf<<endl;
            cout<<"Data : ";
            rep(i,0,data.size()) cout<<data[i]<<" ";
            cout<<endl;
            cout<<"Pointers : ";
            rep(i,0,ptrs.size()) cout<<ptrs[i]<<" ";
            cout<<endl;
        }
};

class BPTree {
    public:
        Node* root;

        void insert(int x){
            Node* chd;
            if(search(x)) return ;
            int key = _insert(x,root,chd);
            if(key != INT_MIN){
                Node* nrt = new Node(root->n,false);
                nrt->data.pb(key);
                nrt->ptrs.pb(root);
                nrt->ptrs.pb(chd);
                root = nrt;
            }
        }

        void remove(int x){
            if(!search(x)) return ;

            Node* chd;
            _remove(x,root,chd);
        }

        bool search(int x){
            Node* cur = root;
            while(!cur->leaf){
                int p = lb(all(cur->data),x) - cur->data.begin();
                cur = cur->ptrs[p];
            }
            return bs(all(cur->data),x);
        }

        void display(Node* ptr){
            ptr->print();
            if(ptr->leaf) return;
            rep(i,0,ptr->ptrs.size()){
                if(ptr->ptrs[i]!=NULL) display(ptr->ptrs[i]);
            }
        }

    private:
        void _remove(int x,Node* cur,Node* par){

            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;

            if(cur->leaf){
                int p = find(all(cd),x)-cd.begin();
                cd.erase(cd.begin()+p);
                cp.erase(cp.begin()+p);


                int k=INT_MIN;
                if(cd.size()<((cur->n + 2)/2)-1){
                    k = _redistribute(cur,par);
                    if(k == INT_MIN ) _merge(cur,par,k);
                }
                return;
            }

            int p = lb(all(cd),x)-cd.begin();
            _remove(x,cp[p],cur);            

            int key=INT_MIN;
            if(cd.size()<((cur->n + 2)/2)-1){
                key = _redistribute(cur,par);
                if(key == INT_MIN) _merge(cur,pak,key);
            }

        }

        int _redistribute(Node* cur,Node* par){
            
            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;
            vector<int>& pd = par->data;
            vector<Node*>& pp = par->ptrs;

            int p = find(all(pp),cur)-pp.begin();
            int key;
            Node* ss;

            // Try with left child
            ss = (p>0?pp[p-1]:NULL);
            if(ss!=NULL){
                
                vector<int>& sd = ss->data;
                vector<Node*>& sp = ss->ptrs;

                if(sd.size()+cd.size()>=2*(((cur->n + 2)/2)-1)){
                    vector<int> temp;
                    rep(i,0,sd.size()) temp.pb(sd[i]);
                    rep(i,0,cd.size()) temp.pb(cd[i]);

                    sd.clear();
                    cd.clear();

                    int mid = (temp.size()+1)/2;
                    rep(i,0,mid+1) sd.pb(temp[i]);
                    rep(i,mid+1,temp.size()) cd.pb(temp[i]);

                    key = temp[mid+1];

                    pd[p-1] = key;
                }

                return key;
            }

            // Try with right child
            ss = (p<pp.size()-1?pp[p+1]:NULL);
            if(ss!=NULL){
                
                vector<int>& sd = ss->data;
                vector<Node*>& sp = ss->ptrs;

                if(sd.size()+cd.size()>=2*(((cur->n + 2)/2)-1)){
                    vector<int> temp;
                    rep(i,0,cd.size()) temp.pb(cd[i]);
                    rep(i,0,sd.size()) temp.pb(sd[i]);

                    sd.clear();
                    cd.clear();

                    int mid = (temp.size()+1)/2;
                    rep(i,0,mid+1) cd.pb(temp[i]);
                    rep(i,mid+1,temp.size()) cs.pb(temp[i]);

                    key = temp[mid+1];

                    pd[p+1] = key;
                }

                return key;
            }

            return INT_MIN;
        }

        int _merge(Node* cur, Node* par){
            
            int p = find(all(pp),cur)-pp.begin();
            int key;
            Node* ss = (p>0?pp[p-1]:NULL);
            if(ss == NULL) return INT_MIN;


        }

        int _insert(int x,Node * cur, Node* &chd){

            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;

            if(cur->leaf){
                if(cp.size()<cur->n){
                    cur->add(x,NULL);
                    return INT_MIN;
                }
                return _split_add(x,NULL,cur,chd);
            }

            int key = INT_MIN;
            Node* temp = NULL;

            int p = lb(all(cd),x)-cd.begin();
            key = _insert(x,cp[p],temp);

            if(key!=INT_MIN){
                if(cp.size()<cur->n){
                    cur->add(key,temp);
                    return INT_MIN;
                }
                return _split_add(key,temp,cur,chd);
            }

            return INT_MIN;
        }

        int _split_add(int x,Node* ptr,Node* cur, Node* &chd){
            
            Node* node = new Node(cur->n,true);
            cur->add(x,ptr);

            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;
            vector<int>& nd = node->data;
            vector<Node*>& np = node->ptrs;

            int pos = cd.size()/2;
            int key = cd[pos];

            rep( i,pos+(cur->leaf?0:1),cd.size()) nd.pb(cd[i]);

            rep( i,pos+(cur->leaf?0:1),cp.size()) np.pb(cp[i]);

            cd.erase(cd.begin()+pos,cd.end());
            cp.erase(cp.begin()+pos+(cur->leaf?0:1), cp.end());

            chd=node;
            return key;
        }
};

int main(){
        

    // Input order of the tree :
    // ( Here order is equal to the number of the keys stored in the node and not the same as the convention )
    int n;
    cout<<"Enter the order of the tree : ";
    cin>>n;

    // Tree Initialization --------------------
    Node* rt = new Node(n,true);
    rt->ptrs.pb(NULL);
    
    BPTree* tree = new BPTree();
    tree->root = rt;
    // ----------------------------------------- 


    // Driver function -------------------------
    cout<<"Menu :\n 1.Insert 2.Remove 3.Search 4.Display 5.Exit\n";
    int q=1;
    while(q){
        int ch,x;
        cout<<"Enter choice : ";
        cin>>ch;
        switch(ch){
            case 1:{
                cout<<"Enter the number to be inderted : ";
                cin>>x;
                tree->insert(x);
                break;
            }
            case 2:{
                cout<<"Enter the number to be removed : ";
                cin>>x;
                tree->remove(x);
                break;
            }
            case 3:{
                cout<<"Enter the number to be searched : ";
                cin>>x;
                cout<<"Found : "<<tree->search(x);
                break;
            }
            case 4:
                cout<<"Display : \n";
                tree->display(tree->root);
                break;
            case 5:
                q=0;
                break;
        }
    }
    // ------------------------------------------

    return 0;
}