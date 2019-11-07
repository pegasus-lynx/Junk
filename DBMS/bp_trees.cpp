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
        int min_data;

        Node(int order, bool isLeaf){
            leaf = isLeaf;
            n = order;
            min_data = ((n+1)/2) - 1;
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
            if(search(x)){
                _remove(x,root,NULL);
            }
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
        int _remove(int x,Node* cur,Node* par){

            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;
            
            if(cur->leaf){
                // Removed data from the leaf
                int p = find(all(cd),x)-cd.begin();
                cd.erase(cd.begin()+p);
                cp.erase(cp.begin()+p);

                // Redistribute data in the leaf
                if(cd.size()<cur->min_data){
                    if(!_redistribute(cur,par)){
                        return _merge(cur,par);
                    }
                }

                return 0;
            }

            vector<int>& pd = par->data;
            vector<Node*>& pp = par->ptrs;

            int p = lb(all(cd),x) - cd.begin();
            int k = _remove(x,cp[p],cur);
            
            if(cd.size()<cur->min_data){
                if(!_redistribute(cur,par)){
                    return _merge(cur,par);
                }
            }

        }

        bool _redistribute(Node* cur,Node* par){
            
            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;
            vector<int>& pd = par->data;
            vector<Node*>& pp = par->ptrs;

            int pc = find(all(pp),cur)-pp.begin();

            Node* ls=(pc>0?pp[pc-1]:NULL);
            Node* rs=(pc+1<pp.size()?pp[pc+1]:NULL);

            if(cur->leaf){
                if(ls!=NULL){

                    vector<int>& ld = ls->data;
                    vector<Node*>& lp = ls->ptrs;                    

                    if(ld.size()>ls->min_data){
                        int sh = ld[ld.size()-1];
                        ld.erase(ld.end()-1);
                        cd.insert(cd.begin(),sh);
                        lp.erase(lp.begin());
                        cp.insert(cp.begin(),NULL);
                        pd[pc-1] = sh;
                        return 1;
                    }
                }

                if(rs!=NULL){
                    
                    vector<int>& rd = rs->data;
                    vector<Node*>& rp = rs->ptrs;                    
                    
                    if(rd.size()>rs->min_data){
                        int sh = rd[0];
                        rd.erase(rd.begin());
                        cd.pb(sh);
                        rp.erase(rp.begin());
                        cp.insert(cp.begin(),NULL);
                        pd[pc+1] = sh;
                        return 1;
                    }
                }
            }
            else{

                if(ls!=NULL){

                    vector<int>& ld = ls->data;
                    vector<Node*>& lp = ls->ptrs;                    
                    
                    if(ld.size()>ls->min_data){
                        
                        int sh = ld[ld.size()-1];
                        int bg = pd[pc-1];
                        ld.erase(ld.end()-1);
                        cd.insert(cd.begin(),bg);

                        cp.insert(cp.begin(),lp[lp.size()-1]);
                        lp.erase(lp.end()-1);
                        
                        pd[pc-1] = sh;
                        
                        return 1;
                    }

                }

                if(rs!=NULL){
                    vector<int>& rd = rs->data;
                    vector<Node*>& rp = rs->ptrs;                    
                    
                    if(rd.size()>rs->min_data){
                        
                        int sh = rd[0];
                        int bg = pd[pc+1];

                        rd.erase(rd.begin());
                        cd.pb(bg);

                        cp.insert(cp.end(),*rp.begin());
                        rp.erase(rp.begin());
                        
                        pd[pc+1] = sh;
                        
                        return 1;
                    }
                }

            }

            return 0;
        }

        int _merge(Node* cur, Node* par){

            vector<int>& cd = cur->data;
            vector<Node*>& cp = cur->ptrs;

            if(cur==root){
                if(cd.size()==0){
                    if(cp.size()==0){
                        root=NULL;
                        free(cur);
                    }
                    else{
                        root = cp[0];
                        free(cur);
                    }
                }
                return 0;
            }

            vector<int>& pd = par->data;
            vector<Node*>& pp = par->ptrs;

            int pc = find(all(pp),cur)-pp.begin();

            Node* ls=(pc>0?pp[pc-1]:NULL);
            Node* rs=(pc+1<pp.size()?pp[pc+1]:NULL);

            Node* temp = new Node(cur->n,cur->leaf);
            vector<int>& td = temp->data;
            vector<Node*>& tp = temp->ptrs;

            if(cur->leaf){
                if(ls!=NULL){

                    vector<int>& ld = ls->data;
                    vector<Node*>& lp = ls->ptrs;                    
                    
                    rep(i,0,ld.size()) td.pb(ld[i]);
                    rep(i,0,cd.size()) td.pb(cd[i]);

                    rep(i,0,lp.size()-1) tp.pb(lp[i]);
                    rep(i,0,cp.size()) tp.pb(cp[i]);    

                    pp[pc] = temp;
                    pd.erase(pd.begin()+pc-1);
                    pp.erase(pp.begin()+pc-1);

                    return 1;
                }

                if(rs!=NULL){
                    rep(i,0,cd.size()) td.pb(cd[i]);
                    rep(i,0,rd.size()) td.pb(rd[i]);

                    rep(i,0,cp.size()-1) tp.pb(cp[i]);
                    rep(i,0,rp.size()) tp.pb(rp[i]);

                    pp[pc+1]=temp;
                    pd.erase(pd.begin()+pc);
                    pp.erase(pp.begin()+pc);

                    return 1;
                }
            }
            else{
                if(ls!=NULL){

                    vector<int>& ld = ls->data;
                    vector<Node*>& lp = ls->ptrs;                    

                    if(!_mergable()

                    rep(i,0,ld.size()) td.pb(ld[i]);
                    rep(i,0,cd.size()) td.pb(cd[i]);

                    rep(i,0,lp.size()) tp.pb(lp[i]);
                    rep(i,0,cp.size()) tp.pb(cp[i]);
                }
                
                if(rs!=NULL){

                    vector<int>& rd = ls->data;
                    vector<Node*>& rp = ls->ptrs;  

                }
            }

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