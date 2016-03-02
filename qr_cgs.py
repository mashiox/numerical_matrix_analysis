#
# QR Factorization
# Classic Gram-Schmidt Algorithm
#
import numpy
import math
    
def qr_cgs(M):
    if ( type( M ) is numpy.ndarray ):
        M = numpy.matrix(M)
    # Creates a new empty matrix same size as M
    Q = numpy.matrix( numpy.empty( shape=M.shape ) )
    R = numpy.matrix( numpy.empty( shape=M.shape ) )
    # Begin the loop defined by column size
    for index in range(0, M.shape[1] ):
        Q[:,index] = M[:,index]
        for kndex in range(0, index-1):
            R[kndex, index] = Q[:, index].H.dot(M[:,index])
            Q[:,index] = Q[:,index] - R[kndex, index]*Q[:,kndex]
        # Compute the norm of v for R
        R[index, index] = math.sqrt( Q[:, index].H.dot(Q[:, index]) )
        Q[:, index] = Q[:,index]/R[index, index]
    return (Q,R)