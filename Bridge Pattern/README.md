# Bridge Pattern in Python

It splits the abstraction from the implementation.

### Example

Airplane Interface: <br />
Can either be Military or Commercial <br />
Can either be Passenger or Cargo <br />

There are 4 possibilities:
1. Military-Passenger
2. Military-Cargo
3. Commercial-Passenger
4. Commercial-Cargo

The Bridge Pattern prevents what's called the cartesian product complexity explosion.

We create a Carrier interface for Passenger/Cargo and Plane interface for Military/Commercial and then connect them using constructors.


