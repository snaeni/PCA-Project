#include <bits/stdc++.h>
#include <sys/time.h>
#include <fstream>

using namespace std;

struct Point
{
	int x, y;
};

/*
 * To find orientation of ordered triplet (p, q, r).
 *  The function returns following values
 *  0 --> p, q and r are collinear
 *  1 --> Clockwise
 *  2 --> Counterclockwise
 */
int orientation(Point p, Point q, Point r)
{
	int val = (q.y - p.y) * (r.x - q.x) -
			(q.x - p.x) * (r.y - q.y);

	// collinear case
	if (val == 0)
		return 0;

	// check for clock or counterclock wise
	return (val > 0)? 1: 2;
}

/*
 * Main function Implementing Jarvis Algorithm
 * Input: Set of Points
 * Output: prints Convex Hull Points
 *
 * Code is sufficiently documented at every step
 */
void convexHull(Point points[], int n)
{
	// There must be at least 3 points
	if (n < 3) return;

	// Initialize Result
	vector<Point> hull;

	// Find the leftmost point
	int l = 0;
	for (int i = 1; i < n; i++)
		if (points[i].x < points[l].x)
			l = i;

	// Start from leftmost point, keep moving counterclockwise
	// until reach the start point again. This loop runs O(h)
	// times where h is number of points in result or output.
	int p = l, q;
	do
	{
		// Add current point to result
		hull.push_back(points[p]);

		// Search for a point 'q' such that orientation(p, x,
		// q) is counterclockwise for all points 'x'. The idea
		// is to keep track of last visited most counterclock-
		// wise point in q. If any point 'i' is more counterclock-
		// wise than q, then update q.
		q = (p+1)%n;
		for (int i = 0; i < n; i++)
		{
		// If i is more counterclockwise than current q, then
		// update q
		if (orientation(points[p], points[i], points[q]) == 2)
			q = i;
		}

		// Now q is the most counterclockwise with respect to p
		// Set p as q for next iteration, so that q is added to
		// result 'hull'
		p = q;

	} while (p != l); // While we don't come to first point

	// Print Convex Hull Points
	for (int i = 0; i < (int)hull.size(); i++)
		cout << "(" << hull[i].x << ", "
			<< hull[i].y << ")\n";
	cout<< "Convex Hull Size: "<< hull.size()<<" Vertex for region of "
			<< n << " points"<<endl;
}

/*
 * main() function:
 * Reads from an input file and forms Points[] array
 * Outputs the total time taken for Finding Convex Hull
 * Using Jarvis Implementation
 */
int main()
{
	int totalPoints = 0, i = 0;
	int a, b;

	// To find time taken in milli seconds
	struct timeval start;
	gettimeofday(&start, NULL);
	long long time1 = (long long)start.tv_sec * 1000 + start.tv_usec / 1000;

	//Name of the input file name
	ifstream infile;
	infile.open("C:\\Users\\Sharath\\Desktop\\graphData5.txt");
	if(!infile.is_open()) {
		cout<<"Unable to Open Input File"<<endl;
		return -1;
	}

	infile >> totalPoints;
	cout<<totalPoints;
	Point points[totalPoints];
	while ((infile >>a >>b) && (i<totalPoints))
	{
		points[i].x = a;
		points[i].y = b;
		i++;
	}

	convexHull(points, totalPoints);
	struct timeval end;
	gettimeofday(&end, NULL);
	long long time2 = (long long)end.tv_sec * 1000 + end.tv_usec / 1000;
	cout << "Time Taken for Jarvis Algorithm: "<<time2-time1<<endl;

	return 0;
}
