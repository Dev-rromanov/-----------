from datetime import datetime,timedelta

def is_older_than_a_day(test_time):
    one_day_ago = datetime.now() - timedelta(days=1)

    if test_time > one_day_ago:
        print ("The test time is less than one day old!")
    else:
        print ("The test time is older than one day.")