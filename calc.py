flag = True

while flag:
  print('Я готов считать! \nВведи числа, например "10.5"\n')
  reg = input('Конверт в регу %: ')
  dep = input('Конверт в деп %: ')
  cpa = input('Сумма выплаты в $: ')

  while type(reg) != float and type(dep) != float and type(cpa) != float:
    try:
      reg = float(reg)
      dep = float(dep)
      cpa = float(cpa)
    except ValueError:
      print('Ошибка ввода. Введите только числа заново:')
      reg = input('Конверт в регу %: ')
      dep = input('Конверт в деп %: ')
      cpa = input('Сумма выплаты в $: ')

  inst_in_reg = 100 / reg
  reg_in_dep = 100 / dep
  inst_in_dep = reg_in_dep * inst_in_reg

  print()
  print('Количество инсталлов на 1 деп = ', round(inst_in_dep))
  roi_null = cpa / inst_in_dep
  print('Максимальная цена инсталла для ROI 0% = ', round(roi_null, 2), '$')
  roi_sto = roi_null / 2
  print('Максимальная цена инсталла для ROI 100% = ', round(roi_sto, 2), '$')
  print('Рассчеты завершены.')
  print()









