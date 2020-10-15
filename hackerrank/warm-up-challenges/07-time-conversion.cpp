#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {

    string hour_string = s.substr(0,2); // select the first two characters of the time
    int hour = stoi(hour_string);
    size_t pos = s.find('PM');

    if(pos != string::npos){
        if(hour + 12 < 24){
            hour_string = to_string(hour+12);}
            }

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
