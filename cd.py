while 1==1:
    def cd(cd="/home/user",kod= input("cd ")):
        yeni_kod=[1]
        sayi = 0
        for a in kod:  #yan-yana olan '/' isaresini silmek meselen:'///'->'/'
            if sayi<len(yeni_kod):
                if a!=yeni_kod[sayi]:
                    yeni_kod.append(a)

                if a==yeni_kod[sayi] and a!='/':
                    yeni_kod.append(a)
            sayi += 1

        yeni_kod=''.join(yeni_kod[1:])
        cd=cd.split('/')
        yeni_kod=yeni_kod.split('/')
        # for k in range(len(yeni_kod)):
        #     if yeni_kod[k]=='':
        #         cd='/'
        #         return print(cd)
        for i in yeni_kod:
            if len(yeni_kod)==1:
                # i=i.split()
                if bool(i)==False:
                    return print(cd)
                elif i[0]=='-':
                    pass
                elif i == "..":
                    cd = cd[:-1]
                    return print('/'.join(cd))
                elif i == '.':
                    cd = cd
                    return print('/'.join(cd))
                else:
                    continue
                    # if bool(i):
                    #     cd.append(i[0])
                    #     return print('/'.join(cd))

            if i=="..":
                cd=cd[:-1]
            elif i=='.':
                cd=cd
            else:
                cd.append(i)
        return print('/'.join(cd))
    cd()
    cixis=input("cixmaq icin 'q' herfine basin :")
    if cixis=='q':
        break