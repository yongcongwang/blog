---
title: Basic 2D Computational Geometry
mathjax: true
categories:
  - coding
date: 2021-03-13 20:52:57
---
To solve geometry problems in 2D with computers, we need some basic knowledge about geometry relationships and equations.

<!-- more -->

# Notion
## Point
In Cartesian Coordinate System, we use coordinates $(x, y)$ to represent a point, for example, $(2, 3)$, $(-7, 0)$.
```C++
struct Point {
  double x{0.};
  double y{0.};
};
```

## Vector
The representation of vector is like point, we use $(x, y)$ to represent a vector.
```C++
using Vector = Point;
```

## Line
There are many variant ways to write the equation of a line:
- Normal form: $ax + by + c = 0$;
- Slope-intercept form: $y = kx + b$;
- Intercept form: $\frac{x}{a} + \frac{y}{b} = 1$;

Consider that we just want to know where the line locates and how the line slopes, we can use the form of:
- a point on line and the unit vector of the line.

```C++
struct Line {
  Point point{0., 0.};
  Vector unit{0., 1.};
};
```

## Line Segment
We use two end points $(x_1, y_1), (x_2, y_2)$of the line segment to represent it.

```C++
struct LineSegment {
  Point start{0., 0.};
  Point end{0., 0.};
};
```

## Polygon
We record all vertices of the polygon to represent it.
```C++
struct Polygon {
  vector<Vector> points{};
};
```

## Curve
Some special curves like Bezier curve and Bell curve, we use its analytical expressions to represent them. For simple curve like circle, we can use the central point and radius of the circle to represent it.
```C++
struct Circle {
  Point center{0., 0.};
  double radius{0.};
};
```

# Basic Equations
## Triangle
### Law of sines
![law of sines](/images/2021/2d_geometry/law_of_sines.png)
$$
\frac{a}{\sin{A}} = \frac{b}{\sin{B}} = \frac{c}{\sin{C}} = 2R
$$
where:
- $a, b, c$ are the lengths of the sides of a triangle;
- $A, B, C$ are the opposite angle of $a, b, c$;
- $R$ is the radius of the triangle's circumcircle.

### Law of cosines
![law of cosines](/images/2021/2d_geometry/law_of_cosines.png)
$$
a^2 = b^2 + c^2 - 2bc\cos{A}
$$
$$
b^2 = a^2 + c^2 - 2ac\cos{B}
$$
$$
c^2 = a^2 + b^2 - 2ab\cos{C}
$$

## Vector
### Addition and Subtraction
The sum of two vectors is a third vector, represented as the diagonal of the parallelogram constructed with the two original vectors as sides. As for subtraction, set the second vector coordinates with its opposite number and use the same equation.
![vector addition](/images/2021/2d_geometry/vector_addition.png)
$$
A(x_1, y_1) + B(x_2, y_2) = C(x_1 + x_2, y_1 + y_2)
$$

```C++
Vector operator+(const Vector& A, const Vector& B) {
  return Vector{A.x + B.x, A.y + B.y};
}

Vector operator-(const Vector& A, const Vector& B) {
  return Vector{A.x - B.x, A.y - B.y};
}

Vector operator*(const Vector& A, const double k) {
  return Vector{A.x * k, A.y * k};
}

Vector operator/(const Vector& A, const double k) {
  return Vector{A.x / k, A.y / k};
}
```

### Dot Production
The dot product, also called the scalar product, is a scalar real number equal to the product of the lengths of vector $|\vec{a}|$ and $|\vec{b}|$ and the cosine of the angle $\theta$ between them:
$$
\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos{\theta} 
$$

We use dot product to:
- check if the two vectors are perpendicular: 
$$a \cdot b = 0$$
- calculate the angle between two vectors:
$$\cos{\theta} = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}$$

The result of dot product is calculated as:
```C++
double operator*(const Vector& A, const Vector& B) {
  return A.x * B.x + A.y * B.y;
}

double Length(const Vector& A) {
  return sqrt(A * A);
}

double Angle(const Vector& A, const Vector& B) {
  return acos(A * B / Length(A) / Length(B));
}
```

### Cross Production
The cross product, also called the vector product, is a third vector $\vec{c}$, perpendicular to the plane of the original vectors. The magnitude of $\vec{c}$ is equal to the product of the lengths of vectorss $\vec{a}$ and $\vec{b}$ and the sine of the angle $\theta$ between them:
$$
|\vec{c}| = |\vec{a}||\vec{b}|\sin{\theta}
$$

We can find the direction of cross product with right-hand rule:
![right hand rule](/images/2021/2d_geometry/right_hand_rule.png)

The cross product $\vec{c} = \vec{a} \times \vec{b}$ (vertical, in purple) changes as the angle between the vector $\vec{a}$(blue) and $\vec{b}$(red) changes. 
The cross product is:
- always orthogonal to both vectors;
- has magnitude $0$ when the vectors are parallel;
- has maximum magnitude $|\vec{a}||\vec{b}|$ when they are orthogonal.

![cross product](/images/2021/2d_geometry/cross_product.gif)

The result of dot product is calculated as:
```C++
double Cross(const Vector& A, const Vector& B) {
  return A.x * B.y - A.y * B.x;
}
```

### Rotation of Vector
![rotation of vector](/images/2021/2d_geometry/rotation_vector.png)

Let's say that we have a point $(x_1, y_1)$, which also defines the vector $\vec{a_1}$. The angle of $\vec{a_1}$ is $\beta$. The vector $\vec{a_1}$ has length $L$. We rotate this vector anticlockwise around the origin by $\alpha$ degrees, the new vector $\vec{a_2}$ has coordinates $(x_2, y_x)$. The length $L$ is not changed, so we have:
$$
x_1 = L \cos{\beta}
$$
$$
y_1 = L \sin{\beta}
$$
As we rotate $(x_1, y_1)$ by angle $\beta$ to get $(x_2, y_2)$, the new vector $\vec{a_2}$ has:
$$
x_2 = L \cos{(\alpha + \beta)}
$$
$$
y_2 = L \sin{(\alpha + \beta)}
$$
Combine all these equations above we have:
$$
\begin{align}
x_2 
& = L \cos{\alpha + \beta} \\\\
& = L (\cos{\alpha}\cos{\beta} - \sin{\alpha}\sin{\beta}) \\\\
& = L \cos{\beta}\cos{\alpha} - L \sin{\beta}\sin{\alpha} \\\\
& = x_1 \cos{\alpha} - y_1 \sin{\alpha} \\\\
\end{align}
$$
$$
\begin{align}
y_2 
& = L \sin{\alpha + \beta} \\\\
& = L (\sin{\alpha}\cos{\beta} + \cos{\alpha}\sin{\beta}) \\\\
& = L \cos{\beta}\sin{\alpha} + L \sin{\beta}\cos{\alpha} \\\\
& = x_1 \sin{\alpha} + y_1 \cos{\alpha} \\\\
\end{align}
$$

So the result of rotation of vector is:
```C++
Vector Rotate(Vector A, double alpha) {
  return Vector{A.x * cos(alpha) - A.y * sin(alpha),
                A.x * sin(alpha) + A.y * cos(alpha)};
}
```

# Basic Problems
## Area of Triangle
![area triangle](/images/2021/2d_geometry/area_triangle.png)

When we know the base and height, the area of triangle is:`
$$
S = \frac{1}{2} |AB| \cdot h
$$
as we have:
$$
|\vec{AB} \times \vec{AC}| = |\vec{AB}||\vec{AC}|sin\theta
$$
and
$$
h = |\vec{AC}|sin\theta
$$
The area of triangle can be calculated:
$$
S = \frac{1}{2} |\vec{AB} \times \vec{AC}| 
$$

```C++
double TriangleArea(const Point& A, const Point& B, const Point& C) {
  return Cross(B - A, C - A) / 2;
}
```

## Area of Polygon
![area polygon](/images/2021/2d_geometry/area_polygon.png)

We can divide a polygon to multiple triagnles and calculate the sum of their areas.
```C++
double PolygonArea(const Polygon& poly) {
  double res{0};
  int m = poly.points.size();
  for (int i = 1; i < m - 1; ++i) {
    res += Cross(poly.points[i] - poly.points[0], 
                 poly.points[i + 1], poly.points[0]);
  }
  return res / 2.;
}
```

## Point on Line Side
![point line side](/images/2021/2d_geometry/point_line_side.png)
We can use the cross product to check a point on wihch side of the line:
if the cross product is 
- $> 0$, point is on line left;
- $< 0$, point is on line right.

```C++
bool IsPointOnLineLeft(const Line& L, const Point& P) {
  return Cross((P - L.point), L.unit) > 0.;
}
```

## Point and Line Distance
The result of cross product is the area of parallelogram, we divide this by parallelogram's base to get height, which is the distance from point to line.

```C++
double DistanceFromPointToLine(const Point& P, const Line& L) {
  Vector v1{L.unit - L.point};
  Vector v2{P - L.point};
  return fabs(Cross(v1, v2) / Length(v1));
}
```

## Point and Line Segment Distance
If the point is not in the rectangle of line segment, we should calculate the distance from point to nearest line segment point; otherwise we can use the line distance to get the result.

```C++
double DistanceFromPointToLineSegment(const Point& P, const LineSegment& L) {
  Vector v1{L.end - L.start};
  Vector v2{P - L.start};
  Vector v3{P - L.end};
  if (sign(v1 * v2) < 0) return Length(v2);
  if (sign(v1 * v3) > 0) return Length(v3);
  return fabs(Cross(v1, v2) / Length(v1));
}
```

## Point on Line Segment
If a point is on line segment, it should meet:
- the point is on the line;
- the point is between two end points of line segment.

```C++
int Sign(double x) {
  return x < -1e-4 ? -1 : x > 1e-4 ? 1 : 0;
}

bool IsPointOnSegment(const LineSegment& L, const Point A) {
  return Sign(Cross(L.start - A, L.end - A)) == 0 &&
         Sign((L.start - A) * (L.end - A)) <= 0;
}
```

## Point in Polygon
There are two methods to check if the point is in polygon:
- Ray casting algorithm, a general mind can be described as [PNPOLY](https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html)
- Winding number algorithm, which links the point to all points of the polygon and calculate the sum of all the angles, if the angle is: 
 - $\ne 0$, the point is not in polygon;
 - $= 0$, the point is in polygon.


 ```C++
 bool PointInPolygon(const Point& P, const Polygon& poly) {
   double accumulate_angle{0};
   int m = poly.points.size();
   for (int i = 0; i < m; ++i) {
     auto& p1 = poly.points[i];
     auto& p2 = poly.points[(i + 1) % m];
     if (IsPointOnSegment(P, {p1, p2})) return false;
     accumulate_angle += acos((p1 - P) * (p2 - P) / Length(p1 - P) / Length(p2 - P));
   }
   return sign(accumulate_angle) == 0;
 }
 ```

## Line Segment Intersection
![line segment intersection](/images/2021/2d_geometry/line_segment_intersection.png)
There are three relationships between two line segments:
- no intersection;
- intersection;
- overlaps.

And as for the intersection case, we can use following methods to calculate its intersection point:
![line segment intersection algo](/images/2021/2d_geometry/line_segment_intersection_algo.png)

We assume that the intersection point is $O$, the area of the $\triangle ABC$ and $\triangle ABD$ can be calculated by:
$$
S_{ABC} = \frac{\vec{AB} \times \vec{AC}} {2}
$$
$$
S_{ABD} = \frac{\vec{AB} \times \vec{AD}} {2}
$$

As we have known that $\triangle ABC$ and $\triangle ABD$ have the same base $AB$:
$$
\frac{S_{ABC}} {S_{ABD}} = \frac{\frac{|AB| * |CN|}{2}}{\frac{|AB| * |DM|}{2}} =  \frac{|CN|} {|DM|}
$$

And according to triangle rules:
$$
\frac{|DM|}{|CN|} = \frac{|DO|}{|CO|}
$$

Finally:
$$
\frac{|DO|}{|CO|} = \frac{S_{ABD}}{S_{ABC}}
$$
$$
\frac{|DO|}{|DC|} = \frac{S_{ABD}}{S_{ABC} + S_{ABD}} = k
$$
$$
\vec{DO} = k * \vec{DC}
$$
```C++
bool IsLineSegmentIntersection(const LineSegment& L1, const LineSegment& L2) {
  return sign(Cross(L1.end - L1.start, L2.start - L1.start)) *
             sign(Cross(L1.end - L1.start, L2.end - L1.start)) < 0 &&
         sign(Cross(L2.end - L2.start, L1.start - L2.start)) *
             sign(Cross(L2.end - L2.start, L1.end - L2.start)) < 0;
}
```

# Reference
- [Geometry](https://oi-wiki.org/geometry/2d/)
- [Computer Geometry Tutorial](https://oi-wiki.org/geometry/2d/)
