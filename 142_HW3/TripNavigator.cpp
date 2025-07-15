#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

int main() {
    int n, t;
    cin >> n >> t;

    //Initialize Graph
    vector<vector<int> > graph(n, vector<int>(n));
    for (int row = 0; row < n; ++row) {
        string line;
        cin >> line;
        for (int i = 0; i < n; ++i) {
            if (line[i] == '-') {
                graph[row][i] = 1;  
            } else {
                graph[row][i] = t + 1;  
            }
        }
    }

    graph[0][0] = 0;  

    //Run Dijkstra's Algorithm
    vector<vector<int> > distances(n, vector<int>(n, INF));
    distances[0][0] = 0;

    priority_queue<pair<int, pair<int, int> >, vector<pair<int, pair<int, int> > >, greater<pair<int, pair<int, int> > > > pq;
    pq.push(make_pair(0, make_pair(0, 0)));  

    while (!pq.empty()) {
        pair<int, pair<int, int> > top = pq.top();
        pq.pop();

        int cost = top.first;
        int x = top.second.first;
        int y = top.second.second;

        if (distances[x][y] < cost) {
            continue;
        }

        vector<pair<int, int> > neighbors = {
            make_pair(x - 1, y),  
            make_pair(x, y - 1),  
            make_pair(x + 1, y),  
            make_pair(x, y + 1)   
        };

        for (const pair<int, int>& neighbor : neighbors) {
            int nx = neighbor.first;
            int ny = neighbor.second;
            //Check bounds
            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                int new_cost = cost + graph[nx][ny];
                if (new_cost < distances[nx][ny]) {
                    distances[nx][ny] = new_cost;
                    pq.push(make_pair(new_cost, make_pair(nx, ny)));
                }
            }
        }
    }
    cout << distances[n - 1][n - 1] << endl;
    return 0;
}