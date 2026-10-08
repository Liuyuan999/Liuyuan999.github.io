# Liuyuan Jiang — The geometry of learning and decisions

A separate static research website with seven project pages with integrated explanations, interactive teaching diagrams, and local video narration/storyboard drafts. Video links, draft pages, and script downloads are excluded from the deployed site until recordings are ready.

## Preview

Run `python3 -m http.server 8765 --bind 127.0.0.1 --directory dist` from this folder, then open http://127.0.0.1:8765/.

## Edit

- `content/papers.json`: author order, titles, venues, links, and source records.
- `content/profile.json`: researcher identity, portrait dimensions, and verified academic/profile/contact links.
- `content/articles.json`: integrated project explanations, evidence, and narration scenes.
- `content/explanations/`: editable Markdown exports of the explanations.
- Old `/blog/` URLs redirect to the matching project page and are excluded from the sitemap.
- `content/site.json`: site origin and `publish_videos` (currently `false`). This flag controls video links, generated video pages, script downloads, and video sitemap entries.
- `video-scripts/`: local narration and storyboard drafts, kept out of `dist/` while video publication is disabled.
- `dist/assets/style.css`: responsive visual design.
- `dist/assets/site.js`: interactive educational diagrams.
- `build.py` and `render_articles.py`: generate static pages and editable Markdown exports.

Run `python3 build.py` after editing content. No npm dependencies or build service are required.

## Publication inventory

1. SURF — NeurIPS 2026 acceptance reported on the author’s homepage. Public arXiv manuscript from May 2026.
2. RetailAgent — NeurIPS 2026 IAB Workshop, per the author’s October 8 venue update. Public arXiv manuscript remains linked.
3. BiRQ — ICASSP 2026 acceptance reported on the author’s homepage. Public arXiv manuscript from September 2025.
4. Efficient Penalty-Based Bilevel Methods — 2025 preprint. Related to the preceding Beyond Value Functions work; kept as a separate public record.
5. Beyond Value Functions / PBGD-Free — NeurIPS 2025.
6. Improved Analysis of Penalty-Based Methods — EUSIPCO 2025.
7. BLOCC — NeurIPS 2024.

The inventory covers publicly discoverable papers checked on October 8, 2026. It does not assert completeness for unpublished work or newly indexed records.

## Research content

Primary paper links are included on every project and explainer page. Code links are included where an author repository was verified. Venue announcements with only author-page verification are labeled accordingly. The website follows the progression of the advisor’s reference: takeaway, explanation, interactive concept, supporting evidence, technical scope, and citation. Its source and design were written independently.

All toy demonstrations identify their status. The BiRQ WER chart uses measured values from Table 2. The timing widget uses synthetic returns. The schedule widget is a teaching illustration and is not a runtime benchmark. Narration scripts include on-screen directions and recording notes.

## Files and hosting

Source repository: https://github.com/Liuyuan999/Liuyuan999.github.io/tree/main/research-source

Website: https://liuyuan999.github.io/research/

The homepage repository’s `.github/workflows/pages.yml` builds the academic homepage and this research site on GitHub, then publishes the research output at `/research/`. Pushing to `main` triggers a deployment; the Actions tab also supports a manual run. The workflow uses GitHub Pages metadata for the site origin so canonical links and the sitemap follow the configured address.

To connect a custom domain, open this repository’s **Settings → Pages**, enter the domain, and follow [GitHub’s DNS instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site). No domain has been configured in this repository.

`work/` holds downloaded public PDFs, extraction files, temporary publishing files, and QA artifacts. It is excluded from Git and deployment. Video drafts stay outside the hosted output.

## Recording the videos

Each file in `video-scripts/` contains narration plus on-screen directions. Record the narration, add paper figures with their table/figure identifiers, include captions, and end with the project URL. After uploading a video, add its verified embed URL to the corresponding video page, then enable `publish_videos` in `content/site.json` and rebuild. Do not label a script as a recorded talk.

## Refined project narratives

`content/project-stories.json` controls each paper’s human-readable headline, hero figure captions, three-step method, technical reasoning, notation, result context, measured chart values, and connections to other papers. `content/articles.json` holds the integrated explanation and video scenes. Measured charts cite their specific table or section. Interactive geometry and bound envelopes are clearly labeled as toy or schematic.

The project pages contain explanations, interactive examples, results, technical details, and citations. Narration and storyboards remain in local `video-scripts/` drafts. The deployed site does not include video pages or script downloads. Legacy `/blog/<slug>/` URLs redirect to the integrated explanation.

## Mathematical notation and research areas

The hub opens with an interactive direction explorer: Multi-objective Learning (SURF), Bilevel Optimization (four papers), and Applications (RetailAgent and BiRQ). The direction labels do not fix a permanent number of research areas. `research_hub.py` controls the topic map and publication rows. The rows show each paper’s full title, authors, venue, figure preview, and available resource links. Preview plots are labeled as illustrative or linked to their primary-paper table.

`content/equations.json` contains the display and inline TeX. `compile_math.mjs` renders it with the pinned, locally vendored KaTeX 0.19.0 package; `math_typesetting.py` adds accessible MathML and bundles the local stylesheet and fonts. `python3 build.py` requires Node.js (uses the installed Codex runtime as a fallback on this computer). Equations are pre-rendered and do not depend on a CDN or browser JavaScript. Malformed TeX fails the build. Main formulations, interactive constraint-regime formulas, and update steps use the same renderer.

### Research atlas and original paper figures

SURF is pinned first at the author’s request. Remaining publications are sorted by publication year, newest first; first public release month breaks ties within a year. `content/hub-curation.json` records this ordering, descriptive paper-jump labels, and the paper-to-visual evidence notes. Direction links include the paper’s contribution and venue and jump to stable `#paper-<slug>` publication anchors.

The opening headline is “The geometry of learning and decisions.” The direction tabs support clicks, arrow keys, Home/End, and direct direction fragments. The opening multi-objective example uses a gently bowed analytic toy front to contrast equal scalarization-weight steps with equal arc-length spacing. Its application view illustrates LLM summary quality versus factual faithfulness. Candidate points and a keyboard-accessible slider expose their illustrative normalized scores. The SURF project page retains its original quadratic/quartic toy. The bilevel example uses a bakery: the seller sets a price and a customer chooses how much bread to buy. Optional customer-budget and stock-limit buttons alter the response and profit. Applications switches between original BiRQ and RetailAgent architecture figures. With JavaScript disabled, all directions remain available.

`content/paper-figures.json` records each original figure or table, its source URL, local image dimensions, explanatory caption, and any PDF crop. Original artwork lives in `dist/assets/paper-figures/`. arXiv PNG/SVG assets are preserved; RetailAgent Figure 2 and EUSIPCO Table I are extracted from the original PDFs. The project page displays a source link and full-size image link for every figure. Preview charts for RetailAgent and smoothness are explicitly distinguished as reported results and an explanatory toy.

## Researcher portrait and profiles

The header’s small circular avatar uses the user-supplied `jiang.PNG` portrait, copied unchanged to `dist/assets/liuyuan-jiang.png`. The biography and profile links appear at the end of the home page. `content/profile.json` centralizes the academic homepage, Google Scholar, GitHub, and email links displayed in the About area. The academic homepage links to Scholar; the GitHub profile matches the verified research repositories. The supplied root photo is kept locally and excluded from Git because the served copy is versioned.

The bakery demo is an illustrative continuous model: the customer maximizes `(8−x)y−y²/2` over nonnegative bread quantity y, giving an unconstrained response `max(0,8−x)`. Optional limits are spending `xy≤12` and stock `y≤3`. The shop’s unit cost is $1/kg, so profit is `(x−1)y`. All calculations use the selected price and constraint states; they are not paper experiment data.

The bakery role cards and controls use decorative system emoji for the baker, customer, bread, budget, and profit. Text labels provide the meaning, and emoji are hidden from assistive technology. Publication overlines show only the year, avoiding numbers that could be mistaken for release months.

The opening front minimizes `f1(z)=z` and `f2(z)=0.5(1−z)+0.5(exp(−5z)−exp(−5))/(1−exp(−5))`, for `z∈[0,1]`, and displays normalized rewards `(1−f1,1−f2)`. Both endpoint tangents have nonzero slopes. The equally spaced weights span the active range `w=s/(1+s)` for `s=−f2′(z)`; they do not include redundant endpoint-only weights outside that range. Arc-length sampling uses the same normalized coordinates and equal plot scales. The application is motivated by SURF Section 4.2 and Appendix F.3, where the real experiment uses summarization-quality and factual-faithfulness reward models with KL regularization; the opening scores are synthetic teaching values.


Project-page refinement (October 8, 2026): `content/project-guides.json` stores the paper-specific problem narrative, figure reading guide, reported comparisons, evaluation protocol, theorem pointers, and reader questions. `render_project_pages.py` renders this material alongside the existing demos and local KaTeX. Evidence tabs select actual comparisons transcribed from the cited papers; their panels remain readable with JavaScript disabled. Scripts and storyboards remain separate from project pages and are kept as local drafts until video publication is enabled.

RetailAgent is listed as **NeurIPS 2026 · IAB Workshop**, following the author’s venue correction; its citation expands IAB to Interpreting Agent Behavior. The wider penalty preprint uses the current source’s theorem labels (3.1, 4.1, 5.1, and 5.2). SURF’s N denotes segments, with N + 1 solved points. Project pages preserve each source’s notation: SURF uses Φ and the vector f_PF, BLOCC uses g^c and μ_g^*, the wider preprint uses the joint objective F̃γ, and EUSIPCO uses Hγ. No shorthand aliases are introduced. The SURF and BLOCC interactives use the source papers’ own examples.
