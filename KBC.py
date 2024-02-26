
#que = {'\nWhat is the capital city of Nepal? ': 'kathmandu', '\nWho  is the President of Nepal?' : 'bidya devi bhandari', '\nWhat is the national flower of nepal? ': 'rhododendon', '\nWhere is Mt. Everest Located? ': 'nepal'}


#BY LIST
que = ['\nWhat is the capital city of Nepal? ', '\nWho  is the President of Nepal?', '\nWhat is the national flower of nepal? ', '\nWhere is Mt. Everest Located? ']

ans = ['kathmandu', 'bidya devi bhandari', 'rhododendon', 'nepal']

count = 0
j = 0
for i in que:
    print(i)
    response = input("Ans: ")
    check = ans[j];
    j += 1
    if response == check.lower():
        count += 1
    else:
        break



Total = 1000;
for j in range (count):
    Total = Total *10;

if count == 0: 
    print(f"\nSorry Wrong Answer!!!\nNumber of que solved: {count}\nTotal Amount: 0")
elif(count != len(que)):
    print(f"\nSorry Wrong Answer!!!\nNumber of que solved: {count}\nTotal Amount: {Total}")
else:
    print(f"\nCONRATULATIONS!!!\nNumber of que solved: {count}\nTotal Amount: {Total}")
