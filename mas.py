from datetime import datetime
date1_str = '5.02.2015'
date2_str = '3.02.2015'
date1 = datetime.strptime(date1_str, '%d.%m.%Y')
date2 = datetime.strptime(date2_str, '%d.%m.%Y')
(date2-date1).days

