#! thrift --gen cpp
namespace cpp Example

service MatrixMath {
  list<double> add(1:list<double> a, 2:list<double> b)
}