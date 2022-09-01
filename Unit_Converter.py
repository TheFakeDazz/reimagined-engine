"""
This is a Unit Converter which converts certain units to another.
"""


def screet(equation, unit):
    total = equation
    print(f"{total:f} {unit}")
    quit()


def unit_converter():
    """
The main function for this
    """
    while True:

        choose = input(
            'Type "quit" to exit out\nTemperature, Measurement, or Time?: '
        ).lower()
        if choose not in ['temperature', 'measurement', 'time', 'quit']:
            print('Please enter a valid category')
            continue
        # Units of Temperature
        while choose == 'temperature':
            degrees_entrance = input(
                'For Celsius, type "c"\nFor Fahrenheit, type "f"\nType "quit" to exit out\nEnter what you want to '
                'convert: ')
            if degrees_entrance == "quit":
                break
            elif degrees_entrance not in ['c', 'f']:
                print('Please enter a valid temperature unit')
                continue

            # Fahrenheit
            if degrees_entrance == 'f':
                while True:
                    try:
                        enter_amount = float(input("Enter the amount of you would like to convert: "))
                        screet((enter_amount - 32) / 1.8, 'C')
                    except ValueError:
                        print('Please enter a number')

            # Celsius
            elif degrees_entrance == 'c':
                while True:
                    try:
                        enter_amount = float(input("Enter the amount of you would like to convert: "))
                        screet(enter_amount * 1.8 + 32, 'F')
                    except ValueError:
                        print('Please enter a number')

        # Units of Measurement
        while choose == 'measurement':
            measure_entrance = input(
                'For centimeters, type "centi"\nFor millimeters, type "milli"\nFor feet, type "feet"\nFor Kilometers, '
                'type "kilometer"\nFor inches, type "inch"\nType "quit" to exit out\nEnter What you want to convert: '
                '').lower()
            if measure_entrance == 'quit':
                break
            # Inches
            if measure_entrance == "inch":
                to_what = input(
                    'For centimeters, type "centi"\nFor millimeters, type "milli"\nFor feet, type "feet"\nFor '
                    'Kilometers, type "kilometer"\nType "quit" to exit out\nTo What?: '
                ).lower().strip()
                if to_what == "quit":
                    break
                if to_what not in ['centi', 'milli', 'feet', 'kilometer']:
                    print('Please Enter a Valid Conversion Unit')
                    continue
                # Converting Inches to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(input("Enter the amount of inches "
                                                       "you would like to convert into centimeters: "))
                            screet(enter_amount * 2.56, 'cm')
                        except ValueError:
                            print('Please enter a number')

                # Converting Inches to Millimeters
                if to_what == "milli":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of inches you would like to convert into millimeters: "))
                            screet(enter_amount * 25.4, 'mm')
                        except ValueError:
                            print('Please enter a number')

                # Converting Inches to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(input(
                                "Enter the amount of inches you would like to convert into feet: "))
                            screet(enter_amount / 12, 'ft')
                        except ValueError:
                            print('Please enter a number')

                # Converting Inches to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of inches you would like to convert into centimeters: "))
                            screet(enter_amount * .0000254, 'km')
                        except ValueError:
                            print('Please enter a number')

            # Centimeters
            if measure_entrance == "centi":
                to_what = input('For inches, type "inch"\nFor millimeters, type "milli"\nFor feet, type "feet"\nFor '
                                'Kilometers, type "kilometer"\nType "quit" to exit out\nTo What?: ').lower().strip()
                if to_what == "quit":
                    break
                if to_what not in ['inch', 'milli', 'feet', 'kilometer']:
                    print('Please Enter a Valid Conversion Unit')
                    continue
                # Converting centi to inches
                if to_what == 'inch':
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of centimeters you would like to convert into inches: "))
                            screet(enter_amount * .3937, 'in')
                        except ValueError:
                            print('Please enter a number')

                # Converting Centimeters to Millimeters
                if to_what == 'milli':
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of centimeters you would like to convert into millimeters: "))
                            screet(enter_amount * 10, 'mm')
                        except NameError:
                            print('Please enter a number')

                # Converting Centimeters to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of centimeters you would like to convert into feet: "))
                            screet(enter_amount / 30.48, 'ft')
                        except NameError:
                            print('Please enter a number')

                # Converting Centimeters to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(input(
                                "Enter the amount of centimeters you would like to convert into kilometers: "))
                            screet(enter_amount * .00001, 'km')
                        except NameError:
                            print('Please enter a number')

            # Millimeters
            if measure_entrance == "milli":
                to_what = input(
                    'For inches, type "inch"\nFor centimeters, type "centi"\nFor feet, type "feet"\nFor '
                    'Kilometers, type "kilometer"\nType "quit" to exit out\nTo What?: '
                ).lower().strip()
                if to_what == "quit":
                    break
                if to_what not in ['kilometer', 'centi', 'feet', 'inch']:
                    print('Please Enter a Valid Conversion Unit')
                    continue
                # Converting Millimeters to Inches
                if to_what == "inch":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of millimeters you would like to convert into inches: "))
                            screet(enter_amount * 25.4, 'in')
                        except ValueError:
                            print('Please enter a number')

                # Converting Millimeters to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of millimeters you would like to convert into centimeters: "))
                            screet(enter_amount / 10, 'cm')
                        except ValueError:
                            print('Please enter a number')

                # Converting Millimeters to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of millimeters you would like to convert into feet: "))
                            screet(enter_amount / 304.8, 'ft')
                        except ValueError:
                            print('Please enter a number')

                # Converting Millimeters to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of millimeters you would like to convert into kilometers: "))
                            screet(enter_amount * .00001, 'km')
                        except ValueError:
                            print('Please enter a number')

            # Feet
            if measure_entrance == "feet":
                to_what = input(
                    'For inches, type "inch"\nFor centimeters, type "centi"\nFor millimeters, type "milli"\nFor '
                    'Kilometers type "kilometer"\nType "quit" to exit out\nTo What?: '
                ).lower().strip()
                if to_what == "quit":
                    break
                if to_what not in ['kilometer', 'centi', 'milli', 'inch']:
                    print('Please Enter a Valid Conversion Unit')
                    continue
                # Converting Feet to Inches
                if to_what == "inch":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of feet you would like to convert into inches: "))
                            screet(enter_amount * 12, 'in')
                        except ValueError:
                            print('Please enter a number')

                # Converting Feet to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of feet you would like to convert into centimeters: "))
                            screet(enter_amount * 30.48, 'cm')
                        except ValueError:
                            print('Please enter a number')

                # Converting Feet to Millimeters
                if to_what == "milli":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of feet you would like to convert into millimeters: "))
                            screet(enter_amount * 304.8, 'mm')
                        except ValueError:
                            print('Please enter a number')

                # Converting feet to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of feet you would like to convert into kilometers: "))
                            screet(enter_amount / 3280.8399, 'km')
                        except ValueError:
                            print('Please enter a number')

            # Kilometer
            if measure_entrance == "kilometer":
                to_what = input(
                    'For inches, type "inch"\nFor centimeters, type "centi"\nFor millimeters, type "milli"\nFor '
                    'feet, type "feet"\nType "quit" to exit out\nTo What?: '
                ).lower().strip()
                if to_what == "quit":
                    break
                if to_what not in ['feet', 'centi', 'milli', 'inch']:
                    print('Please Enter a Valid Conversion Unit')
                    continue
                # Converting Kilometer to Inches
                if to_what == "inch":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of kilometers you would like to convert into inches: "))
                            screet(enter_amount * 39370.0787, 'in')
                        except ValueError:
                            print('Please enter a number')

                # Converting Kilometer to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of kilometers you would like to convert into centimeters: "))
                            screet(enter_amount * 100000, 'cm')
                        except ValueError:
                            print('Please enter a number')

                # Converting Kilometer to Millimeters
                if to_what == "milli":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of kilometers you would like to convert into millimeters: "))
                            screet(enter_amount * 1000000, 'mm')
                        except ValueError:
                            print('Please enter a number')

                # Converting Kilometer to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(
                                input("Enter the amount of kilometers you would like to convert into feet: "))
                            screet(enter_amount * 3280.8399, 'ft')
                        except ValueError:
                            print('Please enter a number')

        # Units of Time
        while choose == 'time':
            time_entrance = input(
                'For hours, type "hours"\nFor minutes, type "minute"\nFor days, type "days"\nFor seconds, '
                'type "seconds"\nType "quit" to exit out\nEnter what you want to convert: '
            )

            # Hours
            while True:
                if time_entrance == "hours":
                    to_what = input(
                        'For minutes, type "minute"\nFor days, type "days"\nFor seconds, type "seconds"\nType "quit" '
                        'to exit out\nTo What?: ').lower().strip()
                    if to_what == "quit":
                        break
                    if to_what not in ['minute', 'days', 'seconds' 'quit']:
                        print('Please Enter a Valid Conversion Unit')
                        continue
                    # Converting hours to minutes
                    if to_what == "minute":
                        while True:
                            try:
                                enter_amount = float(input("Enter the hours you would like to convert into minutes: "))
                                screet(enter_amount * 60, 'minute')
                            except ValueError:
                                print('Please enter a number')

                    # Converting hours to days
                    if to_what == "days":
                        while True:
                            try:
                                enter_amount = float(input("Enter the hours you would like to convert into days: "))
                                screet(enter_amount / 24, 'days')
                            except ValueError:
                                print('Please enter a number')

                    # Converting hours to seconds
                    if to_what == "seconds":
                        while True:
                            try:
                                enter_amount = float(
                                    input("Enter the hours you would like to convert into seconds: "))
                                screet(enter_amount * 3600, 'seconds')
                            except ValueError:
                                print('Please enter a number')

                # Minutes
                if time_entrance == "minute":
                    to_what = input(
                        'For hours, type "hours"\nFor days, type "days"\nFor seconds, type "seconds"\nType "quit" to '
                        'exit out\nTo What?: ').lower().strip()
                    if to_what == "quit":
                        break
                    if to_what not in ['seconds', 'days', 'hours', 'quit']:
                        print('Please Enter a Valid Conversion Unit')
                        continue
                    # Converting minutes to hours
                    if to_what == "hours":
                        while True:
                            try:
                                enter_amount = float(input("Enter the minutes you would like to convert into hours: "))
                                screet(enter_amount / 60, 'hours')
                            except ValueError:
                                print('Please enter a number')

                    # Converting minutes to days
                    if to_what == "days":
                        while True:
                            try:
                                enter_amount = float(input("Enter the minutes you would like to convert into days: "))
                                screet(enter_amount / 1440, 'day(s)')
                            except ValueError:
                                print('Please enter a number')

                    # Converting minutes to seconds
                    if to_what == "seconds":
                        while True:
                            try:
                                enter_amount = float(input("Enter the minutes you would like to convert into seconds: "))
                                screet(enter_amount * 60, 'seconds')
                            except ValueError:
                                print('Please enter a number')

                # Seconds
                if time_entrance == "seconds":
                    to_what = input(
                        'For hours, type "hours"\nFor days, type "days"\nFor minutes, type "minute"\nType "quit" to '
                        'exit out\nTo What?: ').lower().strip()
                    if to_what == "quit":
                        break
                    if to_what not in ['minute', 'days', 'hours', 'quit']:
                        print('Please Enter a Valid Conversion Unit')
                        continue
                    # Converting seconds to hours
                    if to_what == "hours":
                        while True:
                            try:
                                enter_amount = float(input("Enter the seconds you would like to convert into hours: "))
                                screet(enter_amount / 3600, 'hours')
                            except ValueError:
                                print('Please enter a number')

                    # Converting seconds to days
                    if to_what == "days":
                        while True:
                            try:
                                enter_amount = float(input("Enter the seconds you would like to convert into days: "))
                                screet(enter_amount / 86400, 'day(s)')
                            except ValueError:
                                print('Please enter a number')

                    # Converting seconds to minutes
                    if to_what == "minute":
                        while True:
                            try:
                                enter_amount = float(input("Enter the seconds you would like to convert into minutes: "))
                                screet(enter_amount / 60, 'minutes')
                            except ValueError:
                                print('Please enter a number')

                # Days
                if time_entrance == "days":
                    to_what = input(
                        'For hours, type "hours"\nFor seconds, type "seconds"\nFor minutes, type "minute"\nType '
                        '"quit" to '
                        'exit out\nTo What?: '
                    ).lower().strip()
                    if to_what == "quit":
                        break
                    if to_what not in ['minute', 'seconds', 'hours', 'quit']:
                        print('Please Enter a Valid Conversion Unit')
                        continue
                    # Converting Days to hours
                    if to_what == "hours":
                        while True:
                            try:
                                enter_amount = float(input("Enter the days you would like to convert into hours: "))
                                screet(enter_amount * 24, 'hours')
                            except ValueError:
                                print('Please enter a number')

                    # Converting days to seconds
                    if to_what == "seconds":
                        while True:
                            try:
                                enter_amount = float(input("Enter the days you would like to convert into seconds: "))
                                screet(enter_amount * 86400, 'seconds')
                            except ValueError:
                                print('Please enter a number')

                    # Converting days to minutes
                    if to_what == "minute":
                        while True:
                            try:
                                enter_amount = float(input("Enter the days you would like to convert into minutes: "))
                                screet(enter_amount * 1440, 'minutes')
                            except ValueError:
                                print('Please enter a number')

        if choose == "quit":
            break


unit_converter()
