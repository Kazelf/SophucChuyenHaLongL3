from manim import *
from math import *

config.tex_template.add_to_preamble("\\usepackage{pifont}")

class Image(Scene):
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
        self.add(tentruong)

        debai1 = Text(
            text= 'Xét các số phức  z, w thỏa mãn',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(UL).shift(0.1*DOWN)
        self.add(debai1)

        debai2 = Tex(
            r'$|z-3-2i|+|\overline{z} + 2 + 8i| = \sqrt{61}, \ (w+10)(\overline{w} + 8i )$'
        ).scale(0.7).next_to(debai1)
        self.add(debai2) 

        debai4 = Text(
            text= """có phần thực bằng -32. Giá trị lớn nhất của P = |z + w - 6 - 4i | thuộc khoảng nào? """,
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(UL).shift(0.5*DOWN)
        self.add(debai4)

        dapanA=Tex(r'$A. \ (18; 19)$').scale(0.7).to_corner(LEFT).shift(2.3*UP)
        self.add(dapanA)
        dapanB=Tex(r'$B. \ (24; 25)$').scale(0.7).shift(2.3*UP,2*LEFT)
        self.add(dapanB)
        dapanC=Tex(r'$C. \ (19; 20)$').scale(0.7).shift(2.3*UP,2*RIGHT)
        self.add(dapanC)
        dapanD=Tex(r'$D. \ (17; 18)$').scale(0.7).shift(2.3*UP,6*RIGHT)
        self.add(dapanD)

        solution=Text(
            text="Lời giải: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(1.9*UP)     
        self.add(solution)

        #Loi giai duoi day la loi giai-------------------------

        dkz1 = MathTex(
            r'\bullet \ \ |z-3-2i|+|\overline{z} + 2 + 8i| = \sqrt{61}'
        ).scale(0.7).to_corner(LEFT).shift(1.45*UP)
        #self.add(dkz1)

        dkz1trans = MathTex(
            r'\bullet \ \ |z-3-2i|+|z + 2 - 8i| = \sqrt{61}'
        ).scale(0.7).to_corner(LEFT).shift(1.45*UP)
        self.add(dkz1trans)

        dkz2 = MathTex(
            r'M(z), A(3;2), B(-2,8)'
        ).scale(0.7).next_to(dkz1, DOWN).shift(0.1*UP).to_edge(LEFT)
        self.add(dkz2) 

        dkz3 = MathTex(
            r'\Rightarrow MA+MB= \sqrt{61} =AB'
        ).scale(0.7).next_to(dkz2).shift(0.05*UP)
        self.add(dkz3)

        dkz4 =Text(
            text= 'Từ đó suy ra: M thuộc đoạn thẳng AB',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont,
            t2c= {'M thuộc đoạn thẳng AB': RED}
        ).scale(1.05).next_to(dkz3, DOWN).shift(0.1*UP).to_edge(LEFT)
        self.add(dkz4) 

        #Dieu kien cua w

        dkw1 = MathTex(
            r'\bullet \ \ Re[ \ ( w+10 )( \overline{w}+8i ) \ ]= -32'
        ).scale(0.7).to_corner(LEFT).shift(0.1*DOWN)
        #self.add(dkw1)
        
        dkw1trans = MathTex(
            r'\bullet \ \ Re[ \ ( w+10 )( \overline{w}+8i ) \ ] +32=0'
        ).scale(0.7).to_corner(LEFT).shift(0.1*DOWN)
        self.add(dkw1trans)

        CALC1 = Tex(
            r'CALC z=100+0,01i  $\Rightarrow VT=$'
        ).scale(0.7).next_to(dkw1, DOWN).shift(0.1*UP).to_edge(LEFT)
        self.add(CALC1)

        WDichso_1 = MathTex(
            r'11031,9201'
        ).scale(0.7).next_to(CALC1)
        #self.add(WDichso_1)

        WDichso_2 = MathTex(
            r'1 \ \ 10 \ \ 31, \ \ 92 \ \ 01'
        ).scale(0.7).next_to(CALC1)
        self.add(WDichso_2)

        WDichso_3 = MathTex(
            r'x^2 +10x +32 -8y +y^2 =0'
        ).scale(0.7).next_to(WDichso_2, DOWN).shift(0.1*UP, 0.7*RIGHT)
        #self.add(WDichso_3)

        WDichso_4 = MathTex(
            r'(x+5)^2 + (y-4)^2 = 9'
        ).scale(0.7).next_to(WDichso_2, DOWN).shift(0.1*UP, 0.3*RIGHT)
        self.add(WDichso_4)

        w_module = MathTex(
            r'\Rightarrow |w+5-4i|=3' 
        ).scale(0.7).next_to(WDichso_3, DOWN).shift(0.15*UP, 0.5*LEFT)
        w_module.set_color_by_gradient( BLUE)
        self.add(w_module)

        #Xet max P

        giai1 = MathTex(
            r'\bullet \ \ P= |z+w-6-4i|'
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        #self.add(giai1)

        giai1trans = MathTex(
            r'\bullet \ \ P= |z-(-w+6+4i)|'
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.add(giai1trans)

        giai2 = MathTex(
            r'\xrightarrow{\text{u= \ -w+6+4i} \ } \ \ P= |z-u|'
        ).scale(0.7).shift(2*DOWN, 0.2*LEFT)
        self.add(giai2)

        dku1 = MathTex(
            r'\bullet \ \ w=-u+6+4i \Rightarrow |(-u+6+4i)+5-4i|=3 \Rightarrow |u-11|=3'
        ).scale(0.7).to_edge(LEFT).shift(2.5*DOWN)
        dku1[0][30:38].set_color(GREEN)
        self.add(dku1)

        #VẼ ĐỒ THỊ

        axes = Axes(
            x_range=[-3.5,17.5,2],x_length=5,
            y_range=[-4.2,13,2],y_length=4,
            tips=False
        ).shift(4.3*RIGHT,0.2*DOWN)
        pointO = Tex('O').scale(0.5).shift(1.05*DOWN,2.45*RIGHT)
        self.add(pointO, axes)

        dotA =Dot(axes.coords_to_point(3, 2), color=YELLOW).scale(0.7)
        self.add(dotA)
        A_text = Tex('A', color = YELLOW).scale(0.6).next_to(dotA, UP).shift(0.1*DOWN)
        self.add(A_text)

        dotB =Dot(axes.coords_to_point(-2, 8), color=YELLOW).scale(0.7)
        self.add(dotB)
        B_text = Tex('B', color = YELLOW).scale(0.6).next_to(dotB, UP).shift(0.1*DOWN)
        self.add(B_text)

        #vẽ hình tròn
        def c1(t):
            return (3*cos(t) +11, 3*sin(t))
        cir1 = axes.plot_parametric_curve(c1, color=GREEN, t_range=[0, 2 * PI])
        w1_label = MathTex(
            r'(C)', color = GREEN
        ).scale(0.6).next_to(cir1, UP).shift(0.1*DOWN)
        self.add(cir1, w1_label)

        dotI =Dot(axes.coords_to_point(11, 0), color=YELLOW).scale(0.7)
        self.add(dotI)
        I_text = Tex('I', color = YELLOW).scale(0.6).next_to(dotI, UP).shift(0.1*DOWN)
        self.add(I_text)

        #vẽ AB
        AB = Line().set_color_by_gradient(RED)
        AB.put_start_and_end_on(dotA.get_center(), dotB.get_center())
        self.add(AB)
        
        #giai Pmax
        
        dotN =Dot(axes.coords_to_point(13.55497495, -1.57229227), color=YELLOW).scale(0.7)
        self.add(dotN)
        N_text = Tex('N', color = YELLOW).scale(0.6).next_to(dotN).shift(0.1*LEFT)
        self.add(N_text)

        BN = Line().set_color_by_gradient(BLUE_D)
        BN.put_start_and_end_on(dotB.get_center(), dotN.get_center())
        self.add(BN)

        giaiPmax1 = MathTex(
            r'\bullet \ \ P_{max} = IB+R'
        ).scale(0.7).to_corner(LEFT).shift(3*DOWN)
        self.add(giaiPmax1)

        giaiPmax2 = MathTex(
            r'= \sqrt{(11+2)^2 + (0-8)^2} +3 \approx 18,264...'
        ).scale(0.7).next_to(giaiPmax1)
        giaiPmax2[0][20:29].set_color(YELLOW)
        self.add(giaiPmax2)

        Rect = Rectangle(
            width=1.5,
            height=0.6,
            stroke_color = (BLUE, PURPLE)
        ).shift(3*DOWN,1.9*RIGHT)
        self.add(Rect)

        khoanhtron = Circle(
            stroke_color = (RED, ORANGE, YELLOW)
        ).next_to(dapanA, LEFT).scale(0.3).shift(1.4*RIGHT)
        self.add(khoanhtron)

        