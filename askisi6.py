import requests
import json
import datetime
import statistics
from statistics import mode
#Φτιάχνω μία μεταβλητή με την τωρινή ημερομηνία
cur_date = datetime.datetime.now()
#Επαναλαμβάνω για 1 μήνα (31 ημέρες)
for i in range(31):
    # Υπολογίζω από τη σημερινή ημερομηνία και κάθε φορά μείον μία μέρα
    cur_date = cur_date - datetime.timedelta(days=1)
    # Μετατρέπω την ημερομηνία στη μορφή που τη θέλω για το url
    date_str = cur_date.strftime("%Y-%m-%d")
    # Παίρνω από τη διεύθυνση τα δεδομένα
    ad = requests.get(f"https://api.opap.gr/draws/v3.0/1100/draw-date/{date_str}/{date_str}")
    data = json.loads(ad.content)
    wn = []
    lst = []
    # Βρίσκω τα winningNumbers και τα βάζω σε λίστα
    for scan in data['content']:
        wn = scan.get('winningNumbers')
        lst.append(scan["winningNumbers"])
    tmp = []
    lst2 = []
    # Βάζω σε λίστα τις 20σάδες
    for scan in lst:
        tmp = scan.get('list')
        lst2.append(scan['list'])
    lst3 = []
    #Βάζω σε ενιαία λίστα όλους τους αριθμούς
    for i in lst2:
        lst3.extend(i)
    #Βρίσκω τον αριθμό που εμφανίζεται συχνότερα την κάθε μέρα
    frequent = mode(lst3)
    print("The number that appears most often in", date_str, "is: ", frequent)
