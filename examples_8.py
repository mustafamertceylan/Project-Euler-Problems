def findMax(strOfNumber):
    # strOfNumber'ın bir string (rakam dizisi) olduğunu varsayıyoruz
    
    maxMultiplaction = 0  # Maksimum çarpım 1 değil, 0'dan başlamalı (çünkü 0 basamağı olabilir)
    maksList = []         # Maksimum çarpıma ait 13 basamaklı listeyi tutar
    N = len(strOfNumber)  # Sayı dizisinin toplam uzunluğu

    # Dış döngü, 13 basamaklı bloğun başlangıç indeksi (indexofNumber) için döner.
    # En son geçerli başlangıç indeksi N - 13 olmalıdır.
    for indexofNumber in range(N - 13 + 1):
        
        tempMultiplaction = 1
        tempList = [] # Her yeni blok için tempList'i boş liste olarak başlat

        # İç döngü, başlangıç (indexofNumber) noktasından itibaren 13 basamağı alır
        for i in range(13):
            # Basamağın gerçek indeksi: başlangıç indeksi + i. sıra
            current_index = indexofNumber + i 
            digit = int(strOfNumber[current_index])
            
            # Çarpımı ve listeyi oluştur
            tempMultiplaction *= digit
            tempList.append(digit) # .append() ile listeye eleman ekle

        # Maksimum kontrolü
        if tempMultiplaction >= maxMultiplaction:
            maxMultiplaction = tempMultiplaction
            # maksList'e atama yaparken listenin kopyasını almalısınız!
            # Yoksa bir sonraki döngüde tempList değişince maksList de değişir.
            maksList = tempList.copy() 
            
    # Sonuçları ekrana yazdır
    print(f"Maksimum Basamaklar: {maksList}")
    print(f"Maksimum Çarpım: {maxMultiplaction}")

    
numberofText="""73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989343380308135336276614282806444486645238749303590729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""
Mynumber=int(numberofText)
findMax(numberofText)


            

