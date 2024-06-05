def main():
    time = input("What time is it? ").strip()
    time_converted = convert(time)
    if time_converted >= 7.0 and time_converted <= 8.0:
        print("breakfast time")
    elif time_converted >= 12.0 and time_converted <= 13.0:
        print("lunch time")
    elif time_converted >= 18.0 and time_converted <= 19.0:
        print("dinner time")
    else:
        return 0


def convert(time):
    if "a.m." in time:
        hour, minute = time.removesuffix(" a.m.").split(":")
        hour = float(hour)
    elif "p.m." in time:
        hour, minute = time.removesuffix(" p.m.").split(":")
        hour = 12 + float(hour)
    else:
        hour, minute = time.split(":")
        hour = float(hour)
    minute = float(minute)/60
    return hour + minute


if __name__ == "__main__":
    main()