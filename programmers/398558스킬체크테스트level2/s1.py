def solution(cacheSize, cities):
    cache = []
    ans = 0
    for i in range(len(cities)):
        city = cities[i].upper()
        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                ans += 5
            else:
                cache = cache[:cache.index(city)] + cache[cache.index(city)+1:] + [city]
                ans += 1
        else:
            ans += 5
    return ans