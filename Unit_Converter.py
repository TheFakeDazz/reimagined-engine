"""
This is a Unit Converter which converts certain units to another.
"""


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
                        degrees_f = float(input('Enter the degrees: '))
                    except ValueError:
                        print('Please enter a number')
                    else:
                        total = (degrees_f - 32) * 5 / 9
                        print(f'{total} C')
                        return

            # Celsius
            elif degrees_entrance == 'c':
                while True:
                    try:
                        degrees_c = float(input('Enter the degrees: '))
                    except ValueError:
                        print('Please enter a number')
                    else:
                        total = degrees_c * 9 / 5 + 32
                        print(f'{total} F')
                        return

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
                            enter_amount = float(
                                input(
                                    "Enter the amount of inches you would like to convert into centimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 2.56
                            print(f"{total} cm")
                            return

                # Converting Inches to Millimeters
                if to_what == "milli":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of inches you would like to convert into millimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 25.4
                            print(f"{total} mm")
                            return
                # Converting Inches to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of inches you would like to convert into feet: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount / 12
                            print(f"{total} ft")
                            break
                # Converting Inches to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of inches you would like to convert into centimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * .0000254
                            print(f"{total:f} km")
                            return
            # Centimeters
            if measure_entrance == "centi":
                to_what = input(
                    'For inches, type "inch"\nFor millimeters, type "milli"\nFor feet, type "feet"\nFor '
                    'Kilometers, type "kilometer"\nType "quit" to exit out\nTo What?: '
                ).lower().strip()
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
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * .3937
                            print(f"{total} in")
                            return

                # Converting Centimeters to Millimeters
                if to_what == 'milli':
                    while True:
                        try:
                            enter_amount = eval(
                                input("Enter the amount of centimeters you would like to convert into millimeters: "))
                        except NameError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 10
                            print(f"{total} mm")
                            return

                # Converting Centimeters to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = eval(
                                input("Enter the amount of centimeters you would like to convert into feet: "))
                        except NameError:
                            print('Please enter a number')
                        else:
                            total = enter_amount / 30.48
                            print(f"{total} ft")
                            return
                # Converting Centimeters to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = eval(input(
                                "Enter the amount of centimeters you would like to convert into kilometers: "))
                        except NameError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * .00001
                            print(f"{total:f} km")
                            return

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
                                input(
                                    "Enter the amount of millimeters you would like to convert into inches: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 25.4
                            print(f"{total} in")
                            return
                # Converting Millimeters to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of millimeters you would like to convert into centimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount / 10
                            print(f"{total} cm")
                            return
                # Converting Millimeters to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of millimeters you would like to convert into feet: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount / 304.8
                            print(f"{total:f} ft")
                            return
                # Converting Millimeters to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of millimeters you would like to convert into kilometers: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * .00001
                            print(f"{total:f} km")
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
                                input(
                                    "Enter the amount of feet you would like to convert into inches: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 12
                            print(f"{total} in")
                # Converting Feet to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of feet you would like to convert into centimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 30.48
                            print(f"{total} cm")
                            return
                # Converting Feet to Millimeters
                if to_what == "milli":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of feet you would like to convert into millimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 304.8
                            print(f"{total} mm")
                            break
                # Converting feet to Kilometers
                if to_what == "kilometer":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of feet you would like to convert into kilometers: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount / 3280.8399
                            print(f"{total:f} km")
                            return
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
                                input(
                                    "Enter the amount of kilometers you would like to convert into inches: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 39370.0787
                            print(f"{total} in")
                            break
                # Converting Kilometer to Centimeters
                if to_what == "centi":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of kilometers you would like to convert into centimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 100000
                            print(f"{total} cm")
                            return
                # Converting Kilometer to Millimeters
                if to_what == "milli":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of kilometers you would like to convert into millimeters: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 1000000
                            print(f"{total} mm")
                            return
                # Converting Kilometer to Feet
                if to_what == "feet":
                    while True:
                        try:
                            enter_amount = float(
                                input(
                                    "Enter the amount of kilometers you would like to convert into feet: "
                                ))
                        except ValueError:
                            print('Please enter a number')
                        else:
                            total = enter_amount * 3280.8399
                            print(f"{total} ft")
                            return

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
                                enter_amount = float(
                                    input(
                                        "Enter the hours you would like to convert into minutes: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount * 60
                                print(f"{total} minutes")
                                return
                    # Converting hours to days
                    if to_what == "days":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the hours you would like to convert into days: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount / 24
                                print(f"{total} day(s)")
                                return
                    # Converting hours to seconds
                    if to_what == "seconds":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the hours you would like to convert into seconds: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount * 3600
                                print(f"{total} seconds")
                                return
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
                                enter_amount = float(
                                    input(
                                        "Enter the minutes you would like to convert into hours: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount / 60
                                print(f"{total} hours")
                                return
                    # Converting minutes to days
                    if to_what == "days":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the minutes you would like to convert into days: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount / 1440
                                print(f"{total} day(s)")
                                return
                    # Converting minutes to seconds
                    if to_what == "seconds":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the minutes you would like to convert into days: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount * 60
                                print(f"{total} seconds")
                                return
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
                                enter_amount = float(
                                    input(
                                        "Enter the seconds you would like to convert into hours: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount / 3600
                                print(f"{total:f} hours")
                                return
                    # Converting seconds to days
                    if to_what == "days":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the seconds you would like to convert into days: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount / 86400
                                print(f"{total:f} day(s)")
                                return
                    # Converting seconds to minutes
                    if to_what == "minute":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the seconds you would like to convert into minutes: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount / 60
                                print(f"{total} minutes")
                                return
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
                                enter_amount = float(
                                    input(
                                        "Enter the days you would like to convert into hours: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount * 24
                                print(f"{total} hours")
                                return
                    # Converting days to seconds
                    if to_what == "seconds":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the days you would like to convert into seconds: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount * 86400
                                print(f"{total} seconds")
                                return

                    # Converting days to minutes
                    if to_what == "minute":
                        while True:
                            try:
                                enter_amount = float(
                                    input(
                                        "Enter the days you would like to convert into minutes: "
                                    ))
                            except ValueError:
                                print('Please enter a number')
                            else:
                                total = enter_amount * 1440
                                print(f"{total} minutes")
                                return

        if choose == "quit":
            break


unit_converter()
