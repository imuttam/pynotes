word = 'methionylthreonylthreonylglutaminylalanyl...isoleucin'
hist = dict()

for ch in word:
    if ch not in hist:
        hist[ch] = 1
    else:
        hist[ch] += 1

print(hist)

hist_new = dict()
for ch in word:
    hist_new[ch] = hist_new.get(ch, 0) + 1
print(hist_new)