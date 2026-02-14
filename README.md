 # VidProM Explorer: What Do People Ask Video AI to Generate?                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                  
  Exploratory data analysis and clustering of **1.67M video generation prompts** from the [VidProM](https://huggingface.co/datasets/WenhaoWang/VidProM) dataset.                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                    
  ## Motivation

  Text-to-video AI models (Sora, Runway, Pika) are rapidly growing, but little is known about *what* people actually ask them to generate. This project analyzes real user prompts to uncover patterns, themes, and content trends in video generation.

  ## Key Findings

  - **Prompt length:** median 68 characters / 11 words — most prompts are concise scene descriptions
  - **Time span:** 248 days (Jun 2023 — Mar 2024), covering the early adoption period of video AI
  - **Content safety:** 98% of prompts are clean; only 1.89% have toxicity > 0.5
  - **10 thematic clusters** discovered via KMeans on sentence embeddings:

  | Cluster | Count | Theme |
  |---------|-------|-------|
  | 0 | 3,924 | Discord messages/attachments (junk) |
  | 1 | 9,553 | Epic/historical scenes (warriors, mythology) |
  | 2 | 10,132 | Animals/creatures (cats, owls, cartoon animals) |
  | 3 | 12,691 | Cinematic/aesthetic (8K, realism, aspect ratios) |
  | 4 | 15,700 | Mixed/general (diverse, no clear theme) |
  | 5 | 8,929 | Women/girls (female characters, portraits) |
  | 6 | 9,636 | Men/characters (male characters, celebrities) |
  | 7 | 7,478 | Horror/dark (horror, sci-fi, dark atmosphere) |
  | 8 | 10,694 | Animation/cartoon (anime, 3D styles) |
  | 9 | 11,263 | Nature/landscapes (rain, mountains, forests) |

  ## Method

  1. **EDA** — distributions, temporal patterns, NSFW analysis, word frequency (pandas, matplotlib, seaborn)
  2. **Embeddings** — 100K prompts encoded with `all-MiniLM-L6-v2` (384-dim sentence embeddings)
  3. **Clustering** — PCA (384 → 50 dims) + KMeans (k=10), visualized via PCA 2D projection

  ## Sample Visualizations

  | Prompt Length Distribution | Cluster Scatter Plot |
  |---|---|
  | ![](data/prompt_length_dist.png) | ![](data/clusters_scatter.png) |

  ## Notebooks                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                    
  The analysis consists of two parts:

  **Exploratory Data Analysis**
  [1_eda.ipynb](notebooks/1_eda.ipynb) — data overview, distributions, temporal patterns, NSFW analysis, word frequency and bigrams. Produces 10+ visualizations with conclusions.

  **Clustering**
  [02_clustering.ipynb](notebooks/02_clustering.ipynb) — sentence embeddings via `all-MiniLM-L6-v2`, dimensionality reduction with PCA, KMeans clustering (k=10), cluster interpretation.

  ## Tools & Techniques

  - **Data processing:** pandas, numpy
  - **Visualization:** matplotlib, seaborn, wordcloud
  - **Embeddings:** sentence-transformers (`all-MiniLM-L6-v2`, 384-dim)
  - **Clustering:** PCA (scikit-learn), KMeans with Elbow method
  - **Dataset:** HuggingFace `datasets` library

  ## References

  - **Dataset:** [VidProM: A Million-scale Real Prompt-Gallery Dataset for Text-to-Video Diffusion Models](https://arxiv.org/abs/2403.06098) by Wenhao Wang et al.
  - **Embeddings model:** [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) by Sentence-Transformers
