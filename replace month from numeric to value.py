def diction(lst):
    dic = {
        '01' : 'Jan',
        '02' : 'Feb',
        '03' : 'Mar',
        '04' : 'Apr',
        '05' : 'May',
        '06' : 'Jun',
        '07' : 'Jul',
        '08' : 'Aug',
        '09' : 'Sep',
        '10' : 'Oct',
        '11' : 'Nov',
        '12' : 'Dec'
    }
    l = []

    for i in lst:
        day,month,year = i.split("-")
        l.append(f"{day}-{dic[month]}-{year}")
    return l



lst_dates = ['01-01-2020','21-03-2022','11-06-2023','12-12-2020']
print(diction(lst_dates))