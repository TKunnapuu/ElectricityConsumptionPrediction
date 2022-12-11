if (True):
    f = open('daylight.csv', 'r')
    uus = open('daylight_new.txt', 'w')
    for line in f:
        line = line[2:]
        line = line.split("\t")

        tunnirida_tous = line[1].split(":")[0]
        tunnirida_loojang = line[3].split(":")[0]

        ymd = line[0].split(".")
        ymd = ymd[2] + "-" + ymd[1] + "-" + ymd[0]

        uus.write(ymd+","+tunnirida_tous+","+tunnirida_loojang+"\n")
    uus.close()

    ooga = open('daylight_new.txt', 'r')
    for i in range(10):
        rida = ooga.readline()
        rida_paev = rida.split(",")[0].split(".")[0]
