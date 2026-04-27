from flask_babel import lazy_gettext as _l

# =======================
# ARTISTS
# =======================

artists = {
    "aoife-murphy": {
        "id": "aoife-murphy",
        "name": "Aoife Murphy",
        "photo": "/static/assets/img/tree1.png",
        "bio_short": _l("An Irish mixed‑media artist exploring stillness and organic form."),
        "bio_full": _l(
            "Aoife Murphy was born in Cork, Ireland, and builds her mixed-media work from the quiet details of the natural world. "
            "She combines ink, bark textures, pressed foliage, and handmade paper to create layered surfaces that feel collected rather than composed. "
            "Her practice begins with sketchbooks filled during long walks through woodland paths and coastal edges, where she studies how weather changes the tone of a place. "
            "Aoife is drawn to the spaces between things: the pause before movement, the hollow under roots, and the thin light that settles after rain."
        ),
        "works": ["still-branches", "quiet-root", "fog-study", "moss-line", "shadow-bark"]
    },

    "kenji-sato": {
        "id": "kenji-sato",
        "name": "Kenji Sato",
        "photo": "/static/assets/img/tree2.png",
        "bio_short": _l("A Kyoto‑based painter blending abstraction with calligraphic gesture."),
        "bio_full": _l(
            "Kenji Sato was born in 1971 in Kyoto, Japan. His work sits at the boundary between contemporary abstraction "
            "and traditional brush practice. His paintings emphasize balance, negative space, and rhythm. Kenji paints his experiences of nature and memory, often drawing on the aesthetics of wabi-sabi and yūgen. He enjoys making his thoughts visible through the process of painting, allowing for spontaneity and imperfection to guide the final composition."
        ),
        "works": ["silent-river", "ink-memory"]
    },

    "lucia-fernandez": {
        "id": "lucia-fernandez",
        "name": "Lucía Fernández",
        "photo": "/static/assets/img/tree1.png",
        "bio_short": _l("A Spanish painter working with light, pigment, and restrained colour."),
        "bio_full": _l(
            "Lucía Fernández was born in Valencia, Spain, and paints interiors, thresholds, and unguarded moments of stillness. "
            "She works with thin veils of oil and pigment, building colour slowly so that the surface holds the trace of every adjustment. "
            "Her compositions often begin from a remembered room or a patch of afternoon light, then move toward something more intimate and reflective. "
            "Lucía keeps her palette restrained so that slight shifts in warmth, shadow, and reflection carry the emotional weight of the piece."
        ),
        "works": ["soft-afternoon", "window-after-rain"]
    },

    "mei-lin-zhang": {
        "id": "mei-lin-zhang",
        "name": "Mei Lin Zhang",
        "photo": "/static/assets/img/tree2.png",
        "bio_short": _l("A Chinese painter blending ink traditions with contemporary landscape memory."),
        "bio_full": _l(
            "Mei Lin Zhang was born in Hangzhou, China, and works between traditional ink painting and contemporary mixed media. "
            "Her paintings often begin with field notes taken beside rivers, old gardens, and quiet stone paths, then evolve into layered compositions that balance atmosphere and structure. "
            "She is interested in how memory changes the shape of a landscape, and how a single line can suggest both distance and intimacy. "
            "Mei Lin’s practice is grounded in patience, repetition, and close attention to the surfaces where water, paper, and pigment meet."
        ),
        "works": ["moss-line", "shadow-bark"]
    }
}

# =======================
# PAINTINGS
# =======================

paintings = {
    "still-branches": {
        "id": "still-branches",
        "title": _l("Stillness in Branches"),
        "artist_id": "aoife-murphy",
        "year": 2025,
        "material": _l("Ink and mixed media"),
        "size": "70 × 100 cm",
        "description": _l(
            "A quiet composition built from layered ink washes and brittle line work, "
            "suggesting suspended movement."
        ),
        "img": "/static/assets/img/tree1.png",
        "thumb": "/static/assets/img/tree1.png"
    },

    "quiet-root": {
        "id": "quiet-root",
        "title": _l("Quiet Root"),
        "artist_id": "aoife-murphy",
        "year": 2024,
        "material": _l("Ink on handmade paper"),
        "size": "50 × 70 cm",
        "description": _l(
            "A minimal study of grounding forms and negative space."
        ),
        "img": "/static/assets/img/tree2.png",
        "thumb": "/static/assets/img/tree2.png"
    },

    "fog-study": {
        "id": "fog-study",
        "title": _l("Fog Study"),
        "artist_id": "aoife-murphy",
        "year": 2023,
        "material": _l("Ink wash"),
        "size": "60 × 90 cm",
        "description": _l(
            "An atmospheric work exploring diffusion and edge softness."
        ),
        "img": "/static/assets/img/tree1.png",
        "thumb": "/static/assets/img/tree1.png"
    },

    "moss-line": {
        "id": "moss-line",
        "title": _l("Moss Line"),
        "artist_id": "mei-lin-zhang",
        "year": 2025,
        "material": _l("Ink, pigment, and collage on paper"),
        "size": "65 × 85 cm",
        "description": _l(
            "A textured study of damp edges, with fragmented marks suggesting the slow spread of moss along stone and wood."
        ),
        "img": "/static/assets/img/tree1.png",
        "thumb": "/static/assets/img/tree1.png"
    },

    "shadow-bark": {
        "id": "shadow-bark",
        "title": _l("Shadow Bark"),
        "artist_id": "mei-lin-zhang",
        "year": 2024,
        "material": _l("Mixed media on handmade paper"),
        "size": "55 × 75 cm",
        "description": _l(
            "Layered bark rubbings and ink washes create a dark, tactile surface shaped by shifting woodland shade."
        ),
        "img": "/static/assets/img/tree2.png",
        "thumb": "/static/assets/img/tree2.png"
    },

    "silent-river": {
        "id": "silent-river",
        "title": _l("Silent River"),
        "artist_id": "kenji-sato",
        "year": 2026,
        "material": _l("Acrylic and sumi ink on canvas"),
        "size": "120 × 80 cm",
        "description": _l(
            "Large gestural strokes echo the movement of water without direct representation."
        ),
        "img": "/static/assets/img/tree2.png",
        "thumb": "/static/assets/img/tree2.png"
    },

    "ink-memory": {
        "id": "ink-memory",
        "title": _l("Ink Memory"),
        "artist_id": "kenji-sato",
        "year": 2025,
        "material": _l("Ink on canvas"),
        "size": "90 × 90 cm",
        "description": _l(
            "A meditative composition balancing repetition and interruption."
        ),
        "img": "/static/assets/img/tree1.png",
        "thumb": "/static/assets/img/tree1.png"
    },

    "window-after-rain": {
        "id": "window-after-rain",
        "title": _l("Window After Rain"),
        "artist_id": "lucia-fernandez",
        "year": 2025,
        "material": _l("Oil on linen"),
        "size": "95 × 110 cm",
        "description": _l(
            "Soft reflections and washed-out daylight capture the calm atmosphere of a room just after the storm clears."
        ),
        "img": "/static/assets/img/tree2.png",
        "thumb": "/static/assets/img/tree2.png"
    },

    "soft-afternoon": {
        "id": "soft-afternoon",
        "title": _l("Soft Afternoon"),
        "artist_id": "lucia-fernandez",
        "year": 2024,
        "material": _l("Oil on canvas"),
        "size": "100 × 120 cm",
        "description": _l(
            "Muted tones capture the way daylight settles across an empty room."
        ),
        "img": "/static/assets/img/tree2.png",
        "thumb": "/static/assets/img/tree2.png"
    }
}