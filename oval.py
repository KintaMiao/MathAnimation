from manim import *

class Oval(Scene):
    
    def construct(self):
        title = MarkupText(
            "圆锥曲线进行时",
            font="STSong",
            font_size=24,
        )
        subtitle = Text(
            "欢迎来到椭圆的世界",
            font="STSong",
            t2c={
                '椭圆': BLUE,
            },
        )
        VGroup(title, subtitle).arrange(DOWN)
        self.play(
            Write(title),
        )
        self.wait(3)
        self.play(
            Write(subtitle),
        )
        self.wait(3)
        header = MarkupText(
            "椭圆",
            font="STSong",
            font_size=36,
        )
        header.to_corner(UL),
        self.play(
            FadeOut(title),
            Transform(subtitle, header),
        )
        self.wait(3)
        # 开场动画结束

        # 画坐标轴
        axes = Axes(
            x_range=[-5, 5, 1],
            x_length=10,
            y_range=[-3, 3, 1],
            y_length=6,
            axis_config={
                "color": WHITE,
                "font_size": 24,
            },
            tips=True,
        )
        axes_labels = axes.get_axis_labels()
        self.play(Write(axes))
        self.play(Write(axes_labels))

        # 画椭圆
        ellipse_1 = Ellipse(
            width=6,
            height=4,
            color=BLUE,
        )
        self.play(Create(ellipse_1))
        ellipse_1_label = MathTex(
            r"\frac{x^2}{a^2}+\frac{y^2}{b^2}=1",
        ).next_to(ellipse_1, RIGHT)
        self.play(Write(ellipse_1_label))