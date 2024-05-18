# Adapter Pattern in Python
It allows two incompatible interfaces to work together without modifying the internals of each component. This is achieved by adapting one interface, to another, externally.


![Adapter design pattern](adapter_pattern.webp?raw=true "Title")

## Object Adapter
Object Adapter takes on the interface of one object while wrapping the behavior of another.

## Class Adapter
Class Adapter, on the other hand, is a bit more specific. It relies on inheritance, inheriting interfaces from both objects at once. However, it’s only an option in programming languages that support multiple inheritance, like C++.