---
title: "Can You Hear the Biome? Game Music-to-Scene Classification"
date: 2026-08-28
draft: false
tags: ["Video Game Music", "Classification", "MERT"]
summary: "Does video game music encode the scene, or merely stimulate nostalgia? "
showToc: false
weight: 1
---

### Intro
In my childhood, I was a big fan of the game MapleStory. Even now, I can vividly recall the scenes from certain soundtracks. For instance, *Perion* is the land of brave warriors and tribes — and see how well the music fits:

<div style="text-align: center; margin: 20px 0;">
  <img src="../../images/perion.png" alt="Perion, MapleStory" style="width: 75%; max-width: 375px; display: block; margin: 0 auto;">
  <audio controls style="width: 75%; max-width: 375px; display: block; margin: 10px auto 0;">
    <source src="../../audio/perion.mp3" type="audio/mpeg">
  <../../audio/>
  <p style="font-size: 0.9em; color: gray; margin-top: 8px;">Perion, MapleStory</p>
</div>

A real gamer would have their favorite song that perfectly fits the place. But is that connection simply nostalgia, or is the scene somehow actually encoded in the music itself? 

The central question of the post is:
> *Would a first-time-listener also picture a similar scene, or the **biome**? That is, does game music encode **biome**?* 


### Examples
Assuming that you have never played MapleStory, you can try this yourself: listen to each of the tracks below and try picturing the scene.

> HINT: 6 biome categories are used throughout this post: Forest, Desert, Snow, Ocean, Cave, Jungle.

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
From the examples, we realize that this task is surprisingly challenging, at least for humans.

Nevertheless, if these soundtracks really do encode the distinctive elements of their biome, we should be able to train a **music-conditioned biome classifier** on them directly.

#### Data
As mentioned, we fix 6 representative biomes: **forest, desert, snow, ocean, cave, jungle**. Video game tracks for each biome was manually collected from Youtube; fortunately, many curated playlists already exists (such as [this one](https:/youtu.be/Jc_XyrzngZk?si=QIiROKQAJRc1D5NA)). Data count is shown below; each track was split into multiple 15-second **segments** for data regularization/augmentation.

<div style="display: flex; justify-content: center;">

| Biome | Segments (15-sec.) | Tracks |
|:---:|:---:|:---:|
| Forest | 1023 | 89 |
| Desert | 1498 | 131 |
| Snow | 801 | 71 |
| Ocean | 717 | 88 |
| Cave | 420 | 37 |
| Jungle | 501 | 42 |

</div> 

#### Architecture. 
We train a small MLP head on top of a pretrained audio embedding model, MERT [[1]](#ref-mert). For this task, we did not find a specific layer of MERT consistently performing better than others, so we average them.

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
    <text x="400" y="150" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7">dim: 2048</text>
  </g>

  <line x1="450" y1="100" x2="500" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <!-- MLP head -->
  <g>
    <rect x="500" y="55" width="130" height="90" rx="8" fill="none" stroke="currentColor" stroke-width="2"/>
    <text x="565" y="90" text-anchor="middle" font-size="15" font-weight="bold" fill="currentColor">MLP</text>
    <text x="565" y="108" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.6">(trained)</text>
    <text x="565" y="165" text-anchor="middle" font-size="12" fill="currentColor" opacity="0.7"> 2048 → 64 → 6</text>
  </g>

  <line x1="630" y1="100" x2="680" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)" opacity="0.7"/>

  <text x="700" y="105" text-anchor="middle" font-size="12" fill="currentColor">6</text>
</svg>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0 24px; margin: 20px 0;">


```yaml
backbone: MERT-v1-330M ❄️
layer-pool: mean
time-pool: mean+std 
feat-dim: 2048
head: 2048 → 64 → 6  
activation: GELU 
dropout: 0.3
```

```yaml
optimizer: AdamW
weight_decay: 1e-2
lr: 1e-3
batch_size: 64
split: GroupShuffleSplit (7:1:2)
```

</div>



### Results

**Model.** Dev / test accuracy and weighted F1-score:

```yaml
dev:  acc=0.596  f1=0.595
test: acc=0.511  f1=0.507
```

<div style="text-align: center; margin: 20px 0;">
  <img src="../../images/cm_dev.png" alt="Model confusion matrix" style="width: 100%; max-width: 420px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Test confusion matrix (model)</p>
</div>

**Human baseline.**:

```yaml
human: acc=[PLACEHOLDER]  f1=[PLACEHOLDER]
```



<div style="text-align: center; margin: 20px 0;">
  <img src="../../images/cm_human.png" alt="Human confusion matrix" style="width: 100%; max-width: 420px;">
  <p style="font-size: 0.9em; color: gray; margin-top: 6px;">Confusion matrix (human raters)</p>
</div>



### Discussion
[TODO: comment onmodel vs human performance]

Each biome likely has standard musical conventions: desert tracks might share a tempo/rhythm range distinct from forest tracks, certain keys or instrumentation recur within a class, and so on. Call these **cues** — boring, standard descriptors (tempo, rhythm, key, spectral shape) rather than anything resembling "atmosphere." Under this hypothesis, the model isn't recovering the same holistic scene the listener imagines; it's just exploiting these cues, and happens to land at human-level F1 by doing so.

To test this, we train a **cue-based classifier** — the same MLP head, but on standard hand-crafted descriptors (tempo, rhythm, key, spectral/timbral features) instead of MERT embeddings — and compare.

```yaml
cue_model_f1: [PLACEHOLDER]
mert_model_f1: [PLACEHOLDER]  # from Results
human_f1: [PLACEHOLDER]       # from Results
```

[PLACEHOLDER: interpretation — does cue-based model close the gap to MERT/human, or does a gap remain? What does that imply about whether MERT is capturing something beyond boring cues?]


###  References
<a id="ref-mert"></a>
[1] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Y. Guo, and J. Fu, "MERT: Acoustic Music Understanding Model with Large-Scale Self-supervised Training," *arXiv preprint arXiv:2306.00107*, 2023.