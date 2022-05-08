lam = 0
for index in range(10):
    led.unplot(lam - 1, 0)
    led.plot(lam, 0)
    lam += 1
    basic.pause(500)