# Lyric Writer Craft Reference

Detailed tables and reference data for the lyric-writer skill.
Read by the lyric-writer when specific craft guidance is needed.

---

## Rhyme Techniques

### Rhyme Types (use variety)
| Type | Description | Example |
|------|-------------|---------|
| Perfect | Exact match | love/dove |
| Slant/Near | Similar but not exact | love/move |
| Consonance | Same ending consonants | blank/think |
| Assonance | Same vowel sounds | lake/fate |
| Internal | Rhymes within a line | "the late train shakes the window pane" |

### Rhyme Scheme Patterns
| Pattern | Effect |
|---------|--------|
| AABB | Stable, immediate resolution |
| ABAB | Classic, delayed resolution |
| ABCB | Lighter, less pressure |
| AAAX | Strong setup, surprise ending |

### Rhyme Schemes by Genre — Quick Reference

**There is no universal default.** Each genre has its own conventions documented in `${CLAUDE_PLUGIN_ROOT}/genres/[genre]/README.md` under "Lyric Conventions." Always read the genre README before writing.

| Genre Family | Default Scheme | Rhyme Strictness | Key Difference |
|---|---|---|---|
| **Hip-Hop / Rap** | AABB (couplet) | High — multisyllabic + internal rhyme mandatory | Rhyme density throughout the bar, not just end rhymes |
| **Pop** | XAXA (conversational) | Low — near rhymes preferred | Conversational phrasing; if it sounds "crafted," it fails |
| **Rock** | XAXA or ABAB | Low — meaning > rhyme | Imagery and emotional energy over technical rhyming |
| **Punk** | AABB (loose) | Low — half-rhymes authentic | Directness, shoutable, works at 150+ BPM |
| **Metal** | Optional | Very low — can skip entirely | Concrete imagery and riff alignment over rhyme |
| **Country / Folk** | ABCB (ballad stanza) | Moderate — near rhymes OK | Storytelling; lines 2 & 4 rhyme, 1 & 3 free |
| **Blues** | AAB (3-line form) | Moderate | Line 1 stated, line 2 repeats, line 3 resolves |
| **Electronic / EDM** | Repetition > rhyme | Minimal | Less is more; single phrases looped, not verses |
| **Ambient / Lo-Fi** | None | None | Vocals are texture, not content |
| **Trip-Hop** | XAXA (loose) | Low | Most lyrical electronic genre; abstract, moody |
| **R&B / Soul** | Flexible | Low — emotion first | Leave space for melisma and vocal runs |
| **Funk** | Minimal | Very low | Groove lock; lyrics accent the downbeat |
| **Gospel** | Repetitive build | Low | Call-and-response; repetition builds intensity |
| **Jazz** | Varies by tune (AABA is the 32-bar song form, not a rhyme scheme) | Sophisticated | Internal rhyme, wordplay; phrasing behind/ahead of beat |
| **Reggae / Dancehall** | Riddim-driven | Moderate | Groove lock; audience participation by design |
| **Afrobeats** | Call-and-response | Low | Code-switching (English/Pidgin/local languages) |
| **Ballad (any)** | ABCB or ABAB | Moderate | Emotion and narrative serve the story |

**How to use**: Before writing lyrics, read `${CLAUDE_PLUGIN_ROOT}/genres/[genre]/README.md` → "Lyric Conventions" section for the specific genre's rules on rhyme scheme, rhyme quality, verse structure, and what to avoid.

### Rhyme Quality Standards (All Genres)

These apply universally regardless of genre:

- **Forced rhymes** are NEVER acceptable — never bend grammar, invent words, or use filler phrases just to land a rhyme
- **No self-rhymes** — never rhyme a word with itself
- **No identity rhymes** — avoid rhyming a word with one that contains it (mind/remind, light/delight)
- **Meaning over rhyme** — if a perfect rhyme sounds unnatural, use a near rhyme or restructure the line
- **Consistency within sections** — whatever rhyme scheme you choose, maintain it through the section. No random switching mid-verse.

### Flow Checks (All Genres)

Before finalizing any lyrics, verify:
1. Read each rhyming pair aloud — do the end words actually rhyme (per genre expectations)?
2. Are there any orphan lines that should rhyme with something but don't?
3. Is syllable count roughly consistent across corresponding lines? (see tolerance in Line Length table)
4. Are there filler phrases ("spoke the words", "you know what I mean") padding lines?
5. Do quoted/paraphrased lines come from sourced material (for documentary albums)?
6. Does the rhyme scheme match the genre? (Don't use AABB couplets for a folk ballad, don't use ABCB for hip-hop)
7. Say the lyrics without melody as plain prose — do they sound natural for the genre's vocal style?

### Common Anti-Patterns (All Genres)

- ❌ Using the wrong rhyme scheme for the genre (hip-hop couplets in a folk song, etc.)
- ❌ Forcing perfect rhymes where near rhymes sound more natural
- ❌ Using filler lines to set up quotes ("he stood up and spoke the words")
- ❌ Inventing fake quotes for real people when source quotes exist
- ❌ Ending a verse on a line that doesn't connect to its rhyme partner
- ❌ Inconsistent line lengths that break the vocal pocket
- ❌ Cliché phrases: "cold as ice," "broke my heart," "by my side," "set me free," "tonight" (at line endings), "learning to fly"
- ❌ Telling instead of showing ("I was angry" vs. showing anger through imagery)
- ❌ Generic abstractions when specificity would serve better

---

## Line Length

### General Ranges by Genre
| Genre | Syllables/Line | Tolerance |
|-------|----------------|-----------|
| Pop/Folk/Punk | 6-8 | ±2 |
| Rock/Indie | 8-10 | ±2 |
| Hip-Hop/Rap | 10-13+ | ±3 |
| Metal/Electronic | Varies | Flexible |

**Critical**: Verse 1 line lengths must match Verse 2 line lengths.

`check_album_lyrics` uses the Tolerance column to find the odd line out: it reports a verse line that sits more than twice the tolerance from its verse's median (more than 4 syllables for most genres, more than 6 for hip-hop). It treats "Flexible" as ±3. Anything tighter flags four finished songs in ten, so parallel lines within the tolerance are still yours to check by reading.

---

## Song Length

Songs that run past the targets below (about 400 words, 600 for hip-hop) cause Suno to rush, compress sections, or skip lyrics, and it gets worse the further past they go. Songs that are too short produce tracks under 3 minutes — fine if intentional, but usually not what users want.

### Default Target Duration

**3:30–5:00 minutes** for all genres unless the user specifies otherwise. This is the standard range for streaming platforms and what listeners expect.

### Album/Track Duration Override

When a track has a `Target Duration` in its Track Details table (not `—`), use that
instead of the genre default. When the track shows `—`, check the album README's
`Target Duration` in Suno Settings. If both are absent, use the genre defaults below.

**Duration → Word Count mapping:**
| Target Duration | Non-Hip-Hop Words | Hip-Hop Words |
|-----------------|-------------------|---------------|
| 2:00–2:30       | 120–180           | 200–300       |
| 2:30–3:30       | 150–250           | 250–400       |
| 3:30–5:00       | 220–400           | 400–600       |
| 5:00–7:00       | 350–500           | 550–750       |

Add ~30 words per instrumental break/solo when estimating.

Reading a Target Duration:
- **A range uses its midpoint.** `3:00–3:30` is 3:15, so it takes the 2:30–3:30 row.
- **A value on a boundary takes the longer row.** `3:30` uses 3:30–5:00, and `~5:00` uses 5:00–7:00.
- **A bracketed album value is not set.** The album template ships `[3:30–5:00]` as a placeholder. Until someone replaces it, the genre defaults below apply.

The `get_lyrics_stats` tool applies the same lookup and says which one it used in `target_basis`: `track_duration`, `album_duration`, `genre` or `default`. Its numbers are these two tables; a test fails if they stop matching.

### Word Count Targets by Genre (Suno)

These targets produce tracks in the 3:30–5:00 range on Suno. The previous lower targets (e.g., 150 words for electronic) produce 2:00–2:30 tracks.

| Genre | Target Duration | Word Count | Structure |
|-------|-----------------|------------|-----------|
| Electronic / Synthwave / EDM | 3:30–5:00 | 220–300 | 3 verses + pre-chorus + chorus + bridge + instrumental break |
| Pop / Synth-Pop | 3:30–4:30 | 250–350 | 2–3 verses + pre-chorus + chorus + bridge |
| Rock / Alt-Rock | 3:30–5:00 | 250–400 | 2–3 verses + chorus + bridge |
| Hip-Hop / Rap | 3:30–5:00 | 400–600 | 3 verses + hook + bridge |
| Folk / Country | 3:30–5:00 | 250–400 | 3 verses + chorus + bridge |
| Ballad (any) | 3:30–5:00 | 200–300 | 2–3 verses + chorus + bridge (slower tempo = fewer words) |
| Punk / Pop-Punk | 2:30–3:30 | 150–250 | 2 verses + chorus + bridge (punk is short by design) |
| Ambient / Lo-Fi | any | 50–150 | Sparse or wordless by design. Keeps this range whatever the Target Duration, because the duration mapping assumes a song sung throughout |

A genre with no row here uses the default duration's range: 220–400 words.

### Instrumental Tags Count as Runtime

Suno instrumental tags (`[Instrumental Break]`, `[Synth Solo]`, `[Guitar Solo]`, `[Drop]`, `[Interlude]`, etc.) add approximately **20–40 seconds each** to the track. Factor these into duration estimates. A track with 220 words + 2 instrumental breaks will run longer than 220 words alone.

### Structure Defaults

- **Default**: 2–3 verses + chorus + bridge. Use 3 verses to hit duration targets.
- **Chorus**: 4–6 lines, repeated verbatim — not rewritten each time.
- **Bridge**: 2–4 lines.
- **Pre-chorus**: 2–4 lines. Adding a pre-chorus is an effective way to increase duration without bloating sections.
- **Outro**: Optional, 2–4 lines max. Not a new verse.
- **Instrumental breaks**: Use `[Instrumental Break]`, `[Synth Solo]`, etc. to add runtime without more words.

### How to Hit Duration Targets

**Add more sections, not longer sections.** Per-section maximums (see Section Length Limits below) are correct for Suno pacing. The way to reach 3:30+ is:
- Add a **3rd verse** (most effective)
- Add a **pre-chorus** before each chorus
- Add an **instrumental break** or solo
- Add a **bridge** if missing

Do NOT write 10-line verses or 8-line choruses — Suno will rush them.

### Length Limits

- **If draft exceeds 400 words (non-hip-hop) or 600 words (hip-hop)**: Cut it down before presenting.
- **If draft is under the target's minimum** (the low end of its Target Duration row or genre row above: 220 words by default, 150 for punk, 50 for ambient): Flag as "likely too short for target duration" — suggest adding sections. A fixed 200-word floor would flag every punk and ambient track.
- Count words after drafting. If over target, remove a verse or trim sections — don't just shorten lines. If under target, add a verse, pre-chorus, or instrumental break.

### Section Length Limits by Genre

**Why this matters**: Suno rushes, compresses, or skips content when sections are too long. These are hard limits — fix before presenting.

**Which number applies to a verse**: the genre README's `Density/pacing (Suno)` line (`${CLAUDE_PLUGIN_ROOT}/genres/[genre]/README.md` → Lyric Conventions) is the verse limit, because it is written per genre and per tempo (thrash allows more than metal at large, house far less than electronic at large). The Verse rows below are the family ceiling, used when the README has no such line. The other rows (chorus, bridge, pre-chorus) are the limits for those sections; the READMEs rarely give them.

Every Max Lines value is one number. A section may be shorter; it may not be longer.

#### Hip-Hop / Rap / Trap / Drill / Grime / Phonk / Nerdcore

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Suno's ceiling, not the form's: a traditional 16-bar verse is 16 written lines, and Suno rushes past 8. 6 below 85 BPM and for half-time trap |
| Chorus / Hook | 6 | Shorter hooks hit harder |
| Bridge | 6 | |
| Pre-Chorus | 4 | |
| Outro | 4 | Spoken word / ad-lib sections exempt from limit |

#### Pop / Synth-Pop / Dance-Pop / K-Pop / Piano Pop

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 6 | Default 4; 6 only at 100–110 BPM |
| Chorus | 6 | |
| Bridge | 4 | |
| Pre-Chorus | 4 | |

#### Rock / Alt-Rock / Indie Rock / Grunge / Garage Rock / Post-Rock

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Default 6; 4 above 130 BPM |
| Chorus | 6 | |
| Bridge | 4 | |
| Pre-Chorus | 4 | |
| Guitar solo / Interlude | 0 (instrumental) | Use `[Guitar Solo]` or `[Interlude]` tag |

#### Progressive Rock

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 12 | The exception: default 8–10, 12 only at 90–110 BPM, 8 above 130 |
| Chorus | 6 | |
| Bridge | 4 | |
| Pre-Chorus | 4 | |

#### Punk / Hardcore Punk / Pop-Punk / Ska Punk

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4 | Short, fast — keep it tight. Hardcore: 3. Pop-punk and emo run longer; their READMEs say how much |
| Chorus | 4 | Punchy, shoutable |
| Bridge | 4 | |
| Pre-Chorus | 2 | |

#### Metal / Thrash / Doom / Black Metal / Metalcore / Industrial

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Doom: 6. Thrash: 10, per its README |
| Chorus | 6 | |
| Bridge | 4 | |
| Pre-Chorus | 4 | |
| Breakdown | 4 | Often instrumental or minimal lyrics |

#### Country / Folk / Americana / Bluegrass / Singer-Songwriter

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Storytelling verses can use the full 8; ballads 4 |
| Chorus | 6 | |
| Bridge | 4 | |
| Pre-Chorus | 4 | |

#### Blues

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 3 | AAB: line 1 stated, line 2 repeats it, line 3 resolves. Never 4 |
| Chorus / Refrain | 4 | Many blues have none |
| Bridge | 4 | |

#### Electronic / EDM / House / Techno / Trance / Dubstep / DnB / Synthwave

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 6 | Default 4; vocals are sparse in electronic — less is more. House: 2, EDM: 4 |
| Chorus / Hook | 4 | Often just a repeated phrase |
| Bridge | 4 | |
| Drop | 0 (instrumental) | Use `[Drop]` or `[Break]` tag |

#### Ambient / Lo-Fi / Chillwave / Trip-Hop / Vaporwave

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 4 | Minimal vocals, atmosphere first. Trip-hop: 6 |
| Chorus / Hook | 4 | |
| Bridge | 2 | |

#### R&B / Soul / Funk / Gospel

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Default 6; ballads under 80 BPM: 6 |
| Chorus | 6 | |
| Bridge | 4 | |
| Pre-Chorus | 4 | |
| Vamp / Ad-lib | Flexible | Outro vamps are genre-standard |

#### Jazz / Swing / Bossa Nova

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Standard 32-bar form. Bebop: 4 |
| Chorus | 6 | |
| Bridge | 8 | Jazz B-sections can run longer |

#### Reggae / Dancehall / Afrobeats

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 8 | Reggae: 6 |
| Chorus / Hook | 6 | |
| Bridge | 4 | |
| Toast / DJ | 8 | Dancehall toasting sections |

#### Ballad (any genre)

| Section | Max Lines | Notes |
|---------|-----------|-------|
| Verse | 6 | Default 4. Slower tempo = fewer lines needed |
| Chorus | 6 | |
| Bridge | 4 | |

### Section Length Enforcement

**Hard rules — enforce before presenting lyrics:**

1. **Count lines per section** after drafting. Compare verses against the genre README's `Density/pacing (Suno)` line, and everything else (or a verse with no README line) against the genre table above.
2. **If a section exceeds its max**: Fix it before presenting, without asking. A verse is **split in two** when the word budget allows and each half holds a complete thought (spread, don't compress); otherwise it is **trimmed**. A chorus, bridge or pre-chorus is trimmed. List what you did in the Refinement Log so the user sees it.
3. **Hip-hop verse over 8 lines**: Split into two verses or cut. No exceptions.
4. **Any chorus over 6 lines**: Trim. A long chorus loses its punch and causes Suno to rush.
5. **Electronic verse over 6 lines**: Cut. Electronic tracks need space, not walls of text.
6. **Punk sections over limits**: Punk is short and fast. If it's long, it's not punk.
7. **When unsure about genre**: Write 4-line verses and treat 6 as the verse ceiling, with 6 for a chorus and 4 for a bridge. This is the same default as the BPM table below.
8. **Also check BPM-aware limits** in the Lyric Density & Pacing section below — a genre may allow 8-line verses at fast tempo but only 4 at slow tempo.

**Suno-specific reasoning**: Long sections cause:
- Vocal rushing (cramming words into fixed musical time)
- Loss of clarity (words blur together)
- Section compression (Suno shortens the music to fit)
- Skipped lyrics (Suno drops lines entirely)

---

## Lyric Density & Pacing (Suno)

Suno rushes through dense verse blocks. Verse length must match tempo and feel. **The slower the BPM, the fewer lines Suno can handle** without rushing, compressing, or skipping.

**Genre-specific Suno verse limits are in each genre's README** under "Lyric Conventions → Density/pacing (Suno)". Always check the genre README for the track you're writing: its line is the limit. The table below summarizes the genre families for when there is no README line, and its Max Safe column carries the same numbers as the Verse rows in Section Length Limits.

### Suno Verse Length Defaults

| Genre Family | Default Lines/Verse | Max Safe | Topics/Verse | Key Rule |
|---|---|---|---|---|
| **Hip-Hop / Rap** | 8 (4 couplets) | 8 | 2-3 | Never exceed 8; 6 below 85 BPM. Half-time trap = treat as 65-75 BPM, so 6 |
| **Pop** | 4 | 6 | 1-2 | Chorus-first — longer verses bury the hook |
| **Rock** | 6 | 8 | 2 | 120 BPM sweet spot; guitar riffs need space |
| **Punk** | 4 | 4 | 1 | Fast, short, every word punches |
| **Hardcore Punk** | 2-3 | 3 | 1 | Extreme tempo; shouted, minimal |
| **Metal** | 6-8 | 8 | 2-3 | Vocal delivery compresses syllables; thrash handles 10 |
| **Doom Metal** | 4 | 6 | 1 | Slowest metal; each word carries crushing weight |
| **Country / Folk** | 6 | 8 | 1-2 | Storytelling pace; ballads drop to 4 |
| **Blues** | 3 (AAB) | 3 | 1 | Rigid structure — never break AAB |
| **Electronic / EDM** | 2-4 | 6 | 1 | Production is the star; vocals are texture |
| **Ambient / Shoegaze** | 0-2 | 4 | 1 | Often instrumental; vocals are texture |
| **R&B / Soul** | 6 | 8 | 1-2 | Melisma stretches syllables; groove > density |
| **Jazz** | 6-8 | 8 | 1-2 | Bebop: 2-4 lines; ballads: 6-8 |
| **Singer-Songwriter** | 6-8 | 8 | 2-3 | Confessional; stripped-back production carries words |
| **Progressive Rock** | 8-10 | 12 | 3-4 | The exception — handles long verses |

### BPM-Aware Limits (Universal Fallback)

When a genre README doesn't specify, use this table. It is written for sung genres; rap follows the Hip-Hop row above instead (8 lines at 85-95 BPM is its normal verse).

| BPM Range | Max Lines/Verse | Topics/Verse | Feel |
|-----------|----------------|-------------|------|
| < 80 | 4 | 1-2 | Slow, heavy — fewer lines needed |
| 80-93 | 6 | 1-2 | Laid back, mid-tempo — 4 is the comfortable length |
| 94-109 | 6 | 2-3 | Energetic, driving |
| 110-139 | 8 | 2-3 | Standard rock/pop range — 6 is the comfortable length |
| 140+ | 4 | 1 | Fast — short verses, energy over density |

**Default: 4 lines per verse** unless the genre and tempo justify more.

### Topic Density

- Max **1-2 topics per 4-line verse**, **2-3 per 6-8 line verse**
- If a verse covers 3+ topics in 4 lines, split it
- **Prefer more short verses over fewer dense verses** — two 4-line verses beat one 8-line verse

### Red Flags

- 8-line verse under 100 BPM in a sung genre — too dense for Suno (rap is the exception: its README allows 8 lines at 85-95 BPM)
- Verse reads like a list of names/facts — it's a Wikipedia entry, not a verse
- Track concept says "laid back" but verses are wall-to-wall syllables
- More than 3 proper nouns introduced in a single verse
- Every verse in the song is dense (no breathing room anywhere)

### Fix

When a verse is too dense:
1. **Prefer splitting into two verses** over cutting content (spread, don't compress) — as long as the track stays inside its word-count target; when it would not, trim instead
2. Let each topic have at least a full couplet (2 lines) to land
3. Re-read with the BPM in mind — can you actually sing/rap this at tempo without rushing?

### Streaming Exception

Streaming lyrics (distributor text) can have longer verse blocks since they aren't generated by Suno. But verse BREAKS should still align with the Suno structure so the text matches what's actually sung.

### Process

Before finalizing any track, ASK: "Does the verse length match the BPM and mood described in Musical Direction?" Check the genre README's `Density/pacing (Suno)` line. A verse over the genre's **max** is fixed before presenting (see Section Length Enforcement). A verse between the genre's **default** and its max is allowed when the tempo supports it — say so in one line when presenting, so the user can ask for a shorter one.

---

## Refinement Pass Reference

Three-pass schedule for iterative lyric refinement. Each pass targets a different layer.

### Pass 1: Tighten

Remove filler, compress language, eliminate redundancy.

| Pattern | Before | After | Why |
|---------|--------|-------|-----|
| Filler phrases | "He stood up and spoke the words" | "He said" | Setup phrases pad lines without adding meaning |
| Redundant modifiers | "completely destroyed" | "destroyed" | Absolute verbs don't need intensifiers |
| Passive voice | "The door was opened by her" | "She opened the door" | Active voice is more direct and singable |
| Pronoun-heavy lines | "He told him that he should go" | "He told his brother to go" | Name one of them — three pronouns leave the listener guessing who is who |
| Unnecessary prepositions | "She looked up at the sky above" | "She looked at the sky" | Trim directional padding — the sky is already up and above |
| Throat-clearing openers | "Well, I think that maybe I should" | "I should" | Cut hedging — commit to the statement |
| Double-saying | "alone and by myself" | "alone" | One expression per idea |

### Pass 2: Strengthen

Upgrade weak imagery, sharpen sensory detail, replace generic with specific.

The stronger line must say the same thing as the weak one: same moment, same feeling, same fact. A new event, character or idea is a rewrite, not a refinement. On documentary tracks every added detail (a number, a place, an object) has to be in the sources.

| Pattern | Before | After | Why |
|---------|--------|-------|-----|
| Generic imagery | "The city at night" | "Neon bleeding on wet asphalt" | Specific images stick; generic ones slide |
| Abstract emotion | "I felt so lost" | "Couldn't find my keys, my name, my street" | Show the feeling through concrete details |
| Clichés | "Cold as ice" | "Cold as the far side of the bed" | Fresh comparisons earn attention — draw them from the song's own world, here a breakup |
| Single-sense lines | "The room was dark" (sight only) | "Dark — just the hum of pipes and mildew air" | Multi-sensory lines immerse the listener |
| Weak verbs | "He went across the room" | "He cut across the room" | Strong verbs carry energy and specificity |
| Telling emotions | "She was angry" | "Her knuckles white around the glass" | Action reveals emotion without naming it |
| Vague quantities | "A lot of people came" | "Thirty faces in a room for ten" | Numbers create instant visual scale (documentary: only a number the sources give) |

### Pass 3: Flow & Ear

Read-aloud test, smooth transitions, singability at target BPM.

| Pattern | Before | After | Why |
|---------|--------|-------|-----|
| Consonant clusters | "Sixth street's strict structures" | "Sixth Street's sharp edges" | Tongue-trippers kill vocal delivery |
| Unsingable vowel sequences | "She oughta allow our hour" | "She gave us the hour" | Stacked diphthongs muddy at tempo |
| Transition bumps | V1 ends reflective → V2 opens aggressive (no bridge) | Add pre-chorus or transitional line | Jarring shifts break the listener's flow |
| Missing breath points | 12-syllable line with no natural pause | Split at caesura or add a comma break | Singers need air; dense lines get rushed |
| Stress misalignment | "into the DARK-ness" with DARK on a weak beat | Move the phrase so DARK lands on beat 1 or 3: open the bar with "darkness", or put one pickup syllable in front of it | Stressed syllables must land on strong beats; reorder the words you have before reaching for new ones |
| Choppy rhythm | "Stop. Go. Wait. No. Run." | "Stop and go — wait, no — run" | Staccato lines need connective tissue to sing |
| Syllable mismatch | V1 line: 8 syllables, V2 line: 13 syllables | Match within ±2 syllables | Parallel lines should fit the same melodic phrase |

---

