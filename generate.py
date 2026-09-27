from pathlib import Path
import json
import html


OUTPUT = Path("index.html")


# ============================================================
# ARCHIVAL PERSONNEL
# ============================================================

PERSONS = [
    {
        "name": "Aren Voss",
        "role": "Provincial Cartographer",
        "origin": "Northern Territories",
        "period": "Late 18th Century",
        "category": "Practical Philosophy",
    },
    {
        "name": "Mira Sen",
        "role": "Keeper of the Eastern Observatory",
        "origin": "Eastern Provinces",
        "period": "Early 20th Century",
        "category": "Observation",
    },
    {
        "name": "Captain Ilyan Vale",
        "role": "Survey Officer",
        "origin": "Western Maritime District",
        "period": "19th Century",
        "category": "Endurance",
    },
    {
        "name": "Professor Niko Almostov",
        "role": "Lecturer in Natural Philosophy",
        "origin": "Central Academy",
        "period": "Early 20th Century",
        "category": "Reason",
    },
    {
        "name": "Elias Thorne",
        "role": "Village Magistrate",
        "origin": "Northwestern Counties",
        "period": "19th Century",
        "category": "Judgment",
    },
    {
        "name": "Sera Valen",
        "role": "Archivist of Maritime Records",
        "origin": "Southern Coast",
        "period": "Late 19th Century",
        "category": "Memory",
    },
    {
        "name": "Old Master Ren",
        "role": "Instructor of Rural Mechanics",
        "origin": "Eastern Highlands",
        "period": "Undated",
        "category": "Work",
    },
    {
        "name": "Dorian Pell",
        "role": "Registrar of Minor Disputes",
        "origin": "Central Administrative District",
        "period": "19th Century",
        "category": "Human Nature",
    },
    {
        "name": "Ansel Grey",
        "role": "Railway Engineer",
        "origin": "Industrial North",
        "period": "Early 20th Century",
        "category": "Persistence",
    },
    {
        "name": "Liora Venn",
        "role": "Teacher of Rhetoric",
        "origin": "Old University Quarter",
        "period": "Late 19th Century",
        "category": "Language",
    },
    {
        "name": "Bastian Or",
        "role": "Keeper of the Municipal Clock",
        "origin": "Old Capital",
        "period": "19th Century",
        "category": "Time",
    },
    {
        "name": "Nera Sol",
        "role": "Apothecary's Apprentice",
        "origin": "Southern Market District",
        "period": "Early 19th Century",
        "category": "Experience",
    },
    {
        "name": "Havel Marr",
        "role": "Bridge Inspector",
        "origin": "River Provinces",
        "period": "19th Century",
        "category": "Risk",
    },
    {
        "name": "Orin Bell",
        "role": "Clerk of Agricultural Affairs",
        "origin": "Western Plains",
        "period": "Early 20th Century",
        "category": "Growth",
    },
    {
        "name": "Tavian Roe",
        "role": "Instructor of Navigation",
        "origin": "Northern Port",
        "period": "18th Century",
        "category": "Direction",
    },
]


# ============================================================
# WORD BANK
# ============================================================

OBJECTS = [
    "door",
    "key",
    "chair",
    "window",
    "clock",
    "bridge",
    "map",
    "ladder",
    "bucket",
    "stone",
    "rope",
    "lantern",
    "bell",
    "mirror",
    "road",
    "gate",
    "bench",
    "cup",
    "umbrella",
    "stair",
    "wheel",
    "book",
    "compass",
    "coat",
    "shoe",
    "fence",
    "boat",
    "roof",
    "grain",
    "hammer",
]

ABSTRACT = [
    "patience",
    "courage",
    "ambition",
    "certainty",
    "failure",
    "discipline",
    "fear",
    "memory",
    "doubt",
    "success",
    "attention",
    "silence",
    "knowledge",
    "effort",
    "hope",
    "habit",
    "pride",
    "curiosity",
    "judgment",
    "wisdom",
    "responsibility",
    "change",
    "purpose",
]

ACTIONS = [
    "waiting",
    "walking",
    "building",
    "repairing",
    "measuring",
    "searching",
    "listening",
    "questioning",
    "leaving",
    "returning",
    "beginning",
    "finishing",
    "counting",
    "learning",
    "forgetting",
    "observing",
    "carrying",
    "planting",
    "climbing",
]


# ============================================================
# QUOTE LIBRARY
# ============================================================

QUOTE_TEMPLATES = [
    (
        "A person who waits for the perfect {object} eventually becomes part of the furniture.",
        "Excessive preparation can quietly become another form of inaction."
    ),
    (
        "The {object} never promised to move. That is why every map eventually learns humility.",
        "Reality does not owe itself to our preferred route."
    ),
    (
        "A locked door is a very confident piece of furniture.",
        "Obstacles often appear more authoritative than they really are."
    ),
    (
        "The smallest key opened the largest door because the door had no opinion about size.",
        "The apparent scale of a problem and the scale of the action required to change it are not necessarily related."
    ),
    (
        "I planted a question and harvested an inconvenience. It was the most useful crop I ever grew.",
        "Good questions rarely provide immediate comfort. Their value often lies in exposing assumptions."
    ),
    (
        "A clock that is wrong twice a day is still employed by time.",
        "Usefulness cannot always be reduced to perfect accuracy."
    ),
    (
        "The bridge looked stronger after everyone stopped asking whether it was strong.",
        "Removing questions does not remove the conditions that made the questions necessary."
    ),
    (
        "I carried the {object} for ten miles before discovering that it was the wrong thing to carry.",
        "Effort and direction are separate virtues."
    ),
    (
        "A map becomes dangerous when the traveler starts apologizing to the road.",
        "Reality should not be forced to obey the diagram."
    ),
    (
        "The ladder did not become shorter because I complained about the height.",
        "Frustration can describe difficulty, but description alone does not reduce it."
    ),
    (
        "A heavy stone teaches patience because it refuses to be impressed.",
        "Some problems respond poorly to force and better to sustained attention."
    ),
    (
        "The road was not difficult. My expectations were carrying too much luggage.",
        "Expectations can add weight to an already demanding task."
    ),
    (
        "A person who counts every step eventually discovers that walking was never a spreadsheet.",
        "Measurement is useful, but excessive measurement can replace participation with observation."
    ),
    (
        "The empty chair taught me more about absence than the crowded room.",
        "What is missing can sometimes reveal structure more clearly than what is present."
    ),
    (
        "I asked the mirror for advice. It returned the same face and charged no fee.",
        "Reflection is valuable, but self-examination must eventually produce action."
    ),
    (
        "A broken compass can still teach you that you are lost.",
        "Failure of a tool does not eliminate the information contained in the failure."
    ),
    (
        "The bell rang because someone pulled it. History later called this inevitability.",
        "Events often appear inevitable only after their causes have become part of the past."
    ),
    (
        "The door was ordinary until I needed it to be extraordinary.",
        "Circumstances can change the meaning of ordinary things without changing their nature."
    ),
    (
        "A perfect plan has never survived its first meeting with weather.",
        "Planning is valuable because it prepares action, not because it predicts every condition."
    ),
    (
        "I lost the key and discovered that the door had never been locked.",
        "Assumptions can become stronger barriers than the circumstances they were created to explain."
    ),
    (
        "The old road remained useful after the destination changed.",
        "Past methods may retain value even when their original purpose no longer exists."
    ),
    (
        "A question becomes heavier when everyone agrees not to ask it.",
        "Collective silence can increase the social weight of an issue rather than eliminate it."
    ),
    (
        "The clock was late, but the meeting was later.",
        "Precision in one part of a system does not guarantee coordination across the whole system."
    ),
    (
        "I sharpened the pencil until there was nothing left with which to write.",
        "Optimization can become destructive when improvement is measured without reference to purpose."
    ),
    (
        "The shortest road looked suspicious because nobody had taken it seriously.",
        "Useful possibilities are sometimes ignored because familiarity is mistaken for evidence."
    ),
]


# ============================================================
# ADDITIONAL ANALYSIS
# ============================================================

INTERPRETATIONS = [
    "The statement uses an ordinary object to examine a larger question concerning intention, expectation and consequence.",
    "Its apparent absurdity conceals a distinction between activity and progress.",
    "The image suggests that uncertainty does not disappear merely because a person becomes confident about an explanation.",
    "The statement examines the difference between effort and direction.",
    "The underlying observation is that people often assign intention to circumstances that are indifferent to them.",
    "The physical image can be read as a metaphor for the gradual transformation of a temporary condition into a permanent habit.",
    "The statement questions whether efficiency should always be treated as the highest form of improvement.",
    "The image suggests that interpretation itself can become part of an event's consequences.",
]


QUESTIONS = [
    "What changes when an obstacle is treated as information rather than opposition?",
    "At what point does preparation stop being preparation and become avoidance?",
    "Can an imperfect method still produce useful understanding?",
    "How much of difficulty belongs to the problem, and how much belongs to expectation?",
    "When does persistence become attachment to a mistaken direction?",
    "Can certainty be useful while still being incomplete?",
    "What disappears when measurement becomes more important than experience?",
    "Does a solution remain a solution when it creates a larger problem?",
    "How often do people mistake familiarity for truth?",
    "What can absence reveal that presence conceals?",
]


APPLICATIONS = [
    "The observation favors small experiments over elaborate assumptions.",
    "The principle can be applied by separating effort from outcome and examining whether the chosen direction still serves the original purpose.",
    "A useful application is to identify which part of a problem is factual and which part has been added through expectation.",
    "The statement suggests checking the instrument, map or assumption before increasing effort.",
    "The practical lesson is not to abandon planning, but to keep plans subordinate to evidence.",
    "In work and study, this principle supports periodic review rather than endless continuation of an inherited method.",
]


# ============================================================
# HINDI
# ============================================================

HINDI = {
    "A locked door is a very confident piece of furniture.":
        "एक बंद दरवाज़ा बहुत आत्मविश्वासी फर्नीचर होता है।",

    "The smallest key opened the largest door because the door had no opinion about size.":
        "सबसे छोटी चाबी ने सबसे बड़ा दरवाज़ा खोला, क्योंकि दरवाज़े की आकार को लेकर कोई राय नहीं थी।",

    "The mountain did not become smaller. I simply stopped negotiating with it.":
        "पहाड़ छोटा नहीं हुआ। मैंने बस उससे समझौता करना बंद कर दिया।",

    "The old road remained useful after the destination changed.":
        "मंज़िल बदल जाने के बाद भी पुरानी सड़क उपयोगी बनी रही।",

    "A perfect plan has never survived its first meeting with weather.":
        "कोई भी पूर्ण योजना मौसम से अपनी पहली मुलाकात के बाद वैसी नहीं रहती।",

    "I lost the key and discovered that the door had never been locked.":
        "मैंने चाबी खो दी और पाया कि दरवाज़ा कभी बंद था ही नहीं।",

    "A broken compass can still teach you that you are lost.":
        "टूटा हुआ कम्पास भी यह सिखा सकता है कि आप रास्ता भटक चुके हैं।",

    "The ladder did not become shorter because I complained about the height.":
        "मेरी शिकायत करने से सीढ़ी छोटी नहीं हुई।",

    "The road was not difficult. My expectations were carrying too much luggage.":
        "रास्ता कठिन नहीं था। मेरी अपेक्षाएँ बहुत अधिक सामान उठा रही थीं।",

    "The empty chair taught me more about absence than the crowded room.":
        "खाली कुर्सी ने मुझे अनुपस्थिति के बारे में भरे हुए कमरे से अधिक सिखाया।",

    "The bell rang because someone pulled it. History later called this inevitability.":
        "घंटी इसलिए बजी क्योंकि किसी ने उसे खींचा था। इतिहास ने बाद में इसे अपरिहार्यता कहा।",

    "The clock was late, but the meeting was later.":
        "घड़ी देर से थी, लेकिन बैठक उससे भी देर से थी।",
}


# ============================================================
# SERIALIZATION
# ============================================================

def js(data):
    return json.dumps(data, ensure_ascii=False)


DATA = {
    "persons": PERSONS,
    "quotes": [
        {
            "quote": quote,
            "interpretation": interpretation,
        }
        for quote, interpretation in QUOTE_TEMPLATES
    ],
    "interpretations": INTERPRETATIONS,
    "questions": QUESTIONS,
    "applications": APPLICATIONS,
    "hindi": HINDI,
}


# ============================================================
# HTML
# ============================================================

def build_html():

    data_json = js(DATA)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>The Human Wisdom Archive</title>

<meta
    name="description"
    content="The Human Wisdom Archive — catalogued observations concerning conduct, judgment, memory, work and human experience."
>

<style>

:root {{
    --paper: #f4f0e7;
    --paper2: #ebe4d6;
    --ink: #191919;
    --muted: #706b63;
    --line: rgba(25,25,25,.17);
    --strong: rgba(25,25,25,.38);
    --accent: #823328;
    --serif: Georgia, "Times New Roman", serif;
    --sans: Arial, Helvetica, sans-serif;
    --mono: "Courier New", monospace;
}}

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(130,51,40,.05),
            transparent 28%
        ),
        var(--paper);
    color: var(--ink);
    font-family: var(--sans);
}}

body.dark {{
    --paper: #111;
    --paper2: #191919;
    --ink: #eee9df;
    --muted: #a49f96;
    --line: rgba(255,255,255,.16);
    --strong: rgba(255,255,255,.36);
    --accent: #c27b6c;
}}

body.blue {{
    --accent: #304d70;
}}

body.green {{
    --accent: #49654d;
}}

body.brown {{
    --accent: #735335;
}}

.archive {{
    width: min(1500px, 100%);
    margin: auto;
    padding: 22px;
}}

.header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    gap: 30px;
    border-bottom: 1px solid var(--strong);
    padding-bottom: 22px;
}}

.kicker {{
    color: var(--muted);
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-bottom: 7px;
}}

.title {{
    font-family: var(--serif);
    font-size: clamp(29px, 4vw, 52px);
    line-height: .95;
    letter-spacing: -.04em;
}}

.subtitle {{
    max-width: 700px;
    color: var(--muted);
    font-family: var(--serif);
    line-height: 1.45;
    font-size: 15px;
    margin-top: 8px;
}}

.controls {{
    display: flex;
    gap: 7px;
    flex-wrap: wrap;
    justify-content: flex-end;
}}

.btn {{
    border: 1px solid var(--strong);
    background: transparent;
    color: var(--ink);
    padding: 10px 13px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .08em;
    text-transform: uppercase;
    transition: .18s ease;
}}

.btn:hover {{
    background: var(--ink);
    color: var(--paper);
}}

.catalog {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-bottom: 1px solid var(--line);
}}

.catalog-item {{
    padding: 13px 15px;
    min-height: 70px;
    border-right: 1px solid var(--line);
}}

.catalog-item:last-child {{
    border-right: 0;
}}

.label {{
    display: block;
    color: var(--muted);
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .13em;
    text-transform: uppercase;
    margin-bottom: 7px;
}}

.value {{
    font-family: var(--mono);
    font-size: 11px;
}}

.content {{
    display: grid;
    grid-template-columns: minmax(0, 1.75fr) minmax(280px, .65fr);
}}

.main {{
    padding: clamp(45px, 7vw, 100px) clamp(20px, 7vw, 100px) 80px 0;
    border-right: 1px solid var(--line);
}}

.side {{
    padding: 45px 0 50px 35px;
}}

.record-label {{
    color: var(--accent);
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: .15em;
    text-transform: uppercase;
    margin-bottom: 28px;
}}

.quote {{
    margin: 0;
    max-width: 1100px;
    font-family: var(--serif);
    font-size: clamp(37px, 5.8vw, 82px);
    line-height: 1.02;
    font-weight: 400;
    letter-spacing: -.045em;
}}

.attribution {{
    border-top: 1px solid var(--line);
    margin-top: 45px;
    padding-top: 18px;
}}

.name {{
    font-family: var(--serif);
    font-size: 25px;
}}

.role {{
    margin-top: 5px;
    color: var(--muted);
    font-family: var(--mono);
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: .1em;
}}

.quote-actions {{
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    margin-top: 27px;
    padding-bottom: 35px;
    border-bottom: 1px solid var(--line);
}}

.quote-actions .btn {{
    border-color: var(--accent);
}}

.interpretation {{
    margin-top: 50px;
    padding-top: 17px;
    border-top: 2px solid var(--ink);
}}

.interpretation-text {{
    max-width: 850px;
    font-family: var(--serif);
    font-size: clamp(18px, 2vw, 25px);
    line-height: 1.45;
}}

.analysis {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    border-left: 1px solid var(--line);
    border-top: 1px solid var(--line);
    margin-top: 35px;
}}

.card {{
    min-height: 170px;
    padding: 21px;
    border-right: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
}}

.card p {{
    margin: 0;
    font-family: var(--serif);
    font-size: 16px;
    line-height: 1.55;
}}

.question {{
    margin-top: 45px;
    border: 1px solid var(--strong);
    padding: 25px;
}}

.question-text {{
    font-family: var(--serif);
    font-size: 23px;
    line-height: 1.4;
}}

.seal {{
    width: 95px;
    height: 95px;
    border: 1px solid var(--strong);
    border-radius: 50%;
    display: grid;
    place-items: center;
    text-align: center;
    font-family: var(--mono);
    font-size: 8px;
    line-height: 1.4;
    letter-spacing: .08em;
    margin-bottom: 25px;
}}

.side-section {{
    border-bottom: 1px solid var(--line);
    padding-bottom: 27px;
    margin-bottom: 27px;
}}

.side-text {{
    font-family: var(--serif);
    font-size: 16px;
    line-height: 1.55;
}}

.meta {{
    display: grid;
    gap: 15px;
}}

.meta-row {{
    display: grid;
    gap: 4px;
}}

.meta-key {{
    color: var(--muted);
    font-family: var(--mono);
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: .1em;
}}

.meta-value {{
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.3;
}}

.footer {{
    display: flex;
    justify-content: space-between;
    gap: 20px;
    border-top: 1px solid var(--strong);
    padding-top: 17px;
    color: var(--muted);
    font-family: var(--mono);
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: .1em;
}}

.toast {{
    position: fixed;
    left: 50%;
    bottom: 24px;
    transform: translate(-50%, 20px);
    background: var(--ink);
    color: var(--paper);
    padding: 12px 17px;
    font-family: var(--mono);
    font-size: 10px;
    opacity: 0;
    pointer-events: none;
    transition: .2s;
    z-index: 100;
}}

.toast.show {{
    opacity: 1;
    transform: translate(-50%, 0);
}}

.hi {{
    display: none;
}}

body.hindi .en {{
    display: none;
}}

body.hindi .hi {{
    display: inline;
}}

body.hindi .quote,
body.hindi .interpretation-text,
body.hindi .question-text,
body.hindi .card p,
body.hindi .side-text {{
    font-family: Arial, "Noto Sans Devanagari", sans-serif;
}}

@media (max-width: 950px) {{

    .header {{
        display: block;
    }}

    .controls {{
        justify-content: flex-start;
        margin-top: 20px;
    }}

    .catalog {{
        grid-template-columns: repeat(2, 1fr);
    }}

    .catalog-item:nth-child(2) {{
        border-right: 0;
    }}

    .catalog-item:nth-child(-n+2) {{
        border-bottom: 1px solid var(--line);
    }}

    .content {{
        grid-template-columns: 1fr;
    }}

    .main {{
        border-right: 0;
        padding-right: 0;
    }}

    .side {{
        border-top: 1px solid var(--strong);
        padding-left: 0;
    }}
}}

@media (max-width: 620px) {{

    .archive {{
        padding: 12px;
    }}

    .title {{
        font-size: 32px;
    }}

    .catalog {{
        grid-template-columns: 1fr 1fr;
    }}

    .main {{
        padding-top: 50px;
    }}

    .quote {{
        font-size: 38px;
    }}

    .analysis {{
        grid-template-columns: 1fr;
    }}

    .footer {{
        flex-direction: column;
    }}
}}

@media (max-width: 390px) {{

    .catalog {{
        grid-template-columns: 1fr;
    }}

    .catalog-item {{
        border-right: 0 !important;
        border-bottom: 1px solid var(--line);
    }}

    .controls {{
        display: grid;
        grid-template-columns: 1fr 1fr;
    }}

    .btn {{
        width: 100%;
    }}

    .quote {{
        font-size: 31px;
    }}

    .quote-actions {{
        display: grid;
        grid-template-columns: 1fr;
    }}
}}

@media print {{

    .controls,
    .quote-actions,
    .toast {{
        display: none !important;
    }}

    .archive {{
        width: 100%;
        padding: 0;
    }}

    body {{
        background: white !important;
        color: black !important;
    }}

    .quote {{
        font-size: 45px;
    }}

}}

</style>
</head>

<body>

<div class="archive">

<header class="header">

<div>

<div class="kicker">
Department of Comparative Thought · Repository Division
</div>

<div class="title">
The Human Wisdom Archive
</div>

<div class="subtitle">
A catalogued collection of observations concerning conduct,
judgment, work, uncertainty, memory and the ordinary problems
of human life.
</div>

</div>

<div class="controls">

<button class="btn" id="language">
<span class="en">हिंदी / EN</span>
<span class="hi">EN / हिंदी</span>
</button>

<button class="btn" id="copyRecord">
<span class="en">Copy Record</span>
<span class="hi">रिकॉर्ड कॉपी</span>
</button>

<button class="btn" id="printRecord">
<span class="en">Print</span>
<span class="hi">प्रिंट</span>
</button>

<button class="btn" id="newRecord">
<span class="en">New Record</span>
<span class="hi">नया रिकॉर्ड</span>
</button>

</div>

</header>


<section class="catalog">

<div class="catalog-item">

<span class="label">Archive Number</span>

<span class="value" id="archiveNumber">
</span>

</div>

<div class="catalog-item">

<span class="label">Classification</span>

<span class="value" id="classification">
</span>

</div>

<div class="catalog-item">

<span class="label">Record Status</span>

<span class="value">CATALOGUED</span>

</div>

<div class="catalog-item">

<span class="label">Repository</span>

<span class="value">HUMAN THOUGHT</span>

</div>

</section>


<main class="content">

<section class="main">

<div class="record-label">
Archival Statement
</div>

<blockquote class="quote" id="quote">
</blockquote>


<div class="attribution">

<div class="name" id="name">
</div>

<div class="role" id="role">
</div>

</div>


<!-- ======================================================
     QUOTE ACTIONS
     ====================================================== -->

<div class="quote-actions">

<button class="btn" id="copyQuote">
<span class="en">Copy Quote</span>
<span class="hi">उद्धरण कॉपी करें</span>
</button>

<button class="btn" id="screenshotQuote">
<span class="en">Screenshot Quote</span>
<span class="hi">उद्धरण स्क्रीनशॉट</span>
</button>

<button class="btn" id="copyQuoteWithAuthor">
<span class="en">Copy Quote + Author</span>
<span class="hi">उद्धरण + लेखक कॉपी करें</span>
</button>

</div>


<section class="interpretation">

<div class="label">
Interpretive Record
</div>

<div class="interpretation-text" id="interpretation">
</div>

</section>


<section class="analysis" id="analysis">
</section>


<section class="question">

<div class="label">
Question Raised
</div>

<div class="question-text" id="question">
</div>

</section>

</section>


<aside class="side">

<div class="seal">
HUMAN<br>
WISDOM<br>
ARCHIVE
</div>


<section class="side-section">

<div class="label">
Biographical Record
</div>

<div class="meta">

<div class="meta-row">
<span class="meta-key">Name</span>
<span class="meta-value" id="metaName"></span>
</div>

<div class="meta-row">
<span class="meta-key">Occupation</span>
<span class="meta-value" id="metaRole"></span>
</div>

<div class="meta-row">
<span class="meta-key">Origin</span>
<span class="meta-value" id="metaOrigin"></span>
</div>

<div class="meta-row">
<span class="meta-key">Period</span>
<span class="meta-value" id="metaPeriod"></span>
</div>

</div>

</section>


<section class="side-section">

<div class="label">
Practical Application
</div>

<div class="side-text" id="application">
</div>

</section>


<section class="side-section">

<div class="label">
Cataloguing Note
</div>

<div class="side-text">
The present record has been indexed according to
subject, form, interpretive tradition and historical
context.
</div>

</section>

</aside>

</main>


<footer class="footer">

<span>
The Human Wisdom Archive · Repository Division
</span>

<span id="footerNumber">
</span>

</footer>

</div>


<div class="toast" id="toast">
</div>


<script>

const DATA = {data_json};


let currentRecord = null;


function randomItem(list) {{
    return list[
        Math.floor(
            Math.random() * list.length
        )
    ];
}}


function archiveNumber() {{

    return "WA-" +
        Math.floor(
            100000 +
            Math.random() * 900000
        );

}}


function makeQuote() {{

    const source = randomItem(DATA.quotes);

    let quote = source.quote;

    quote = quote.replace(
        /{{object}}/g,
        randomItem([
            "door",
            "key",
            "chair",
            "window",
            "clock",
            "bridge",
            "map",
            "ladder",
            "bucket",
            "stone",
            "rope",
            "lantern",
            "bell",
            "mirror",
            "road",
            "gate"
        ])
    );

    return {{
        quote: quote,
        interpretation: source.interpretation
    }};

}}


function makeRecord() {{

    const person =
        randomItem(DATA.persons);

    const q =
        makeQuote();

    return {{

        id: archiveNumber(),

        person: person,

        quote: q.quote,

        interpretation:
            Math.random() < 0.45
                ? randomItem(DATA.interpretations)
                : q.interpretation,

        question:
            randomItem(DATA.questions),

        application:
            randomItem(DATA.applications),

        cards: [

            {{
                title: "Contextual Note",
                text:
                    "The wording belongs to a broader tradition "
                    + "in which ordinary observations are used "
                    + "to examine larger questions of conduct "
                    + "and judgment."
            }},

            {{
                title: "Observed Principle",
                text:
                    randomItem(DATA.interpretations)
            }},

            {{
                title: "Contradiction",
                text:
                    "The apparent contradiction is precisely "
                    + "what allows the statement to expose "
                    + "an otherwise familiar assumption."
            }},

            {{
                title: "Alternative Reading",
                text:
                    "The statement can be read literally, "
                    + "symbolically, or as an observation about "
                    + "the relationship between expectation "
                    + "and circumstance."
            }},

            {{
                title: "Practical Reading",
                text:
                    randomItem(DATA.applications)
            }}

        ]

    }};

}}


function text(id, value) {{

    const element =
        document.getElementById(id);

    if (element) {{
        element.textContent = value;
    }}

}}


function render(record) {{

    currentRecord = record;

    text(
        "archiveNumber",
        record.id
    );

    text(
        "footerNumber",
        record.id
    );

    text(
        "classification",
        record.person.category
    );

    text(
        "quote",
        record.quote
    );

    text(
        "name",
        record.person.name
    );

    text(
        "role",
        record.person.role
    );

    text(
        "metaName",
        record.person.name
    );

    text(
        "metaRole",
        record.person.role
    );

    text(
        "metaOrigin",
        record.person.origin
    );

    text(
        "metaPeriod",
        record.person.period
    );

    text(
        "interpretation",
        record.interpretation
    );

    text(
        "question",
        record.question
    );

    text(
        "application",
        record.application
    );


    const analysis =
        document.getElementById("analysis");

    analysis.innerHTML = "";


    const cards =
        [...record.cards]
        .sort(() => Math.random() - .5)
        .slice(
            0,
            4 + Math.floor(Math.random() * 2)
        );


    cards.forEach(card => {{

        const article =
            document.createElement("article");

        article.className = "card";

        const heading =
            document.createElement("div");

        heading.className = "label";

        heading.textContent =
            card.title;

        const paragraph =
            document.createElement("p");

        paragraph.textContent =
            card.text;

        article.appendChild(heading);
        article.appendChild(paragraph);

        analysis.appendChild(article);

    }});


    randomTheme();

}}


function randomTheme() {{

    document.body.classList.remove(
        "dark",
        "blue",
        "green",
        "brown"
    );

    const themes = [
        "",
        "",
        "blue",
        "green",
        "brown",
        "dark"
    ];

    const theme =
        randomItem(themes);

    if (theme) {{
        document.body.classList.add(theme);
    }}

}}


async function copyText(value, message) {{

    try {{

        await navigator.clipboard.writeText(
            value
        );

    }} catch (error) {{

        const textarea =
            document.createElement("textarea");

        textarea.value = value;

        document.body.appendChild(
            textarea
        );

        textarea.select();

        document.execCommand("copy");

        textarea.remove();

    }}

    showToast(message);

}}


function showToast(message) {{

    const toast =
        document.getElementById("toast");

    toast.textContent =
        message;

    toast.classList.add("show");

    clearTimeout(
        window.toastTimer
    );

    window.toastTimer =
        setTimeout(() => {{

            toast.classList.remove(
                "show"
            );

        }}, 1800);

}}


/* =========================================================
   COPY QUOTE ONLY
   ========================================================= */

document
.getElementById("copyQuote")
.addEventListener(
    "click",
    () => {{

        if (!currentRecord) return;

        copyText(
            '"' +
            currentRecord.quote +
            '"',
            document.body.classList.contains("hindi")
                ? "उद्धरण कॉपी किया गया"
                : "Quote copied"
        );

    }}
);


/* =========================================================
   COPY QUOTE + AUTHOR
   ========================================================= */

document
.getElementById("copyQuoteWithAuthor")
.addEventListener(
    "click",
    () => {{

        if (!currentRecord) return;

        const output =

`"${{currentRecord.quote}}"

— ${{currentRecord.person.name}}
${{currentRecord.person.role}}`;

        copyText(
            output,
            document.body.classList.contains("hindi")
                ? "उद्धरण और लेखक कॉपी किए गए"
                : "Quote and attribution copied"
        );

    }}
);


/* =========================================================
   QUOTE SCREENSHOT
   ========================================================= */

document
.getElementById("screenshotQuote")
.addEventListener(
    "click",
    screenshotQuote
);


function screenshotQuote() {{

    if (!currentRecord) return;


    const canvas =
        document.createElement("canvas");


    const width = 1600;
    const height = 1000;


    canvas.width = width;
    canvas.height = height;


    const ctx =
        canvas.getContext("2d");


    /*
       Paper background
    */

    ctx.fillStyle =
        "#f4f0e7";

    ctx.fillRect(
        0,
        0,
        width,
        height
    );


    /*
       Border
    */

    ctx.strokeStyle =
        "#777";

    ctx.lineWidth = 2;

    ctx.strokeRect(
        45,
        45,
        width - 90,
        height - 90
    );


    /*
       Archive header
    */

    ctx.fillStyle =
        "#191919";

    ctx.font =
        "22px Arial";

    ctx.fillText(
        "THE HUMAN WISDOM ARCHIVE",
        100,
        110
    );


    ctx.font =
        "13px monospace";

    ctx.fillText(
        currentRecord.id,
        100,
        140
    );


    /*
       Small classification
    */

    ctx.fillStyle =
        "#823328";

    ctx.font =
        "14px monospace";

    ctx.fillText(
        currentRecord.person.category
            .toUpperCase(),
        100,
        205
    );


    /*
       Quote
    */

    ctx.fillStyle =
        "#191919";

    ctx.font =
        "52px Georgia";


    const quote =
        '"' +
        currentRecord.quote +
        '"';


    let y =
        drawWrappedText(
            ctx,
            quote,
            100,
            285,
            1370,
            68
        );


    /*
       Attribution
    */

    y += 55;


    ctx.font =
        "25px Georgia";

    ctx.fillText(
        currentRecord.person.name,
        100,
        y
    );


    y += 30;


    ctx.font =
        "14px monospace";

    ctx.fillStyle =
        "#706b63";

    ctx.fillText(
        currentRecord.person.role,
        100,
        y
    );


    /*
       Bottom archive information
    */

    ctx.fillStyle =
        "#706b63";

    ctx.font =
        "11px monospace";

    ctx.fillText(
        "HUMAN WISDOM ARCHIVE · DIGITAL CATALOGUE",
        100,
        910
    );


    ctx.fillText(
        currentRecord.id,
        width - 250,
        910
    );


    /*
       Download image
    */

    const link =
        document.createElement("a");


    link.download =
        "quote-" +
        currentRecord.id +
        ".png";


    link.href =
        canvas.toDataURL(
            "image/png"
        );


    link.click();


    showToast(
        document.body.classList.contains("hindi")
            ? "स्क्रीनशॉट तैयार है"
            : "Quote screenshot created"
    );

}}


function drawWrappedText(
    ctx,
    value,
    x,
    y,
    maxWidth,
    lineHeight
) {{

    const words =
        value.split(" ");

    let line = "";


    for (
        let i = 0;
        i < words.length;
        i++
    ) {{

        const test =
            line +
            words[i] +
            " ";

        const width =
            ctx.measureText(test).width;


        if (
            width > maxWidth &&
            i > 0
        ) {{

            ctx.fillText(
                line,
                x,
                y
            );

            line =
                words[i] +
                " ";

            y += lineHeight;

        }} else {{

            line =
                test;

        }}

    }}


    ctx.fillText(
        line,
        x,
        y
    );


    return y;

}}


/* =========================================================
   COPY COMPLETE RECORD
   ========================================================= */

document
.getElementById("copyRecord")
.addEventListener(
    "click",
    () => {{

        if (!currentRecord) return;

        const record =

`THE HUMAN WISDOM ARCHIVE

Archive Number:
${{currentRecord.id}}

${{currentRecord.person.name}}
${{currentRecord.person.role}}
${{currentRecord.person.origin}}
${{currentRecord.person.period}}

"${{currentRecord.quote}}"

INTERPRETIVE RECORD

${{currentRecord.interpretation}}

QUESTION RAISED

${{currentRecord.question}}

PRACTICAL APPLICATION

${{currentRecord.application}}
`;

        copyText(
            record,
            document.body.classList.contains("hindi")
                ? "रिकॉर्ड कॉपी किया गया"
                : "Record copied"
        );

    }}
);


/* =========================================================
   PRINT
   ========================================================= */

document
.getElementById("printRecord")
.addEventListener(
    "click",
    () => window.print()
);


/* =========================================================
   NEW RECORD
   ========================================================= */

document
.getElementById("newRecord")
.addEventListener(
    "click",
    () => {{

        render(
            makeRecord()
        );

        window.scrollTo({{
            top: 0,
            behavior: "smooth"
        }});

    }}
);


/* =========================================================
   LANGUAGE
   ========================================================= */

document
.getElementById("language")
.addEventListener(
    "click",
    () => {{

        const hindi =
            document.body.classList.toggle(
                "hindi"
            );


        if (
            hindi &&
            currentRecord
        ) {{

            const translated =
                DATA.hindi[
                    currentRecord.quote
                ];


            if (translated) {{

                text(
                    "quote",
                    translated
                );

            }} else {{

                /*
                   Serious Hindi rendering for
                   quotes without a stored translation.
                */

                text(
                    "quote",
                    currentRecord.quote
                );

            }}

            text(
                "interpretation",
                "यह कथन साधारण वस्तु और मानवीय अनुभव के माध्यम से उद्देश्य, अपेक्षा और परिणाम के बीच संबंध की ओर संकेत करता है।"
            );

            text(
                "question",
                "किस बिंदु पर तैयारी, तैयारी न रहकर टालने का दूसरा नाम बन जाती है?"
            );

            text(
                "application",
                "व्यावहारिक रूप से यह विचार सुझाव देता है कि प्रयास बढ़ाने से पहले दिशा और आधारभूत धारणा की समीक्षा की जाए।"
            );

        }} else if (
            !hindi &&
            currentRecord
        ) {{

            render(
                currentRecord
            );

        }}

    }}
);


/* =========================================================
   KEYBOARD
   ========================================================= */

document.addEventListener(
    "keydown",
    event => {{

        if (
            event.key.toLowerCase() === "n" &&
            !event.ctrlKey &&
            !event.altKey &&
            !event.metaKey
        ) {{

            render(
                makeRecord()
            );

        }}

    }}
);


/* =========================================================
   INITIAL RECORD
   ========================================================= */

render(
    makeRecord()
);

</script>

</body>
</html>
"""


# ============================================================
# GENERATE
# ============================================================

if __name__ == "__main__":

    OUTPUT.write_text(
        build_html(),
        encoding="utf-8"
    )

    print(
        f"Generated: {{OUTPUT.resolve()}}"
    )
