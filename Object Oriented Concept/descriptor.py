# Descriptor is an object attributes with "binding behaviour" one whose attributes access has been overridden by method in the descriptor
# Protocol.Those methods are  __get__(), __set__() and __delete__() if any of these methods are defined for an object then it is said to be
# descriptor.

# __get__() : accesses the attributes.It return the value of the attributes or raise the AttributesError exception if a requested
# attributes is no present.

# __set__() : is called in an attributes assignment operation and Return Nothing.

# __delete__() : controls aa delete operation  and it also return nothing.

# Example

# Descriptor uses is already by using property decorator we can also used by using class approach and function approach practice later.
