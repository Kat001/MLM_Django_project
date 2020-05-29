#include <bits/stdc++.h>
using namespace std;
const int N = 5E3 + 5;
int a[N];
int main() {
    int cases;
    cin>>cases:

    while(cases>0){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int n;
        cin >> n;
        for(int i = 0; i < n; i ++)
            cin >> a[i];
        int ans = 0;
        for(int i = 0; i < n; i ++) {
            double total = 0;
            for(int j = i; j < n; j ++) {
                total += a[j];
                double chkr = total;
                chkr = sqrt(chkr);
                if(chkr == floor(chkr))
                    ans ++;
            }
        }
        cout <<"Case #"<<cases<<":"<<ans;
        cases--;
    }
    return 0;