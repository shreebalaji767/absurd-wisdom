from pathlib import Path
import json
import random
import html
import hashlib


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
# No localStorage
# No external dependencies
# ============================================================


OUTPUT = Path("index.html")


# ============================================================
# ARCHIVAL PERSONNEL
# ============================================================

FICTIONAL_PERSONS = [
    {
        "name": "Aren Voss",
        "role": "Provincial Cartographer",
        "origin": "Northern Territories",
        "period": "Late 18th Century",
        "category": "Practical Philosophy",
        "style": "measured",
    },
    {
        "name": "Mira Sen",
        "role": "Keeper of the Eastern Observatory",
        "origin": "Eastern Provinces",
        "period": "Early 20th Century",
        "category": "Observation",
        "style": "quiet",
    },
    {
        "name": "Captain Ilyan Vale",
        "role": "Survey Officer",
        "origin": "Western Maritime District",
        "period": "19th Century",
        "category": "Endurance",
        "style": "military",
    },
    {
        "name": "Professor Niko Almostov",
        "role": "Lecturer in Natural Philosophy",
        "origin": "Central Academy",
        "period": "Early 20th Century",
        "category": "Reason",
        "style": "academic",
    },
    {
        "name": "Elias Thorne",
        "role": "Village Magistrate",
        "origin": "Northwestern Counties",
        "period": "19th Century",
        "category": "Judgment",
        "style": "legal",
    },
    {
        "name": "Sera Valen",
        "role": "Archivist of Maritime Records",
        "origin": "Southern Coast",
        "period": "Late 19th Century",
        "category": "Memory",
        "style": "archival",
    },
    {
        "name": "Old Master Ren",
        "role": "Instructor of Rural Mechanics",
        "origin": "Eastern Highlands",
        "period": "Undated",
        "category": "Work",
        "style": "proverbial",
    },
    {
        "name": "Dorian Pell",
        "role": "Registrar of Minor Disputes",
        "origin": "Central Administrative District",
        "period": "19th Century",
        "category": "Human Nature",
        "style": "bureaucratic",
    },
    {
        "name": "Ansel Grey",
        "role": "Railway Engineer",
        "origin": "Industrial North",
        "period": "Early 20th Century",
        "category": "Persistence",
        "style": "industrial",
    },
    {
        "name": "Liora Venn",
        "role": "Teacher of Rhetoric",
        "origin": "Old University Quarter",
        "period": "Late 19th Century",
        "category": "Language",
        "style": "rhetorical",
    },
    {
        "name": "Bastian Or",
        "role": "Keeper of the Municipal Clock",
        "origin": "Old Capital",
        "period": "19th Century",
        "category": "Time",
        "style": "observational",
    },
    {
        "name": "Nera Sol",
        "role": "Apothecary's Apprentice",
        "origin": "Southern Market District",
        "period": "Early 19th Century",
        "category": "Experience",
        "style": "practical",
    },
    {
        "name": "Havel Marr",
        "role": "Bridge Inspector",
        "origin": "River Provinces",
        "period": "19th Century",
        "category": "Risk",
        "style": "technical",
    },
    {
        "name": "Orin Bell",
        "role": "Clerk of Agricultural Affairs",
        "origin": "Western Plains",
        "period": "Early 20th Century",
        "category": "Growth",
        "style": "plain",
    },
    {
        "name": "Tavian Roe",
        "role": "Instructor of Navigation",
        "origin": "Northern Port",
        "period": "18th Century",
        "category": "Direction",
        "style": "nautical",
    },
    {
        "name": "Marek Doss",
        "role": "Inspector of Public Roads",
        "origin": "Highland District",
        "period": "19th Century",
        "category": "Progress",
        "style": "administrative",
    },
]


REAL_PERSONS = [
    {
        "name": "Albert Einstein",
        "role": "Physicist",
        "origin": "Germany / Switzerland / United States",
        "period": "1879–1955",
        "category": "Scientific Thought",
    },
    {
        "name": "Marie Curie",
        "role": "Physicist and Chemist",
        "origin": "Poland / France",
        "period": "1867–1934",
        "category": "Scientific Thought",
    },
    {
        "name": "Leonardo da Vinci",
        "role": "Artist, Engineer and Polymath",
        "origin": "Italian States",
        "period": "1452–1519",
        "category": "Observation",
    },
    {
        "name": "Ada Lovelace",
        "role": "Mathematician and Writer",
        "origin": "United Kingdom",
        "period": "1815–1852",
        "category": "Computation",
    },
    {
        "name": "Rabindranath Tagore",
        "role": "Poet and Philosopher",
        "origin": "Bengal",
        "period": "1861–1941",
        "category": "Literature",
    },
    {
        "name": "Nikola Tesla",
        "role": "Inventor and Engineer",
        "origin": "Austrian Empire / United States",
        "period": "1856–1943",
        "category": "Invention",
    },
    {
        "name": "Socrates",
        "role": "Philosopher",
        "origin": "Ancient Athens",
        "period": "c. 470–399 BCE",
        "category": "Philosophy",
    },
    {
        "name": "Confucius",
        "role": "Teacher and Philosopher",
        "origin": "Ancient China",
        "period": "551–479 BCE",
        "category": "Ethics",
    },
    {
        "name": "Marcus Aurelius",
        "role": "Roman Emperor and Stoic Writer",
        "origin": "Roman Empire",
        "period": "121–180 CE",
        "category": "Stoicism",
    },
]


# ============================================================
# WORD BANKS
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
    "timing",
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

PLACES = [
    "the old station",
    "the northern road",
    "the market square",
    "the observatory",
    "the river crossing",
    "the empty classroom",
    "the western gate",
    "the workshop",
    "the hill road",
    "the village archive",
    "the harbor",
    "the railway yard",
    "the courthouse",
    "the orchard",
    "the mountain pass",
]

NOUNS = [
    "a question",
    "a mistake",
    "an idea",
    "a promise",
    "a problem",
    "a decision",
    "a habit",
    "a plan",
    "a memory",
    "an answer",
    "a silence",
    "a warning",
    "a map",
    "a lesson",
    "a beginning",
]

ADJECTIVES = [
    "patient",
    "stubborn",
    "quiet",
    "ordinary",
    "broken",
    "unfinished",
    "small",
    "heavy",
    "unexpected",
    "lonely",
    "old",
    "careful",
    "impatient",
    "awkward",
    "simple",
]


# ============================================================
# QUOTE CONSTRUCTION
# ============================================================

QUOTE_TEMPLATES = [
    (
        "A person who waits for the perfect {object} eventually becomes part of the furniture.",
        "Excessive preparation can quietly become another form of inaction."
    ),
    (
        "The {object} never promised to move. That is why every map eventually learns humility.",
        "Reality does not owe itself to our preferred route. A plan becomes useful only when it remains responsive to what actually exists."
    ),
    (
        "A locked door is a very confident piece of furniture.",
        "Obstacles often appear more authoritative than they really are. Their presence does not automatically establish their permanence."
    ),
    (
        "The smallest key opened the largest door because the door had no opinion about size.",
        "The apparent scale of a problem and the scale of the action required to change it are not necessarily related."
    ),
    (
        "I planted a question and harvested an inconvenience. It was the most useful crop I ever grew.",
        "Good questions rarely provide immediate comfort. Their value often lies in exposing assumptions that had previously gone unnoticed."
    ),
    (
        "A clock that is wrong twice a day is still employed by time.",
        "Usefulness cannot always be reduced to perfect accuracy. Even imperfect instruments can reveal something about the system around them."
    ),
    (
        "The bridge looked stronger after everyone stopped asking whether it was strong.",
        "Confidence can make uncertainty invisible. Removing questions does not remove the conditions that made the questions necessary."
    ),
    (
        "I carried the {object} for ten miles before discovering that it was the wrong thing to carry.",
        "Effort and direction are separate virtues. Persistence cannot compensate indefinitely for a mistaken premise."
    ),
    (
        "A map becomes dangerous when the traveler starts apologizing to the road.",
        "Representations are useful precisely because they are representations. Reality should not be forced to obey the diagram."
    ),
    (
        "The quietest person in the room may simply have forgotten where the argument was going.",
        "Silence has many meanings. It should not automatically be interpreted as agreement, wisdom, confidence, or opposition."
    ),
    (
        "I repaired the {object} until it became more complicated than the original problem.",
        "Improvement can create unnecessary complexity when the desire to fix something becomes detached from the purpose of the repair."
    ),
    (
        "The ladder did not become shorter because I complained about the height.",
        "Frustration can describe difficulty, but description alone does not reduce the distance between intention and achievement."
    ),
    (
        "A heavy stone teaches patience because it refuses to be impressed.",
        "Some problems respond poorly to force and better to sustained attention."
    ),
    (
        "The road was not difficult. My expectations were carrying too much luggage.",
        "Difficulty is partly shaped by what we believe a journey should look like. Expectations can add weight to an already demanding task."
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
        "Reflection is valuable, but self-examination can become circular unless it eventually produces a different action."
    ),
    (
        "A broken compass can still teach you that you are lost.",
        "Failure of a tool does not eliminate the information contained in the failure."
    ),
    (
        "The bell rang because someone pulled it. History later called this inevitability.",
        "Events often appear inevitable only after their causes have already become part of the past."
    ),
    (
        "The door was ordinary until I needed it to be extraordinary.",
        "Circumstances can change the meaning of ordinary objects, abilities, and relationships without changing their underlying nature."
    ),
    (
        "I searched for wisdom in the library and found a chair with better posture.",
        "Knowledge is not automatically transformed into wisdom. The way one inhabits knowledge matters as much as possessing it."
    ),
    (
        "A perfect plan has never survived its first meeting with weather.",
        "Planning is valuable because it prepares action, not because it predicts every condition."
    ),
    (
        "The bucket leaked slowly enough to make every journey educational.",
        "Small recurring losses can teach more than dramatic failures because they expose patterns that are easy to ignore."
    ),
    (
        "The mountain did not become smaller. I simply stopped negotiating with it.",
        "Acceptance can change the relationship between a person and a difficulty without changing the difficulty itself."
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
        "Optimization can become destructive when improvement is measured without reference to the purpose of the activity."
    ),
    (
        "The shortest road looked suspicious because nobody had taken it seriously.",
        "Useful possibilities are sometimes ignored because familiarity is mistaken for evidence."
    ),
]


# ============================================================
# SECONDARY INTERPRETATIONS
# ============================================================

INTERPRETATION_TEMPLATES = [
    "The statement treats an ordinary object as if it possessed judgment, revealing a distinction between physical reality and the meanings people attach to it.",
    "At first reading the statement is deliberately literal and unreasonable. Its deeper structure concerns the gap between intention and consequence.",
    "The apparent contradiction is useful because it places two normally separate ideas in the same frame. The resulting tension makes an ordinary assumption visible.",
    "The statement can be read as an argument against confusing activity with progress. Movement is measurable; direction is harder to establish.",
    "The image suggests that uncertainty does not disappear simply because a person becomes more confident about an explanation.",
    "The underlying observation is that human beings often assign intention to circumstances that are indifferent to them.",
    "The statement uses an absurd physical image to describe a familiar psychological pattern: the gradual transformation of a temporary condition into a permanent habit.",
    "The deeper argument concerns proportion. A small action may have consequences much larger than its physical scale, while enormous effort may accomplish very little.",
    "The statement questions whether efficiency should always be treated as the highest form of improvement.",
    "The image suggests that a person's interpretation of an event can become part of the event's consequences.",
    "The apparent nonsense disappears when the objects are understood as metaphors for assumptions, habits, and expectations.",
    "The statement distinguishes between knowing what something is and knowing what should be done with that knowledge.",
]


QUESTION_TEMPLATES = [
    "What changes when an obstacle is treated as information rather than opposition?",
    "At what point does preparation stop being preparation and become avoidance?",
    "Can an imperfect method still produce a useful understanding?",
    "How much of difficulty belongs to the problem, and how much belongs to expectation?",
    "When does persistence become attachment to a mistaken direction?",
    "Can certainty be useful while still being incomplete?",
    "What disappears when measurement becomes more important than experience?",
    "Does a solution remain a solution when it creates a larger problem?",
    "How often do people mistake familiarity for truth?",
    "What can absence reveal that presence conceals?",
    "Can a failed attempt contain better information than a successful one?",
    "When does simplification become oversimplification?",
]


APPLICATION_TEMPLATES = [
    "In practical terms, the observation favors small experiments over elaborate assumptions.",
    "The principle can be applied by separating effort from outcome and examining whether the chosen direction still serves the original purpose.",
    "A useful application is to identify which part of a problem is factual and which part has been added through expectation.",
    "The statement suggests checking the instrument, the map, or the assumption before increasing the amount of effort.",
    "Applied to ordinary decisions, the idea recommends leaving room for circumstances that could not have been predicted in advance.",
    "The practical lesson is not to abandon planning, but to keep plans subordinate to evidence.",
    "In work and study, this principle supports periodic review rather than endless continuation of an inherited method.",
]


CONTRADICTION_TEMPLATES = [
    "Its central contradiction is that the object appears to behave like a person while the person behaves like an object.",
    "The statement is deliberately unreasonable on its surface, yet the unreasonable image exposes a reasonable human habit.",
    "The paradox comes from treating permanence and change as if they were opposites, when in practice they often describe different stages of the same process.",
    "The tension lies between effort and usefulness: more effort is not automatically more valuable.",
    "The statement places certainty beside uncertainty without resolving the difference.",
    "The apparent contradiction comes from confusing the measurement of an event with its meaning.",
]


OBSERVATION_TEMPLATES = [
    "Observed principle: direction generally matters before acceleration.",
    "Observed principle: assumptions can become invisible precisely when they are shared by everyone.",
    "Observed principle: repeated small consequences can outweigh one dramatic event.",
    "Observed principle: an instrument is useful only in relation to the question it is being used to answer.",
    "Observed principle: confidence changes perception without necessarily changing circumstances.",
    "Observed principle: attention can convert an ordinary event into useful evidence.",
    "Observed principle: a system can remain functional while still containing an unresolved contradiction.",
]


# ============================================================
# HINDI TRANSLATION
# ============================================================

HINDI_QUOTE_MAP = {
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


HINDI_INTERPRETATIONS = [
    "यह कथन साधारण वस्तु को मानवीय निर्णय देने के माध्यम से वास्तविकता और उसके अर्थ के बीच का अंतर दिखाता है।",
    "ऊपरी स्तर पर यह कथन असंगत दिखाई देता है, लेकिन इसके भीतर उद्देश्य और परिणाम के बीच का अंतर छिपा है।",
    "यह विचार बताता है कि किसी समस्या के सामने अधिक प्रयास करना हमेशा सही दिशा में आगे बढ़ना नहीं होता।",
    "कभी-कभी हमारी धारणाएँ स्वयं उस परिस्थिति से बड़ी बाधा बन जाती हैं जिसे वे समझाने के लिए बनाई गई थीं।",
    "यह कथन योजना और वास्तविकता के बीच आवश्यक दूरी की ओर संकेत करता है।",
    "अपूर्ण साधन भी उपयोगी जानकारी दे सकते हैं, यदि उनकी सीमाओं को समझा जाए।",
    "यह विचार बताता है कि किसी घटना की व्याख्या भी उस घटना के परिणामों का हिस्सा बन सकती है।",
]


# ============================================================
# HTML HELPERS
# ============================================================

def esc(value):
    return html.escape(str(value), quote=True)


def js(value):
    return json.dumps(value, ensure_ascii=False)


def archive_id(seed):
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return "WA-" + str(int(digest[:10], 16) % 900000 + 100000)


def build_initial_entry():
    rng = random.Random()

    person = rng.choice(FICTIONAL_PERSONS)

    quote_template, interpretation = rng.choice(QUOTE_TEMPLATES)

    quote = quote_template.format(
        object=rng.choice(OBJECTS),
        abstract=rng.choice(ABSTRACT),
        action=rng.choice(ACTIONS),
    )

    return {
        "name": person["name"],
        "role": person["role"],
        "origin": person["origin"],
        "period": person["period"],
        "category": person["category"],
        "quote": quote,
        "interpretation": interpretation,
        "record_type": "Archival Statement",
        "status": "Catalogued",
    }


# ============================================================
# BROWSER DATA
# ============================================================

BROWSER_DATA = {
    "persons": FICTIONAL_PERSONS,
    "quotes": [
        {
            "q": q,
            "i": i,
        }
        for q, i in QUOTE_TEMPLATES
    ],
    "interpretations": INTERPRETATION_TEMPLATES,
    "questions": QUESTION_TEMPLATES,
    "applications": APPLICATION_TEMPLATES,
    "contradictions": CONTRADICTION_TEMPLATES,
    "observations": OBSERVATION_TEMPLATES,
    "objects": OBJECTS,
    "abstract": ABSTRACT,
    "actions": ACTIONS,
    "places": PLACES,
    "nouns": NOUNS,
    "adjectives": ADJECTIVES,
    "hindiQuotes": HINDI_QUOTE_MAP,
    "hindiInterpretations": HINDI_INTERPRETATIONS,
}


# ============================================================
# HTML
# ============================================================

def generate_html():
    initial = build_initial_entry()
    initial_json = json.dumps(initial, ensure_ascii=False)
    browser_json = json.dumps(BROWSER_DATA, ensure_ascii=False)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>The Human Wisdom Archive</title>

<meta
    name="description"
    content="A digital repository of philosophical observations, historical thought, practical reasoning and archival records."
>

<meta name="theme-color" content="#171717">

<style>

:root {{
    --ink: #171717;
    --muted: #686868;
    --paper: #f5f1e8;
    --paper-dark: #e8e1d4;
    --line: rgba(23,23,23,.16);
    --strong-line: rgba(23,23,23,.35);
    --accent: #8b2e24;
    --white: #fffdf8;
    --serif: Georgia, "Times New Roman", serif;
    --sans: Inter, Arial, Helvetica, sans-serif;
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
    min-height: 100vh;
    color: var(--ink);
    background:
        radial-gradient(circle at 10% 10%, rgba(139,46,36,.045), transparent 25%),
        radial-gradient(circle at 90% 80%, rgba(0,0,0,.035), transparent 28%),
        var(--paper);
    font-family: var(--sans);
}}

body.layout-editorial {{
    --accent: #293b54;
}}

body.layout-ledger {{
    --accent: #5a4932;
}}

body.layout-museum {{
    --accent: #65452e;
}}

body.layout-night {{
    --paper: #111;
    --paper-dark: #191919;
    --ink: #eee9df;
    --muted: #aaa39a;
    --line: rgba(255,255,255,.15);
    --strong-line: rgba(255,255,255,.34);
    --white: #171717;
}}

button {{
    font: inherit;
}}

.archive-shell {{
    width: min(1480px, 100%);
    margin: 0 auto;
    padding: 24px;
}}

.topbar {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 20px;
    align-items: end;
    border-bottom: 1px solid var(--strong-line);
    padding-bottom: 20px;
}}

.brand {{
    display: flex;
    flex-direction: column;
    gap: 5px;
}}

.brand-kicker {{
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--muted);
}}

.brand-title {{
    font-family: var(--serif);
    font-size: clamp(26px, 4vw, 46px);
    line-height: .95;
    letter-spacing: -.035em;
}}

.brand-subtitle {{
    max-width: 680px;
    font-family: var(--serif);
    font-size: 15px;
    color: var(--muted);
    line-height: 1.5;
}}

.top-actions {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: flex-end;
}}

.button {{
    border: 1px solid var(--strong-line);
    background: transparent;
    color: var(--ink);
    padding: 9px 13px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: .08em;
    text-transform: uppercase;
    transition: .18s ease;
}}

.button:hover {{
    background: var(--ink);
    color: var(--paper);
}}

.archive-strip {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-bottom: 1px solid var(--line);
}}

.archive-cell {{
    min-height: 70px;
    padding: 13px 15px;
    border-right: 1px solid var(--line);
}}

.archive-cell:last-child {{
    border-right: 0;
}}

.archive-label {{
    display: block;
    margin-bottom: 6px;
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .13em;
    text-transform: uppercase;
    color: var(--muted);
}}

.archive-value {{
    font-family: var(--mono);
    font-size: 11px;
}}

.main-grid {{
    display: grid;
    grid-template-columns: minmax(0, 1.7fr) minmax(280px, .7fr);
    gap: 0;
    border-bottom: 1px solid var(--strong-line);
}}

.primary {{
    min-width: 0;
    padding: clamp(35px, 6vw, 90px) clamp(20px, 6vw, 90px) 70px 0;
    border-right: 1px solid var(--line);
}}

.secondary {{
    min-width: 0;
    padding: 40px 0 50px 35px;
}}

.record-type {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 30px;
    font-family: var(--mono);
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: .15em;
    color: var(--accent);
}}

.record-type::before {{
    content: "";
    width: 25px;
    height: 1px;
    background: currentColor;
}}

.quote {{
    max-width: 1050px;
    margin: 0;
    font-family: var(--serif);
    font-size: clamp(35px, 6vw, 82px);
    line-height: 1.02;
    letter-spacing: -.045em;
    font-weight: 400;
}}

.layout-editorial .quote {{
    font-size: clamp(38px, 5vw, 72px);
    max-width: 850px;
}}

.layout-minimal .quote {{
    font-size: clamp(34px, 5vw, 65px);
}}

.layout-ledger .quote {{
    font-size: clamp(32px, 4.7vw, 68px);
}}

.attribution {{
    margin-top: 45px;
    padding-top: 18px;
    border-top: 1px solid var(--line);
}}

.person-name {{
    font-family: var(--serif);
    font-size: 24px;
}}

.person-role {{
    margin-top: 4px;
    font-family: var(--mono);
    font-size: 10px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .1em;
}}

.interpretation {{
    margin-top: 60px;
    border-top: 2px solid var(--ink);
    padding-top: 18px;
}}

.section-label {{
    margin-bottom: 13px;
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: var(--muted);
}}

.interpretation-text {{
    max-width: 850px;
    font-family: var(--serif);
    font-size: clamp(18px, 2vw, 26px);
    line-height: 1.42;
}}

.analysis-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    margin-top: 35px;
    border-top: 1px solid var(--line);
    border-left: 1px solid var(--line);
}}

.analysis-card {{
    min-height: 190px;
    padding: 22px;
    border-right: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
}}

.analysis-card p {{
    margin: 0;
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.55;
}}

.sidebar-block {{
    padding-bottom: 28px;
    margin-bottom: 28px;
    border-bottom: 1px solid var(--line);
}}

.sidebar-title {{
    font-family: var(--mono);
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: .15em;
    color: var(--muted);
    margin-bottom: 13px;
}}

.metadata {{
    display: grid;
    gap: 15px;
}}

.meta-row {{
    display: grid;
    gap: 4px;
}}

.meta-key {{
    font-family: var(--mono);
    font-size: 9px;
    text-transform: uppercase;
    letter-spacing: .12em;
    color: var(--muted);
}}

.meta-value {{
    font-family: var(--serif);
    font-size: 17px;
    line-height: 1.3;
}}

.catalog-note {{
    font-family: var(--serif);
    font-size: 16px;
    line-height: 1.55;
}}

.index-mark {{
    width: 90px;
    height: 90px;
    border: 1px solid var(--strong-line);
    border-radius: 50%;
    display: grid;
    place-items: center;
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: .08em;
    text-align: center;
    line-height: 1.3;
    margin-bottom: 20px;
}}

.question-block {{
    margin-top: 55px;
    padding: 25px;
    border: 1px solid var(--strong-line);
    background: rgba(255,255,255,.15);
}}

.question-text {{
    font-family: var(--serif);
    font-size: 23px;
    line-height: 1.35;
}}

.bottom-bar {{
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding-top: 20px;
    font-family: var(--mono);
    font-size: 9px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: .1em;
}}

.copy-status {{
    position: fixed;
    left: 50%;
    bottom: 22px;
    transform: translateX(-50%) translateY(20px);
    padding: 11px 16px;
    background: var(--ink);
    color: var(--paper);
    font-family: var(--mono);
    font-size: 10px;
    opacity: 0;
    pointer-events: none;
    transition: .2s ease;
    z-index: 50;
}}

.copy-status.show {{
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}}

.lang-hi .en {{
    display: none !important;
}}

.lang-en .hi {{
    display: none !important;
}}

body.hindi .brand-subtitle,
body.hindi .interpretation-text,
body.hindi .catalog-note,
body.hindi .question-text,
body.hindi .analysis-card p {{
    font-family: Arial, "Noto Sans Devanagari", sans-serif;
}}

@media (max-width: 900px) {{

    .archive-shell {{
        padding: 15px;
    }}

    .topbar {{
        grid-template-columns: 1fr;
    }}

    .top-actions {{
        justify-content: flex-start;
    }}

    .archive-strip {{
        grid-template-columns: repeat(2, 1fr);
    }}

    .archive-cell:nth-child(2) {{
        border-right: 0;
    }}

    .archive-cell:nth-child(-n+2) {{
        border-bottom: 1px solid var(--line);
    }}

    .main-grid {{
        grid-template-columns: 1fr;
    }}

    .primary {{
        padding-right: 0;
        border-right: 0;
    }}

    .secondary {{
        padding: 35px 0;
        border-top: 1px solid var(--strong-line);
    }}

}}

@media (max-width: 620px) {{

    .brand-title {{
        font-size: 31px;
    }}

    .brand-subtitle {{
        font-size: 14px;
    }}

    .archive-strip {{
        grid-template-columns: 1fr 1fr;
    }}

    .archive-cell {{
        min-height: 65px;
        padding: 11px;
    }}

    .primary {{
        padding-top: 45px;
        padding-bottom: 45px;
    }}

    .quote {{
        font-size: 37px;
        line-height: 1.03;
    }}

    .analysis-grid {{
        grid-template-columns: 1fr;
    }}

    .analysis-card {{
        min-height: auto;
    }}

    .bottom-bar {{
        flex-direction: column;
        gap: 8px;
    }}

}}

@media (max-width: 390px) {{

    .archive-shell {{
        padding: 10px;
    }}

    .top-actions {{
        display: grid;
        grid-template-columns: 1fr 1fr;
    }}

    .button {{
        width: 100%;
        padding: 10px 5px;
    }}

    .archive-strip {{
        grid-template-columns: 1fr;
    }}

    .archive-cell {{
        border-right: 0 !important;
        border-bottom: 1px solid var(--line);
    }}

    .archive-cell:last-child {{
        border-bottom: 0;
    }}

    .quote {{
        font-size: 32px;
    }}

    .person-name {{
        font-size: 21px;
    }}

}}

@media print {{

    body {{
        background: white !important;
        color: black !important;
    }}

    .top-actions,
    .copy-status {{
        display: none !important;
    }}

    .archive-shell {{
        padding: 0;
        width: 100%;
    }}

    .primary {{
        padding-right: 30px;
    }}

    .quote {{
        font-size: 42px;
    }}

    .analysis-card,
    .question-block {{
        break-inside: avoid;
    }}

}}

</style>
</head>

<body class="layout-classic lang-en">

<div class="archive-shell">

    <header class="topbar">

        <div class="brand">

            <div class="brand-kicker">
                Department of Comparative Thought · Repository Division
            </div>

            <div class="brand-title">
                The Human Wisdom Archive
            </div>

            <div class="brand-subtitle">
                A catalogued collection of observations concerning conduct,
                judgment, work, uncertainty, memory and the ordinary problems
                of human life.
            </div>

        </div>

        <div class="top-actions">

            <button class="button" id="languageButton">
                हिंदी / EN
            </button>

            <button class="button" id="copyButton">
                Copy Record
            </button>

            <button class="button" id="printButton">
                Print
            </button>

            <button class="button" id="newButton">
                New Record
            </button>

        </div>

    </header>


    <section class="archive-strip">

        <div class="archive-cell">
            <span class="archive-label">Archive Number</span>
            <span class="archive-value" id="archiveId"></span>
        </div>

        <div class="archive-cell">
            <span class="archive-label">Classification</span>
            <span class="archive-value" id="classification"></span>
        </div>

        <div class="archive-cell">
            <span class="archive-label">Record Status</span>
            <span class="archive-value">CATALOGUED</span>
        </div>

        <div class="archive-cell">
            <span class="archive-label">Repository</span>
            <span class="archive-value">HUMAN THOUGHT</span>
        </div>

    </section>


    <main class="main-grid">

        <article class="primary">

            <div class="record-type">
                Archival Statement
            </div>

            <blockquote class="quote" id="quote"></blockquote>


            <div class="attribution">

                <div class="person-name" id="personName"></div>

                <div class="person-role" id="personRole"></div>

            </div>


            <section class="interpretation">

                <div class="section-label">
                    Interpretive Record
                </div>

                <div class="interpretation-text" id="interpretation"></div>

            </section>


            <section class="analysis-grid" id="analysisGrid"></section>


            <section class="question-block">

                <div class="section-label">
                    Question Raised
                </div>

                <div class="question-text" id="question"></div>

            </section>

        </article>


        <aside class="secondary">

            <div class="index-mark">
                HUMAN<br>
                WISDOM<br>
                ARCHIVE
            </div>


            <div class="sidebar-block">

                <div class="sidebar-title">
                    Biographical Record
                </div>

                <div class="metadata">

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

            </div>


            <div class="sidebar-block">

                <div class="sidebar-title">
                    Cataloguing Note
                </div>

                <div class="catalog-note" id="catalogNote">
                    The present record has been indexed according to
                    subject, form, interpretive tradition and historical
                    context.
                </div>

            </div>


            <div class="sidebar-block">

                <div class="sidebar-title">
                    Practical Application
                </div>

                <div class="catalog-note" id="application"></div>

            </div>


            <div class="sidebar-block">

                <div class="sidebar-title">
                    Record Class
                </div>

                <div class="catalog-note">
                    Philosophical Observation<br>
                    Practical Reasoning<br>
                    Human Conduct
                </div>

            </div>

        </aside>

    </main>


    <footer class="bottom-bar">

        <span>
            Human Wisdom Archive · Repository Division
        </span>

        <span>
            <span id="footerRecord"></span>
            · Digital Catalogue
        </span>

    </footer>

</div>


<div class="copy-status" id="copyStatus">
    Record copied
</div>


<script>

const ARCHIVE = {browser_json};

const INITIAL = {initial_json};


const $ = (selector) => document.querySelector(selector);


function randomItem(array) {{
    return array[Math.floor(Math.random() * array.length)];
}}


function shuffle(array) {{
    const result = [...array];

    for (let i = result.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));

        [result[i], result[j]] = [result[j], result[i]];
    }}

    return result;
}}


function archiveNumber() {{
    const value =
        Math.floor(100000 + Math.random() * 900000);

    return "WA-" + value;
}}


function createQuote() {{

    const template = randomItem(ARCHIVE.quotes);

    let quote = template.q;

    quote = quote.replace(
        /{{object}}/g,
        randomItem(ARCHIVE.objects)
    );

    quote = quote.replace(
        /{{abstract}}/g,
        randomItem(ARCHIVE.abstract)
    );

    quote = quote.replace(
        /{{action}}/g,
        randomItem(ARCHIVE.actions)
    );

    return {{
        quote,
        interpretation: template.i
    }};
}}


function createRecord() {{

    const person = randomItem(ARCHIVE.persons);

    const quoteData = createQuote();

    const interpretation =
        Math.random() < 0.45
            ? randomItem(ARCHIVE.interpretations)
            : quoteData.interpretation;

    const id = archiveNumber();

    const shuffledQuestions =
        shuffle(ARCHIVE.questions);

    const shuffledApplications =
        shuffle(ARCHIVE.applications);

    const shuffledContradictions =
        shuffle(ARCHIVE.contradictions);

    const shuffledObservations =
        shuffle(ARCHIVE.observations);

    const place = randomItem(ARCHIVE.places);
    const noun = randomItem(ARCHIVE.nouns);
    const adjective = randomItem(ARCHIVE.adjectives);

    return {{

        id,

        person,

        quote: quoteData.quote,

        interpretation,

        question: shuffledQuestions[0],

        application: shuffledApplications[0],

        place,

        noun,

        adjective,

        analysis: [

            {{
                label: "Contextual Note",
                text:
                    "The wording is consistent with a broader tradition "
                    + "of ordinary observations being used to examine "
                    + "larger questions of conduct and judgment."
            }},

            {{
                label: "Observed Principle",
                text:
                    randomItem(ARCHIVE.observations)
            }},

            {{
                label: "Contradiction",
                text:
                    randomItem(ARCHIVE.contradictions)
            }},

            {{
                label: "Alternative Reading",
                text:
                    "Read literally, the statement is concerned with "
                    + adjective + " circumstances at "
                    + place + ". Read conceptually, it concerns "
                    + noun + "."
            }},

            {{
                label: "Practical Reading",
                text:
                    randomItem(ARCHIVE.applications)
            }},

            {{
                label: "Further Question",
                text:
                    randomItem(ARCHIVE.questions)
            }}

        ]

    }};

}}


function setText(selector, value) {{
    const element = $(selector);

    if (element) {{
        element.textContent = value;
    }}
}}


function renderAnalysis(record) {{

    const grid = $("#analysisGrid");

    grid.innerHTML = "";

    const cards = shuffle(record.analysis).slice(
        0,
        4 + Math.floor(Math.random() * 2)
    );

    cards.forEach(card => {{

        const article = document.createElement("article");

        article.className = "analysis-card";

        article.innerHTML = `
            <div class="section-label"></div>
            <p></p>
        `;

        article.querySelector(".section-label").textContent =
            card.label;

        article.querySelector("p").textContent =
            card.text;

        grid.appendChild(article);

    }});

}}


function render(record) {{

    setText("#archiveId", record.id);
    setText("#footerRecord", record.id);

    setText("#classification", record.person.category);

    setText("#quote", record.quote);

    setText("#personName", record.person.name);

    setText("#personRole", record.person.role);

    setText("#metaName", record.person.name);

    setText("#metaRole", record.person.role);

    setText("#metaOrigin", record.person.origin);

    setText("#metaPeriod", record.person.period);

    setText("#interpretation", record.interpretation);

    setText("#question", record.question);

    setText("#application", record.application);

    renderAnalysis(record);

    applyLayout();

    updateLanguage();

    window.currentRecord = record;
}}


function applyLayout() {{

    const layouts = [
        "classic",
        "editorial",
        "minimal",
        "ledger",
        "museum",
        "night"
    ];

    const layout = randomItem(layouts);

    document.body.classList.remove(
        "layout-classic",
        "layout-editorial",
        "layout-minimal",
        "layout-ledger",
        "layout-museum",
        "layout-night"
    );

    document.body.classList.add(
        "layout-" + layout
    );

    const quote = $(".quote");

    if (Math.random() > .5) {{
        quote.style.textAlign = "left";
    }} else {{
        quote.style.textAlign = "left";
    }}

    document.documentElement.style.setProperty(
        "--archive-random-spacing",
        Math.floor(20 + Math.random() * 70) + "px"
    );

}}


function showStatus(message) {{

    const status = $("#copyStatus");

    status.textContent = message;

    status.classList.add("show");

    clearTimeout(window.statusTimer);

    window.statusTimer = setTimeout(() => {{
        status.classList.remove("show");
    }}, 1700);

}}


async function copyRecord() {{

    const record = window.currentRecord;

    if (!record) {{
        return;
    }}

    const text =

`${{record.person.name}}
${{record.person.role}}
${{record.person.origin}}
${{record.person.period}}

"${{record.quote}}"

Interpretive Record:
${{record.interpretation}}

Question Raised:
${{record.question}}

Practical Application:
${{record.application}}

Archive Number:
${{record.id}}
`;

    try {{

        await navigator.clipboard.writeText(text);

        showStatus("Record copied");

    }} catch (error) {{

        const area = document.createElement("textarea");

        area.value = text;

        document.body.appendChild(area);

        area.select();

        document.execCommand("copy");

        area.remove();

        showStatus("Record copied");

    }}

}}


function screenshotRecord() {{

    const width = 1400;
    const height = 900;

    const canvas =
        document.createElement("canvas");

    canvas.width = width;
    canvas.height = height;

    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "#f5f1e8";
    ctx.fillRect(0, 0, width, height);

    ctx.fillStyle = "#171717";

    ctx.font = "16px Arial";

    ctx.fillText(
        "THE HUMAN WISDOM ARCHIVE",
        70,
        75
    );

    ctx.font = "12px monospace";

    ctx.fillText(
        window.currentRecord.id,
        70,
        105
    );

    ctx.font = "42px Georgia";

    const quote =
        '"' + window.currentRecord.quote + '"';

    wrapCanvasText(
        ctx,
        quote,
        70,
        180,
        1150,
        58
    );

    ctx.font = "18px Georgia";

    ctx.fillText(
        window.currentRecord.person.name,
        70,
        430
    );

    ctx.font = "13px Arial";

    ctx.fillText(
        window.currentRecord.person.role,
        70,
        455
    );

    ctx.font = "16px Georgia";

    wrapCanvasText(
        ctx,
        window.currentRecord.interpretation,
        70,
        530,
        1150,
        28
    );

    const link =
        document.createElement("a");

    link.download =
        "wisdom-" +
        window.currentRecord.id +
        ".png";

    link.href =
        canvas.toDataURL("image/png");

    link.click();

}}


function wrapCanvasText(
    ctx,
    text,
    x,
    y,
    maxWidth,
    lineHeight
) {{

    const words = text.split(" ");

    let line = "";

    for (let n = 0; n < words.length; n++) {{

        const testLine =
            line + words[n] + " ";

        const metrics =
            ctx.measureText(testLine);

        if (
            metrics.width > maxWidth &&
            n > 0
        ) {{

            ctx.fillText(
                line,
                x,
                y
            );

            line =
                words[n] + " ";

            y += lineHeight;

        }} else {{

            line = testLine;

        }}

    }}

    ctx.fillText(line, x, y);

}}


function toggleLanguage() {{

    const isHindi =
        document.body.classList.contains("hindi");

    if (isHindi) {{
        document.body.classList.remove("hindi");
        document.body.classList.remove("lang-hi");
        document.body.classList.add("lang-en");
    }} else {{
        document.body.classList.add("hindi");
        document.body.classList.remove("lang-en");
        document.body.classList.add("lang-hi");

        translateCurrentRecord();
    }}

}}


function translateCurrentRecord() {{

    const record = window.currentRecord;

    if (!record) {{
        return;
    }}

    const translated =
        ARCHIVE.hindiQuotes[record.quote];

    if (translated) {{
        setText("#quote", translated);
    }}

    const hindiInterpretation =
        randomItem(ARCHIVE.hindiInterpretations);

    setText(
        "#interpretation",
        hindiInterpretation
    );

    setText(
        "#question",
        "किस बिंदु पर तैयारी, तैयारी न रहकर टालने का दूसरा नाम बन जाती है?"
    );

    setText(
        "#application",
        "व्यावहारिक रूप से यह विचार सुझाव देता है कि प्रयास बढ़ाने से पहले दिशा और आधारभूत धारणा की समीक्षा की जाए।"
    );

    document.querySelectorAll(
        "#analysisGrid .analysis-card p"
    ).forEach((element, index) => {{

        const translations = [
            "यह कथन मानव व्यवहार और निर्णय के एक सामान्य पैटर्न की ओर संकेत करता है।",
            "अवलोकित सिद्धांत: साझा धारणाएँ अक्सर तब अदृश्य हो जाती हैं जब उन पर कोई प्रश्न नहीं उठाता।",
            "विरोधाभास यह है कि असंगत दिखाई देने वाला चित्र एक परिचित मानवीय आदत को स्पष्ट कर देता है।",
            "वैकल्पिक पाठ: साधारण घटना को व्यापक मानवीय अनुभव के रूप में पढ़ा जा सकता है।",
            "व्यावहारिक पाठ: प्रमाण और उद्देश्य की समीक्षा किए बिना केवल प्रयास बढ़ाना पर्याप्त नहीं है।"
        ];

        element.textContent =
            translations[index % translations.length];

    }});

}}


function updateLanguage() {{

    const isHindi =
        document.body.classList.contains("hindi");

    document.documentElement.lang =
        isHindi ? "hi" : "en";

}}


function newRecord() {{

    const record = createRecord();

    render(record);

    window.scrollTo({{
        top: 0,
        behavior: "smooth"
    }});

}}


$("#copyButton").addEventListener(
    "click",
    copyRecord
);


$("#printButton").addEventListener(
    "click",
    () => window.print()
);


$("#newButton").addEventListener(
    "click",
    newRecord
);


$("#languageButton").addEventListener(
    "click",
    toggleLanguage
);


window.addEventListener(
    "keydown",
    event => {{

        if (
            (event.ctrlKey || event.metaKey) &&
            event.key.toLowerCase() === "s"
        ) {{
            event.preventDefault();
        }}

        if (
            event.key.toLowerCase() === "n" &&
            !event.ctrlKey &&
            !event.metaKey &&
            !event.altKey
        ) {{
            newRecord();
        }}

    }}
);


/*
    The first record is generated immediately.
    A fresh record is generated after each page load,
    so browser refreshes do not require persistent storage.
*/

render(createRecord());

</script>

</body>
</html>
"""

    return page


# ============================================================
# WRITE FILE
# ============================================================

if __name__ == "__main__":
    content = generate_html()

    OUTPUT.write_text(
        content,
        encoding="utf-8"
    )

    print(f"Generated: {OUTPUT.resolve()}")
    print("Static site generation complete.")
