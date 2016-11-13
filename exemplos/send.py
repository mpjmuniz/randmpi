# - - coding: utf- 8 - -
import numpy
from mpi4py import MPI
a = numpy([1,2,3])
if MPI.COMM_WORLD.rank == 0:
        MPI.COMM_WORLD.Send(a, dest = 1)
#  Comm.Send(buf, dest = 0, tag = 0)
#    Comm (MPI comm) – communicator we wish to query
#    buf (choice) – data to send
#    dest (integer) – rank of destination
#    tag (integer) – message tag

else:
        MPI.COMM_WORLD.Recv(a, source = 0)

# Comm.Recv(buf, source = 0, tag = 0, Status status = None)
#    Comm (MPI comm) – communicator we wish to query
#    buf (choice) – initial address of receive buffer (choose receipt location)
#    source (integer) – rank of source
#    tag (integer) – message tag
#    status (Status) – status of object


#On a Recv you do not always need to specify the source. Instead, you can allow the calling process to accept a message from any process that happend to be sending to the receiving process. This is done by setting source to a predefined MPI constant, source=ANY_SOURCE (note that you would first need to import this with from mpi4py.MPI import ANY_SOURCE or use the syntax source=MPI.ANY_SOURCE).
