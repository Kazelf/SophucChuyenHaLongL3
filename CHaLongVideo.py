from manim import *
from math import *

class Video(Scene):
    def construct(self):
        import manimpango

        #Debai----------------------------------------

        defaultfont = 26

        tentruong = Text(
            text="Câu 49. ( Chuyên Hạ Long - Quảng Ninh lần 3 ): ",
            font= "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.45).to_corner(UL).shift(0.3*UP)
        self.play(Write(tentruong))
        self.wait()

        debai1 = Text(
            text= 'Xét các số phức  z, w thỏa mãn',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(UL).shift(0.1*DOWN)
        self.play(Write(debai1))
        
        debai2 = Tex(
            r'$|z-3-2i|+|\overline{z} + 2 + 8i| = \sqrt{61}, \ (w+10)(\overline{w} + 8i )$'
        ).scale(0.7).next_to(debai1)
        self.play(Write(debai2)) 
        
        debai4 = Text(
            text= """có phần thực bằng -32. Giá trị lớn nhất của P = |z + w - 6 - 4i | thuộc khoảng nào? """,
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(UL).shift(0.5*DOWN)
        self.play(Write(debai4), run_time = 2)
        self.wait()

        dapanA=Tex(r'$A. \ (18; 19)$').scale(0.7).to_corner(LEFT).shift(2.3*UP)
        self.play(Write(dapanA))
        dapanB=Tex(r'$B. \ (24; 25)$').scale(0.7).shift(2.3*UP,2*LEFT)
        self.play(Write(dapanB))
        dapanC=Tex(r'$C. \ (19; 20)$').scale(0.7).shift(2.3*UP,2*RIGHT)
        self.play(Write(dapanC))
        dapanD=Tex(r'$D. \ (17; 18)$').scale(0.7).shift(2.3*UP,6*RIGHT)
        self.play(Write(dapanD))

        self.wait(3)

        solution=Text(
            text="Lời giải: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(1.9*UP)     
        self.play(Write(solution))
        self.wait()

        #Loi giai duoi day la loi giai-------------------------

        dkz1 = MathTex(
            r'\bullet \ \ |z-3-2i|+|\overline{z} + 2 + 8i| = \sqrt{61}'
        ).scale(0.7).to_corner(LEFT).shift(1.45*UP)
        self.play(Write(dkz1))

        dkz1trans = MathTex(
            r'\bullet \ \ |z-3-2i|+|z + 2 - 8i| = \sqrt{61}'
        ).scale(0.7).to_corner(LEFT).shift(1.45*UP)
        self.play(Transform(dkz1, dkz1trans))
        self.wait(3)

        dkz2 = MathTex(
            r'M(z), A(3;2), B(-2,8)'
        ).scale(0.7).next_to(dkz1, DOWN).shift(0.1*UP).to_edge(LEFT)
        self.play(Write(dkz2))
        self.wait()

        dkz3 = MathTex(
            r'\Rightarrow MA+MB= \sqrt{61} =AB'
        ).scale(0.7).next_to(dkz2).shift(0.05*UP)
        self.play(Write(dkz3))
        self.wait(3)

        dkz4 =Text(
            text= 'Từ đó suy ra: M thuộc đoạn thẳng AB',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont,
            t2c= {'M thuộc đoạn thẳng AB': RED}
        ).scale(1.05).next_to(dkz3, DOWN).shift(0.1*UP).to_edge(LEFT)
        self.play(Write(dkz4))
        self.wait(3) 

        #Dieu kien cua w 

        dkw1 = MathTex(
            r'\bullet \ \ Re[ \ ( w+10 )( \overline{w}+8i ) \ ]= -32'
        ).scale(0.7).to_corner(LEFT).shift(0.1*DOWN)
        self.play(Write(dkw1))
        self.wait(3)
        
        dkw1trans = MathTex(
            r'\bullet \ \ Re[ \ ( w+10 )( \overline{w}+8i ) \ ] +32=0'
        ).scale(0.7).to_corner(LEFT).shift(0.1*DOWN)
        self.play(Transform(dkw1, dkw1trans))

        CALC1 = Tex(
            r'CALC w=100+0,01i  $\Rightarrow VT=$'
        ).scale(0.7).next_to(dkw1, DOWN).shift(0.1*UP).to_edge(LEFT)
        self.play(Write(CALC1))

        WDichso_1 = MathTex(
            r'11031,9201'
        ).scale(0.7).next_to(CALC1)
        self.play(Write(WDichso_1))
        self.wait()

        WDichso_2 = MathTex(
            r'1 \ \ 10 \ \ 31, \ \ 92 \ \ 01'
        ).scale(0.7).next_to(CALC1)
        self.play(Transform(WDichso_1, WDichso_2))
        self.wait()

        WDichso_3 = MathTex(
            r'x^2 +10x +32 -8y +y^2 =0'
        ).scale(0.7).next_to(WDichso_2, DOWN).shift(0.1*UP, 0.7*RIGHT)
        self.play(Write(WDichso_3))
        self.wait(3)

        WDichso_4 = MathTex(
            r'(x+5)^2 + (y-4)^2 = 9'
        ).scale(0.7).next_to(WDichso_2, DOWN).shift(0.1*UP, 0.3*RIGHT)
        self.play(Transform(WDichso_3, WDichso_4))
        self.wait(2)

        w_module = MathTex(
            r'\Rightarrow |w+5-4i|=3' 
        ).scale(0.7).next_to(WDichso_3, DOWN).shift(0.15*UP, 0.5*LEFT)
        w_module.set_color_by_gradient( BLUE)
        self.play(Write(w_module))
        self.wait(3)

        #Xet max P

        giai1 = MathTex(
            r'\bullet \ \ P= |z+w-6-4i|'
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.play(Write(giai1))
        self.wait(3)

        giai1trans = MathTex(
            r'\bullet \ \ P= |z-(-w+6+4i)|'
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.play(Transform(giai1, giai1trans))
        self.wait(3)

        giai2 = MathTex(
            r'\xrightarrow{\text{u= \ -w+6+4i} \ } \ \ P= |z-u|'
        ).scale(0.7).shift(2*DOWN, 0.2*LEFT)
        self.play(Write(giai2))
        self.wait(5)

        dku1 = MathTex(
            r'\bullet \ \ w=-u+6+4i \Rightarrow |(-u+6+4i)+5-4i|=3 \Rightarrow |u-11|=3'
        ).scale(0.7).to_edge(LEFT).shift(2.5*DOWN)
        dku1[0][30:38].set_color(GREEN)
        self.play(Write(dku1), run_time = 1.5)
        self.wait()
        
        #VẼ ĐỒ THỊ

        axes = Axes(
            x_range=[-3.5,17.5,2],x_length=5,
            y_range=[-4.2,13,2],y_length=4,
            tips=False
        ).shift(4.3*RIGHT,0.2*DOWN)
        pointO = Tex('O').scale(0.5).shift(1.05*DOWN,2.45*RIGHT)

        self.play(
            Create(axes),
            Write(pointO)
        )
        self.wait()

        #Lấy AB ====

        dotA =Dot(axes.coords_to_point(3, 2), color=YELLOW).scale(0.7)
        A_text = Tex('A', color = YELLOW).scale(0.6).next_to(dotA, UP).shift(0.1*DOWN)

        dotB =Dot(axes.coords_to_point(-2, 8), color=YELLOW).scale(0.7)
        B_text = Tex('B', color = YELLOW).scale(0.6).next_to(dotB, UP).shift(0.1*DOWN)

        AB = Line().set_color_by_gradient(RED)
        AB.add_updater(
            lambda mob: mob.put_start_and_end_on(dotA.get_center(), dotB.get_center())
        )

        self.play( Create(dotA), Create(dotB))
        self.play(Write(A_text), Write(B_text))
        self.play(Create(AB))

        #Lấy Đường tròn u

        def c1(t):
            return (3*cos(t) +11, 3*sin(t))
        cir1 = axes.plot_parametric_curve(c1, color=GREEN, t_range=[0, 2 * PI])
        w1_label = MathTex(
            r'(C)', color = GREEN
        ).scale(0.6).next_to(cir1, UP).shift(0.1*DOWN)

        dotI =Dot(axes.coords_to_point(11, 0), color=YELLOW).scale(0.7)
        I_text = Tex('I', color = YELLOW).scale(0.6).next_to(dotI, UP).shift(0.1*DOWN)

        self.play(Create(dotI))
        self.play(Write(I_text))
        self.play(Create(cir1), Write(w1_label))

        self.wait(5)

        #Giai P max
        dotN =Dot(axes.coords_to_point(13.55497495, -1.57229227), color=YELLOW).scale(0.7)
        N_text = Tex('N', color = YELLOW).scale(0.6).next_to(dotN).shift(0.1*LEFT)

        BN = Line().set_color_by_gradient(BLUE_D)
        BN.add_updater(
            lambda mob: mob.put_start_and_end_on(dotB.get_center(), dotN.get_center())
        )

        giaiPmax1 = MathTex(
            r'\bullet \ \ P_{max} = IB+R'
        ).scale(0.7).to_corner(LEFT).shift(3*DOWN)

        self.add(dotN, N_text)
        self.play(
            Create(BN),
            Write(giaiPmax1)
        )
        self.wait(3)

        giaiPmax2 = MathTex(
            r'= \sqrt{(11+2)^2 + (0-8)^2} +3 \approx 18,264...'
        ).scale(0.7).next_to(giaiPmax1)
        giaiPmax2[0][20:29].set_color(YELLOW)
        self.play(Write(giaiPmax2))

        self.wait(1)

        Rect = Rectangle(
            width=1.5,
            height=0.6,
            stroke_color = (BLUE, PURPLE)
        ).shift(3*DOWN,1.9*RIGHT)

        khoanhtron = Circle(
            stroke_color = (RED, ORANGE, YELLOW)
        ).next_to(dapanA, LEFT).scale(0.3).shift(1.4*RIGHT)

        self.play(Create(Rect), Create(khoanhtron))
        self.wait(3)
        