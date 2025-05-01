#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, m;
    cin >> t >> n >> m;

    // Vector to store events
    vector<tuple<int, int, int>> events;

    // Read upper layer intervals
    for (int i = 0; i < n; ++i) {
        int start, end, glowing;
        cin >> start >> end >> glowing;
        int points = 0;
        if (glowing == 1) {
            points = 3;
        } else {
            points = 1;
        }
        events.emplace_back(start, points, 0);       // Start event
        events.emplace_back(end + 1, -points, 0);   // End event
    }

    // Read lower layer intervals
    for (int i = 0; i < m; ++i) {
        int start, end, glowing;
        cin >> start >> end >> glowing;
        int points = 0;
        if (glowing == 1) {
            points = 3;
        } else {
            points = 1;
        }
        events.emplace_back(start, points, 1);      
        events.emplace_back(end + 1, -points, 1);   
    }

    // Sort events by position
    sort(events.begin(), events.end());

    int upper_active_points = 0;
    int lower_active_points = 0;
    int point_total = 0;  
    int last_position = 0;

    // Process events
    for (const auto& event : events) {
        int position, change, layer;
        tie(position, change, layer) = event;

        // Calculate points for the range between the last position and the current position
        if (last_position != position) {
            point_total += max(upper_active_points, lower_active_points) * (position - last_position);
            last_position = position;
        }

        // Update active points for the respective layer
        if (layer == 0) {
            upper_active_points += change;
        } else {
            lower_active_points += change;
        }
    }

    cout << point_total << endl;

    return 0;
}