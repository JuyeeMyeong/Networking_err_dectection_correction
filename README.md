# Error Correction

From sender to receiver, we have to detect and correct the errors when data is transmitted.

- Backward error correction: Once the error is discovered, the receiver requests the sender to retransmit the entire data unit.
- Forward error correction: The receiver uses the error-correcting code which automatically corrects the errors.

Let's say r is the number of redundant bits and d is the total number of the data bits. The number of redundant bits r can be calculated by using the formula:
2^r>=d+r+1


### Hamming Code
Hamming code requires adding additional parity bits with the data. It it commonly used in error correction code (ECC) RAM. Whenever data is transmitted or stored, it's possible that the data may become corrupted. This can take the form of bit flips, where a binary. 1 becomes a 0 or vice versa. Error correcting codes seek to find when an error is introduced into some data. This is done by adding parity bits, or reduncdant information, to the data. 

<<Encoding>>
1. Calculate the number of redundant bits
If the messege contains m number of data bits, r number of redundant bits are added to it at least (m + r + 1) different states. (m + r) is location of an error in each of (m + r) bit positions and one additional state indicates no error. [2^r>=d+r+1]

2. Position the redundant bits
The r redundatn bits placed at bit positions of powers of 2. (2, 4, 8, 16 ...) 

3. Calculate the values of each redundant bit
**Even parity**: The total number of bits in the message is made even
**Odd parity**: The total number of bits in the message is made odd

Each redundant bit is calculated as the parity based upon its bit position. 

<<Decoding>>
1. Calculate the number of redundant bits
2. Position the redundant bits
3. Parity checking
4. Error detection and correction


### CRC
