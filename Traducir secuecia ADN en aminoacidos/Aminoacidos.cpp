#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<pair<vector<string>,string>> Cadena;

void Insertar_aminoacido(){
    vector<string> F= {"TTT","TTC"};
    vector<string> L= {"TTA","TTG","CTT","CTC","CTA","CTG"};
    vector<string> W={"TGG"};
    vector<string> C={"TGC","TGT"};
    vector<string> S= {"TCG","TCA","TCC","TCT","AGT","AGC"};

    vector<string> Y= {"TAT","TAC"};
    vector<string> Stop= {"TAA","TAG","TGA"};
    vector<string> V= {"GTG","GTA","GTC","GTT"};
    vector<string> P= {"CCT","CCC","CCA","CCG"};
    vector<string> H= {"CAT","CAC"};
    vector<string> Q= {"CCA","CAG"};
    vector<string> R= {"CGT","CGC","CGA","CGG","AGA","AGG"};
    vector<string> I= {"ATT","ATC","ATA"};
    vector<string> M= {"ATG"};
    vector<string> T= {"ACT","ACC","ACA","ACG"};
    vector<string> N= {"AAT","AAC"};
    vector<string> K= {"AAA","AAG"};
    vector<string> A= {"GCT","GCC","GCA","GCG"};
    vector<string> D= {"GAT","GAC"};
    vector<string> E= {"GAA","GAG"};
    vector<string> G= {"GGT","GGC","GGA","GGG"};


    Cadena.push_back(make_pair(F,"F"));
    Cadena.push_back(make_pair(L,"L"));
    Cadena.push_back(make_pair(W,"W"));
    Cadena.push_back(make_pair(C,"C"));
    Cadena.push_back(make_pair(Stop,"Stop"));
    Cadena.push_back(make_pair(S,"S"));
    Cadena.push_back(make_pair(Y,"Y"));
    Cadena.push_back(make_pair(V,"V"));
    Cadena.push_back(make_pair(P,"P"));
    Cadena.push_back(make_pair(H,"H"));
    Cadena.push_back(make_pair(Q,"Q"));
    Cadena.push_back(make_pair(R,"R"));
    Cadena.push_back(make_pair(I,"I"));
    Cadena.push_back(make_pair(M,"M"));
    Cadena.push_back(make_pair(T,"T"));
    Cadena.push_back(make_pair(N,"N"));
    Cadena.push_back(make_pair(K,"K"));
    Cadena.push_back(make_pair(A,"A"));
    Cadena.push_back(make_pair(D,"D"));
    Cadena.push_back(make_pair(E,"E"));
    Cadena.push_back(make_pair(G,"G"));


}


string TraducirAminoacidos(string seq){
    for(int x=0;x<Cadena.size();x++){
        for(int y=0;y<Cadena[x].first.size();y++){
            vector<string> temp=Cadena[x].first;
            if(temp[y]==seq){
                return Cadena[x].second;
            }
        }
    }
}

void desmenusar(string seq){
    int s=seq.size()/3;
    string tem="123";
    int cont=0;
    for(int x=0;x<s;x++){
        tem[0]=seq[cont];
        tem[1]=seq[cont+1];
        tem[2]=seq[cont+2];
        cont+=3;
        cout<<tem<<"  "<<TraducirAminoacidos(tem)<<endl;
    }
}
int main(){
	Insertar_aminoacido();
	desmenusar("ATGGAAGTATTTAAAGCGCCACCTATTGGGATATAA");


}
