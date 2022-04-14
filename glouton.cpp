#include <iostream>
#include <fstream>
#include <vector>
#include <cstring> 
#include <string.h>
#include <stdio.h>




using namespace std;

int main()
{
    char str[100];
    int a=0;
    int k = 0;
    int t = 0;
    int energie =0;

    string filename("N10_K3_0");
    vector<string> lines;
    string line;

    ifstream input_file(filename);
    if (!input_file.is_open()) {
        cerr << "Could not open the file - '"
             << filename << "'" << endl;
        return EXIT_FAILURE;
    }

    while (getline(input_file, line)){
        lines.push_back(line);
    }

    for (const auto &i : lines)
        cout << i << endl;

    input_file.close();

    char p[lines[0].length()];
 
    int i;
    for (i = 0; i < sizeof(p); i++) {
        p[i] = lines[0][i];
        cout << p[i];
    }
    char* test;
    
    test = strtok(p," ");
    cout << test << endl;
    
}
