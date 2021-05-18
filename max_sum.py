""" Task:
  Finding the maximum sum of the numbers in the list given to us,
   an adjacent sub-array.

Test1 : Liste = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  Sonuc = 6
Test 2: Liste = [] Sonuc = 0
Test 3: Liste= [-2,-4,-15,-6,-9,-27] Sonuc = -2
Test 4: Liste = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43] 
Sonuc = 155 """

liste = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
def max_sum(liste):
  toplam=[]
  if len(liste)==0:
    return 0
  for i in range(len(liste)):
    for j in range(i+1):
      x=sum(liste[j:i+1])
      toplam.append(x)
  return max(toplam)

print(max_sum(liste))
