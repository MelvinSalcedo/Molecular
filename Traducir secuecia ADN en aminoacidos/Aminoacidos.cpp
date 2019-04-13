#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

map<string, vector<string> > Cadena;

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


    Cadena.insert(make_pair("F",F));
    Cadena.insert(make_pair("L",L));
    Cadena.insert(make_pair("W",W));
    Cadena.insert(make_pair("C",C));
    Cadena.insert(make_pair("Stop",Stop));
    Cadena.insert(make_pair("S",S));
    Cadena.insert(make_pair("Y",Y));
    Cadena.insert(make_pair("V",V));
    Cadena.insert(make_pair("P",P));
    Cadena.insert(make_pair("H",H));
    Cadena.insert(make_pair("Q",Q));
    Cadena.insert(make_pair("R",R));
    Cadena.insert(make_pair("I",I));
    Cadena.insert(make_pair("M",M));
    Cadena.insert(make_pair("T",T));
    Cadena.insert(make_pair("N",N));
    Cadena.insert(make_pair("K",K));
    Cadena.insert(make_pair("A",A));
    Cadena.insert(make_pair("D",D));
    Cadena.insert(make_pair("E",E));
    Cadena.insert(make_pair("G",G));


}


string TraducirAminoacidos(string seq){

    for(auto iteratorCadena=Cadena.begin();iteratorCadena!=Cadena.end();iteratorCadena++){
        auto iteratorVector=find(iteratorCadena->second.begin(),iteratorCadena->second.end(),seq);
        if(iteratorVector!=iteratorCadena->second.end()){
            return iteratorCadena->first;
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
	//TraducirAminoacidos("TGG");


}
