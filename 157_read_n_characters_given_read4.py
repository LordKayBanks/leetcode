# 157 Read N Characters Given Read4
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read.
# For example, it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n)
# that reads n characters from the file.
#
# Note:
# The read function will only be called once for each test case.


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while True:
            count = read4(temp)
            count = min(count, n-index)
            for i in range(count):
                buf[index] = temp[i]
                index += 1
            if index == n or count < 4:
                return index
