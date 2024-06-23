"""task1.py"""

import datetime
if __name__ == "__main__":
    time = datetime.datetime.utcnow()
    local_time = datetime.datetime.now()

    print("Time for Grinvich:", time.strftime('%Y-%m-%d %H:%M:%S'))
    print("Local time:", local_time.strftime('%Y-%m-%d %H:%M:%S'))
