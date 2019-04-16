'''
SpaceX has built a reliable Earth-Mars communication system that uses n links to transmit messages that are broken into fragments. The messages are sequences of ASCII characters that terminate with '#'. n copies of each fragment are sent, meaning that normally n copies of each fragment are received (one per link). However, some fragments may be lost. It's also possible that they can be corrupted or arrive out of order.

Each fragment contains the following data:

seq - The sequential number of the fragment in the message. This part of the fragment is never corrupted.
fragmentData - A single character from the message contained in the fragment.
Implement a function that receives an array of message fragments and reconstructs the original message according to the following rules:

For each sequential number, pick the data character that is present in more than 50% of the fragments with that sequential number. Note that we calculate 50% based on the total number of copies that were sent (which is always equal to n), while the number of received fragments can be smaller.
The last fragment of the message that's been reconstructed according to rule 1 (and no other fragment) contains '#'.
There can be no gaps in the message, so all of the fragments numbered 0, 1, 2, ..., <number of the last fragment> should be restored.
If the message cannot be reconstructed, return an empty string. Otherwise, return the reconstructed message.

Example

For seq = [1, 1, 0, 0, 0, 2, 2, 2], fragmentData = ['+', '+', 'A', 'A', 'B', '#', '#', '#'], and n = 3, the output should be
packetDescrambler(seq, fragmentData, n) = "A+#".

For the fragment with index 0 (sequential number), 2 'A's and 1 'B' were received. So, the number of fragments with 'A' is more than 50% out of n = 3. Both parts of rule 1 hold, meaning that the initial character of the message is 'A'.
For the fragment with index 1 (sequential number), 2 '+'s were received and the third fragment was lost. Again, the number of fragments with '+' is more than 50% out of n = 3. Therefore, the next character of the message is '+'.
For the fragment with index 2 (sequential number), 3 '#'s were received. All the sent fragments agree, so rule 1 holds. There are no fragments with a sequential number of more than 2, meaning that this is the last character. Since this character is '#', rule 2 holds as well.
Note that there were no gaps before '#', so rule 3 holds. Hence, the message can be considered correctly reconstructed.
Input/Output

[execution time limit] 0.5 seconds (cpp)

[input] array.integer seq

An array of non-negative integers. seq[i] contains the sequential number of the ith received fragment.

Guaranteed constraints:
1 ≤ seq.length ≤ 105,
0 ≤ seq[i] < 25000.

[input] array.char fragmentData

An array of characters. fragmentData[i] contains a printable ASCII character transmitted in the ith received fragment.

Guaranteed constraints:
fragmentData.length = seq.length.

[input] integer n

The number of links (in other words, the number of copies of the message that were sent).

Guaranteed constraints:
3 ≤ n ≤ 25000.

[output] string

Return the reconstructed message. If the message can't be reconstructed correctly, return an empty string.
'''



def packetDescrambler(seq, fragmentData, n):
    l = [None] * len(set(seq))

    for i in range(len(seq)):
        if seq[i] >= len(l):
            return ''

        if not l[seq[i]]:
            l[seq[i]] = {fragmentData[i] : 1}
        else:
            if fragmentData[i] in l[seq[i]]:
                l[seq[i]][fragmentData[i]] += 1
            else:
                l[seq[i]][fragmentData[i]] = 1
        #print(l)
    #print(l)
    ret = ''
    prev = -1
    for i in range(len(l)):
        if not l[i] and ret == '':
            return ''
        elif l[i]:
            for key in l[i].keys():
                if l[i][key]/n > 0.5:
                    if len(ret) > 0 and ret[len(ret) - 1] == '#':
                        return ''
                    else:
                        if prev != i - 1:
                            return ''
                        ret += key
                        prev = i
    return ret

if __name__ == '__main__':

    print(packetDescrambler([1, 1, 0, 0, 0, 3, 3, 3], ["+","+","A","A","B","#","#","#"], 4)) # Expected Empty
    print(packetDescrambler([1, 1, 0, 0, 0, 2, 2], ['+', '+', 'A', 'A', 'B', '#', '#', '#'], 3)) # Expected "A+#"
    print(packetDescrambler([1, 2, 2, 2, 0, 0, 0], ['+', 'A', 'A', 'B', '#', '#', '#'], 3)) # Expected Empty
    print(packetDescrambler([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], ["#","?","?","?","?","?","?","?","#","?","#","#"], 3)) #  expected "???#"
    print(packetDescrambler([0, 0], ['#', '#'], 3)) # Should be '#'
    print(packetDescrambler([1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0], ["X","#","Y","x","#","Y","x","#","Y","x","#","Y","X","#","Y","W","#","Y"], 6)) # expected Empty
