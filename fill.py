import csv
import requests

url = "http://localhost:8082/events"

def string_to_bool(string):
    if string == '0':
        return False
    else:
        return True

if __name__ == '__main__':
    with open("terrorism.csv") as csvfile:
        spamreader = csv.reader(csvfile, dialect="excel", delimiter=';')
        for row in spamreader:
            eventid, iyear, imonth, iday,country_txt, region_txt, provstate, city, summary, crit1, crit2, crit3,\
            success, suicide, attacktype1_txt, targtype1_txt, targsubtype1_txt, corp1, target1, natlty1_txt, gname,\
            weaptype1_txt, nkill, nwound = row
            crit1 = string_to_bool(crit1)
            crit2 = string_to_bool(crit2)
            crit3 = string_to_bool(crit3)
            success = string_to_bool(success)
            suicide = string_to_bool(suicide)
            print(crit1)
            request_json = {
                "eventid": eventid,
                "iyear": iyear,
                "imonth": imonth,
                "iday": iday,
                "country_txt": country_txt,
                "region_txt": region_txt,
                "provstate": provstate,
                "city": city,
                "summary": summary,
                "crit1": crit1,
                "crit2": crit2,
                "crit3": crit3,
                "success": success,
                "suicide": suicide,
                "attacktype1_txt": attacktype1_txt,
                "targtype1_txt": targtype1_txt,
                "targsubtype1_txt": targsubtype1_txt,
                "corp1": corp1,
                "target1": target1,
                "natlty1_txt": natlty1_txt,
                "gname": gname,
                "weaptype1_txt": weaptype1_txt,
                "nkill": nkill,
                "nwound": nwound
            }
            # request = requests.post(url, json=request_json)
            # print(request.text)