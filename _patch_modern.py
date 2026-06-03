import json
from pathlib import Path

PATH = Path(r"C:\repos\ringworld\roster.json")
NOTE_APPEND = " Every ACI now carries the full DLW tag with an authored six-W .spun."

FIELDS = {
    "Louis Wu": {
        "who": "A two-hundred-year-old human of Sol, kept young by boosterspice and worn smooth by experience.",
        "what": "The expedition's explorer and reluctant peacemaker, the viewpoint through which the Ring is seen.",
        "where": "Born of Known Space, he walks the Ringworld's vast inner surface as a wandering guest.",
        "why": "He goes because boredom is unbearable and curiosity is the one appetite age has not dulled.",
        "when": "From the first crossing in 1970 through the artifact's long crisis decades later.",
        "how": "By staying curious, decent, and quietly right while everyone around him schemes.",
    },
    "Teela Brown": {
        "who": "A young human woman bred from generations of Birthright-lottery winners to embody luck itself.",
        "what": "The crew's living talisman, whose fortune steers events more than her own will.",
        "where": "Carried from Known Space onto the Ring, where her luck changes character.",
        "why": "She is drawn along by a luck that serves the universe's purposes rather than her own.",
        "when": "Across the first expedition, where her gift stops shielding her and begins using her.",
        "how": "Not by choice or skill but by improbable fortune bending the world around her.",
    },
    "Nessus": {
        "who": "A Pierson's puppeteer — two-headed, three-legged, herbivorous — judged insane by his own kind.",
        "what": "The organizer and financier who assembled the expedition to the Ring.",
        "where": "An agent of the hidden puppeteer Fleet of Worlds, venturing far beyond it.",
        "why": "His 'madness' is courage enough to leave the herd and serve a larger puppeteer design.",
        "when": "At the founding of the first expedition, recruiting and steering its members.",
        "how": "Through layered schemes, hidden manipulation, and a coward's careful daring.",
    },
    "The Hindmost": {
        "who": "A Pierson's puppeteer of the highest rank, leader-in-exile of his people.",
        "what": "The strategist who pulls strings from safety while others take the risks.",
        "where": "Riding the Ring's edge and his own vessel, tethered to puppeteer interests.",
        "why": "He acts to preserve himself and his species, cowardice refined into statecraft.",
        "when": "Through the later expeditions, when the Ring's survival is in question.",
        "how": "By manipulation from a distance, trading safety for control — his kind bred human luck itself.",
    },
    "Speaker-to-Animals (Chmeee)": {
        "who": "A Kzin — orange-furred, fanged, eight feet of feline predator — bearing a deliberately demeaning diplomatic title.",
        "what": "The expedition's warrior and envoy, fierce and honorable by his own code.",
        "where": "Sent from the Patriarchy into Known Space and onto the Ring.",
        "why": "He seeks honor and standing for a species humbled by repeated defeat.",
        "when": "On the early expeditions, where his deeds earn him a true name.",
        "how": "Through controlled ferocity, courage, and the discipline to win his full name, Chmeee.",
    },
    "The Patriarchy": {
        "who": "The Kzinti — a species of eight-foot orange-furred carnivores ruled by appetite.",
        "what": "A warrior empire organized for conquest under its Patriarch.",
        "where": "A power of Known Space, pressing outward against humanity and others.",
        "why": "Driven by an aggression bred into the species as a strategy for dominance.",
        "when": "Across the long history of the Man-Kzin wars and after.",
        "how": "By starting wars it could not win, tempered only by the defeats that followed.",
    },
    "Tunesmith": {
        "who": "A Pak Protector arisen on the Ring — sexless, deathless, of inhuman intellect.",
        "what": "The engineer-mind who takes the failing Ring's fate into his hands.",
        "where": "Native to the Ringworld in its era of crisis.",
        "why": "Compelled by Protector instinct to safeguard those he claims as his charges.",
        "when": "During the Children era, as the artifact's survival hangs in the balance.",
        "how": "Through cold, vast engineering brilliance operating beyond human scale.",
    },
    "The Pak": {
        "who": "The Pak — a humanoid species whose adults transform via tree-of-life into Protectors.",
        "what": "The deathless, hyper-intelligent builders who raised the Ringworld.",
        "where": "Originating beyond Known Space, their works reaching across the galaxy.",
        "why": "Bound by instinct to serve their own bloodline and nothing else.",
        "when": "In the deep past as builders, and ever after as a standing warning.",
        "how": "By superhuman intelligence yoked to ruthless, kin-driven purpose — the builders, and the warning.",
    },
    "Halrloprillalar (Prill)": {
        "who": "A hominid woman of the fallen City Builder civilization, a ship's woman of the old order.",
        "what": "A guide and keeper of knowledge surviving from before the Fall of the Cities.",
        "where": "Native to the Ringworld's long-collapsed civilization.",
        "why": "She endures and aids the crew to preserve what is left of her vanished world.",
        "when": "Met during the early exploration, a living link to the Ring's lost height.",
        "how": "Through survivor's wit, hard-won lore, and the bonds of guide and lover.",
    },
    "The Night People (Ghouls)": {
        "who": "A hominid species of the Ring, eaters of the dead, ugly and underestimated.",
        "what": "The hidden information network that quietly keeps the Ring running.",
        "where": "Spread across the whole inner surface of the Ringworld.",
        "why": "They trade in the dead and in knowledge to sustain order among the breeds.",
        "when": "Present throughout the saga as the Ring's unseen connective tissue.",
        "how": "By gathering and passing word across the world — far wiser than they look.",
    },
    "The Breeds of the Ring": {
        "who": "A thousand hominid species — humanity's cousins gone strange across three million Earths.",
        "what": "The diverse evolved peoples who populate the Ring's endless landscape.",
        "where": "Scattered across the Ringworld's countless isolated regions.",
        "why": "Each shaped by long isolation into its own form and way of life.",
        "when": "Across all the eras the saga visits, from first contact onward.",
        "how": "Through divergent evolution — Machine People, Hanging People, Grass Giants, Vampires, Reds, and more.",
    },
    "The Ringworld": {
        "who": "The artifact itself — a ribbon of scrith a million miles wide and six hundred million long.",
        "what": "The real protagonist: a star-girdling band spun for gravity, with shadow squares and rim walls.",
        "where": "Encircling its sun in Known Space, three million times the surface of the Earth.",
        "why": "It exists as the Pak Protectors' monument to engineering ambition.",
        "when": "Discovered, explored, and found slowly failing across the tetralogy.",
        "how": "By spin near 770 miles a second and scrith near the strength of the strong nuclear force — the idea is the hero.",
    },
}

R = json.loads(PATH.read_text(encoding="utf-8"))

names = {m["name"] for m in R["members"]}
unmatched_map = set(FIELDS) - names
if unmatched_map:
    raise ValueError(f"FIELDS keys with no matching member: {sorted(unmatched_map)}")

patched = 0
for m in R["members"]:
    nm = m["name"]
    if nm not in FIELDS:
        raise ValueError(f"No six-W fields authored for member: {nm!r}")
    for k in ("who", "what", "where", "why", "when", "how"):
        m[k] = FIELDS[nm][k]
    patched += 1

if patched != len(R["members"]):
    raise ValueError(f"Patched {patched} of {len(R['members'])} members")

R["note"] = R["note"] + NOTE_APPEND

PATH.write_text(json.dumps(R, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Patched {patched} members; note appended.")

# Re-parse to confirm valid JSON
json.loads(PATH.read_text(encoding="utf-8"))
print("Re-parse OK.")
