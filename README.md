# Backend AYED

## What is this?

This is a repository for all the files used to create a backend with flask in order to connect our functions with a simple JavaScript web application.

## Getting Started

For implementing this library you will need to have Python installed in your computer.

### Prerequisites
To use this library you will need to have Python installed in your computer, at least the version 3.7. <br/>
You can check your Python version typing on cmd:

```
python --version
```

### Installing
- Clone this git repository into your computer.
- Start coding!

```
# In your root folder:

git clone https://github.com/juancho20sp/final-ayed-backend.git

```
### Using the Virtual Environment
**Activate**:
``` python
cd venv/Scripts
activate
```

Deactivate:
``` python
cd venv/Scripts
deactivate
```

Install requirements:
- With the **venv** activated: 

``` python
pip install -r requirements.txt
```

### How to implement it
- 
## Functions
```python
  from library import *
  
  library.add(a, b) # Add two complex numbers: a and b
  library.substract(a, b) # Substract two complex numbers: a and b
  library.multiply(a, b) # Multiply two complex numbers: a and b
  library.divide(a, b) # Divide two complex numbers: a and b
  library.conjugate(a) # Returns the conjugate of a given complex number
  library.module(a) # Returns the module of a given complex number
  library.polar(a) # Returns the given complex number in polar coordinates
  library.phase(a) # Returns the fase of a given complex
  
  library.add_arrays(m1, m2) # Add two multidimensional arrays, in case they have the same dimensions
  library.inverse_matrix(m1) # Returns a matrix where every item is the inverse of its corresponding in m1
  library.scalar_product(scalar, m1) # Returns the scalar product between 'scalar' and 'm1'. 'scalar' might be an integer or a complex number.
  library.transpose(m1) # Returns the given array BUT transposed
  library.conjugate_mx(m1) # Returns the given array conjugated, in case it has COMPLEX values
  library.adjoint(m1) # Returns the adjoint of the given array 
  library.multiply_mx(m1, m2) # Returns the product of (Array M1 x Array M2)
  library.trace(m1) # Returns the sum of the elements of the diagonal of the matrix
  library.inner_product(m1, m2) # Returns the inner product of <m1, m2>
  liibrary.norm(m1) # Returns the norm of the given array
  library.is_hermitian(m1) # Returns True if the given array is Hermitian, False otherwise
  library.inner(v1, v2) # Returns the inner product between two vectors
  library.norm_vector(v1) # Returns the norm of the given vector
  library.tensor(m1, m2) # Returns the tensor product between m1 and m2
  library.distance(v1, v2) # Returns the distance between two vectors
  library.action(m1, v2) # Returns the action between an array and a vector. IMPORTANT! If the array is a complex array (array of tuples), the vector must be written as a vector of complex numbers, even if it is real
  library.is_unitary(m1) # Returns 'True' if the given 2x2 array is unitary, 'False' otherwise
  
  ```
  
 ### Special Functions
   ```python
   library.prettyPrinting(tuple) # Basically prints the complex numbers (saved as tuples) in a *stylish* way: a + bi
   library.summable(m1, m2) # Checks if both multidimensional arrays have the same dimension
   library.substract_by_element(v1, v2) # Returns a vector whose each component are the substract V1 - V2 
   library.det(m1) # Returns the determinant of a 2x2 array
   ```



## Let's run the tests!
- For running the automated tests of the [Complex Calculator](https://github.com/juancho20sp/Complex-Calculator/blob/master/library.py), just open the [testlib.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/Vectors%20and%20Arrays%20Library/testLib.py) file in your favorite editor and run it.
- For running the automates tests of the [Programming drills](https://github.com/juancho20sp/Complex-Calculator/blob/master/Programming_drills.py), just open the [test_drills.py](https://github.com/juancho20sp/Complex-Calculator/blob/master/test_drills.py) file in your code editor and run it.

### Breaking down the tests
You will find a variety tests for each function, trying to get over all the possibilities. <br/>
An example will look like:

```
  A = [[1, 2, 3], [4, 5, 6]]
  B = [[1, 2, 3, 4], [5, 6, 7, 8]]
  C = [1, 2, 3]
  D = [[(101, 10), (1, 1), (1, 1)], [(2, 2), (2, 2), (2, 2)]]

  self.assertEqual(transpose(A), [[1, 4], [2, 5], [3, 6]])
  self.assertEqual(transpose(B), [[1, 5], [2, 6], [3, 7], [4, 8]])
  self.assertEqual(transpose(C), [[1], [2], [3]])
  self.assertEqual(transpose(D), [[(101, 10), (2, 2)], [(1, 1),(2, 2)], [(1, 1), (2, 2)]])
```




## Built With

* [Python 3.8](https://www.python.org/) - As the main programming language.



## Author

* **Juan David Murillo** - [Github](https://github.com/juancho20sp) | [Twitter](https://twitter.com/juancho20sp)<br/>
* **Diego Fernando Ruiz** -<br/>
Students at: [Escuela Colombiana de Ingeniería Julio Garavito](https://www.escuelaing.edu.co/es/) <br/>
2020 



## License

This is an *open source* project.

### Thanks for checking out!


