---
title: "Can You Hear the Biome?"
date: 2026-08-30
draft: false
tags: ["Video Game Music", "Classification", "MERT"]
summary: "Game music-to-biome classification: does music encode biome or just nostalgia?"
showToc: false
weight: 1
---

### Intro
My favorite childhood game was MapleStory. Some soundtracks still remind me of certain spots. For instance, *Perion* is the land of warriors and tribes — and see how well it fits:

<div style="text-align: center; margin: 20px 0;">
  <img src="../../images/perion.png" alt="Perion, MapleStory" style="width: 75%; max-width: 375px; display: block; margin: 0 auto;">
  <audio controls style="width: 75%; max-width: 375px; display: block; margin: 10px auto 0;">
    <source src="../../audio/perion.mp3" type="audio/mpeg">
  <../../audio/>
  <p style="font-size: 0.9em; color: gray; margin-top: 8px;">Perion, MapleStory</p>
</div>

But is that fit simply nostalgia, or does the music somehow encode the characteristics of the place? In other words,

> *Would a first-time-listener also picture a similar scene?* 

In this post, we make this an easier question by replacing **scene** with **biome**.  


### Examples
<a id="sec-examples"></a>
Let us try this ourselves first. Each of the tracks below fall into one of the following biomes: Forest, Desert, Snow, Ocean, Cave, and Jungle. Can you guess which one is which?

<div class="audio-quiz-grid">

<div class="audio-quiz">
  <div class="track-player" data-audio="../../audio/ariant.mp3" data-label="Example 1">
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
    <img src="../../images/ariant.png" alt="Ariant, MapleStory">
    <p><b>Ariant</b> — Desert</p>
  </details>
</div>


<div class="audio-quiz">
  <div class="track-player" data-audio="../../audio/ellinia.mp3" data-label="Example 2">
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
    <img src="../../images/ellinia.png" alt="Ellinia, MapleStory">
    <p><b>Ellinia</b> — Forest</p>
  </details>
</div>

<div class="audio-quiz">
  <div class="track-player" data-audio="../../audio/elnath.mp3" data-label="Example 3">
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
    <img src="../../images/elnath.png" alt="Elnath, MapleStory">
    <p><b>Elnath</b> — Snow</p>
  </details>
</div>

<div class="audio-quiz">
  <div class="track-player" data-audio="../../audio/mine.mp3" data-label="Example 4">
    <button class="play-btn" aria-label="Play">
      <svg class="icon-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      <svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
    </button>
    <div class="track-info">
      <span class="track-label">Example 4</span>
      <div class="progress-bar"><div class="progress-fill"></div></div>
    </div>
  </div>
  <details class="reveal">
    <summary>Reveal</summary>
    <img src="../../images/mine.png" alt="Mine, MapleStory">
    <p><b>Mine</b> — Cave</p>
  </details>
</div>

<div class="audio-quiz">
  <div class="track-player" data-audio="../../audio/sellas.mp3" data-label="Example 5">
    <button class="play-btn" aria-label="Play">
      <svg class="icon-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      <svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
    </button>
    <div class="track-info">
      <span class="track-label">Example 5</span>
      <div class="progress-bar"><div class="progress-fill"></div></div>
    </div>
  </div>
  <details class="reveal">
    <summary>Reveal</summary>
    <img src="../../images/sellas.png" alt="Sellas, MapleStory">
    <p><b>Sellas</b> — Ocean</p>
  </details>
</div>

<div class="audio-quiz">
  <div class="track-player" data-audio="../../audio/partem.mp3" data-label="Example 6">
    <button class="play-btn" aria-label="Play">
      <svg class="icon-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
      <svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
    </button>
    <div class="track-info">
      <span class="track-label">Example 6</span>
      <div class="progress-bar"><div class="progress-fill"></div></div>
    </div>
  </div>
  <details class="reveal">
    <summary>Reveal</summary>
    <img src="../../images/partem.png" alt="Partem, MapleStory">
    <p><b>Partem</b> — Jungle (Tropical) </p>
  </details>
</div>


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
While this is a challenging task even for humans, if these soundtracks really do encode the distinctive elements of their biome, we should be able to train a **music-to-biome classifier** on them.

**Data**
We fix 6 representative biomes: **Forest, Desert, Snow, Ocean, Cave, Jungle**. Tracks were manually gathered from YouTube, mostly using curated playlists ([example](https:/youtu.be/Jc_XyrzngZk?si=QIiROKQAJRc1D5NA)). To augment/regularize data, tracks were split into 15-second **segments**. Dataset breakdown:

<div align="center">

| Biome | Segments (15s) | Tracks |
|:---:|:---:|:---:|
| Forest | 1023 | 89 |
| Desert | 1498 | 131 |
| Snow | 801 | 71 |
| Ocean | 717 | 88 |
| Cave | 420 | 37 |
| Jungle | 501 | 42 |

</div>

**Architecture**
We train a small MLP head on top of MERT [[1]](#ref-mert), a pretrained audio embedding model. Mean-pooling was applied across the layer and time axes to obtain a 1024-dim feature vector for each 15-second segment.

<div style="text-align: center; margin: 24px 0;">
<svg viewBox="0 0 720 200" xmlns="http:/www.w3.org/2000/svg" style="width: 100%; max-width: 640px; font-family: inherit;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>

  <!-- Waveform input -->
  <g>
    <rect x="10" y="70" width="90" height="60" rx="8" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.7"/>
    <path d="M20 100 L30 85 L40 115 L50 90 L60 110 L70 95 L80 105 L90 100" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.7"/>
    <text x="55" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">15s segment</text>
  </g>

  <line x1="100" y1="100" x2="150" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- MERT (frozen) -->
  <g>
    <rect x="150" y="55" width="150" height="90" rx="8" fill="none" stroke="currentColor" stroke-width="1.5"/>
    <text x="225" y="95" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">MERT</text>
    <text x="225" y="115" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.6">(frozen)</text>
    <text x="225" y="160" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.7">n_layers=25, t_patches=1125</text>
    <text x="225" y="173" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.7">dim=1024</text>
  </g>

  <line x1="300" y1="100" x2="350" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- Pooling -->
  <g>
    <rect x="350" y="70" width="100" height="60" rx="8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.85"/>
    <text x="400" y="105" text-anchor="middle" font-size="12" fill="currentColor">mean-pool</text>
    <text x="400" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">dim=1024</text>
  </g>

  <line x1="450" y1="100" x2="500" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- MLP head -->
  <g>
    <rect x="500" y="55" width="130" height="90" rx="8" fill="none" stroke="currentColor" stroke-width="2"/>
    <text x="565" y="90" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">MLP</text>
    <text x="565" y="118" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.6">(trained)</text>
    <text x="565" y="175" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7"> 1024 → 64 → 6 </text>
  </g>

  <!-- <line x1="630" y1="100" x2="680" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/> 분포 histogram 추가하면 좋을듯? -->

</svg>
</div>


### Results

We report the model test and human results below. Surprisingly, our model outperforms human raters, despite it being trained on a modest-sized dataset (# tracks < 500).

| | Accuracy | Weighted F1 |
|---|:---:|:---:|
| Model (test) | 0.493 | 0.500 |
| Human        | 0.385 | 0.383 |

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 24px 0;">

<div style="text-align: center;">
  <img src="../../images/cm_model.png" alt="Model confusion matrix" style="width: 100%; max-width: 380px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Test confusion matrix (model)</p>
</div>

<div style="text-align: center;">
  <img src="../../images/cm_human.png" alt="Human confusion matrix" style="width: 100%; max-width: 380px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Confusion matrix (human)</p>
</div>

</div>

**Observation**
While the comparison above isn't entirely fair (different set of tracks were used), there are some interesting observations to make.

- Ocean is the easiest to recognize.
- Cave is hard to recognize--possibly due to lack of data.
- Desert is easily recognized, but is often confused with Jungle.
- Forest is the hardest to recognize for humans (lowest recall).


### Discussion

While the results are understandable, this task requires understanding music *atmosphere*--so a small model outperforming humans raises a question:

> Is the model cheating by learning uninteresting, statistical cues?

Most Desert tracks, for instance, could share key, rhythm, spectral shape, instrumentation — call these **cues**, standard music descriptors. The model could be exploiting these instead of the *atmosphere* itself.

To test this, we train a **cue-based classifier**: same MLP head, but fed 626 standard audio descriptors (extracted via librosa) instead of MERT embeddings. It scores only 0.233 F1 — far below both the model and human baseline.

From this, we can deduce that game music does represent its biome to some extent. More importantly, *it* wasn't just nostalgia!

### Additional Results
Here, we show the model's outputs for the six examples presented in the [Examples](#sec-examples) section above (unseen during training). While not perfectly accurate, do compare it to your initial guesses (for fun).

<div style="text-align: center; margin: 20px 0;">
  <img src="../../images/track_prediction_histograms.png" alt="Model prediction histograms for six example tracks" style="width: 100%; max-width: 700px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Model output distributions for the six tracks from [Examples](#sec-examples)</p>
</div>

### References
<a id="ref-mert"></a>
[1] Y. Li *et al.*, "MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training," *arXiv preprint arXiv:2306.00107*, 2023.

---

All MapleStory audio and imagery used in this post are property of Nexon Korea Corp., used here under Nexon's [non-commercial fan content guidelines](https://www.nexon.com/game-ip-guide).