import numpy as np

from ldpc.codes import hamming_code, rep_code

from ldpc.gf2sparse import nullspace

from ldpc.bp_decoder import bp_decoder, BpDecoder


if __name__ == "__main__":

    H = hamming_code(3)

    ker = nullspace(H, method='dense')

    nulls = H@ker.T

    print(nulls.data %2)


    H = rep_code(3)

    # input_vector = np.array([1,0,1,0,1])

    input_vector = np.array([1,0,1])

    bpd = bp_decoder(H,error_probs=[0.1,0.1,0.1], input_vector_type='auto')

    print(bpd.decode(input_vector))

    print(bpd.input_vector_type)
