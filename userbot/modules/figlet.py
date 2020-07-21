# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to UserBot by @MoveAngel

import pyfiglet
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.figlet(?: |$)(.*)")
async def figlet(fg):
    if fg.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital",
        "3x5": "3x5",
        "acro": "acrobatic",
        "allig2": "alligator2",
        "avatar": "avatar",
        "bann": "banner",
        "bann3": "banner3",
        "barb": "barbwire",
        "basic": "basic",
        "bell": "bell",
        "big": "big",
        "bigc": "bigchief",
        "bin": "binary",
        "block": "block",
        "calg": "calgphy2",
        "cali": "caligraphy",
        "cat": "catwalk",
        "chunk": "chunky",
        "coin": "coinstak",
        "colo": "colossal",
        "comp": "computer",
        "cont": "contessa",
        "contr" "contrast",
        "cos": "cosmic",
        "cosm": "cosmike",
        "crick": "cricket",
        "curs": "cursive",
        "cyberl": "cyberlarge",
        "cyberm": "cybermedium",
        "cybers": "cybersmall",
        "diam": "diamond",
        "doom": "doom",
        "drp": "drpepper",
        "eftic": "eftichess",
        "eftif": "eftifont",
        "eftip": "eftipiti",
        "eftir": "eftirobot",
        "eftit": "eftitalic",
        "eftiw": "eftiwall",
        "eftiwa": "eftiwater",
        "epic": "epic",
        "fend": "fender",
        "fourt": "fourtops",
        "fuzz": "fuzzy",
        "goof": "goofy",
        "goth": "gothic",
        "graff": "graffiti",
        "holly": "hollywood",
        "inv": "invita",
        "italic": "italic",
        "ivr": "ivrit",
        "jaz": "jazmine",
        "jerus": "jerusalem",
        "kata": "katakana",
        "kban": "kban",
        "larry": "larry3d",
        "lcd": "lcd",
        "lean": "lean",
        "linux": "linux",
        "lock": "lockergnome",
        "madrid": "madrid",
        "marq": "marquee",
        "max": "maxfour",
        "mike": "mike",
        "mini": "mini",
        "mirr": "mirror",
        "mne": "mnemonic",
        "mors": "morse",
        "mosc": "moscow",
        "nancf": "nancyj-fancy",
        "nancu": "nancyj-underlined",
        "nanc": "nancyj",
        "nipp": "nipples",
        "ntg": "ntgreek",
        "o8": "o8",
        "ogre": "ogre",
        "paw": "pawp",
        "peak": "peaks",
        "pebb": "pebbles",
        "pepp": "pepper",
        "poi": "poison",
        "puff": "puffy",
        "pyr": "pyramid",
        "rect": "rectangles",
        "rel": "relief",
        "rel2": "relief2",
        "rev": "rev",
        "roma": "roman",
        "rot": "rot13",
        "round": "rounded",
        "row": "rowancap",
        "rozz": "rozzo",
        "run": "runic",
        "runy": "runyc",
        "sbl": "sblood",
        "scr": "script",
        "ser": "serifcap",
        "sha": "shadow",
        "sho": "short",
        "sli": "slide",
        "sls": "slscript",
        "small": "small",
        "smis": "smisomel",
        "smk": "smkeyboard",
        "smsc": "smscript",
        "smsh": "smshadow",
        "smsl": "smslant",
        "smt": "smtengwar",
        "speed": "speed",
        "stamp": "stampatello",
        "stand": "standard",
        "star": "starwars",
        "stell": "stellar",
        "stop": "stop",
        "str": "straight",
        "tanja": "tanja",
        "teng": "tengwar",
        "term": "term",
        "thick": "thick",
        "thin": "thin",
        "three": "threepoint",
        "tick": "ticks",
        "ticks": "ticksslant",
        "tink": "tinker-toy",
        "tomb": "tombstone",
        "trek": "trek",
        "tsa": "tsalagi",
        "two": "twopoint",
        "uni": "univers",
        "usa": "usaflag",
        "wav": "wavy",
        "weird": "weird"}
    input_str = fg.pattern_match.group(1)
    if "." in input_str:
        text, cmd = input_str.split(".", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await fg.edit("`Please add some text to figlet`")
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await fg.edit("`Invalid selected font.`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await fg.respond("‌‌‎`{}`".format(result))
    await fg.delete()

CMD_HELP.update({
    "figlet":
        ".figlet"
    "\nUsage: Enhance ur text to strip line with anvil."
    "\n\nExample: `.figlet <Text Style>`"
    "\nSTYLE LIST: `slant`, `3D`, `5line`, `alpha`, `banner`, `doh`, `iso`, `letter`, `allig`, `dotm`, `bubble`, `bulb`, `digi`, `3x5`, `acro`, `allig2`, `avatar`, `bann`, `bann3`, `barb`, `basic`, `bell`, `big`, `bigc`, `bin`, `block`, `calg`, `cali`, `cat`, `chunk`, `coin`, `colo`, `compt`, `cont`, `contr`, `cos`, `cosm`, `crick`, `curs`, `cyberl`, `cyberm`, `cybers`, `diam`, `doom`, `drp`, `eftic`, `eftif`, `eftip`, `eftir`, `eftit`, `eftiw`, `eftiwa`, `epic`, `fend`, `fourt`, `fuzz`, `goof`, `goth`, `graff`, `holly`, `inv`, `italic`, `ivr`, `jaz`, `jerus`, `kata`, `kban`, `larry`, `lcd`, `lean`, `linux`, `lock`, `madrid`, `marq`, `max`, `mike`, `mini`, `mirr`, `mne`, `mors`, `mosc`, `nancf`, `nancu`, `nanc`, `nipp`, `ntg`, `o8`, `ogre`, `paw`, `peak`, `pebb`, `pepp`, `poi`, `puff`, `pyr`, `rect`, `rel`, `rel2`, `rev`, `roma`, `rot`, `round`, `row`, `rozz`, `run`, `runy`, `sbl`, `scr`, `ser`, `sha`, `sho`, `sli`, `sls`, `small`, `smis`, `smk`, `smsc`, `smsh`, `smsl`, `smt`, `speed`, `stamp`, `stand`, `star`, `stell`, `stop`, `str`, `tanja`, `tang`, `term`, `thick`, `thin`, `three`, `tick`, `ticks`, `tink`, `tomb`, `trek`, `tsa`, `two`, `uni`, `usa`, `wav`, `weird`"
})
