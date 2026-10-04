#!/usr/bin/env python3
"""
Imperial College London – Directed Reading Programme
Advertisement Video  (~2–3 minutes)

──────────────────────────────────────────────────────────────
QUICK START
──────────────────────────────────────────────────────────────
  High-quality render:   manim -pqh drp_advert.py DRPAdvertisement
  Preview (fast):        manim -pql drp_advert.py DRPAdvertisement
  Single scene test:     manim -pql drp_advert.py DRPAdvertisement -n 2

──────────────────────────────────────────────────────────────
VOICE-OVER SUPPORT
──────────────────────────────────────────────────────────────
  Each scene has a VOICEOVER docstring describing the suggested spoken
  text.  To add programmatic TTS (e.g. ElevenLabs / Google):

    pip install manim-voiceover
    # then change: class DRPAdvertisement(Scene)
    # to:          class DRPAdvertisement(VoiceoverScene)
    # and wrap animation blocks in:
    #   with self.voiceover(text="..."):

──────────────────────────────────────────────────────────────
FILE STRUCTURE
──────────────────────────────────────────────────────────────
  Section 1  –  Asset paths          (edit these)
  Section 2  –  Text content         (edit these)
  Section 3  –  Design tokens        (colours / sizes)
  Section 4  –  Topic & cluster data (edit to add / remove topics)
  Section 5  –  DRPAdvertisement     (the Manim Scene class)
               ├─ construct()         top-level orchestration
               ├─ Shared utilities    (_fade_all, _safe_image, etc.)
               ├─ Topic factories     (_build_topic_visual, _animate_topic_entrance)
               └─ Scene methods       (scene_1_welcome … scene_7_closing)
"""

from manim import *
import numpy as np


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 – ASSET PATHS
# Replace every path below with the path to your actual file.
# The script will render placeholder boxes if a file is missing,
# so it always works even before you have the real assets.
# ══════════════════════════════════════════════════════════════════════════════

LOGO_PATH       = "assets/drp_logo.png"
LEADER_1_PHOTO  = "assets/leader1.jpg"
LEADER_2_PHOTO  = "assets/leader2.jpg"
LEADER_3_PHOTO  = "assets/leader3.jpg"
LEADER_4_PHOTO  = "assets/leader3.jpg"
LEADER_5_PHOTO  = "assets/leader3.jpg"
LEADER_6_PHOTO  = "assets/leader3.jpg"

FOUNDERS_PHOTO  = "assets/founders.jpg"
QR_CODE_PATH    = "assets/qr_code.png"

GROUP_PHOTOS: list = [
    "assets/g1.jpg",
    "assets/g2.jpg",
    "assets/g3.jpg",
    "assets/g4.jpg",
    "assets/g5.jpg",
    "assets/g6.jpg",
    "assets/g7.jpg",
    "assets/g8.jpg",
    "assets/g9.jpg",
    "assets/g10.jpg",
]
    

# Add / remove photo paths freely – the script handles any number ≥ 1
SYMPOSIUM_PHOTOS: list = [
    "assets/s1.jpg",
    "assets/s2.jpg",
    "assets/s3.jpg",
    "assets/s4.jpg",
    "assets/s5.jpg",
    "assets/s6.jpg",
    "assets/s7.jpg",
    "assets/s8.jpg",
    "assets/s9.jpg",
    "assets/s10.jpg",
    "assets/s11.jpg",
    "assets/s12.jpg",
]

PAPER_IMAGES: list = [
    "assets/paper1.jpg",
    "assets/paper2.jpg",
]


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 – TEXT CONTENT
# ══════════════════════════════════════════════════════════════════════════════

LEADER_1 = {
    "name":  "Afjal",
    "years": "Year 3",
    "role":  "Events & Outreach",
    "photo": LEADER_1_PHOTO,
}
LEADER_2 = {
    "name":  "Rafael",
    "years": "Year 2",
    "role":  "Matching and Admin",
    "photo": LEADER_2_PHOTO,
}
LEADER_3 = {
    "name":  "Yuhuan",
    "years": "Year 2",
    "role":  "Events & Outreach",
    "photo": LEADER_3_PHOTO,
}
LEADER_4 = {
    "name":  "Ariff",
    "years": "PhD",
    "role":  "Matching and Admin",
    "photo": LEADER_4_PHOTO,
}
LEADER_5 = {
    "name":  "David",
    "years": "PhD",
    "role":  "Events & Outreach",
    "photo": LEADER_5_PHOTO,
}
LEADER_6 = {
    "name":  "Shen",
    "years": "PhD",
    "role":  "Matching and Admin",
    "photo": LEADER_6_PHOTO,
}

# Committee members in display order.  Scene 4 shows them in batches of 3:
# LEADERS[0:3] first, then LEADERS[3:6].
LEADERS: list = [LEADER_1, LEADER_2, LEADER_3, LEADER_4, LEADER_5, LEADER_6]

# Each tuple is (quote_text, attribution)
QUOTES: list = [
    (
        '"I saw it as a challenge for myself, to study new topics independently\n and then explain clearly to others.\nIt was a unique chance to explore topics in depth with peers, \ndeveloping collaborative research and discussion skills"',
        '- DRP participant Year 1',

    ),
    (
        '"I’d never been able to find people with similar\ninterests to collaborate and research with \n- this was the perfect opportunity"',
        '- DRP participant Year 3',
    ),
    (
        "The DRP has been really fulfilling and exciting, \ncreating a community in an area I'm passionate about \nand want to pursue in research",
        "- DRP participant Year 4",
    ),
    (
        """The mix of independent curiosity and group learning\n really appealed to me. It was great that there\n weren't any expectations of pre-existing knowledge""",
        '- DRP participant Year 2',
    ),
    (
        '"I got to make friends while exploring mathematics\n - getting to know more people is always a great bonus!"',
        '- DRP participant Year 1',
    ),
]

HIGHLIGHT_WORDS = [
    "challenge",
    "unique",
    "collaborative",
    "perfect opportunity",
    "community",
    "passionate about",
    "independent curiosity",
    "any expectations",
    "make friends",
    "great bonus",
]

CONTACT_EMAIL   = "rohan.shenoy22@imperial.ac.uk"
CONTACT_WEBSITE = "sites.google.com/view/imperial-drp"


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 – DESIGN TOKENS  (colours & global sizes)
# ══════════════════════════════════════════════════════════════════════════════

IMP_BLUE = "#003E74"   # Imperial College blue
IMP_NAVY = "#001A3A"   # Deeper navy used on the closing slide
IMP_GOLD = "#D4AF37"   # Gold accent
ACC_TEAL = "#009CBC"   # Teal accent
BG_DARK  = "#08080F"   # Near-black global background


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 – TOPIC & CLUSTER DATA
# ══════════════════════════════════════════════════════════════════════════════

# (label shown on screen,  colour,  grid-index 0-based left→right, top→bottom)
# Grid is TOPICS_COLS wide; add rows freely.
TOPICS_COLS = 4
TOPICS_DATA: list = [
    ("Geometry &\nTopology",   BLUE,   0),
    ("Category\nTheory",        PURPLE, 1),
    ("Number\nTheory",          RED,    2),
    ("Quantitative\nFinance",   GREEN,  3),
    ("Fluids",                  TEAL,   4),
    ("ML / AI",                 ORANGE, 5),
    ("Optimal\nTransport",      PINK,   6),
    ("PDEs",                    YELLOW, 7),
]

# Pre-set cluster centres for Scene 2's dot-clustering animation.
# Arranged in a loose ring across the frame; add/remove to match group count.

# put cluster centres into a ellipse around the origin with no noise
CLUSTER_CENTRES: list = []
num_clusters = 10
for i in range(num_clusters):
    angle = 2 * PI * i / num_clusters
    x = 4.8 * np.cos(angle)
    y = 2.7 * np.sin(angle)-0.6
    CLUSTER_CENTRES.append(np.array([x, y, 0]))

# CLUSTER_CENTRES: list = [
#     np.array([-4.8,  1.4, 0]),
#     np.array([-2.4,  2, 0]),
#     np.array([ 0.2,  2.2, 0]),
#     np.array([ 2.8,  2.1, 0]),
#     np.array([ 4.9,  0.7, 0]),
#     np.array([ 4.5, -1.2, 0]),
#     np.array([ 1.7, -2.2, 0]),
#     np.array([-1.3, -2.5, 0]),
#     np.array([-4.0, -1.8, 0]),
#     np.array([-5.1, -0.1, 0]),
# ]
# CLUSTER_COLORS: list = [
#     BLUE, TEAL, GREEN, BLUE, TEAL, GREEN, BLUE, TEAL, GREEN, TEAL_D,
# ]

CLUSTER_COLORS: list = [
    PURPLE, TEAL, BLUE, YELLOW, GREEN, PURPLE, TEAL, BLUE, YELLOW, GREEN,
]


# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 – MAIN SCENE CLASS
# ══════════════════════════════════════════════════════════════════════════════

class DRPAdvertisement(ThreeDScene):
    """
    Imperial College London – Directed Reading Programme advertisement.

    Approx. pure-animation runtime: ~90 seconds.
    With voice-over pauses:         ~2½–3 minutes.
    """

    # ─────────────────────────────────────────────────────────────
    # TOP-LEVEL ORCHESTRATION
    # ─────────────────────────────────────────────────────────────

    def construct(self):
        self.camera.background_color = BLACK

        self.scene_1_welcome()
        self._fade_all()

        self.scene_1_5_why_we_started_the_drp()
        self._fade_all()

        self.scene_2_what_is_drp()
        self._fade_all()

        self.scene_3_topics()
        self._fade_all()

        self.scene_4_how_it_works()
        self._fade_all()

        self.scene_5_symposium()
        self._fade_all()

        self.scene_6_outcomes()
        self._fade_all()

        self.scene_7_closing()

    # ─────────────────────────────────────────────────────────────
    # SHARED UTILITIES
    # ─────────────────────────────────────────────────────────────

    def _fade_all(self, run_time: float = 0.5) -> None:
        """Fade every visible mobject to black between scenes."""
        if self.mobjects:
            self.play(FadeOut(*self.mobjects), run_time=run_time)

    def _safe_image(
        self,
        path: str,
        width: float = 3.0,
        fallback: str = "[image]",
    ) -> Mobject:
        """
        Load an image; return a labelled placeholder rectangle if the file is
        missing so the script always renders even before real assets exist.
        """
        try:
            return ImageMobject(path).set_width(width)
        except Exception:
            box = Rectangle(
                width=width, height=width * 0.65,
                fill_color=GRAY_D, fill_opacity=0.25,
                stroke_color=GRAY_C, stroke_width=2,
            )
            lbl = Text(
                fallback,
                font_size=max(11, int(width * 5.5)),
                color=GRAY_C,
            ).move_to(box)
            return VGroup(box, lbl)

    def _section_banner(self, text: str, bg_color: str = BLACK, font_size = 50) -> VGroup:
        """Coloured title banner pinned to the top of the frame."""
        lbl = Text(text, font_size=font_size, color=WHITE, weight=BOLD).to_edge(UP, buff=0.5)
        return VGroup(lbl)

    def _gold_rule(self, width: float = 8.0) -> Line:
        """Horizontal decorative gold separator line."""
        return Line(
            LEFT * width / 2, RIGHT * width / 2,
            color=IMP_GOLD, stroke_width=2.5,
        )

    # ─────────────────────────────────────────────────────────────
    # COMMITTEE CARD FACTORIES  (used by scene 4)
    # ─────────────────────────────────────────────────────────────

    def _leader_card(self, leader: dict) -> Group:
        """One committee-member card: photo + name / year / role on a rounded box."""
        photo  = self._safe_image(leader["photo"], width=2.4, fallback="Photo")
        name_t = Text(leader["name"],  font_size=30, color=WHITE,   weight=BOLD)
        year_t = Text(leader["years"], font_size=23, color=YELLOW)
        role_t = Text(leader["role"],  font_size=15, color=GRAY_A)
        info   = VGroup(name_t, year_t, role_t).arrange(DOWN, buff=0.1)
        inner  = Group(photo, info).arrange(DOWN, buff=0.18)

        bg = RoundedRectangle(
            corner_radius=0.2,
            width  = inner.get_width()  + 0.55,
            height = inner.get_height() + 0.45,
            fill_color=BLACK, fill_opacity=0.45,
            stroke_color=IMP_GOLD, stroke_width=1.8,
        ).move_to(inner)
        return Group(bg, inner)

    def _leader_row(self, leaders: list) -> Group:
        """A horizontally-arranged row of committee cards, in the order given."""
        # Use Group (not VGroup) because ImageMobject is not a VMobject.
        row = Group(*[self._leader_card(l) for l in leaders])
        row.arrange(RIGHT, buff=1.0).shift(UP * 0.62)
        return row

    # ─────────────────────────────────────────────────────────────
    # TOPIC VISUAL FACTORIES
    # ─────────────────────────────────────────────────────────────

    def _build_topic_visual(self, topic: str, color) -> Mobject:
        """
        Build the animated Mobject for each mathematical topic.

        Internal structure of each returned VGroup is documented so that
        ``_animate_topic_entrance`` can unpack sub-elements correctly.
        """

        # ── Topology: 3-D torus ───────────────────────────────────────────
        if "Topology" in topic:
            torus = Torus(major_radius=0.55, minor_radius=0.22).set_color(color)
            torus.rotate(PI / 4, UP).rotate(PI / 4, RIGHT).scale(0.65)
            return torus  # single surface Mobject

        # ── Category Theory: commutative diagram ─────────────────────────
        if "Category" in topic:
            dots = VGroup(*[Dot(color=color, radius=0.045) for _ in range(4)])
            dots.arrange_in_grid(rows=2, cols=2, buff=0.7)
            arrows = VGroup(
                Arrow(dots[0], dots[1], buff=0.08, color=color,
                      stroke_width=2.5, max_tip_length_to_length_ratio=0.2),
                Arrow(dots[0], dots[2], buff=0.08, color=color,
                      stroke_width=2.5, max_tip_length_to_length_ratio=0.2),
                Arrow(dots[1], dots[3], buff=0.08, color=color,
                      stroke_width=2.5, max_tip_length_to_length_ratio=0.2),
                Arrow(dots[2], dots[3], buff=0.08, color=color,
                      stroke_width=2.5, max_tip_length_to_length_ratio=0.2),
            )
            return VGroup(dots, arrows).scale(0.85)  # [0]=dots, [1]=arrows

        # ── Number Theory: Archimedean spiral ────────────────────────────
        if "Number" in topic:
            return (
                ParametricFunction(
                    lambda t: np.array([
                        0.27 * t * np.cos(2 * PI * t),
                        0.27 * t * np.sin(2 * PI * t),
                        0,
                    ]),
                    t_range=[0, 3],
                    color=color,
                    stroke_width=3,
                )
                .scale(0.8)
                .rotate(PI / 6, RIGHT)
                .rotate(PI / 6, UP)
            )  # single ParametricFunction

        # ── Quantitative Finance: stock-price chart ───────────────────────
        if "Quant" in topic or "Finance" in topic:
            axes = Axes(
                x_range=[0, 5, 1], y_range=[-1, 1, 1],
                x_length=1.8, y_length=1.1,
                axis_config={"include_tip": False, "stroke_width": 1.8},
            ).set_color(color)
            graph = axes.plot(
                lambda x: 0.4 * np.sin(3 * x) + 0.3 * np.cos(5 * x),
                color=color, stroke_width=2.5,
            )
            return VGroup(axes, graph).scale(0.65)  # [0]=axes, [1]=graph

        # ── Fluids: parallel flow arrows ─────────────────────────────────
        if "Fluid" in topic:
            return VGroup(*[
                Arrow(
                    LEFT * 0.75 + UP * y, RIGHT * 0.75 + UP * y,
                    buff=0, stroke_width=2.5, color=color,
                    max_tip_length_to_length_ratio=0.15,
                )
                for y in np.linspace(-0.45, 0.45, 5)
            ]).scale(0.9)  # iterable VGroup of Arrow objects

        # ── AI / ML: three-layer neural network ──────────────────────────
        if "AI" in topic or "ML" in topic:
            def _layer(x_off: float, n: int) -> VGroup:
                return VGroup(*[
                    Dot(radius=0.09, color=color).shift(
                        UP * (i - (n - 1) / 2) * 0.38 + RIGHT * x_off
                    )
                    for i in range(n)
                ])

            l1, l2, l3 = _layer(-0.55, 3), _layer(0.0, 4), _layer(0.55, 3)
            conns = VGroup()
            for src, dst in [(l1, l2), (l2, l3)]:
                for a in src:
                    for b in dst:
                        conns.add(Line(
                            a.get_center(), b.get_center(),
                            stroke_width=0.9, stroke_opacity=0.5, color=color,
                        ))
            return VGroup(conns, l1, l2, l3).scale(0.8)  # [0]=conns, [1-3]=layers

        # ── Optimal Transport: mass-transport diagram ─────────────────────
        if "Optimal" in topic or "Transport" in topic:
            rng = np.random.default_rng(42)
            left_pts = VGroup(*[
                Dot(radius=0.035, color=color).move_to(np.array([
                    -0.5 + float(rng.uniform(-0.18, 0.18)),
                    float(rng.normal(0, 0.18)), 0,
                ]))
                for _ in range(16)
            ])
            right_pts = VGroup(*[
                Dot(radius=0.035, color=color).move_to(np.array([
                    0.5 + float(rng.uniform(-0.18, 0.18)),
                    float(rng.normal(0, 0.18)), 0,
                ]))
                for _ in range(16)
            ])
            arrows = VGroup(*[
                Arrow(
                    left_pts[i].get_center(), right_pts[i].get_center(),
                    buff=0.04, stroke_width=1.5, color=color,
                    stroke_opacity=0.4, max_tip_length_to_length_ratio=0.04,
                )
                for i in range(16)
            ])
            return VGroup(left_pts, arrows, right_pts).scale(0.9)
            # [0]=left_pts, [1]=arrows, [2]=right_pts

        # ── PDEs: heat-equation bell-curve surface ────────────────────────
        if "PDE" in topic:
            surf = Surface(
                lambda u, v: np.array([u, v, 1.8 * np.exp(-(u**2 + v**2) / 0.55)]),
                u_range=[-1.5, 1.5], v_range=[-1.5, 1.5],
                resolution=(14, 14), fill_opacity=0.55,
            ).set_color(color).scale(0.38)
            surf.rotate(-PI / 2 - 0.1, RIGHT)
            return surf  # single Surface Mobject

        return VGroup()  # ← fallback for any topic not listed above

    def _animate_topic_entrance(self, topic: str, visual: Mobject) -> None:
        """
        Drive the entrance animation for one topic cell.
        Mirrors the VGroup structure documented in ``_build_topic_visual``.
        """
        t_fast, t_main = 0.25 , 0.5

        if "Topology" in topic:
            self.play(FadeIn(visual, scale=0.7), run_time=t_fast)
            self.play(Rotate(visual, PI, axis=UP + RIGHT), run_time=t_main)

        elif "Category" in topic:
            dots, arrows = visual[0], visual[1]
            self.play(FadeIn(dots, scale=0.8), run_time=t_fast)
            self.play(
                LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.18),
                run_time=t_main,
            )

        elif "Number" in topic:
            self.play(Create(visual), run_time=t_fast + t_main)

        elif "Quant" in topic or "Finance" in topic:
            axes, graph = visual[0], visual[1]
            self.play(FadeIn(axes), run_time=t_fast)
            self.play(Create(graph), run_time=t_main)

        elif "Fluid" in topic:
            self.play(
                LaggedStart(*[GrowArrow(a) for a in visual], lag_ratio=0.12),
                run_time=t_fast + t_main,
            )

        elif "AI" in topic or "ML" in topic:
            conns, l1, l2, l3 = visual[0], visual[1], visual[2], visual[3]
            for layer in (l1, l2, l3):
                self.play(FadeIn(layer, scale=0.8), run_time=t_fast)
            self.play(
                LaggedStart(*[Create(c) for c in conns], lag_ratio=0.01),
                run_time=t_main,
            )

        elif "Optimal" in topic or "Transport" in topic:
            left, arrows, right = visual[0], visual[1], visual[2]
            self.play(FadeIn(left, scale=0.8), run_time=t_main)
            self.play(
                LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2),
                LaggedStart(*[FadeIn(d, scale=0.5) for d in right], lag_ratio=0.2),
                run_time=t_main,
            )

        elif "PDE" in topic:
            self.play(FadeIn(visual, scale=0.8), run_time=t_fast)
            self.play(Rotate(visual, 3 * PI / 4, axis=UP), run_time=t_main + t_fast)

        else:
            self.play(FadeIn(visual), run_time=t_fast + t_main)

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 1 – WELCOME
    # ═══════════════════════════════════════════════════════════════════

    def scene_1_welcome(self) -> None:
        """
        VOICEOVER:
            "Welcome to the Imperial College London Directed Reading Programme –
             a community built on the belief that we learn better together."

        Approx. animation time: ~8 s
        """
        # ── Starfield background ─────────────────────────────────────────────
        # rng = np.random.default_rng(0)
        # stars = VGroup(*[
        #     Dot(
        #         radius=float(rng.uniform(0.01, 0.04)),
        #         color=WHITE,
        #         fill_opacity=float(rng.uniform(0.15, 0.85)),
        #     ).move_to(np.array([
        #         float(rng.uniform(-7.2, 7.2)),
        #         float(rng.uniform(-4.2, 4.2)),
        #         0,
        #     ]))
        #     for _ in range(140)
        # ])
        # self.add(stars)

        # ── Logo ─────────────────────────────────────────────────────────────
        # scale up logo entrance with a slight overshoot for a more dynamic feel
        logo = self._safe_image(LOGO_PATH, width=7.6, fallback="DRP  Logo")
        logo.shift(UP * 1)

        # ── Titles ───────────────────────────────────────────────────────────
        title = VGroup(
            Text("Celebrate Collaboration!", font_size=46, color=YELLOW,    weight=BOLD),
        ).arrange(DOWN, buff=0.08).next_to(logo, DOWN, buff=1.5)

        # institution = Text("Imperial College London", font_size=22, color=GOLD)
        # institution.next_to(title, DOWN, buff=0.18)

        # rule = self._gold_rule(5.5).next_to(institution, DOWN, buff=0.22)

        # motto = Text(
        #     "Celebrate Collaboration !",
        #     font_size=24, color=ACC_TEAL, slant=ITALIC,
        # ).next_to(rule, DOWN, buff=0.22)

        # ── Animations ───────────────────────────────────────────────────────
        # self.play(FadeIn(stars), run_time=0.6)
        self.play(FadeIn(logo, scale=0.8), run_time=1)
        self.wait(1)
        self.play(
            Write(title),
            # FadeIn(institution, shift=UP * 0.2),
            run_time=1,
        )
        # self.play(Create(rule), run_time=0.55)
        # self.play(FadeIn(motto, shift=UP * 0.15), run_time=0.8)
        self.wait(1)

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 1.5 – WHY WE STARTED THE DRP
    # ═══════════════════════════════════════════════════════════════════

    def scene_1_5_why_we_started_the_drp(self) -> None:
        """
        VOICEOVER:
            "The DRP was born from a simple idea: that students learn better
             together. We wanted to create a space where curious minds could
             connect, collaborate, and explore advanced mathematics beyond the
             standard curriculum."

        Approx. animation time: ~10 s
        """

        # Big quote at the top, 'great minds think alike', where the text then animates to instead say 'great minds _dont_ think alike'
        

        quote = Text(
            '"Great minds think alike."',
            font_size=40, color=WHITE, slant=ITALIC,
        ).to_edge(ORIGIN)
        self.play(FadeIn(quote, shift=UP * 0.25), run_time=1)

        self.wait(1)

        correction = Text(
            '"Great minds don\'t think alike."',
            font_size=40, color=ACC_TEAL, slant=ITALIC,
        ).move_to(quote)
        self.play(Transform(quote, correction), run_time=1.0)
        # move this up a bit to make room for the follow-up text
        self.wait(1)
        self.play(quote.animate.to_edge(UP + LEFT, buff=1), run_time=1)
        # self.play(
        #     quote.animate.to_edge(UP + LEFT, buff=1),
        #     run_time=0.8,
        # )

        founders_photo = self._safe_image(FOUNDERS_PHOTO, width=4.5, fallback="Founders' Photo")
        founders_photo.to_edge(UP + RIGHT, buff=0.8)
        self.play(FadeIn(founders_photo, shift=UP * 0.25), run_time=1)
        # put (centred)caption under the picture
        caption = Text(
            'Ariff (Left) and Shen (Right)',
            font_size=18, color=YELLOW,
        ).next_to(founders_photo, DOWN, buff=0.2)
        caption_2= Text(
            'DRP Co-Founders (August 2024)',
            font_size=18, color=YELLOW,
        ).next_to(caption, DOWN, buff=0.2)

        self.play(Write(caption), run_time=0.5)
        self.play(Write(caption_2), run_time=0.5)

        lines = [
            "This is the ethos cementing the DRP - our department here ",
            "is one of the most supportive, diverse and encouraging ",
            "places to be ...",]
        lines_2 = [
            "We want to celebrate that!",]
        lines_3 = [
            "The goal is to provide an environment where ",
            "collaborative Mathematics can thrive.",
        ]

        follow_up = VGroup(*[
            Text(
                line,
                font_size=25 if "celebrate that!" not in line else 35,
                color=YELLOW if "celebrate that!" in line else WHITE,
                weight=BOLD if "celebrate that!" in line else NORMAL,
            )
            for line in lines
        ]).arrange(DOWN, buff=0.22, aligned_edge=ORIGIN)

        follow_up.move_to(LEFT * 2.5 + UP * 1)

        follow_up_2 = VGroup(*[
            Text(
                line,
                font_size=25 if "celebrate that!" not in line else 35,
                color=YELLOW if "celebrate that!" in line else WHITE,
                weight=BOLD if "celebrate that!" in line else NORMAL,
            )
            for line in lines_2
        ]).arrange(DOWN, buff=0.22, aligned_edge=ORIGIN)

        follow_up_2.move_to(follow_up.get_center() + DOWN * 1.5)

        follow_up_3 = VGroup(*[
            Text(
                line,
                font_size=25 if "collaborative Mathematics" not in line else 35,
                color=TEAL if "collaborative Mathematics" in line else WHITE,
                weight=BOLD if "collaborative Mathematics" in line else NORMAL,
            )
            for line in lines_3
        ]).arrange(DOWN, buff=0.22, aligned_edge=ORIGIN)

        follow_up_3.move_to(follow_up_2.get_center() + DOWN * 1.5)

        self.play(
            LaggedStart(
                *[FadeIn(line) for line in follow_up],
                lag_ratio=0.3
            ),
            run_time=2
        )
        
        self.wait(1)

        self.play(
            LaggedStart(
                *[Write(line) for line in follow_up_2],
                lag_ratio=0.2
            ),
            run_time=1
        )

        self.wait(1)

        self.play(
            LaggedStart(
                *[FadeIn(line) for line in follow_up_3],
                lag_ratio=0.3
            ),
            run_time=2
        )

        self.wait(2)
        

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 2 – WHAT IS THE DRP?
    # ═══════════════════════════════════════════════════════════════════

    def scene_2_what_is_drp(self) -> None:
        """
        VOICEOVER:
            "This year, over 200 students formed 40 reading groups to explore
             advanced mathematics together – each matched by shared interests
             and the ambition to go beyond the standard curriculum."

        Animation sequence:
          1. Coloured dots scattered randomly across the frame
          2. Dots cluster into groups (matching)
          3. Clusters morph into circle nodes
          4. Graph edges connect the nodes
          5. Stats text fades in

        Approx. animation time: ~14 s
        """
        NUM_GROUPS   = len(CLUSTER_CENTRES)
        DOTS_PER_GRP = 13
        rng = np.random.default_rng(31)

        title = self._section_banner("We match students with like-minded interests together", font_size=25)
        title2 = self._section_banner("to learn new topics together as a group", font_size=25).next_to(title, DOWN, buff=0.1)
        self.play(Write(title), run_time=0.5)
        self.play(Write(title2), run_time=0.5)

        self.wait(1)

        # ── Phase 1: scatter dots randomly ──────────────────────────────────
        all_dots    = VGroup()
        dot_targets = []   # list of (Dot, target_np_array)

        for g in range(NUM_GROUPS):
            colour = CLUSTER_COLORS[g]
            centre = CLUSTER_CENTRES[g]
            for _ in range(DOTS_PER_GRP):
                start = np.array([
                    float(rng.uniform(-6.8, 6.8)),
                    float(rng.uniform(-3.6, 2.9)),
                    0,
                ])
                target = centre + np.array([
                    float(rng.uniform(-0.27, 0.27)),
                    float(rng.uniform(-0.27, 0.27)),
                    0,
                ])
                dot = Dot(radius=0.05, color=colour, fill_opacity=0.8).move_to(start)
                all_dots.add(dot)
                dot_targets.append((dot, target))

        self.play(FadeIn(all_dots), run_time=0.4)
        self.wait(0.3)

        # ── Phase 2: cluster dots toward their group centres ─────────────────
        self.play(
            LaggedStart(
                *[dot.animate.move_to(tgt) for dot, tgt in dot_targets],
                lag_ratio=0.02,
            ),
            run_time=4,
        )

        # ── Phase 3: shrink dot clouds → grow circle nodes ───────────────────
        circles = VGroup(*[
            Circle(
                radius=0.48,
                color=CLUSTER_COLORS[g],
                stroke_width=2.8,
                fill_color=CLUSTER_COLORS[g],
                fill_opacity=0.14,
            ).move_to(CLUSTER_CENTRES[g])
            for g in range(NUM_GROUPS)
        ])

        cluster_dot_groups = [
            VGroup(*[
                dot_targets[g * DOTS_PER_GRP + d][0]
                for d in range(DOTS_PER_GRP)
            ])
            for g in range(NUM_GROUPS)
        ]

        self.play(
            LaggedStart(*[FadeOut(gd, scale=0.2) for gd in cluster_dot_groups],
                        lag_ratio=0.07),
            LaggedStart(*[GrowFromCenter(c) for c in circles],
                        lag_ratio=0.07),
            run_time=1.5,
        )

        # ── Phase 4: draw sparse graph edges between nodes ───────────────────
        edges: VGroup   = VGroup()
        seen_pairs: set = set()
        rng2 = np.random.default_rng(13)

        for g in range(NUM_GROUPS):
            candidates = [h for h in range(NUM_GROUPS) if h != g]
            shuffled   = rng2.permutation(candidates)
            n_connect  = int(rng2.integers(2, 4))
            for h in shuffled[:n_connect]:
                pair = (min(g, h), max(g, h))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    edges.add(Line(
                        CLUSTER_CENTRES[g], CLUSTER_CENTRES[h],
                        color=WHITE, stroke_opacity=0.22, stroke_width=1.3,
                    ))

        self.play(
            LaggedStart(*[Create(e) for e in edges], lag_ratio=0.05),
            run_time=1.0,
        )

        self.wait(0.5)

        # ── Phase 5: dim graph, reveal headline statistics ───────────────────
        stats = VGroup(
            Text("This year we had 200+ students", font_size=26, color=YELLOW, weight=BOLD),
            Text("across 40 reading groups", font_size=26, color=WHITE),
            Text("learning advanced mathematics together!",
                 font_size=26, color=GRAY_A),
        ).to_edge(ORIGIN).arrange(DOWN, buff=0.2)

        self.play(
            *[c.animate.set_stroke(opacity=0.32) for c in circles],
            edges.animate.set_stroke(opacity=0.09),
            run_time=0.5,
        )
        self.play(Write(stats), run_time=0.9)
        self.wait(1.5)

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 3 – TOPICS
    # ═══════════════════════════════════════════════════════════════════

    def scene_3_topics(self) -> None:
        """
        VOICEOVER:
            "Our groups span a rich spectrum of modern mathematics –
             from topology and category theory, to AI, fluids, and
             quantitative finance."

        Approx. animation time: ~26 s  (8 topics × ~3.2 s each)
        """
        title = self._section_banner("Some topics covered last year !")
        self.play(Write(title), run_time=1)

        self.wait(1)

        COL_STEP = 3.5
        ROW_STEP = 2.38

        for topic, color, idx in TOPICS_DATA:
            col = idx % TOPICS_COLS
            row = idx // TOPICS_COLS

            # Centre the grid horizontally
            cx = col * COL_STEP - COL_STEP * (TOPICS_COLS - 1) / 2
            cy = -row * ROW_STEP + 0.55

            label = Text(topic, font_size=21, color=color, weight=BOLD)
            label.move_to(np.array([cx, cy + 1, 0]))

            visual = self._build_topic_visual(topic, color)
            visual.move_to(np.array([cx, cy - 0.08, 0]))

            self.play(Write(label), run_time=0.5)
            self._animate_topic_entrance(topic, visual)

        # Text at the bottom 'And many more !'
        more_text = Text("And many more !", font_size=24, color=YELLOW, weight=BOLD)
        more_text.to_edge(DOWN, buff=0.6)
        self.play(Write(more_text), run_time=1.5)

        self.wait(2)

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 4 – HOW IT WORKS
    # ═══════════════════════════════════════════════════════════════════

    def scene_4_how_it_works(self) -> None:
        """
        VOICEOVER:
            "Six student committee members handle all the matchmaking – pairing
             participants by shared interests into an environment where
             curiosity and collaboration can truly flourish.
             Students give us their preferences; we give them a community
             of like-minded individuals to grow with."

        Timeline (TOTAL = 9.5 s, identical to the original 2-person version):
            0.0 – 0.5   title writes
            0.5 – 1.5   committee batch 1 (members 1-3) fades in  + gold rule draws
            1.5 – 5.5   process text writes (batch 1 stays on screen)
            5.5 – 6.5   batch 1 -> batch 2 (members 4-6) swap
            6.5 – 9.5   hold (batch 2 + process text on screen)
        """
        title = self._section_banner("Meet the team !")
        self.play(Write(title), run_time=0.5)                                   # 0.5

        # ── Committee cards: two batches of three ────────────────────────────
        batch1 = self._leader_row(LEADERS[0:3])
        batch2 = self._leader_row(LEADERS[3:6])

        rule = self._gold_rule(9.5).shift(DOWN * 1.8)

        # Batch 1 fades in while the gold rule is drawn (same 1.0 s window).
        self.play(
            LaggedStart(*[FadeIn(c, shift=UP * 0.3) for c in batch1], lag_ratio=0.5),
            Create(rule),
            run_time=1.0,                                                       # 1.5
        )

        # ── Process text ─────────────────────────────────────────────────────
        STEPS = [
            ("You tell us what you'd like to learn, and we'll match you with a group of like-minded peers!"),
            ("All levels of experience are welcome: from year 1 UG to PhD students,"),
            ("there's a group for you!")
        ]
        step_mobs = VGroup(*[
            VGroup(
                Text(txt, font_size=23 if 'for you' not in txt else 30, color=WHITE if 'for you' not in txt else YELLOW, weight=BOLD if 'for you' in txt else NORMAL),
            ).arrange(RIGHT, buff=0.22)
            for txt in STEPS
        ]).arrange(DOWN, aligned_edge=ORIGIN, buff=0.24).shift(DOWN * 2.9)

        self.play(
            LaggedStart(*[Write(s) for s in step_mobs],
                        lag_ratio=0.66),
            run_time=4,                                                         # 5.5
        )

        # ── Swap batch 1 -> batch 2 ──────────────────────────────────────────
        self.play(
            LaggedStart(*[FadeOut(c, shift=UP * 0.15) for c in batch1], lag_ratio=0.15),
            LaggedStart(*[FadeIn(c, shift=UP * 0.3)   for c in batch2], lag_ratio=0.15),
            run_time=1.0,                                                       # 6.5
        )

        self.wait(3)                                                            # 9.5

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 5 – SYMPOSIUM
    # ═══════════════════════════════════════════════════════════════════

    def scene_5_symposium(self) -> None:
        """
        VOICEOVER:
            "Each year the DRP culminates in our Symposium – an open celebration
             where students present everything they have learnt to peers,
             academics, and the wider Imperial community.
             A great opportunity to share the joy of mathematics."

        Approx. animation time: ~11 s
        """
        title = self._section_banner("The Symposium")
        self.play(Write(title), run_time=0.5)

        headline = Text(
            "A Celebration of Mathematics & Collaboration",
            font_size=27, color=YELLOW, weight=BOLD,
        ).shift(UP * 2.5)
        desc = Text(
            "100+ Students presented their projects to the Imperial community !",
            font_size=25, color=WHITE,
        ).next_to(headline, DOWN, buff=0.25)

        self.play(FadeIn(headline, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(desc), run_time=0.5)

        # ── Photo grid – first batch ─────────────────────────────────────────
        PHOTO_POSITIONS = [LEFT * 4.25, ORIGIN, RIGHT * 4.25]
        PHOTO_WIDTH     = 4
        ROW_OFFSET      = DOWN * 0.72

        def _photo_row(paths: list, labels: list) -> Group:
            # Group (not VGroup) since ImageMobject is not a VMobject.
            row = Group()
            for pos, path, lbl in zip(PHOTO_POSITIONS, paths, labels):
                img = self._safe_image(path, width=PHOTO_WIDTH, fallback=lbl)
                img.move_to(pos + ROW_OFFSET)
                row.add(img)
            return row

        batch1 = _photo_row(SYMPOSIUM_PHOTOS[:3], ["Photo 1", "Photo 2", "Photo 3"])
        self.play(
            LaggedStart(*[FadeIn(p, scale=0.85) for p in batch1], lag_ratio=0.22),
            run_time=1.0,
        )

        callout = Text(
            "We have an amazingly open and inclusive community, celebrating the joy of learning together!",
            font_size=25, color=BLUE,
        ).to_edge(DOWN, buff=1)
        self.play(Write(callout), run_time=1)

        self.wait(1)

        # ── Photo grid – second batch (cross-fade) ───────────────────────────
        if len(SYMPOSIUM_PHOTOS) >= 6:
            batch2 = _photo_row(
                SYMPOSIUM_PHOTOS[3:6], ["Photo 4", "Photo 5", "Photo 6"]
            )
            self.play(
                LaggedStart(*[FadeOut(p, scale=0.9) for p in batch1], lag_ratio=0.1),
                LaggedStart(*[FadeIn(p,  scale=0.85) for p in batch2], lag_ratio=0.18),
                run_time=1,
            )
            self.wait(1)

        if len(SYMPOSIUM_PHOTOS) >= 9:
            batch3 = _photo_row(
                SYMPOSIUM_PHOTOS[6:9], ["Photo 7", "Photo 8", "Photo 9"]
            )
            self.play(
                LaggedStart(*[FadeOut(p, scale=0.9) for p in batch2], lag_ratio=0.1),
                LaggedStart(*[FadeIn(p,  scale=0.85) for p in batch3], lag_ratio=0.18),
                run_time=1,
            )
            self.wait(1)

        if len(SYMPOSIUM_PHOTOS) >= 12:
            batch4 = _photo_row(
                SYMPOSIUM_PHOTOS[9:12], ["Photo 10", "Photo 11", "Photo 12"]
            )
            self.play(
                LaggedStart(*[FadeOut(p, scale=0.9) for p in batch3], lag_ratio=0.1),
                LaggedStart(*[FadeIn(p,  scale=0.85) for p in batch4], lag_ratio=0.18),
                run_time=1,
            )
            self.wait(1)

        self.wait(1.0)

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 6 – OUTCOMES
    # ═══════════════════════════════════════════════════════════════════

    def scene_6_outcomes(self) -> None:
        """
        VOICEOVER:
            "The impact extends well beyond the end of term.
            Some groups go on to produce original research –
            and here is what past participants have to say."

        Approx. animation time: ~13 s
        """
        title = self._section_banner("The DRP Experience !")
        self.play(Write(title), run_time=0.5)

        self.wait(0.5)

        # ── Quote carousel ────────────────────────────────────────────────────
        for i, (q_text, q_attr) in enumerate(QUOTES):

            # Split into lines
            lines = q_text.split("\n")

            # Create centered line-by-line text
            text_lines = VGroup(*[
                Text(
                    line,
                    font_size=35,
                    color=WHITE,
                    slant=ITALIC,
                    t2c={word: BLUE for word in HIGHLIGHT_WORDS},
                    t2w={word: BOLD for word in HIGHLIGHT_WORDS},
                )
                for line in lines
            ]).arrange(DOWN, center=True, aligned_edge=ORIGIN, buff=0.2)

            text_lines.move_to(ORIGIN)

            # Attribution
            block2 = Text(q_attr, font_size=20, color=YELLOW)
            block2.next_to(text_lines, DOWN, buff=0.4)

            # Animate lines sequentially
            for line in text_lines:
                self.play(Write(line), run_time=0.5)

            # Fade in attribution
            self.play(FadeIn(block2, shift=DOWN * 0.15), run_time=0.5)

            self.wait(3)

            # Fade out everything (except last quote)
            if i < len(QUOTES) - 1:
                self.play(
                    LaggedStart(
                        FadeOut(text_lines, shift=UP * 0.15),
                        FadeOut(block2, shift=UP * 0.15),
                        lag_ratio=0.0
                    ),
                    run_time=0.5,
                )

    # ═══════════════════════════════════════════════════════════════════
    # SCENE 7 – CLOSING
    # ═══════════════════════════════════════════════════════════════════

    def scene_7_closing(self) -> None:
        """
        VOICEOVER:
            "We look forward to seeing what next year's groups will discover.
             We would love to hear from you!"

        Approx. animation time: ~9 s
        """
        # Full-frame deep-navy background
        bg = Rectangle(
            width=16, height=10,
            fill_color=BLACK, fill_opacity=1, stroke_width=0,
        )
        self.add(bg)

        # ── Logo ─────────────────────────────────────────────────────────────
        logo = self._safe_image(LOGO_PATH, width=7, fallback="DRP  Logo")
        logo.to_edge(ORIGIN)
        self.play(FadeIn(logo, scale=1.5), run_time=1.0, rate_func=smooth)

        self.wait(1)

        # move logo up to top and shrink it a bit to make room for the main message
        self.play(
            logo.animate.to_edge(UP, buff=0.8).scale(0.85),
            run_time=1,
        )

        self.wait(0.5)

        # ── Main message ─────────────────────────────────────────────────────
        msg = VGroup(
            Text("Looking forward to seeing what you can achieve!",       font_size=38, color=BLUE, weight=BOLD),
        ).next_to(logo, DOWN, buff=0.6).shift(UP *0.22)
        self.play(Write(msg), run_time=0.5)

        # self.wait(0.5)

        # ── Gold separator ───────────────────────────────────────────────────
        rule = self._gold_rule(10)
        rule.next_to(msg, DOWN, buff=0.4)
        self.play(Create(rule), run_time=0.48)

        # ── Contact info + QR code ───────────────────────────────────────────
        contact = VGroup(
            # Text(CONTACT_EMAIL,   font_size=20, color=WHITE),
            Text(CONTACT_WEBSITE, font_size=25, color=GRAY_A),
        ).next_to(rule, DOWN, buff=1.3)
        # put contact a bit to the left to make room for the QR code on the right
        contact.shift(LEFT * 0.4)

        # put QR code to the right of the contact info
        qr = self._safe_image(QR_CODE_PATH, width=1.9, fallback="QR Code")
        qr.next_to(contact, RIGHT, buff=0.6)

        self.play(FadeIn(contact), run_time=0.7)
        self.play(FadeIn(qr, shift=RIGHT * 0.3), run_time=0.7)

        # qr = self._safe_image(QR_CODE_PATH, width=1.9, fallback="QR Code")
        # # Group (not VGroup) because qr may be an ImageMobject.
        # contact_row = Group(contact, qr).arrange(RIGHT, buff=0.6)
        # self.play(FadeIn(contact_row), run_time=0.7)

        self.wait(2)
