---
title: "TITLE_TBD"
date: 2026-08-28
draft: true
tags: ["Audio", "Music Information Retrieval", "MERT"]
summary: "SUMMARY_TBD"
showToc: false
weight: 1
---

### Intro
Think back to games like MapleStory or Pokémon. If you were a real fan, hearing the music alone brings the map back — vividly.

<div style="text-align: center; margin: 20px 0;">
  <audio controls style="width: 100%; max-width: 500px;">
    <source src="/static/audio/perion.mp3" type="audio/mpeg">
  </audio>
  <img src="/static/images/perion.png" alt="Perion, MapleStory" style="width: 100%; max-width: 500px; margin-top: 10px;">
  <p style="font-size: 0.9em; color: gray;">Perion, MapleStory</p>
</div>

But is that recall nostalgia, or is the map's character actually encoded in the music itself? In other words: if we played the same track to someone who's never touched the game, would they picture a similar scene?


### Examples
Start with the phenomenon itself. Listen to each of the four tracks below and picture the scene — you don't need to know MapleStory for this.

<div class="audio-quiz-grid">

<div class="audio-quiz">
  <div class="track-player" data-audio="/static/audio/ariant.mp3" data-label="Example 1">
    <button class="play-btn" aria-label="Play">
      <svg class="icon-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      <svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
    </button>
    <div class="track-info">
      <span class="track-label">Example 1</span>
      <div class="progress-bar"><div class="progress-fill"></div></div>
    </div>
  </div>
  <details class="reveal">
    <summary>Reveal</summary>
    <img src="/static/images/ariant.png" alt="Ariant, MapleStory">
    <p><b>Ariant</b> — Desert</p>
  </details>
</div>


<div class="audio-quiz">
  <div class="track-player" data-audio="/static/audio/ellinia.mp3" data-label="Example 2">
    <button class="play-btn" aria-label="Play">
      <svg class="icon-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      <svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
    </button>
    <div class="track-info">
      <span class="track-label">Example 2</span>
      <div class="progress-bar"><div class="progress-fill"></div></div>
    </div>
  </div>
  <details class="reveal">
    <summary>Reveal</summary>
    <img src="/static/images/ellinia.png" alt="Ellinia, MapleStory">
    <p><b>Ellinia</b> — Forest</p>
  </details>
</div>

<div class="audio-quiz">
  <div class="track-player" data-audio="/static/audio/elnath.mp3" data-label="Example 3">
    <button class="play-btn" aria-label="Play">
      <svg class="icon-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      <svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
    </button>
    <div class="track-info">
      <span class="track-label">Example 3</span>
      <div class="progress-bar"><div class="progress-fill"></div></div>
    </div>
  </div>
  <details class="reveal">
    <summary>Reveal</summary>
    <img src="/static/images/elnath.png" alt="Elnath, MapleStory">
    <p><b>Elnath</b> — Snow</p>
  </details>
</div>

<style>
.audio-quiz-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin: 24px 0;
}
.audio-quiz {
  border: 1px solid rgba(128,128,128,0.25);
  border-radius: 12px;
  padding: 14px;
}
.track-player {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}
.play-btn {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: rgba(128,128,128,0.15);
  color: inherit;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.15s ease;
}
.play-btn:hover { background: rgba(128,128,128,0.28); }
.play-btn svg { width: 18px; height: 18px; fill: currentColor; }
.track-info { flex: 1; min-width: 0; }
.track-label { font-size: 0.85em; opacity: 0.7; }
.progress-bar {
  margin-top: 6px;
  height: 4px;
  border-radius: 2px;
  background: rgba(128,128,128,0.2);
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  width: 0%;
  background: currentColor;
  opacity: 0.6;
  transition: width 0.1s linear;
}
.audio-quiz .reveal {
  margin-top: 12px;
  font-size: 0.9em;
}
.audio-quiz .reveal summary {
  cursor: pointer;
  color: #007bff;
  font-weight: bold;
}
.audio-quiz .reveal img {
  width: 100%;
  border-radius: 8px;
  margin-top: 8px;
}
.audio-quiz .reveal p { margin-top: 6px; }
</style>

<script>
document.querySelectorAll('.track-player').forEach(player => {
  const audio = new Audio(player.dataset.audio);
  const btn = player.querySelector('.play-btn');
  const iconPlay = player.querySelector('.icon-play');
  const iconPause = player.querySelector('.icon-pause');
  const fill = player.querySelector('.progress-fill');

  const toggle = () => {
    document.querySelectorAll('audio').forEach(a => { if (a !== audio) a.pause(); });
    if (audio.paused) { audio.play(); } else { audio.pause(); }
  };

  player.addEventListener('click', toggle);
  audio.addEventListener('play', () => { iconPlay.style.display = 'none'; iconPause.style.display = ''; });
  audio.addEventListener('pause', () => { iconPlay.style.display = ''; iconPause.style.display = 'none'; });
  audio.addEventListener('ended', () => { iconPlay.style.display = ''; iconPause.style.display = 'none'; fill.style.width = '0%'; });
  audio.addEventListener('timeupdate', () => {
    fill.style.width = (audio.currentTime / audio.duration * 100 || 0) + '%';
  });
});
</script>


### Method
Our working hypothesis: if map OSTs really do encode the distinctive elements of their biome, we should be able to train a music → biome classifier on them directly. (Spoiler, if the examples above didn't already give it away: this is far from an easy task.)

We picked six representative biomes: **forest, desert, snow, ocean, cave, jungle**.

The dataset was hand-collected from YouTube — [PLACEHOLDER: scraping/curation summary, ~N hours of manual review]. We restricted to **modern-era** tracks [PLACEHOLDER: exact era boundary / how "modern" was defined — hardware generation vs. release year] to avoid confounding biome signal with chiptune/lo-fi production-era artifacts. Per-class counts:

| Biome | Segments | Tracks |
|---|---|---|
| Forest | [PLACEHOLDER] | [PLACEHOLDER] |
| Desert | [PLACEHOLDER] | [PLACEHOLDER] |
| Snow | [PLACEHOLDER] | [PLACEHOLDER] |
| Ocean | [PLACEHOLDER] | [PLACEHOLDER] |
| Cave | [PLACEHOLDER] | [PLACEHOLDER] |
| Jungle | [PLACEHOLDER] | [PLACEHOLDER] |

representative tracks you might recognize: [PLACEHOLDER, 2 per class]

**Architecture.** We freeze a pretrained MERT backbone and train a lightweight MLP head on top of its pooled representation:

<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" style="width: 100%; max-width: 640px; font-family: inherit;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <!-- Waveform input -->
  <g>
    <rect x="10" y="70" width="90" height="60" rx="8" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.7"/>
    <path d="M20 100 L30 85 L40 115 L50 90 L60 110 L70 95 L80 105 L90 100" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.7"/>
    <text x="55" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">15s clip</text>
  </g>

  <line x1="100" y1="100" x2="150" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- MERT (frozen) -->
  <g>
    <rect x="150" y="55" width="150" height="90" rx="8" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="225" y="95" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">MERT</text>
    <text x="225" y="115" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.6">(frozen)</text>
    <text x="225" y="165" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">25 layers × 1024-d</text>
  </g>

  <line x1="300" y1="100" x2="350" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- Pooling -->
  <g>
    <rect x="350" y="70" width="100" height="60" rx="8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.85"/>
    <text x="400" y="95" text-anchor="middle" font-size="12" fill="currentColor">mean+std</text>
    <text x="400" y="112" text-anchor="middle" font-size="12" fill="currentColor">pool</text>
    <text x="400" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">[PLACEHOLDER: dim]</text>
  </g>

  <line x1="450" y1="100" x2="500" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- MLP head -->
  <g>
    <rect x="500" y="55" width="130" height="90" rx="8" fill="none" stroke="currentColor" stroke-width="2"/>
    <text x="565" y="90" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">MLP</text>
    <text x="565" y="108" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.6">(trained)</text>
    <text x="565" y="165" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">[PLACEHOLDER: layers]</text>
  </g>

  <line x1="630" y1="100" x2="680" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <text x="700" y="105" text-anchor="middle" font-size="12" fill="currentColor">6</text>
</svg>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; margin: 20px 0;">


```yaml
backbone: MERT-v1-330M (frozen)
pooling: mean+std  # [PLACEHOLDER: layer(s)]
head: [PLACEHOLDER]  # e.g. 2048 -> 256 -> 6
activation: [PLACEHOLDER]
dropout: [PLACEHOLDER]
```

```yaml
optimizer: [PLACEHOLDER]
lr: [PLACEHOLDER]
schedule: [PLACEHOLDER]
batch_size: [PLACEHOLDER]
epochs: [PLACEHOLDER]
split: [PLACEHOLDER]  # e.g. GroupShuffleSplit, 8:1:1
```

</div>



### Results

**Model.** Dev / test weighted-F1:

```yaml
dev_f1:  [PLACEHOLDER]
test_f1: [PLACEHOLDER]
```

<div style="text-align: center; margin: 20px 0;">
  <img src="/images/cm_model.png" alt="Model confusion matrix" style="width: 100%; max-width: 420px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Test confusion matrix (model)</p>
</div>

**Human baseline.** Weighted-F1:

```yaml
human_f1: [PLACEHOLDER]
```



<div style="text-align: center; margin: 20px 0;">
  <img src="/images/cm_human.png" alt="Human confusion matrix" style="width: 100%; max-width: 420px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Confusion matrix (human raters)</p>
</div>



### Discussion
Model performance matches the human baseline — but consider a pessimistic reading of this result.

Each biome likely has standard musical conventions: desert tracks might share a tempo/rhythm range distinct from forest tracks, certain keys or instrumentation recur within a class, and so on. Call these **cues** — boring, standard descriptors (tempo, rhythm, key, spectral shape) rather than anything resembling "atmosphere." Under this hypothesis, the model isn't recovering the same holistic scene the listener imagines; it's just exploiting these cues, and happens to land at human-level F1 by doing so.

To test this, we train a **cue-based classifier** — the same MLP head, but on standard hand-crafted descriptors (tempo, rhythm, key, spectral/timbral features) instead of MERT embeddings — and compare.

```yaml
cue_model_f1: [PLACEHOLDER]
mert_model_f1: [PLACEHOLDER]  # from Results
human_f1: [PLACEHOLDER]       # from Results
```

[PLACEHOLDER: interpretation — does cue-based model close the gap to MERT/human, or does a gap remain? What does that imply about whether MERT is capturing something beyond boring cues?]