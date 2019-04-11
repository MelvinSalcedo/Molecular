#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<pair<vector<string>,string>> Cadena;

void Insertar_aminoacido(){
    vector<string> Phe= {"TTT","TTC"};
    vector<string> Leu= {"TTA","TTG","CTT","CTC","CTA","CTG"};
    vector<string> Ser= {"TCT","TCC","TCA","TCG","AGT","AGC"};
    vector<string> Tyr= {"TAT","TAC"};
    vector<string> Stop= {"TAA","TAG","TGA"};
    vector<string> Cys= {"TGT","TGC"};
    vector<string> Trp= {"TGG"};
    vector<string> Pro= {"CCT","CCC","CCA","CCG"};
    vector<string> His= {"CAT","CAC"};
    vector<string> Gln= {"CCA","CAG"};
    vector<string> Arg= {"CGT","CGC","CGA","CGG","AGA","AGG"};
    vector<string> Lle= {"ATT","ATC","ATA"};
    vector<string> Met= {"ATG"};
    vector<string> Thr= {"ACT","ACC","ACA","ACG"};
    vector<string> Asn= {"AAT","AAC"};
    vector<string> Lys= {"AAA","AAG"};
    vector<string> Val= {"GTT","GTC","GTA","GTG"};
    vector<string> Ala= {"GCT","GCC","GCA","GCG"};
    vector<string> Asp= {"GAT","GAC"};
    vector<string> Glu= {"GAA","GAG"};
    vector<string> Gly= {"GGT","GGC","GGA","GGG"};


    Cadena.push_back(make_pair(Phe,"Phe"));
    Cadena.push_back(make_pair(Leu,"Leu"));
    Cadena.push_back(make_pair(Ser,"Ser"));
    Cadena.push_back(make_pair(Tyr,"Tyr"));
    Cadena.push_back(make_pair(Stop,"Stop"));
    Cadena.push_back(make_pair(Cys,"Cys"));
    Cadena.push_back(make_pair(Trp,"Trp"));
    Cadena.push_back(make_pair(Pro,"Pro"));
    Cadena.push_back(make_pair(His,"His"));
    Cadena.push_back(make_pair(Gln,"Gln"));
    Cadena.push_back(make_pair(Arg,"Arg"));
    Cadena.push_back(make_pair(Lle,"Lle"));
    Cadena.push_back(make_pair(Met,"Met"));
    Cadena.push_back(make_pair(Thr,"Thr"));
    Cadena.push_back(make_pair(Asn,"Asn"));
    Cadena.push_back(make_pair(Lys,"Lys"));
    Cadena.push_back(make_pair(Val,"Val"));
    Cadena.push_back(make_pair(Ala,"Ala"));
    Cadena.push_back(make_pair(Asp,"Asp"));
    Cadena.push_back(make_pair(Glu,"Glu"));
    Cadena.push_back(make_pair(Gly,"Gly"));


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
