# ChunzhenDB
Search ip location from Chunzhen database with python code.

# Run with...
*chunzhenDB.py* must be together with *chunzhen.csv*, which is an ip-indexed database.
A newer Chunzhen database will always be available on (http://cz88.net), and if you want to construct a new *chunzhen.csv*, the function *chunzhenDB.CreateNewChunzhen()* is ready for you.

# Simple example
import chunzhenDB
db=chunzhenDB.ChunzhenDB()
location=db.GetChunzhenInfo('1.2.3.4')

# You won't believe...
There is none *try:... except:...* in the code. I assume your carefulness in running this code, and your enthusiasm in helping me. Thanks!
