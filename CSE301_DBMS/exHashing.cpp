#include<bits/stdc++.h>


// Macros

#define pb push_back
#define rep(i,a,b) for(int i=a;i<b;i++)


class Bucket {
	public:
		int ld;
		vector<int> arr;

        Bucket(){};

        Bucket(int depth){
            ld = depth;
        }

		int lHash(int x){
			return x & ((1<<ld)-1);
		}
}

class HashMap {
	public:
		int global_depth;
		int bucket_size;
		
		map<int, Bucket*> dirs;

        Directory(int depth, int bucket_size){
            this->bucket_size = bucket_size;
            this->global_depth = depth;

            rep(i,0,(1<<depth)){
                dirs[i] = new Bucket(depth);
            }
        }

		bool search(int x){
            int gsh = gHash(x);
            Bucket* bk = dirs[gsh];

            for( auto it : bk->arr){
                if(it==x) return true;
            }
            return false;
		}

		void insert(int x){
            if(!search(x)){

                int gsh = gHash(x);
                Bucket* bk = dirs[gsh];
                vector<int>& v = bk->arr;

                if(v.size()<bucket_size){
                    v.push_back(x);
                }
                else{
                    split(gsh, bk);
                    insert(x);
                }

            }
		}

		void remove(int x){
            if(search(x)){
                int gsh = gHash(x);
                Bucket* bk = dirs[gsh];
                vector<int>& v = bk->arr;
                v.erase(v.begin()+find(v.begin(),v.end(),x));

                merge(bk);
            }
		}

		void display(){
            
            cout<<"Hash Set :\n";    
            for(auto it : dirs){
                cout<<"Dir "<<it.first<<" :\nLocal Depth :"<<it.second->ld<<"\n";
                for(auto i:it.second->arr){
                    cout<<i<<" ";
                }
                cout<<"\n";
            }

		}

	private:
		void split(int hs, Bucket* b){

            Bucket* nb = new Bucket();
            vector<int> temp;
            for(auto it:b->arr) temp.pb(i);
            b->arr.clear();

            if(b->ld == global_depth) expand();

            dirs[hs^(1<<(gd-1))] = nb;
            nb->ld = ++b->ld;
            for(auto it:temp){
                dirs[gHash(it)]->arr.pb(it);
            }    

        }

		void merge(int hs, Bucket* bk){
            
            int chs = cgHash(hs);
            Bucket* cbk = dirs[chs];

            if( bk != cbk ){
                if( bk->arr.size() + cbk->arr.size() <= bucket_size && bk->ld == cbk->ld ){
                    
                    Bucket* mbk = (chs>hs?bk:cbk);
                    Bucket* dbk = (chs>hs?cbk:bk);
                    for(auto it:dbk->arr) mbk->arr.pb(it);
                    dbk->arr.clear();
                    mbk->ld--;
                    dirs.erase((chs>hs?chs:hs));
                    shrink();
                }
            }

		}

		void shrink(){
            for(auto it:dirs){
                if(it.first>=gd){
                    return;
                }
            }
		
            rep(i,(1<<(gd-1)),1<<gd){
                dirs.erase(i);
            }

            shrink();
        }

		void expand(){
            rep(i,0,(1<<gd)){
                dirs[i^(1<<gd)] = dirs[i];
            }
			global_depth++;
		}

        int gHash(int x){
            return x & ((1<<gd)-1);
        }

        int cgHash(int hs){
            return hs ^ (1<<(gd-1));
        }
}