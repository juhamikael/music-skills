# Genre-Specific Best Practices

Detailed prompting strategies for five common genre families. For any other genre, and for subgenre detail on these, read `${CLAUDE_PLUGIN_ROOT}/genres/[genre]/README.md` → "Suno Prompt Keywords"; every genre the plugin knows has one.

The Exclude Styles tables list candidates. Use one only when the track's arrangement really is the one named, check it against the Style Box (an exclusion must not name something the prompt asks for), and keep to the 2–4 item limit.

---

## Hip-Hop

**Vocals**: Clear enunciation, rhythmic delivery, confident
**Beat**: Specific drum sounds, matched to the style (sampled breaks and crisp snare for boom-bap; 808 kick and fast hi-hats for trap)
**Tempo**: 70-100 BPM for laid-back, 100-140 for energetic
**Production**: Vocal upfront, beat as foundation

**Example prompt**:
```
Male rapper, clear delivery, storytelling flow. Boom-bap hip-hop,
sampled drum break, vinyl crackle, dusty piano loop. Warm, unpolished mix.
```

**Key instruments**:
- Kick, snare, hi-hats, 808 bass
- Piano, strings, vocal samples
- Minimal (let vocals breathe)

### Exclude Styles

| Arrangement | Exclusions |
|-------------|------------|
| Boom-bap | `autotune, synths` |
| Lo-fi | `live drums, electric guitar` |
| Trap | `live instruments, acoustic guitar` |

---

## Alternative Rock

**Vocals**: Passionate, dynamic (quiet verse / loud chorus)
**Guitars**: Specify clean vs distorted, tone
**Energy**: Build from verse to chorus
**Production**: Live feel, room ambience

**Example prompt**:
```
Male baritone, emotional delivery, dynamic range. Alternative rock,
clean guitar in verses, distorted chorus, driving bass, tight drums.
Modern production with live energy.
```

**Key instruments**:
- Electric guitar (clean/distorted), bass, drums
- Organ, keys (optional)
- Live feel, energy

### Exclude Styles

| Arrangement | Exclusions |
|-------------|------------|
| Acoustic version | `electric guitar, drums` |
| Stripped-down | `synths, backing vocals` |
| Unplugged | `electric instruments, programmed drums` |

---

## Electronic

**Vocals**: Often processed (reverb, delay, vocoder)
**Synths**: Describe texture (warm analog, cold digital, pad, lead)
**Rhythm**: Programmed drums, quantized or swing
**Production**: Layered, atmospheric, effects

**Example prompt**:
```
Female alto, ethereal, breathy vocals. Downtempo electronic,
warm analog synths, sub-bass, crisp programmed drums.
Atmospheric production, spacious reverb.
```

**Key instruments**:
- Synths (analog, digital, pads, leads)
- Programmed drums, sub-bass
- Layers, textures, effects

### Exclude Styles

| Arrangement | Exclusions |
|-------------|------------|
| Ambient | `drums, electric guitar` |
| Minimal | `acoustic instruments, live drums` |
| Downtempo | `live drums, electric guitar` |

For a track with no singing, set `Instrumental: On` rather than excluding `vocals`: an exclusion only shifts the odds, and on a track with lyrics it works against the Lyrics Box.

---

## Folk/Indie

**Vocals**: Conversational, intimate, natural
**Instruments**: Acoustic, organic
**Arrangement**: Sparse, room for vocals
**Production**: Minimal, natural ambience

**Example prompt**:
```
Male tenor, intimate storytelling, conversational. Indie folk,
fingerpicked acoustic guitar, subtle upright bass, light brushed drums.
Natural room sound, minimal production.
```

**Key instruments**:
- Acoustic guitar, banjo, mandolin
- Upright bass, light percussion
- Organic, room ambience

### Exclude Styles

| Arrangement | Exclusions |
|-------------|------------|
| Sparse/intimate | `drums, electric instruments` |
| Solo acoustic | `drums, electric instruments, harmony vocals` |
| Full band | `synths, electric guitar` |

---

## Country

**Vocals**: Twang optional, clear storytelling
**Instruments**: Steel guitar, fiddle, acoustic
**Rhythm**: Straight or shuffle feel
**Production**: Natural, warm, organic

**Example prompt**:
```
Male baritone, warm twang, clear storytelling. Traditional country,
steel guitar, acoustic rhythm, walking bass. Classic Nashville production.
```

**Key instruments**:
- Steel guitar, fiddle, acoustic
- Walking bass, light drums
- Warm, organic

### Exclude Styles

| Arrangement | Exclusions |
|-------------|------------|
| Traditional | `synths, drum machine` |
| Acoustic | `drums, electric guitar` |
| Bluegrass | `drums, electric guitar, synths` |

Don't exclude `electric instruments` from a country prompt that asks for steel guitar: pedal steel is one, and the exclusion pulls against the prompt.

---

## Production Direction Reference

### Mix Style

| Term | Effect |
|------|--------|
| Clean production | Polished, professional, clear separation |
| Lo-fi | Vintage, tape hiss, warm distortion |
| Raw | Unpolished, garage band, live feel |
| Polished | Radio-ready, compressed, loud |
| Atmospheric | Spacious, reverb, ambient |

### Era/Vintage

- "80s production" - gated reverb, synths, big drums
- "90s grunge" - raw, mid-heavy, distorted
- "Modern pop" - compressed, bright, wide stereo
- "Vintage soul" - warm, analog, tape saturation

### Dynamic Range

- "Dynamic range" - loud/soft variation (ballads, emotional arcs)
- "Compressed" - consistent volume (pop, radio)
- "Punchy" - impactful transients (rock, hip-hop)

---

## Voice Type Reference

| Term | Range | Best For |
|------|-------|----------|
| Soprano | High female | Pop, musical theater, operatic |
| Alto | Low female | Jazz, soul, folk |
| Tenor | High male | Pop, rock, R&B |
| Baritone | Mid male | Rock, country, spoken word |
| Bass | Low male | Blues, gospel, deep storytelling |

## Vocal Delivery

| Style | Effect | Use For |
|-------|--------|---------|
| Gritty | Raw, textured | Rock, grunge, blues |
| Smooth | Polished, clean | Pop, R&B, jazz |
| Raspy | Worn, emotional | Country, rock, soul |
| Breathy | Intimate, soft | Indie, folk, bedroom pop |
| Powerful | Commanding, strong | Anthems, ballads, gospel |
| Conversational | Natural, storytelling | Folk, hip-hop, indie |

---

## Artist Name Warning

**NEVER use real artist names in Suno style prompts** - Suno rewrites them into styles of its own choosing, and the plugin's Artist Names gate blocks the track before that. Full list with alternatives: `${CLAUDE_PLUGIN_ROOT}/reference/suno/artist-blocklist.md`.

Instead, describe the artist's style:

| Don't Write | Write Instead |
|-------------|---------------|
| "NIN style" | "dark industrial, grinding synths, distorted vocals" |
| "Carly Rae Jepsen" | "upbeat synth-pop, 80s-influenced, breathy female vocals" |
| "Ministry influence" | "aggressive industrial rock, rapid-fire percussion, distorted" |
| "Johnny Cash" | "deep baritone, traditional country, train-beat rhythm" |
