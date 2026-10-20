"""Generate the 60s background track (synth pad + beat + UI sound cues) as music.wav."""
import numpy as np, wave
SR = 44100; DUR = 60.0; N = int(SR * DUR)
t = np.arange(N) / SR
out = np.zeros(N)
BEAT = 60 / 100  # 100 BPM
BAR = BEAT * 4
note = lambda m: 440 * 2 ** ((m - 69) / 12)
CHORDS = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]  # Am F C G

def env(n, a, r):
    e = np.ones(n); ai = int(a * SR); ri = int(r * SR)
    e[:ai] = np.linspace(0, 1, ai); e[-ri:] *= np.linspace(1, 0, ri); return e

def add(sig, start):
    i = int(start * SR); j = min(N, i + len(sig)); out[i:j] += sig[:j - i]

def tone(freq, dur, harm=(1, .5, .25), detune=0.0):
    tt = np.arange(int(dur * SR)) / SR
    s = sum(a * np.sin(2 * np.pi * freq * (k + 1) * tt * (1 + detune)) for k, a in enumerate(harm))
    return s

# pad
bar = 0
while bar * BAR < DUR:
    ch = CHORDS[bar % 4]; st = bar * BAR
    for m in ch:
        s = (tone(note(m), BAR + .4) + tone(note(m), BAR + .4, detune=.003)) * .5
        add(s * env(len(s), .6, .6) * .05, st)
    b = tone(note(ch[0] - 12), BAR, (1, .3)); add(b * env(len(b), .02, .5) * .09 * (st >= 12), st)
    bar += 1

# drums & arp
for k in range(int(DUR / BEAT)):
    st = k * BEAT
    if st >= 12.3 and st < 57.5:
        n = int(.35 * SR); tt = np.arange(n) / SR
        kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9)
        add(kick * .35, st)
    if st >= 17 and st < 57.5:
        for half in (0, BEAT / 2):
            n = int(.06 * SR); hat = np.random.randn(n) * np.exp(-np.arange(n) / SR * 70)
            hat = np.diff(hat, prepend=0)
            add(hat * (.05 if half else .03), st + half)
    if st >= 17 and st < 56:
        ch = CHORDS[int(st / BAR) % 4]
        for q in range(2):
            m = ch[(k * 2 + q) % 3] + 12
            p = tone(note(m), .3, (1, .2)); add(p * env(len(p), .005, .25) * .045, st + q * BEAT / 2)

# whooshes on reveal / CTA
for w in (12.0, 55.8):
    n = int(1.0 * SR); x = np.random.randn(n); x = np.convolve(x, np.ones(40) / 40, 'same')
    add(x * np.sin(np.linspace(0, np.pi, n)) ** 2 * .5, w)
# message pops & strike clicks
for p in (22.5, 24.0, 26.2, 30.8, 32.2, 33.6, 38.8, 4.0, 4.4, 4.8):
    n = int(.15 * SR); tt = np.arange(n) / SR
    f = 1400 if p > 10 else 500
    add(np.sin(2 * np.pi * f * tt * (1 + tt * 3)) * np.exp(-tt * 30) * .25, p)

fade = np.ones(N); fade[:int(.5 * SR)] = np.linspace(0, 1, int(.5 * SR)); fade[-int(2.5 * SR):] = np.linspace(1, 0, int(2.5 * SR))
out *= fade
out = out / np.max(np.abs(out)) * .89
st = np.stack([out, out], 1)
with wave.open('music.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes())
