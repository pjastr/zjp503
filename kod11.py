try:
    x = int(input("Podaj liczbe x"))
    y = int(input("Podaj liczbe y"))
    print("dzielenie=", x/y)
except ValueError:
    print("Błędna wartość!")
except ZeroDivisionError:
    print("Dzielenie przez zero!")
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
