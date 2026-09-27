from pathlib import Path
import json
import random
import html

# ============================================================
# THE HUMAN WISDOM ARCHIVE
# Static-site generator
#
# Run:
#     python generate.py
#
# Output:
#     index.html
#
# No database
# No login
# No signup
# No server-side storage
# Browser memory only
# ============================================================

OUTPUT = Path("index.html")


# ============================================================
# ARCHIVE PEOPLE
# ============================================================

PEOPLE = [
    {
        "name": "Aren Voss",
        "role": "Provincial Cartographer",
        "origin": "Northern Territories",
        "period": "Late 18th Century",
        "subject": "Practical Philosophy",
    },
    {
        "name": "Mira Sen",
        "role": "Keeper of the Eastern Observatory",
        "origin": "Eastern Provinces",
        "period": "Early 20th Century",
        "subject": "Observation",
    },
    {
        "name": "Captain Ilyan Vale",
        "role": "Survey Officer",
        "origin": "Western Maritime District",
        "period": "19th Century",
        "subject": "Endurance",
    },
    {
        "name": "Professor Niko Almostov",
        "role": "Lecturer in Natural Philosophy",
        "origin": "Central Academy",
        "period": "Early 20th Century",
        "subject": "Reason",
    },
    {
        "name": "Elias Thorne",
        "role": "Village Magistrate",
        "origin": "Northwestern Counties",
        "period": "19th Century",
        "subject": "Judgment",
    },
    {
        "name": "Sera Valen",
        "role": "Archivist of Maritime Records",
        "origin": "Southern Coast",
        "period": "Late 19th Century",
        "subject": "Memory",
    },
    {
        "name": "Old Master Ren",
        "role": "Instructor of Rural Mechanics",
        "origin": "Eastern Highlands",
        "period": "Undated",
        "subject": "Work",
    },
    {
        "name": "Dorian Pell",
        "role": "Registrar of Minor Disputes",
        "origin": "Central Administrative District",
        "period": "19th Century",
        "subject": "Human Nature",
    },
    {
        "name": "Ansel Grey",
        "role": "Railway Engineer",
        "origin": "Industrial North",
        "period": "Early 20th Century",
        "subject": "Persistence",
    },
    {
        "name": "Liora Venn",
        "role": "Teacher of Rhetoric",
        "origin": "Old University Quarter",
        "period": "Late 19th Century",
        "subject": "Language",
    },
    {
        "name": "Bastian Or",
        "role": "Keeper of the Municipal Clock",
        "origin": "Old Capital",
        "period": "19th Century",
        "subject": "Time",
    },
    {
        "name": "Nera Sol",
        "role": "Apothecary's Apprentice",
        "origin": "Southern Market District",
        "period": "Early 19th Century",
        "subject": "Experience",
    },
    {
        "name": "Havel Marr",
        "role": "Bridge Inspector",
        "origin": "River Provinces",
        "period": "19th Century",
        "subject": "Risk",
    },
    {
        "name": "Orin Bell",
        "role": "Clerk of Agricultural Affairs",
        "origin": "Western Plains",
        "period": "Early 20th Century",
        "subject": "Growth",
    },
    {
        "name": "Tavian Roe",
        "role": "Instructor of Navigation",
        "origin": "Northern Port",
        "period": "18th Century",
        "subject": "Direction",
    },
]


# ============================================================
# LARGE OBJECT VOCABULARY
# ============================================================

OBJECTS = [
    "umbrella",
    "wooden chair",
    "compass",
    "ladder",
    "rusted key",
    "tea kettle",
    "bicycle",
    "bucket",
    "clock",
    "map",
    "suitcase",
    "lantern",
    "wooden spoon",
    "bridge",
    "broken ruler",
    "coat",
    "window",
    "door",
    "stone",
    "rope",
    "bell",
    "wheelbarrow",
    "candle",
    "wooden box",
    "train ticket",
    "empty bottle",
    "fountain pen",
    "fishing net",
    "boots",
    "folding table",
    "old notebook",
    "metal cup",
    "garden gate",
    "broom",
    "brick",
    "raincoat",
    "wooden crate",
    "calendar",
    "thermos",
    "spare button",
    "sack of flour",
    "rubber stamp",
    "hand mirror",
    "bucket of nails",
    "pocket watch",
    "rope ladder",
    "wooden sign",
    "market scale",
    "paper envelope",
    "iron hook",
    "travel bag",
    "small hammer",
    "large hammer",
    "newspaper",
    "shoelace",
    "wooden ruler",
    "fence post",
    "rain barrel",
    "wheel",
    "spade",
    "garden hose",
    "ink bottle",
    "messenger bag",
    "wooden bench",
    "tea cup",
    "screwdriver",
    "paint brush",
    "walking stick",
    "metal bucket",
    "folded map",
    "rope coil",
    "old photograph",
    "biscuit tin",
    "brass key",
    "stone tablet",
    "paperweight",
    "wooden cart",
    "street sign",
    "train whistle",
    "garden shovel",
    "fishing rod",
    "oil lamp",
    "book",
    "empty notebook",
    "wooden ruler",
    "hand bell",
    "metal spoon",
    "coat hanger",
    "travel trunk",
    "broken chair",
    "small mirror",
    "wooden bowl",
    "ink pen",
    "field notebook",
]


# ============================================================
# PLACES
# ============================================================

PLACES = [
    "the eastern market",
    "the railway platform",
    "the municipal square",
    "the old observatory",
    "the village bridge",
    "the northern road",
    "the public library",
    "the agricultural office",
    "the harbor",
    "the courthouse corridor",
    "the mountain path",
    "the town workshop",
    "the abandoned station",
    "the central archive",
    "the riverside warehouse",
    "the school courtyard",
    "the old clock tower",
    "the southern gate",
    "the grain market",
    "the provincial road",
    "the town hall",
    "the railway office",
    "the village inn",
    "the public garden",
    "the customs house",
    "the old university",
    "the harbor office",
    "the municipal workshop",
    "the mountain village",
]


# ============================================================
# ACTIONS
# ============================================================

ACTIONS = [
    "carried",
    "measured",
    "examined",
    "ignored",
    "repaired",
    "lost",
    "found",
    "borrowed",
    "returned",
    "dragged",
    "followed",
    "questioned",
    "protected",
    "misplaced",
    "polished",
    "opened",
    "closed",
    "studied",
    "forgot",
    "recorded",
]


# ============================================================
# CONSEQUENCES
# ============================================================

CONSEQUENCES = [
    "and discovered that the problem had been waiting patiently",
    "and learned that the object had no intention of helping",
    "and discovered that nobody had agreed on what the object was for",
    "and found that the simplest explanation had been standing nearby",
    "and realized that the plan had survived only because nobody used it",
    "and discovered that everyone had been solving a different problem",
    "and learned that patience works better when it has somewhere to sit",
    "and found that the obstacle was mostly a disagreement with reality",
    "and discovered that the shortest explanation required the longest meeting",
    "and learned that a sensible decision can look absurd before lunch",
    "and discovered that the answer had been correct but inconvenient",
    "and realized that certainty had arrived without evidence",
    "and found that the mistake had already become part of the procedure",
    "and learned that nobody notices a successful plan until it fails",
    "and discovered that the road had not changed, only the confidence of the traveler",
]


# ============================================================
# LOGICAL ABSURDITY TEMPLATES
# ============================================================

TEMPLATES = [
    "A {object} becomes dangerous when everyone agrees it is harmless.",
    "The {object} was useless until someone gave it a deadline.",
    "I {action} the {object} for three hours {consequence}.",
    "A person who fears the {object} has already granted it authority.",
    "The {object} never promised to cooperate, which made it the most reliable member of the committee.",
    "The smallest {object} in the room received the largest responsibility.",
    "Nobody questioned the {object} until it became useful.",
    "The {object} looked ordinary, which was precisely why everyone underestimated it.",
    "A locked {object} is usually less troublesome than an unlocked opinion.",
    "The {object} remained where I left it, proving that at least one thing in life respects instructions.",
    "A perfect plan is merely a complicated way of becoming surprised by the {object}.",
    "The {object} did not create the confusion. It merely gave the confusion somewhere to sit.",
    "If the {object} cannot solve the problem, move the problem closer to the {object}.",
    "The {object} became important only after everyone had agreed that it was unnecessary.",
    "A wise person checks the {object} twice and then checks whether checking it twice was wise.",
    "The {object} was heavier than expected, but expectations are notoriously bad at lifting things.",
    "I asked the {object} for direction. It provided no answer, which was at least honest.",
    "The {object} had one job and completed it badly enough to become memorable.",
    "A committee can discuss a {object} for six hours without discovering what it is.",
    "The {object} survived because nobody had written a procedure explaining how to break it.",
    "A person who counts every step eventually discovers that walking was never a spreadsheet.",
    "The road was not difficult. The expectations were carrying too much luggage.",
    "A question becomes heavier when everyone agrees not to ask it.",
    "The door was ordinary until someone needed it to be extraordinary.",
    "A broken compass can still teach you that you are lost.",
    "The bell rang because someone pulled it. History later called this inevitability.",
    "The ladder did not become shorter because I complained about the height.",
    "A clock that is wrong twice a day is still employed by time.",
    "The bridge looked stronger after everyone stopped asking whether it was strong.",
    "The shortest road looked suspicious because nobody had taken it seriously.",
    "I sharpened the pencil until there was nothing left with which to write.",
    "The empty chair taught me more about absence than the crowded room.",
    "I asked the mirror for advice. It returned the same face and charged no fee.",
    "I lost the key and discovered that the door had never been locked.",
    "The old road remained useful after the destination changed.",
    "A perfect plan has never survived its first meeting with weather.",
    "The clock was late, but the meeting was later.",
    "The smallest key opened the largest door because the door had no opinion about size.",
    "The mountain did not become smaller. I simply stopped negotiating with it.",
    "A heavy stone teaches patience because it refuses to be impressed.",
    "The road became shorter when I stopped arguing with the map.",
    "A chair cannot solve an argument, but it can make everyone sit down long enough to regret having one.",
    "The umbrella was unnecessary until the rain arrived, at which point it became everyone's responsibility.",
    "A map is most confident when nobody has checked the road.",
    "The key was perfectly shaped for the lock and completely wrong for the door.",
    "A person can carry a bucket all day and still forget why it was empty.",
    "The meeting ended when someone asked what the meeting was supposed to accomplish.",
    "A fence exists partly because someone once believed walking around it was too complicated.",
    "The strongest rope is still useless if nobody agrees which end to pull.",
    "A broken chair is an honest chair. It makes no promise about sitting.",
    "The safest road was avoided because it looked too simple.",
    "A full notebook can still contain no useful answer.",
    "The answer was obvious after the question had become unnecessary.",
    "A locked drawer creates more curiosity than an empty one.",
    "The tool worked perfectly once everyone stopped improving it.",
    "A missing button can delay a journey more effectively than a broken wheel.",
    "The box was empty, but three people argued about what had been inside it.",
    "A straight line is easy to draw and surprisingly difficult to walk.",
    "The sign pointed correctly, which did not prevent everyone from walking the other way.",
    "A small mistake becomes official when someone writes it down.",
    "The river did not change direction because the bridge requested it.",
    "A schedule is a promise made to a future that has not agreed to cooperate.",
    "The key opened the cabinet, but nobody knew why the cabinet was locked.",
    "A tool becomes complicated when its instructions become longer than its purpose.",
    "The empty road was not lonely. It simply had fewer witnesses.",
    "A person who waits for perfect weather eventually becomes an expert at waiting.",
    "The basket was full of useful things and one completely unnecessary lemon.",
    "The old clock stopped, but nobody could convince the meeting to do the same.",
]


# ============================================================
# INTERPRETATION BUILDING
# ============================================================

INTERPRETATIONS = [
    "The observation concerns the difference between usefulness and appearance. Something may look ordinary while quietly exposing a weakness in the surrounding system.",
    "The record suggests that uncertainty is not always an obstacle. Sometimes uncertainty is the first honest description of a situation.",
    "The observation concerns expectations. A large portion of difficulty is created before the difficult thing is even encountered.",
    "The record suggests that procedures can become more important than the problem they were originally designed to solve.",
    "The observation concerns judgment. A reasonable conclusion can still be inconvenient, unpopular, or strangely timed.",
    "The record suggests that simplicity is often mistaken for insignificance until circumstances make its value obvious.",
    "The observation concerns human confidence. People frequently become certain before they become informed.",
    "The record examines persistence without glorifying unnecessary effort. Continuing is useful only when the direction remains worth pursuing.",
    "The observation concerns memory. Once an event becomes part of a record, the explanation surrounding it can become more durable than the event itself.",
    "The record suggests that practical wisdom often appears less impressive than theoretical certainty because practical wisdom must survive contact with reality.",
    "The observation concerns responsibility. Giving something a formal role does not guarantee that it understands the assignment.",
    "The record examines the strange human tendency to complicate a problem after discovering that the simple answer was inconvenient.",
]


# ============================================================
# QUESTIONS
# ============================================================

QUESTIONS = [
    "At what point does preparation become another form of delay?",
    "How much confidence should be placed in an explanation that has never been tested?",
    "Why do people often distrust simple solutions?",
    "When does persistence become unnecessary stubbornness?",
    "Can a mistake become useful without becoming correct?",
    "Why do procedures survive after their original purpose disappears?",
    "How much of difficulty comes from the task, and how much from expectation?",
    "Can uncertainty be more honest than confidence?",
    "Why does a missing object attract more attention than an ordinary one?",
    "When does organization become a substitute for understanding?",
    "How often does a person solve the wrong problem efficiently?",
    "Can an inconvenient truth still be a practical one?",
]


# ============================================================
# APPLICATIONS
# ============================================================

APPLICATIONS = [
    "Before solving a complicated problem, identify what is actually being asked.",
    "Test the simplest explanation before constructing a more elaborate one.",
    "Separate the difficulty of a task from the expectations surrounding it.",
    "When a procedure stops serving its purpose, reconsider the procedure.",
    "Do not confuse confidence with evidence.",
    "When several people disagree, first determine whether they are solving the same problem.",
    "A useful plan should be allowed to change when circumstances change.",
    "Record important decisions, but do not mistake the record for reality itself.",
    "Practical judgment requires both evidence and awareness of limitations.",
    "When something appears unnecessarily complicated, examine the assumptions supporting it.",
    "Use persistence deliberately rather than automatically.",
    "Before adding another solution, verify that the original problem still exists.",
]


# ============================================================
# HINDI TRANSLATIONS
# ============================================================

HINDI_QUOTES = {
    "A locked {object} is usually less troublesome than an unlocked opinion.":
        "एक बंद {object} अक्सर खुली हुई राय से कम परेशानी देता है।",

    "A broken compass can still teach you that you are lost.":
        "टूटा हुआ कम्पास भी यह सिखा सकता है कि आप रास्ता भटक चुके हैं।",

    "The ladder did not become shorter because I complained about the height.":
        "मेरी शिकायत करने से सीढ़ी छोटी नहीं हुई।",

    "A clock that is wrong twice a day is still employed by time.":
        "जो घड़ी दिन में दो बार गलत होती है, वह फिर भी समय के अधीन काम कर रही होती है।",

    "The bridge looked stronger after everyone stopped asking whether it was strong.":
        "जब सबने यह पूछना बंद कर दिया कि पुल मजबूत है या नहीं, तब वह अधिक मजबूत दिखाई देने लगा।",

    "The empty chair taught me more about absence than the crowded room.":
        "खाली कुर्सी ने मुझे अनुपस्थिति के बारे में भरे हुए कमरे से अधिक सिखाया।",

    "I asked the mirror for advice. It returned the same face and charged no fee.":
        "मैंने आईने से सलाह मांगी। उसने वही चेहरा लौटाया और कोई शुल्क नहीं लिया।",

    "I lost the key and discovered that the door had never been locked.":
        "मैंने चाबी खो दी और पाया कि दरवाज़ा कभी बंद था ही नहीं।",

    "The old road remained useful after the destination changed.":
        "मंज़िल बदल जाने के बाद भी पुरानी सड़क उपयोगी बनी रही।",

    "A perfect plan has never survived its first meeting with weather.":
        "कोई भी पूर्ण योजना मौसम से अपनी पहली मुलाकात के बाद वैसी नहीं रहती।",

    "The clock was late, but the meeting was later.":
        "घड़ी देर से थी, लेकिन बैठक उससे भी देर से थी।",

    "The smallest key opened the largest door because the door had no opinion about size.":
        "सबसे छोटी चाबी ने सबसे बड़ा दरवाज़ा खोला, क्योंकि दरवाज़े की आकार को लेकर कोई राय नहीं थी।",

    "The mountain did not become smaller. I simply stopped negotiating with it.":
        "पहाड़ छोटा नहीं हुआ। मैंने बस उससे समझौता करना बंद कर दिया।",

    "A heavy stone teaches patience because it refuses to be impressed.":
        "भारी पत्थर धैर्य सिखाता है क्योंकि वह प्रभावित होने से इनकार करता है।",

    "The road became shorter when I stopped arguing with the map.":
        "जब मैंने नक्शे से बहस करना बंद किया, तो रास्ता छोटा लगने लगा।",

    "A perfect plan has never survived its first meeting with weather.":
        "कोई भी पूर्ण योजना मौसम से अपनी पहली मुलाकात के बाद वैसी नहीं रहती।",
}


# ============================================================
# HTML ESCAPE
# ============================================================

def esc(value):
    return html.escape(str(value), quote=True)


# ============================================================
# GENERATE A RECORD
# ============================================================

def make_record():
    person = random.choice(PEOPLE)

    template = random.choice(TEMPLATES)

    object_name = random.choice(OBJECTS)
    place = random.choice(PLACES)
    action = random.choice(ACTIONS)
    consequence = random.choice(CONSEQUENCES)

    quote = (
        template
        .replace("{object}", object_name)
        .replace("{place}", place)
        .replace("{action}", action)
        .replace("{consequence}", consequence)
    )

    # Some templates do not use all variables.
    # This deliberately allows unusual combinations.

    interpretation = random.choice(INTERPRETATIONS)
    question = random.choice(QUESTIONS)
    application = random.choice(APPLICATIONS)

    record_key = (
        person["name"]
        + "|"
        + person["role"]
        + "|"
        + quote
        + "|"
        + interpretation
        + "|"
        + question
    )

    return {
        "person": person,
        "quote": quote,
        "interpretation": interpretation,
        "question": question,
        "application": application,
        "record_key": record_key,
    }


# ============================================================
# INITIAL SERVER-SIDE RECORD
# ============================================================

initial_records = []

for _ in range(20):
    initial_records.append(make_record())


# ============================================================
# CSS
# ============================================================

CSS = r"""
:root {
    --bg: #ece8df;
    --paper: #f8f5ed;
    --paper-2: #f1ede3;
    --ink: #20201d;
    --muted: #6c6a63;
    --line: #b9b3a7;
    --line-dark: #777268;
    --accent: #353a3d;
    --accent-2: #5d5041;
    --shadow: rgba(25, 24, 20, .10);
}

* {
    box-sizing: border-box;
}

html {
    width: 100%;
    min-width: 0;
    scroll-behavior: smooth;
}

body {
    margin: 0;
    min-width: 0;
    background:
        linear-gradient(rgba(255,255,255,.16), rgba(255,255,255,.16)),
        repeating-linear-gradient(
            0deg,
            rgba(60,55,45,.018) 0,
            rgba(60,55,45,.018) 1px,
            transparent 1px,
            transparent 4px
        ),
        var(--bg);
    color: var(--ink);
    font-family: Georgia, "Times New Roman", serif;
    line-height: 1.6;
}

button {
    font: inherit;
}

.page {
    width: min(1500px, calc(100% - 32px));
    margin: 0 auto;
    padding: 26px 0 50px;
}

.archive-header {
    border-top: 5px solid var(--ink);
    border-bottom: 1px solid var(--line-dark);
    padding: 24px 0 20px;
    margin-bottom: 14px;
}

.header-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 25px;
    align-items: end;
}

.kicker {
    margin: 0 0 7px;
    color: var(--muted);
    font-size: 12px;
    letter-spacing: .18em;
    text-transform: uppercase;
}

h1 {
    margin: 0;
    font-size: clamp(28px, 4vw, 55px);
    line-height: 1.02;
    font-weight: 700;
    letter-spacing: -.035em;
}

.subtitle {
    max-width: 920px;
    margin: 13px 0 0;
    color: #55534d;
    font-size: 15px;
}

.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    justify-content: flex-end;
}

.control {
    border: 1px solid var(--line-dark);
    background: rgba(255,255,255,.35);
    color: var(--ink);
    padding: 9px 12px;
    cursor: pointer;
    font-size: 12px;
    letter-spacing: .04em;
    transition: .15s ease;
}

.control:hover {
    background: var(--ink);
    color: white;
}

.catalog {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    border-bottom: 1px solid var(--line-dark);
    margin-bottom: 22px;
}

.catalog-cell {
    padding: 12px 15px;
    border-right: 1px solid var(--line);
}

.catalog-cell:last-child {
    border-right: 0;
}

.catalog-label {
    display: block;
    color: var(--muted);
    font-size: 10px;
    letter-spacing: .14em;
    text-transform: uppercase;
}

.catalog-value {
    display: block;
    margin-top: 2px;
    font-size: 13px;
    font-weight: 700;
}

.main-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 330px;
    gap: 22px;
    align-items: start;
}

.paper {
    min-width: 0;
    background: var(--paper);
    border: 1px solid #aaa398;
    box-shadow: 0 12px 30px var(--shadow);
}

.record-main {
    padding: clamp(22px, 4vw, 50px);
}

.record-number {
    color: var(--muted);
    font-size: 11px;
    letter-spacing: .17em;
    text-transform: uppercase;
    margin-bottom: 25px;
}

.quote-box {
    border-left: 5px solid var(--ink);
    padding: 4px 0 5px 27px;
    margin-bottom: 32px;
}

.quote {
    margin: 0;
    font-size: clamp(25px, 3.2vw, 47px);
    line-height: 1.17;
    letter-spacing: -.025em;
}

.attribution {
    margin-top: 25px;
    font-size: 15px;
}

.author {
    font-weight: 700;
}

.role {
    color: var(--muted);
}

.meta-line {
    margin-top: 4px;
    color: var(--muted);
    font-size: 12px;
}

.quote-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 0 0 34px;
}

.quote-action {
    border: 1px solid var(--line-dark);
    background: var(--paper-2);
    padding: 9px 13px;
    cursor: pointer;
    font-size: 12px;
}

.quote-action:hover {
    background: var(--ink);
    color: white;
}

.section-rule {
    height: 1px;
    background: var(--line);
    margin: 27px 0;
}

.section-title {
    margin: 0 0 12px;
    font-size: 12px;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: var(--muted);
}

.interpretation {
    font-size: 17px;
    max-width: 900px;
}

.analysis-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 20px;
}

.analysis-card {
    border: 1px solid var(--line);
    padding: 17px;
    background: rgba(255,255,255,.24);
}

.analysis-card h3 {
    margin: 0 0 9px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .12em;
    color: var(--muted);
}

.analysis-card p {
    margin: 0;
    font-size: 14px;
}

.sidebar {
    display: grid;
    gap: 14px;
}

.side-card {
    background: var(--paper);
    border: 1px solid #aaa398;
    padding: 20px;
}

.side-label {
    color: var(--muted);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: .14em;
    margin-bottom: 9px;
}

.side-name {
    margin: 0;
    font-size: 22px;
}

.side-role {
    margin: 3px 0 16px;
    color: var(--muted);
    font-size: 13px;
}

.fact-list {
    margin: 0;
    padding: 0;
    list-style: none;
}

.fact-list li {
    border-top: 1px solid var(--line);
    padding: 8px 0;
    font-size: 13px;
}

.fact-list li:last-child {
    border-bottom: 1px solid var(--line);
}

.application {
    font-size: 14px;
}

.catalog-note {
    color: #5e5b54;
    font-size: 13px;
}

.archive-footer {
    border-top: 1px solid var(--line-dark);
    margin-top: 22px;
    padding-top: 14px;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    color: var(--muted);
    font-size: 11px;
}

.toast {
    position: fixed;
    left: 50%;
    bottom: 25px;
    transform: translateX(-50%) translateY(20px);
    background: #24231f;
    color: white;
    padding: 10px 15px;
    font-size: 12px;
    opacity: 0;
    pointer-events: none;
    transition: .2s ease;
    z-index: 9999;
}

.toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}

@media (max-width: 950px) {
    .main-grid {
        grid-template-columns: 1fr;
    }

    .sidebar {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .catalog {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .catalog-cell:nth-child(2) {
        border-right: 0;
    }

    .catalog-cell:nth-child(-n+2) {
        border-bottom: 1px solid var(--line);
    }

    .analysis-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 620px) {
    .page {
        width: min(100% - 18px, 1500px);
        padding-top: 10px;
    }

    .header-grid {
        grid-template-columns: 1fr;
    }

    .controls {
        justify-content: flex-start;
    }

    .catalog {
        grid-template-columns: 1fr 1fr;
    }

    .record-main {
        padding: 22px 17px;
    }

    .quote-box {
        padding-left: 17px;
    }

    .quote {
        font-size: 28px;
    }

    .sidebar {
        grid-template-columns: 1fr;
    }

    .archive-footer {
        flex-direction: column;
    }
}

@media (max-width: 390px) {
    .catalog {
        grid-template-columns: 1fr;
    }

    .catalog-cell,
    .catalog-cell:nth-child(2) {
        border-right: 0;
        border-bottom: 1px solid var(--line);
    }

    .catalog-cell:last-child {
        border-bottom: 0;
    }

    .quote-actions,
    .controls {
        flex-direction: column;
    }

    .quote-action,
    .control {
        width: 100%;
    }
}

@media print {
    @page {
        size: A4;
        margin: 12mm;
    }

    body {
        background: white;
    }

    .page {
        width: 100%;
        padding: 0;
    }

    .controls,
    .quote-actions,
    .toast {
        display: none !important;
    }

    .archive-header {
        margin-bottom: 10px;
    }

    .paper,
    .side-card {
        box-shadow: none;
    }

    .main-grid {
        grid-template-columns: 1fr;
    }

    .sidebar {
        grid-template-columns: repeat(3, 1fr);
    }

    .paper {
        border: 0;
    }

    .record-main {
        padding: 15px 0;
    }
}
"""


# ============================================================
# JAVASCRIPT
# ============================================================

JS = r"""
const INITIAL_RECORDS = __INITIAL_RECORDS__;

const PEOPLE = __PEOPLE__;
const TEMPLATES = __TEMPLATES__;
const OBJECTS = __OBJECTS__;
const PLACES = __PLACES__;
const ACTIONS = __ACTIONS__;
const CONSEQUENCES = __CONSEQUENCES__;
const INTERPRETATIONS = __INTERPRETATIONS__;
const QUESTIONS = __QUESTIONS__;
const APPLICATIONS = __APPLICATIONS__;
const HINDI_QUOTES = __HINDI_QUOTES__;

const MEMORY_KEY = "human_wisdom_archive_seen_v3";

let currentRecord = null;
let language = "en";


// ============================================================
// SAFE RANDOM
// ============================================================

function randomItem(array) {
    return array[Math.floor(Math.random() * array.length)];
}


// ============================================================
// BROWSER MEMORY
// ============================================================

function getSeen() {
    try {
        const raw = localStorage.getItem(MEMORY_KEY);

        if (!raw) {
            return [];
        }

        const parsed = JSON.parse(raw);

        if (!Array.isArray(parsed)) {
            return [];
        }

        return parsed;
    } catch (error) {
        return [];
    }
}


function saveSeen(seen) {
    try {
        localStorage.setItem(MEMORY_KEY, JSON.stringify(seen));
    } catch (error) {
        // Browser storage may be unavailable.
        // The site continues functioning without it.
    }
}


function rememberRecord(key) {
    const seen = getSeen();

    if (!seen.includes(key)) {
        seen.push(key);
    }

    saveSeen(seen);
}


// ============================================================
// RECORD CREATION
// ============================================================

function makeRecord() {
    const person = randomItem(PEOPLE);
    const template = randomItem(TEMPLATES);

    const objectName = randomItem(OBJECTS);
    const place = randomItem(PLACES);
    const action = randomItem(ACTIONS);
    const consequence = randomItem(CONSEQUENCES);

    let quote = template
        .replaceAll("{object}", objectName)
        .replaceAll("{place}", place)
        .replaceAll("{action}", action)
        .replaceAll("{consequence}", consequence);

    const interpretation = randomItem(INTERPRETATIONS);
    const question = randomItem(QUESTIONS);
    const application = randomItem(APPLICATIONS);

    const recordKey =
        person.name +
        "|" +
        person.role +
        "|" +
        quote +
        "|" +
        interpretation +
        "|" +
        question;

    return {
        person,
        quote,
        interpretation,
        question,
        application,
        record_key: recordKey
    };
}


// ============================================================
// FIND UNSEEN RECORD
// ============================================================

function getNewRecord() {
    const seen = new Set(getSeen());

    /*
     * We try many combinations before falling back to the
     * browser's initial generated records.
     *
     * Because the quote system combines:
     * people + templates + objects + actions + consequences
     * + interpretations + questions + applications,
     * the practical pool is extremely large.
     */

    for (let attempt = 0; attempt < 1000; attempt++) {
        const record = makeRecord();

        if (!seen.has(record.record_key)) {
            return record;
        }
    }

    /*
     * Extremely unlikely unless the browser has already seen
     * a very large number of records.
     *
     * Search the server-generated records too.
     */

    const shuffled = [...INITIAL_RECORDS]
        .sort(() => Math.random() - 0.5);

    for (const record of shuffled) {
        if (!seen.has(record.record_key)) {
            return record;
        }
    }

    /*
     * Entire combinatorial pool exhausted.
     *
     * Reset only this site's browser history.
     * No server data is affected.
     */

    saveSeen([]);

    return makeRecord();
}


// ============================================================
// RECORD ID
// ============================================================

function makeArchiveNumber() {
    const number = Math.floor(100000 + Math.random() * 899999);

    return "HWA-" + number;
}


// ============================================================
// HTML HELPERS
// ============================================================

function setText(id, value) {
    const element = document.getElementById(id);

    if (element) {
        element.textContent = value;
    }
}


function getHindiQuote(quote) {
    if (HINDI_QUOTES[quote]) {
        return HINDI_QUOTES[quote];
    }

    return quote;
}


// ============================================================
// RENDER
// ============================================================

function render(record) {
    currentRecord = record;

    rememberRecord(record.record_key);

    const archiveNumber = makeArchiveNumber();

    const quoteText =
        language === "hi"
            ? getHindiQuote(record.quote)
            : record.quote;

    setText("archive-number", archiveNumber);
    setText("quote", "“" + quoteText + "”");

    setText("author", record.person.name);
    setText("role", record.person.role);

    setText(
        "origin-period",
        record.person.origin + " · " + record.person.period
    );

    setText("classification", record.person.subject);

    setText(
        "interpretation",
        language === "hi"
            ? translateInterpretation(record.interpretation)
            : record.interpretation
    );

    setText(
        "question",
        language === "hi"
            ? translateQuestion(record.question)
            : record.question
    );

    setText(
        "application",
        language === "hi"
            ? translateApplication(record.application)
            : record.application
    );

    setText("side-name", record.person.name);
    setText("side-role", record.person.role);
    setText("side-origin", record.person.origin);
    setText("side-period", record.person.period);
    setText("side-subject", record.person.subject);

    updateLanguageLabels();
}


// ============================================================
// HINDI SUPPORT
// ============================================================

function translateInterpretation(text) {
    const translations = {
        "The observation concerns the difference between usefulness and appearance. Something may look ordinary while quietly exposing a weakness in the surrounding system.":
            "यह अवलोकन उपयोगिता और बाहरी रूप के अंतर से संबंधित है। कोई चीज़ साधारण दिखाई दे सकती है, फिर भी आसपास की व्यवस्था की कमजोरी को स्पष्ट कर सकती है।",

        "The record suggests that uncertainty is not always an obstacle. Sometimes uncertainty is the first honest description of a situation.":
            "यह अभिलेख बताता है कि अनिश्चितता हमेशा बाधा नहीं होती। कभी-कभी अनिश्चितता किसी स्थिति का पहला ईमानदार वर्णन होती है।",

        "The observation concerns expectations. A large portion of difficulty is created before the difficult thing is even encountered.":
            "यह अवलोकन अपेक्षाओं से संबंधित है। कठिनाई का बड़ा हिस्सा कठिन वस्तु या परिस्थिति के सामने आने से पहले ही पैदा हो जाता है।",

        "The record suggests that procedures can become more important than the problem they were originally designed to solve.":
            "यह अभिलेख बताता है कि कभी-कभी प्रक्रिया उस समस्या से अधिक महत्वपूर्ण हो जाती है जिसके समाधान के लिए उसे बनाया गया था।"
    };

    return translations[text] || text;
}


function translateQuestion(text) {
    const translations = {
        "At what point does preparation become another form of delay?":
            "किस बिंदु पर तैयारी स्वयं देरी का एक रूप बन जाती है?",

        "How much confidence should be placed in an explanation that has never been tested?":
            "ऐसी व्याख्या पर कितना विश्वास किया जाना चाहिए जिसे कभी परखा ही नहीं गया?",

        "Why do people often distrust simple solutions?":
            "लोग अक्सर सरल समाधानों पर अविश्वास क्यों करते हैं?",

        "When does persistence become unnecessary stubbornness?":
            "कब दृढ़ता अनावश्यक जिद बन जाती है?",

        "Can a mistake become useful without becoming correct?":
            "क्या कोई गलती सही हुए बिना भी उपयोगी बन सकती है?",

        "Why do procedures survive after their original purpose disappears?":
            "अपने मूल उद्देश्य के समाप्त हो जाने के बाद भी प्रक्रियाएँ क्यों बनी रहती हैं?"
    };

    return translations[text] || text;
}


function translateApplication(text) {
    const translations = {
        "Before solving a complicated problem, identify what is actually being asked.":
            "किसी जटिल समस्या को हल करने से पहले यह पहचानें कि वास्तव में पूछा क्या जा रहा है।",

        "Test the simplest explanation before constructing a more elaborate one.":
            "अधिक जटिल व्याख्या बनाने से पहले सबसे सरल व्याख्या को परखें।",

        "Separate the difficulty of a task from the expectations surrounding it.":
            "किसी कार्य की वास्तविक कठिनाई और उससे जुड़ी अपेक्षाओं को अलग-अलग देखें।",

        "Do not confuse confidence with evidence.":
            "आत्मविश्वास को प्रमाण न समझें।",

        "When several people disagree, first determine whether they are solving the same problem.":
            "जब कई लोग असहमत हों, तो पहले यह देखें कि वे वास्तव में एक ही समस्या हल कर रहे हैं या नहीं।"
    };

    return translations[text] || text;
}


// ============================================================
// LANGUAGE LABELS
// ============================================================

function updateLanguageLabels() {
    const hi = language === "hi";

    setText(
        "language-button",
        hi ? "English" : "हिन्दी"
    );

    setText(
        "interpretation-label",
        hi ? "व्याख्यात्मक अभिलेख" : "Interpretive Record"
    );

    setText(
        "question-label",
        hi ? "उठाया गया प्रश्न" : "Question Raised"
    );

    setText(
        "application-label",
        hi ? "व्यावहारिक उपयोग" : "Practical Application"
    );

    setText(
        "copy-record-button",
        hi ? "अभिलेख कॉपी करें" : "Copy Record"
    );

    setText(
        "print-button",
        hi ? "प्रिंट" : "Print"
    );

    setText(
        "new-button",
        hi ? "नया अभिलेख" : "New Record"
    );

    setText(
        "copy-quote-button",
        hi ? "उद्धरण कॉपी करें" : "Copy Quote"
    );

    setText(
        "screenshot-button",
        hi ? "उद्धरण स्क्रीनशॉट" : "Screenshot Quote"
    );

    setText(
        "copy-author-button",
        hi ? "उद्धरण + लेखक" : "Copy Quote + Author"
    );
}


// ============================================================
// NEW RECORD
// ============================================================

function newRecord() {
    const record = getNewRecord();

    render(record);
}


// ============================================================
// COPY QUOTE
// ============================================================

async function copyQuote() {
    if (!currentRecord) {
        return;
    }

    const quote =
        language === "hi"
            ? getHindiQuote(currentRecord.quote)
            : currentRecord.quote;

    try {
        await navigator.clipboard.writeText(
            "“" + quote + "”"
        );

        showToast(
            language === "hi"
                ? "उद्धरण कॉपी हो गया।"
                : "Quote copied."
        );
    } catch (error) {
        fallbackCopy(
            "“" + quote + "”"
        );
    }
}


// ============================================================
// COPY QUOTE + AUTHOR
// ============================================================

async function copyQuoteWithAuthor() {
    if (!currentRecord) {
        return;
    }

    const quote =
        language === "hi"
            ? getHindiQuote(currentRecord.quote)
            : currentRecord.quote;

    const text =
        "“" + quote + "”\n\n" +
        "— " + currentRecord.person.name + "\n" +
        currentRecord.person.role + "\n" +
        currentRecord.person.origin + " · " +
        currentRecord.person.period;

    try {
        await navigator.clipboard.writeText(text);

        showToast(
            language === "hi"
                ? "उद्धरण और लेखक की जानकारी कॉपी हो गई।"
                : "Quote and attribution copied."
        );
    } catch (error) {
        fallbackCopy(text);
    }
}


// ============================================================
// COPY FULL RECORD
// ============================================================

async function copyRecord() {
    if (!currentRecord) {
        return;
    }

    const quote =
        language === "hi"
            ? getHindiQuote(currentRecord.quote)
            : currentRecord.quote;

    const interpretation =
        language === "hi"
            ? translateInterpretation(currentRecord.interpretation)
            : currentRecord.interpretation;

    const question =
        language === "hi"
            ? translateQuestion(currentRecord.question)
            : currentRecord.question;

    const application =
        language === "hi"
            ? translateApplication(currentRecord.application)
            : currentRecord.application;

    const text =
        "THE HUMAN WISDOM ARCHIVE\n\n" +
        "“" + quote + "”\n\n" +
        "— " + currentRecord.person.name + "\n" +
        currentRecord.person.role + "\n" +
        currentRecord.person.origin + " · " +
        currentRecord.person.period + "\n\n" +
        "INTERPRETIVE RECORD\n" +
        interpretation + "\n\n" +
        "QUESTION RAISED\n" +
        question + "\n\n" +
        "PRACTICAL APPLICATION\n" +
        application;

    try {
        await navigator.clipboard.writeText(text);

        showToast(
            language === "hi"
                ? "पूरा अभिलेख कॉपी हो गया।"
                : "Full record copied."
        );
    } catch (error) {
        fallbackCopy(text);
    }
}


function fallbackCopy(text) {
    const area = document.createElement("textarea");

    area.value = text;
    area.style.position = "fixed";
    area.style.left = "-9999px";

    document.body.appendChild(area);

    area.select();

    try {
        document.execCommand("copy");

        showToast(
            language === "hi"
                ? "कॉपी हो गया।"
                : "Copied."
        );
    } catch (error) {
        showToast(
            language === "hi"
                ? "कॉपी नहीं हो सका।"
                : "Copy failed."
        );
    }

    document.body.removeChild(area);
}


// ============================================================
// SCREENSHOT QUOTE
// ============================================================

function screenshotQuote() {
    if (!currentRecord) {
        return;
    }

    const canvas = document.createElement("canvas");

    canvas.width = 1800;
    canvas.height = 1100;

    const ctx = canvas.getContext("2d");

    if (!ctx) {
        return;
    }

    /*
     * Paper background
     */
    ctx.fillStyle = "#f8f5ed";
    ctx.fillRect(
        0,
        0,
        canvas.width,
        canvas.height
    );

    /*
     * Border
     */
    ctx.strokeStyle = "#8f897e";
    ctx.lineWidth = 3;

    ctx.strokeRect(
        40,
        40,
        canvas.width - 80,
        canvas.height - 80
    );

    /*
     * Header
     */
    ctx.fillStyle = "#20201d";
    ctx.font = "700 52px Georgia";

    ctx.fillText(
        "THE HUMAN WISDOM ARCHIVE",
        100,
        125
    );

    ctx.fillStyle = "#6c6a63";
    ctx.font = "20px Georgia";

    ctx.fillText(
        "CATALOGUED OBSERVATION",
        100,
        165
    );

    /*
     * Divider
     */
    ctx.fillStyle = "#777268";

    ctx.fillRect(
        100,
        195,
        canvas.width - 200,
        2
    );

    /*
     * Archive number
     */
    ctx.fillStyle = "#6c6a63";
    ctx.font = "18px Georgia";

    ctx.fillText(
        document.getElementById("archive-number").textContent,
        100,
        245
    );

    /*
     * Quote
     */
    const quote =
        language === "hi"
            ? getHindiQuote(currentRecord.quote)
            : currentRecord.quote;

    ctx.fillStyle = "#20201d";
    ctx.font = "italic 44px Georgia";

    wrapCanvasText(
        ctx,
        "“" + quote + "”",
        100,
        330,
        canvas.width - 200,
        62
    );

    /*
     * Attribution
     */
    ctx.fillStyle = "#20201d";
    ctx.font = "700 26px Georgia";

    ctx.fillText(
        "— " + currentRecord.person.name,
        100,
        720
    );

    ctx.fillStyle = "#6c6a63";
    ctx.font = "20px Georgia";

    ctx.fillText(
        currentRecord.person.role,
        100,
        755
    );

    ctx.fillText(
        currentRecord.person.origin +
        " · " +
        currentRecord.person.period,
        100,
        788
    );

    /*
     * Footer
     */
    ctx.fillStyle = "#b0aa9e";

    ctx.fillRect(
        100,
        850,
        canvas.width - 200,
        2
    );

    ctx.fillStyle = "#6c6a63";
    ctx.font = "18px Georgia";

    ctx.fillText(
        "THE HUMAN WISDOM ARCHIVE",
        100,
        900
    );

    ctx.fillText(
        currentRecord.person.subject,
        100,
        935
    );

    /*
     * Download
     */
    canvas.toBlob(function(blob) {
        if (!blob) {
            return;
        }

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download =
            "quote-" +
            document.getElementById("archive-number").textContent +
            ".png";

        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);

        setTimeout(() => {
            URL.revokeObjectURL(url);
        }, 1000);

        showToast(
            language === "hi"
                ? "स्क्रीनशॉट तैयार है।"
                : "Screenshot created."
        );
    }, "image/png");
}


function wrapCanvasText(
    ctx,
    text,
    x,
    y,
    maxWidth,
    lineHeight
) {
    const words = text.split(" ");
    let line = "";

    for (let i = 0; i < words.length; i++) {
        const testLine =
            line +
            (line ? " " : "") +
            words[i];

        const width = ctx.measureText(testLine).width;

        if (width > maxWidth && line) {
            ctx.fillText(line, x, y);

            line = words[i];
            y += lineHeight;
        } else {
            line = testLine;
        }
    }

    if (line) {
        ctx.fillText(line, x, y);
    }
}


// ============================================================
// PRINT
// ============================================================

function printRecord() {
    window.print();
}


// ============================================================
// LANGUAGE
// ============================================================

function toggleLanguage() {
    language =
        language === "en"
            ? "hi"
            : "en";

    render(currentRecord);
}


// ============================================================
// TOAST
// ============================================================

let toastTimer = null;

function showToast(message) {
    const toast =
        document.getElementById("toast");

    toast.textContent = message;

    toast.classList.add("show");

    clearTimeout(toastTimer);

    toastTimer = setTimeout(() => {
        toast.classList.remove("show");
    }, 1800);
}


// ============================================================
// KEYBOARD
// ============================================================

document.addEventListener("keydown", function(event) {
    if (
        event.target.tagName === "INPUT" ||
        event.target.tagName === "TEXTAREA"
    ) {
        return;
    }

    if (
        event.key.toLowerCase() === "n"
    ) {
        newRecord();
    }
});


// ============================================================
// INITIAL LOAD
// ============================================================

document.addEventListener("DOMContentLoaded", function() {
    newRecord();
});
"""


# ============================================================
# HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <meta
        name="description"
        content="The Human Wisdom Archive — a catalogued collection of observations concerning conduct, judgment, work, uncertainty, memory and ordinary human problems."
    >

    <meta
        name="robots"
        content="index, follow"
    >

    <title>The Human Wisdom Archive</title>

    <style>
        __CSS__
    </style>
</head>

<body>

<div class="page">

    <header class="archive-header">

        <div class="header-grid">

            <div>

                <p class="kicker">
                    Historical Observation Repository
                </p>

                <h1>
                    The Human Wisdom Archive
                </h1>

                <p class="subtitle">
                    A catalogued collection of observations concerning
                    conduct, judgment, work, uncertainty, memory and
                    the ordinary problems of human life.
                </p>

            </div>

            <div class="controls">

                <button
                    class="control"
                    id="language-button"
                    onclick="toggleLanguage()"
                >
                    हिन्दी
                </button>

                <button
                    class="control"
                    id="copy-record-button"
                    onclick="copyRecord()"
                >
                    Copy Record
                </button>

                <button
                    class="control"
                    id="print-button"
                    onclick="printRecord()"
                >
                    Print
                </button>

                <button
                    class="control"
                    id="new-button"
                    onclick="newRecord()"
                >
                    New Record
                </button>

            </div>

        </div>

    </header>


    <section class="catalog">

        <div class="catalog-cell">

            <span class="catalog-label">
                Archive Number
            </span>

            <span
                class="catalog-value"
                id="archive-number"
            >
                HWA-000000
            </span>

        </div>


        <div class="catalog-cell">

            <span class="catalog-label">
                Classification
            </span>

            <span
                class="catalog-value"
                id="classification"
            >
                Observation
            </span>

        </div>


        <div class="catalog-cell">

            <span class="catalog-label">
                Record Status
            </span>

            <span class="catalog-value">
                Catalogued
            </span>

        </div>


        <div class="catalog-cell">

            <span class="catalog-label">
                Repository
            </span>

            <span class="catalog-value">
                Human Conduct Collection
            </span>

        </div>

    </section>


    <main class="main-grid">


        <article class="paper">

            <div class="record-main">

                <div class="record-number">
                    ARCHIVAL ENTRY
                </div>


                <div class="quote-box">

                    <p
                        class="quote"
                        id="quote"
                    >
                        “A record is being consulted.”
                    </p>


                    <div class="attribution">

                        <div>
                            <span class="author" id="author">
                                —
                            </span>
                        </div>

                        <div
                            class="role"
                            id="role"
                        >
                            —
                        </div>

                        <div
                            class="meta-line"
                            id="origin-period"
                        >
                            —
                        </div>

                    </div>

                </div>


                <div class="quote-actions">

                    <button
                        class="quote-action"
                        id="copy-quote-button"
                        onclick="copyQuote()"
                    >
                        Copy Quote
                    </button>

                    <button
                        class="quote-action"
                        id="screenshot-button"
                        onclick="screenshotQuote()"
                    >
                        Screenshot Quote
                    </button>

                    <button
                        class="quote-action"
                        id="copy-author-button"
                        onclick="copyQuoteWithAuthor()"
                    >
                        Copy Quote + Author
                    </button>

                </div>


                <div class="section-rule"></div>


                <section>

                    <h2
                        class="section-title"
                        id="interpretation-label"
                    >
                        Interpretive Record
                    </h2>

                    <p
                        class="interpretation"
                        id="interpretation"
                    >
                        —
                    </p>

                </section>


                <div class="analysis-grid">

                    <div class="analysis-card">

                        <h3
                            id="question-label"
                        >
                            Question Raised
                        </h3>

                        <p id="question">
                            —
                        </p>

                    </div>


                    <div class="analysis-card">

                        <h3>
                            Classification
                        </h3>

                        <p id="classification-card">
                            Human Conduct
                        </p>

                    </div>


                    <div class="analysis-card">

                        <h3
                            id="application-label"
                        >
                            Practical Application
                        </h3>

                        <p id="application">
                            —
                        </p>

                    </div>

                </div>

            </div>

        </article>


        <aside class="sidebar">


            <section class="side-card">

                <div class="side-label">
                    Biographical Record
                </div>

                <h2
                    class="side-name"
                    id="side-name"
                >
                    —
                </h2>

                <p
                    class="side-role"
                    id="side-role"
                >
                    —
                </p>


                <ul class="fact-list">

                    <li>
                        <strong>Origin:</strong>
                        <span id="side-origin">
                            —
                        </span>
                    </li>

                    <li>
                        <strong>Period:</strong>
                        <span id="side-period">
                            —
                        </span>
                    </li>

                    <li>
                        <strong>Subject:</strong>
                        <span id="side-subject">
                            —
                        </span>
                    </li>

                </ul>

            </section>


            <section class="side-card">

                <div class="side-label">
                    Practical Application
                </div>

                <p
                    class="application"
                    id="side-application"
                >
                    Observe the situation before attempting
                    to improve it.
                </p>

            </section>


            <section class="side-card">

                <div class="side-label">
                    Cataloguing Note
                </div>

                <p class="catalog-note">
                    This entry is classified according to
                    its principal subject and preserved as
                    an observation concerning ordinary human
                    conduct.
                </p>

            </section>


        </aside>

    </main>


    <footer class="archive-footer">

        <span>
            The Human Wisdom Archive
        </span>

        <span>
            Catalogued Collection · Human Conduct
        </span>

    </footer>

</div>


<div
    class="toast"
    id="toast"
>
</div>


<script>

__JS__

</script>

</body>
</html>
"""


# ============================================================
# BUILD
# ============================================================

def build():

    js = JS

    js = js.replace(
        "__INITIAL_RECORDS__",
        json.dumps(
            initial_records,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__PEOPLE__",
        json.dumps(
            PEOPLE,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__TEMPLATES__",
        json.dumps(
            TEMPLATES,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__OBJECTS__",
        json.dumps(
            OBJECTS,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__PLACES__",
        json.dumps(
            PLACES,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__ACTIONS__",
        json.dumps(
            ACTIONS,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__CONSEQUENCES__",
        json.dumps(
            CONSEQUENCES,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__INTERPRETATIONS__",
        json.dumps(
            INTERPRETATIONS,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__QUESTIONS__",
        json.dumps(
            QUESTIONS,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__APPLICATIONS__",
        json.dumps(
            APPLICATIONS,
            ensure_ascii=False
        )
    )

    js = js.replace(
        "__HINDI_QUOTES__",
        json.dumps(
            HINDI_QUOTES,
            ensure_ascii=False
        )
    )

    page = HTML.replace(
        "__CSS__",
        CSS
    )

    page = page.replace(
        "__JS__",
        js
    )

    # Fix classification card dynamically.
    page = page.replace(
        '<p id="classification-card">\n                            Human Conduct\n                        </p>',
        '<p id="classification-card">Human Conduct</p>'
    )

    # Add synchronization for classification card.
    page = page.replace(
        'setText("classification", record.person.subject);',
        'setText("classification", record.person.subject);\n    setText("classification-card", record.person.subject);'
    )

    # Keep the sidebar application synchronized.
    page = page.replace(
        'setText(\n        "application",',
        'setText(\n        "side-application",\n        language === "hi"\n            ? translateApplication(record.application)\n            : record.application\n    );\n\n    setText(\n        "application",'
    )

    OUTPUT.write_text(
        page,
        encoding="utf-8"
    )

    print(
        f"Generated {OUTPUT.resolve()}"
    )


if __name__ == "__main__":
    build()
