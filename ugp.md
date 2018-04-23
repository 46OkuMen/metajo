

00-02: "Ugp"

0c-0d: Width (02 80 = 640)
0e-0f: Height (01 90 = 400)

10-3f: Palette?
00 00 00, 03 03 03, 05 05 05, 09 09 09,
0b 0b 0b, 0b 0a 0a, 08 08 08, 07 07 07,
0d 0d 0d, 0e 0e 0e, 0f 0f 0f, 0d 04 06,
0f 00 00, 0e 00 01, 03 03 0a, 00 00 0a

0 Black
1 Blue
2 Purplish Blue
3 Grey
4 Green
5 Sickly Green
6 Red
7 White
8 Light Orange
9 Orange
a Brown
b Brick
c Peach
d Pink
e Dark Grey
f Light Grey


Replacing an 84 with 55.

x84 = 132
x55 = 85

Portrait instead.
Portrait is 80 wide, 96 tall

Color 07 in the pallete is white.

01 28: Same
01 30: Same
01 37: Same
01 38: (Default)
01 30: Same
01 39: Same
01 3f: Same

01 24: Same as default
01 25: New tan pixel, below rightmost one
01 26: " "
01 27: " "

01 18: New tan pixel near bottom of shoulder, 0001 0000
01 17: Another tan pixel to its right,        0001 0100
01 16: Same^
01 15: Same^
01 14: Right pixel disappears
01 13: Both pixels disappear
01 12: Same^
01 11: Same^

00 00: Shoulder block empty but still brown

01 ff: Copies a 16x2 block to the left into this one
01 fe: Copies the left 8x2 block from the previous one, and another 8x2 block from... somewhere else? Up on her shoulder? But extended
01 fd: Copies the left block, and a weird blue/grey block from somewhere else that doesn't exist
01 ef: Copies the shoulder block twice

Replacing the 49 right before the 01 38:

49: Normal
00: Three tan pixels (0101 0100) disappear
48: Only two tan pixels

Hm. THe last appearance of those three tan pixels, in the 0101 0100 arrangement, was 57+15 = 73 = 0x49 pixels ago...

4b: Adds a light tan pixel below and between the first two:
1010 1000
0100 0000

4d: Left two pixels only (101)






Really early in the portrait image:

4f (default): Orange for the rest of the time
4e: Green for the rest of the image
4d: White and green stripes for the rest of the image
4c: Lighter green for the rest of the image
4b: Green and red stripes for the rest of the image
4a: White and red stripes

Longer shapes:
49: Red pixels at edges, then light green for the rest of the image
48: Same shape, but red for rest of image
46: Long white rectangle, light green
45: Red/white stripes after a long (7px) white rectangle
44: Red, after a long (7px) white rectangle
43: Longer white thing, light green for rest of image
42: Red pixels at edges, also red for rest of image
41: Entirely white
40: Entirely white

50: White 6x2, then red
51: White 6x2, then a red line, then the rest is light green
52: White 6x2, then a red column, then green and red stripes
53: ^Same but darker green
54: White 6x2, then red and white stripes
55: White 6-x, then one red pixel, then green/white stripes

09: white 4x2, white, red, red, light green->

Clearly something really important is happening in the 40s line. What kind of pattern data is beting stored there?

fa 8e 47 29 11 07 04 04 04 01 03 02 02 01 02 07

fa doesn't change anything if above aa or so, but turns everything into garbage below that?

The first 5 bytes are always decreasing, around a fairly similar set of values

Deploying a high contrast color palette.

The lack of sensitivity suggests they aren't pointers, but maybe buffer sizes?






Tons of 55s from the very beginning:
Black stripes alternating with tan, brown, tan, brown (1010) etc


AA's at the beginning:

Each AA puts eight(?) new pixels on the screen:

tan brown tan brown
black tan black tan

Putting different stuff in the first byte might change which color each stripe is??

A9 (1010 1001) = Turns second row black

AA (1010 1010)

AB (1010 1011) = Turns second row into black peach black peach
AC (1010 1100) = Turns first row into tan peach tan peach, second row is all black
AD (1010 1101) = Turns first row into tan peach (fca) tan peach, second row to black brown black brown
AE (1010 1110) = Turns first row into tan pink tan pink (fb7), black tan black tan
AF (1010 1111) =  More color changes, but also less copying??

AA x2: 4 cols
AA x3: 8 cols
AA x4: 12 cols
AA x5: 16 cols

Depends on how you count the "leftover" colors that get striped across the screen.

Just AA by itself puts the same brown/tan stripes.

AB: All brown
AC: Peach/black
AD: Peach/tan
AE: Peach(?)/black


First (0x50) byte experiments:

Determines the first 2x2 pixel block?

00: Black x4
01: Black, tan, black, tan
02: Black, tan, tan, tan
03: Black, brown, brown, brown
04: Tan, tan, tan, tan
05: Tan, tan, black, black
06: Brown x4
07: Peach x4
08-0f: Black x4
10: Tan x4
11: Tan, brown, brown, brown
12: Black, black, tan, tan
13: Brown, brown, tan, tan
14: Actually 3x2 nobw. Black, black, black, / black, tan, tan
15: " "
16: Black, black, black, / black, black, tan
17: " "
18: Brown x4
19: Black, black, brown, brown
1a: Black, black, black / black, tan, tan (same as 14)
1b: Black, black, black / black, black, tan (same as 15)
1c: Peach x4
1d: Black, black, black / black, peach, peach
1e: Sickly green x4
1f: Red x4
20: Tan x4
21: Tan, tan, brown, brown
22: Brown, brown, tan, tan - stripes
23: Peach, peach, tan, tan - stripes
24: Black, tan, black, tan
25: Black, tan, black, tan
26: Black, black, black / black, black, tan
27: " "
28: Tan, tan, black, black - stripes
29: Brown, brown, black, black - stripes
2a: Black, tan, black, black - stripes (tan and black)
2b: Black x4
2c: Tan, tan, brown, brown - stripes


fb: Orange x4
fc: peach, peach, peach, peach
fd: brown, brown, peach, peach
fe: peach, peach, black, black
ff: Peach, peach, tan, tan


Second portrait:

Palette:

0 Black
1 Blue
2 Purplish Blue
3 Grey
4 Green
5 Sickly Green
6 Red
7 White
8 Light Orange
9 Orange
10 Brown
11 Brick
12 Peach
13 Pink
14 Dark Grey
15 Light Grey

ed 60: Bottom right corner 2x2 becomes red instead of purple
ed 70: Bottom right corner becomes brown, brown, brown, grey
ed 71: Bottom right corner becomes brown
ed 72: Brown, pink, brown, grey
ed 73: brown, blue, brown, grey
ed 80: Normal (default)
ed 81: Normal
ed 8f: Normal

ee 80: purple black purple black
ee 81: Same

ef 80: Same

f0 00: Different garbage
f0 80: Little orange thing gets copied. Kind of looks like the top-left corner of the hair, with different colors?
f0 81: Different garbage

f1 80: Eh, looks like some more garbage getting copied really







Bricks:

24 f7 fc 78
fc: copy it once

f6 fc: Copies 504 pixels fewer than f7 fc
f7 fc: 504 pixels of copying?
f7 fd: Copies 256 more pixels than f7 fc






Disassembling in Zai Metajo

fc b3 4c 26 11 09 05 03 02 01 01 01 01 01 01 04

EAX: 0
EBX: 1000
ECX: 10
EDX: 2e3c

di: 52

CS: 1896

lodsb
mov cs:[di], ax
add di, +-2
loop 03a8          ; (lodsb above)

Since ECX is 10, this reads the whole mystery row

Go to address cs:di (1896:52, 54, ..., etc) to see the values in memory

What happens to them once they're there?

...
mov ax, cs
mov dx, ax

And yes, they have to be below the first one

Hm. Lots of complex stuff I'm not sure about
They get zeroed out at that location though. But they do appear just a bit later (1896:94, etc)
Those values remain the same, in that location, for the rest of the image I think

09 ff f7 22 42 ed 99 f9 76 c3 87 65 9b 9a 10 41

Loop when looking at values after that:

Useful to look at the ANJIN image at the beginning, to avoid the interrupts every few instructions.

fs is a segment register, currently equal to ds and es: 7465
si: 8850

mov dl, fs:[si]
mov dh, 08
inc si
cmp cs:[0189], 01    ; Some value that is 00
cmp si, f800
jnz 0676
->

add dl, dl        ; now edx is 0812
jnb 0682cs

->

mov bl, cs:[bx+00da]   ; bx (1f) + da = f9. Value at cs:f9 is still just 0
cmp 10, jump if above, but not this time
mov cx, bx
mov bx, si              ; 8851
shr ah, 04           ; still 0
add ax, cx           ; yep, both 0
mov si, ax
lodsb               ; 0 in eax, esi now ffff
or cx, cx
jz 070c

->

mov si, bx
mov cs:[0688], al
... some stuff
dec dh
jz 06ab
add dl, dl         ; now 0824
jnb 0724
-> (Jumps to the "mov bl, cs:[bx+00da]" instruction above)



fd b6 7c 46 22 12 07 01 01 01 01 01 01 01 01 01

Loops through a ton of stosw instances. Store AX at address ES:DI, which here is 00 at 2765:5c78.
That's around 2e, 3000, so not VRAM yet

VRAM is at a8,000 - c0,000

dl += dl
if dl overflows:
	goto 06e8
		mov bl, cs:[bx+00d6]        ; the last value in one of those mystery value-derived value lists? (1d)
		cmp bl, 10
		ja 06d8
		mov cx, bx
else:
	mov bl, cs:[bx+00f8]           ; A standalone value in one of those lists. (1e)


Mystery values: fc b3 4c 26 11 09 05 03 02 01 01 01 01 01 01 01 04

First few image bytes: 09 ff f7 22 42 ed 99 f9 76




The countdown buffer gets accessed through lodsb.
	load ds:si into al. DS = 2765, SI = 0f

	lea di, [si+01] moves the value at si+01 into di?
		I think it just moved (0e+1=0f) into di.
	repe movsb: Move ECX bytes from DS:SI into ES:DI.
		Moves 0f bytes from 0e into 0f. Which shifts a portion of the row over to the right, or all of it since SI = 0f

Writes some bytes to the 2d870 area with stosw.
	Store AX at ES:DI.
	Also with mov [di], cx just after that. So, four things get stored here - two bytes of AX (00 00), two bytes of CX (20 20).
	Checks some stuff around cs:172 when deciding what to do next. This looks like it's one of the mystery value-derived locations
		Are these values really derived that way? And do they change during the rendering process?