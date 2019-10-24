#include<bits/stdc++.h>
#define pb push_back
#define rep(i,a,b) for(int i=a;i!=b;i++)
#define all(a) (a).begin(),(a).end()
#define bs binary_search
#define lb lower_bound
#define ub upper_bound

using namespace std;

class TreeNode {
    
    public:
        bool leaf;
        int n;
        vector<TreeNode*> ptrs;
        vector<int> data;

        TreeNode(int order, bool isLeaf){
            n = order;
            leaf = isLeaf;
        }

        bool isFull(){
            return ptrs.size()>=n;
        }

        void print(){
            cout<<"Order : "<<n<<" isLeaf :"<<leaf<<"\n";
            rep(i,0,data.size()) cout<<data[i]<<" ";
            cout<<endl;
            rep(i,0,ptrs.size()) cout<<ptrs[i]<<" ";
            cout<<endl;
        }

        void add(int x, TreeNode* chd){

            int pos = lb(all(data),x)-data.begin();

            data.pb(x);
            ptrs.pb(chd);

            int y=x,t;
            TreeNode *next=chd, *prev;

            rep(i,pos,data.size()-1){
                t = data[i];
                data[i]=y;
                y=t;
            }

            data[data.size()-1]=y;

            rep(i,pos+1,ptrs.size()-1){
                prev = ptrs[i];
                ptrs[i] = next;
                next = prev; 
            }

            ptrs[ptrs.size()-1] = next;

        }
};

class BPTree {
    public:
        TreeNode *root;

        bool search(int x, TreeNode* ptr){
            TreeNode* head=ptr;
            ptr = NULL;

            bool found=false;
            if(head->leaf){
                return bs(all(head->data),x);
            }

            rep(i,0,head->data.size()){
                if(x<head->data[i]){
                    ptr = head->ptrs[i];
                    break;
                }
            }
            if(ptr==NULL) ptr = head->ptrs[head->ptrs.size()-1];

            return search(x,ptr);
        }

        int insert(int x,TreeNode* cur,TreeNode* &chd){
            
            if(cur->leaf){
                if(cur->ptrs.size()<=cur->n){
                    cur->add(x,NULL);
                    return INT_MIN;
                }
                
                return split_node(x,NULL,cur,chd); 
            }

            int mid=INT_MIN;
            TreeNode* temp=NULL;
            if(x>=cur->data[cur->data.size()-1]){
                // cout<<"OK\n";
                mid = insert(x,cur->ptrs[cur->ptrs.size()-1],temp);
            }
            else{
                rep(i,0,cur->data.size()){
                    if(x<cur->data[i]){
                        mid = insert(x,cur->ptrs[i],temp);
                        break;
                    }
                }
            }
            
            if(mid != INT_MIN){
                if(cur->ptrs.size()<=cur->n){
                    cur->add(mid,temp);
                    return INT_MIN;
                }
                else{
                    cout<<"Root Split";
                    int kr = split_node(x,temp,cur,chd);
                    cout<<" "<<kr<<endl;
                    return kr;
                }
            }

            return INT_MIN;
        }

        void display(){
            dfs(root);
        }



    private:

        void dfs(TreeNode* ptr){
            ptr->print();
            rep(i,0,ptr->ptrs.size()){
                if(ptr->ptrs[i]!=NULL && ptr->leaf==false){
                    dfs(ptr->ptrs[i]);
                }
            }
        }

        int split_node(int x,TreeNode* ptr,TreeNode* cur, TreeNode* &chd){

            // cout<<"-----------------------------------------\n";
            // cout<<"In split node func : "<<x<<"\n";
            // cur->print();
            // cout<<"-----------------------------------------\n";
            
            TreeNode* next = cur->ptrs[cur->ptrs.size()-1];
            TreeNode* node = new TreeNode(cur->n,true);
            cur->add(x,ptr);
            
            // cur->print();

            vector<int>& dt = cur->data;
            vector<TreeNode*>& pt = cur->ptrs;
            vector<int>& ndt = node->data;
            vector<TreeNode*>& npt = node->ptrs;

            int mid_pos = (dt.size()+1)/2;
            int key = dt[mid_pos];

            if(cur->leaf){      
                
                rep(i,mid_pos,dt.size()){
                    ndt.pb(dt[i]);
                }
                rep(i,mid_pos,pt.size()){
                    npt.pb(pt[i]);
                }

                // Erasing data from the first list
                dt.erase(dt.begin()+mid_pos,dt.end());
                pt.erase(pt.begin()+mid_pos,pt.end());
                
                // Setting up the node link
                pt.pb(node);


            }

            else{
                node->leaf = false;
                rep(i,mid_pos+1,dt.size()){
                    ndt.pb(dt[i]);
                }
                rep(i,mid_pos+1,pt.size()){
                    npt.pb(pt[i]);
                }
                dt.erase(dt.begin()+mid_pos,dt.end());
                pt.erase(pt.begin()+mid_pos+1,pt.end());
                
            }

            chd = node;
            return key;
        }

};

int main(){
    
    int n;
    cout<<"Enter the order of the tree : ";
    cin>>n;

    TreeNode* root = new TreeNode(n,true);
    root->ptrs.pb(NULL);
    BPTree* bpTree = new BPTree();
    bpTree->root = root;

    cout<<"Menu :\n 1.Insert 2.Remove 3.Display 4.Exit\n";
    int q=1;
    while(q){
        int ch,x;
        cout<<"Enter choice : ";
        cin>>ch;
        switch(ch){
            case 1:{
                cout<<"Enter the number : ";
                cin>>x;
                TreeNode* chk=NULL;
                int y;
                y = bpTree->insert(x,bpTree->root,chk);
                if(y!=INT_MIN){
                    cout<<"OK";
                    cout<<y;
                    TreeNode* nroot = new TreeNode(n,false);
                    nroot->data.pb(y);
                    nroot->ptrs.pb(bpTree->root);
                    nroot->ptrs.pb(chk);
                    bpTree->root = nroot;
                }
                break;
            }
            case 3:
                bpTree->display();
                break;
            case 4:
                q=0;
                break;
        }
    }
}