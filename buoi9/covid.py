def bai_covid():
    data = [{"total_confirmed":2572087,"total_deaths":39122,"total_recovered":2242273,"last_updated":"2022-02-15"},{"total_confirmed":2606824,"total_deaths":39188,"total_recovered":2249155,"last_updated":"2022-02-16"},{"total_confirmed":2643024,"total_deaths":39278,"total_recovered":2254965,"last_updated":"2022-02-17"},{"total_confirmed":2685463,"total_deaths":39358,"total_recovered":2261180,"last_updated":"2022-02-18"},{"total_confirmed":2685463,"total_deaths":39358,"total_recovered":2261180,"last_updated":"2022-02-19"},{"total_confirmed":2787493,"total_deaths":39501,"total_recovered":2281434,"last_updated":"2022-02-20"},{"total_confirmed":2834373,"total_deaths":39605,"total_recovered":2294669,"last_updated":"2022-02-21"},{"total_confirmed":2890522,"total_deaths":39682,"total_recovered":2305081,"last_updated":"2022-02-22"},{"total_confirmed":2890522,"total_deaths":39682,"total_recovered":2305081,"last_updated":"2022-02-23"},{"total_confirmed":3041506,"total_deaths":39884,"total_recovered":2339784,"last_updated":"2022-02-24"},{"total_confirmed":3120301,"total_deaths":39962,"total_recovered":2355619,"last_updated":"2022-02-25"},{"total_confirmed":3219177,"total_deaths":40050,"total_recovered":2376046,"last_updated":"2022-02-26"},{"total_confirmed":3219177,"total_deaths":40050,"total_recovered":2376046,"last_updated":"2022-02-27"},{"total_confirmed":3321005,"total_deaths":40144,"total_recovered":2411912,"last_updated":"2022-02-28"}]
    fig, ax = plt.subplots(dpi=200) # tạo figure và 1 axes
    fig.suptitle("Thống kê Covid")  # đặt title cho figure
    dates = []
    total_confirmed = []
    total_deaths = []
    total_recovered = []
    width = 0.8
    for item in data:
        dates.append(datetime.fromisoformat(item["last_updated"]))
        total_confirmed.append(item["total_confirmed"])
        total_recovered.append(item["total_recovered"])
        total_deaths.append(item["total_deaths"])
    total_confirmed = npy.array(total_confirmed)
    total_deaths = npy.array(total_deaths)
    total_recovered = npy.array(total_recovered)
    print(total_confirmed)
    ax.bar(dates, total_confirmed, width)
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    myFmt = mdates.DateFormatter('%d/%m')
    ax.xaxis.set_major_formatter(myFmt)
    ax.bar(dates, total_recovered, width,bottom=total_confirmed)
    ax.bar(dates, total_deaths, width,bottom=total_recovered + total_confirmed)
    fig.autofmt_xdate()
    plt.show()    
    
bai_covid()