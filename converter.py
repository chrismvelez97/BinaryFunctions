def numToBinary(num):
    '''These are the place holders of the binary system,
    which we will use to determine the actual binary number'''
    binaryPlaceholders = [256,128,64,32,16,8,4,2,1]

    '''This is the name of the variable we will use for each index
    of the binaryPlaceholders list'''
    index = 0

    '''This will be the actual binary number converted.  The final
    form of this list will be the binary value for the original number'''
    binaryVal = []

    '''To start we iterate through each place in binaryPlaceholders'''
    while num != 0:
        '''Here we make the comparison to see if that index value
        goes into the original number'''
        if binaryPlaceholders[index] > num:
            '''What we did here is start generating a list that
            tracks the binary value as comparisons are made'''
            binaryVal.append(0)
        else:
            '''Once the number does go into an index value, we
            update the binary value with a 1 and create a new num
            which derives from the original num and starts at the next index'''
            binaryVal.append(1)
            num = num - binaryPlaceholders[index]
        index += 1

    '''We return with the final binary value in list format'''
    return(binaryVal)

numToBinary(257)
#257 in binary should be 1.0.0.0.0.0.0.0.1
