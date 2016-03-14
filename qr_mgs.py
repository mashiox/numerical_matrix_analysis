#
# QR Factorization
# Modified Gram-Schmidt Algorithm
#
import numpy
import math
    
def qr_cgs(M):
    if ( type( M ) is numpy.ndarray ):
        M = numpy.matrix(M)
    # Creates a new empty matrix same size as M
    Q = numpy.matrix( numpy.empty( shape=M.shape ) )
    R = numpy.matrix( numpy.empty( shape=M.shape ) )
    # Collect necessary v_i
    # TODO: This may be a wasteful assignment, and is O(n). 
    for index in range(0, M.shape[1] ):
        Q[:,index] = M[:,index]
    
    for index in range(0, M.shape[1] ):
        # Normalize r_(i,i)
        R[index, index] = numpy.linalg.norm( Q[:,index] )
        Q[:, index] = Q[:, index]/R[index, index]
        
        for  jndex in range( index+1, M.shape[1] ):
            R[index, jndex] = Q[:, index].H*R[:, jndex]
            R[:, jndex] = R[:, jndex] - R[index, jndex]*Q[:, index]
            
    return (Q,R)