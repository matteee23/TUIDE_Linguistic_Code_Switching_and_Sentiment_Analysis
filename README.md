# TUIDE: Linguistic Code-Switching & Sentiment Analysis

## Overview and Motivation

TUIDE's debut has been thought with the idea of blending different musical languages and strong performances on the stages. The question that I want to answer to is:

> **Do the lyrics of the five tracks on *Tune & Play* confirm this multilingual fusion and if so, in what proportion and how does it changes from song to song?**

The project also looks at how the emotional tone of each track is characterized.

## Data & Methodology
* **source**: lyrics for the five tracks (*ABD*, *SUN KISS*, *Echo*, *Flip-Flop Girl*, *GRLS*) were collected from Genius website;
* **copyright note**: raw lyrics are **not included in this repository** and are excluded via `.gitignore`. To reproduce the analysis, you'll need to source the lyrics yourself and place them locally as `.txt` files, one per song;
* **unit of analysis**: each song was split line by line and every line was analyzed independently for both language and sentiment.

## Tools & Models
| Task | Tool / Model |
|---|---|
| Language detection | [`lingua-py`](https://github.com/pemistahl/lingua-py), restricted to English, Spanish, French, Korean, and Japanese |
| Sentiment analysis | [`cardiffnlp/twitter-xlm-roberta-base-sentiment`](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment) |
| Aggregation | Python (`collections.Counter`) |

## Results

### Linguistic presence per song
<img src="./Linguistic_Presence_Graph.png" width="550">

| Song | Korean | English | Spanish | French | Japanese |
|---|---|---|---|---|---|
| ABD | 22.0% | 70.7% | 7.3% | 0% | 0% |
| SUN KISS | 14.9% | 67.2% | 17.9% | 0% | 0% |
| Echo | 7.3% | 87.8% | 4.9% | 0% | 0% |
| Flip-Flop Girl | 23.3% | 75.0% | 1.7% | 0% | 0% |
| GRLS | 0% | 98.0% | 0% | 2.0% | 0% |

### Sentiment per song
<img src="./Sentiment_Analysis_Graph.png" width="550">

| Song | Positive | Negative | Neutral |
|---|---|---|---|
| ABD | 22.0% | 0% | 78.0% |
| SUN KISS | 38.8% | 17.9% | 43.3% |
| Echo | 2.4% | 19.5% | 78.0% |
| Flip-Flop Girl | 48.3% | 5.0% | 46.7% |
| GRLS | 18.0% | 0% | 82.0% |

## Interpretation
* **multilingual fusion**: English dominates every track, ranging from 67% to 98% of lines. Korean plays a secondary role, peaking at 23.3% in *Flip-Flop Girl*, and French appears only marginally (2%, exclusively in *GRLS*). **Japanese was not detected in any of the five tracks.** Basically, the "multilingual fusion" of the group is promoted, for now, only in the group's visual/promotional concept, rather than in the lyrics themselves (**at least for this debut EP**);

* **sentiment**: majority of the lines in the album are classified as neutral (43–82%). Two tracks have to be put in evidence: *Flip-Flop Girl* has the most "positive" profile (48.3% positive, only 5% negative), while *Echo* has the album's highest negative share (19.5%) and almost no positive lines (2.4%), suggesting a more melancholic tone that contrasts with the rest of the EP.

## Limitations
- **Spanish and French detections are probably false positives**: until now, TUIDE didn't record any lyrics in Spanish or French. The model's predictions (Spanish up to 17.9% in *SUN KISS* and French around 2% in *GRLS*) were phonetically ambiguous lines misclassified due to the line-by-line, out-of-context approach. This was manually verified line by line and should be treated as a known weakness;
- **small sample**: five songs is not enough to generalize about the artist or genre beyond this specific EP. Since they are a novel group, this analysis could be extended in the future for obtaining a more precise answer;
- **single lines approach**: both language detection and sentiment models were applied to single lines, which is harder because short or ambiguous lines are more error-prone.

## Reproducing this analysis
1. Get lyrics for the five tracks and save them locally as `ABD_lyrics.txt`, `SUNKISS_lyrics.txt`, `Echo_lyrics.txt`, `Flip_Flop_Girl_lyrics.txt`, `GRLS_lyrics.txt`: these files are gitignored and must be sourced independently for copyright reasons;
2. Install dependencies: `pip install lingua-language-detector transformers torch`;
3. Run `TUIDE_LD.py`.

## License

Code released under the MIT License. Song lyrics are not included and remain the property of their respective rights holders.
