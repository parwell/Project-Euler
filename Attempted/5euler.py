num = 20
while True:
 if num % 20 == 0:
  if num % 19 == 0:
   if num % 18 == 0:
    if num % 17 == 0:
     if num % 16 == 0:
      if num % 15 == 0:
       if num % 14 == 0:
        if num % 13 == 0:
         if num % 12 == 0:
          if num % 11 == 0:
           print(num)
          num += 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12 * 11
          print('----------')
         num += 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12
         print('999999999')
        num += 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13
        print('88888888')
       num += 20 * 19 * 18 * 17 * 16 * 15 * 14
       print('7777777')
      num += 20 * 19 * 18 * 17 * 16 * 15
      print('666666')
     num += 20 * 19 * 18 * 17 * 16
     print('55555')
    num += 20 * 19 * 18 * 17
    print('4444')
   num += 20 * 19 * 18
   print('333')
  num += 20 * 19
  print('22')
 num += 20
 print('1')
