while True:
    try:
        import pygeoip
        Ip_addr = input("Enter the IP address of the user: ")
        gip = pygeoip.GeoIP("GeoLiteCity.dat")
        res = gip.record_by_addr(Ip_addr)
        for key, val in res.items():
            print('%s : %s' % (key,val))
    except:
        print(f"No IP found {Ip_addr}")
