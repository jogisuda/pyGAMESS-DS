import os

log = open(r"C:/LOG_pyGAMESS-DataScan.txt", "w")

for (root, dirs, files) in os.walk(".", topdown=True):
    num_files = int ((len(files) - 1)/2) #files - 1 para excluir o proprio bot
    for n in range(1, num_files + 1):
        print("[*] Analizando E{} - G{}".format(n, n))
        log.write("############### START OF E{}.out AND G{}.out #################\n".format(n, n))
        goals = [0, 0, 0, 0, 0, 0]
        lines = [None] * 6
        geometry = ""

        GCV = []
        GCV_flag = 0

        GEOMETRY = []
        GEOMETRY_flag = 0

        FREQIN_flag = 0
        line_number = 0

        NET_CHARGE = []
        NET_CHARGE_LAST = -1
        for j in range(2):
            if j == 0:
                f = "E" + str(n) + ".out"
            else:
                f = "G" + str(n) + ".out"
            with open(f, "r") as file:
                for line in file:
                    if GCV_flag > 0:
                        if GCV_flag == 9: #critério de parada
                            GCV_flag = 0
                            lines[3] = GCV
                            continue
                        GCV.append(line)
                        GCV_flag += 1
                        
                    if GEOMETRY_flag > 0:
                        if line == "\n": #critério de parada
                            GEOMETRY_flag = 0
                            GEOMETRY.append("\n")
                            lines[0] = GEOMETRY
                            continue
                        GEOMETRY.append(line.strip())
                    for i in range(6):
                        if goals[i] == 0:
                            if i == 0:
                                if "EQUILIBRIUM GEOMETRY LOCATED" in line:
                                    GEOMETRY.append(line)
                                    GEOMETRY_flag = 1
                                    goals[i] = 1
                                    #doStuff
                            if i == 1 and f.startswith("E"):
                                if "TOTAL FREE ENERGY IN SOLVENT" in line:
                                    lines[i] = line
                                    goals[i] = 1
                                    #doStuff
                            if i == 2:
                                if "TOTAL INTERACTION (DELTA + ES + CAV + DISP + REP)" in line:
                                    lines[i] = line
                                    goals[i] = 1
                                    #doStuff
                            if i == 3:
                                if "G         CV" in line:
                                    GCV.append(line)
                                    GCV_flag = 1
                                    goals[i] = 1
                                    #doStuff
                            if i == 4:
                                if "FREQUENCY" in line:
                                    lines[i] = line
                                    goals[i] = 1
                                    #doStuff
                            if i == 5:
                                #goals[i] = 1
                                lines[i] = ""
                                if "NET CHARGES:" in line: #ler backwards
                                    NET_CHARGE_LAST = line_number #pegar a última NET CHARGE
                    line_number += 1
                #line_number = 0
                #NET_CHARGE_LAST = -1

        f = open("E" + str(n) + ".out", "r")
        lines_aux = f.readlines()
        while bool(lines_aux[NET_CHARGE_LAST].strip()) != False:
            NET_CHARGE.append(lines_aux[NET_CHARGE_LAST].strip())
            NET_CHARGE_LAST += 1
        lines[5] = NET_CHARGE
        f.close()

        if goals[0] == 0:
            lines[0] = "[ - ] GEOMETRY NOT LOCATED\n"


        for l in lines:
            if isinstance(l, str):
                log.write(l.lstrip() + "\n")
            else:
                for ll in l:
                    log.write(ll + "\n")
        log.write("############### END OF E{}.out AND G{}.out #################\n\n\n".format(n, n))
log.close()

