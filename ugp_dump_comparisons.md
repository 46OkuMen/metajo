Comparing some memory dumps

~27000-~28650: Long countdowns from f0 e0 d0 c0 b0 a0 90 etc, often out of order and with 00s
2dab0: Some new 50's and 70's
2dfa0: More 50's and 70's
Some more of that 
Then a bunch of stuff in VRAM, around aa000~

Palette loading stuff:
Goes in ~1b080, pretty much straight

Mysterious value loading stuff:
Loads all the values two apart, and 2+ more lines of values that might be derived from it?
And some stuff at 27040
And it initializes the giant countdown from 0x27650 - 0x2864f (0x1000 bytes)
	They count down, but whenever it gets to a line break, it repeates that one.
		Like, e0 d0 c0 b0 a0 90 80 70 60 50 40 30 20 10 00 f0
		      f0 e0 d0 c0 b0 a0 90 80 70 60 50 40 30 20 10 00

After rendering first byte, 09:
	27040: 00 50 changes to 51 88
		...That's it

After rendering second byte, ff:
	No changes?

After rendering rest of the image:
	Tons of the countdown section got re-ordered in various ways
The 50's and 70's 

After rendering the fifth byte(?), which is 22:
1b0c0: 90 -> 30, 00 -> 1e
Some values change around 27000, but not the countdown

After rendering the sixth byte:
	Puts a 10 at 1b580
	Shifts the first line of the countdown.
		00 f0 e0 d0 c0 b0 a0 90 80 70 60 50 40 30 20 10 ->
		10 00 f0 e0 d0 c0 b0 a0 90 80 70 60 50 40 30 20
	Puts a 10 at 2d878 which is in a bunch of 0s.

After rendering the 7th byte, which is 99
	1b57d 00 -> 10, 1b580 10 -> 00
	27037 72 -> 16
	2704a 56 -> 57, 2704c 28 -> 2c
	Shift the first two entries of the first two lines of the countodwn:
		10 00, 10 00 -> 00 10, 00 10
	2d87a 00 -> 10, which is 3 after the previous one

After rendering the 8th byte, which is f9:
	1b580 00 -> 10
	2704a 57 -> 58, 2c -> 30
	Countdown: Second row switches 00 10 -> 10 00
	2d87e: 00 00 -> 10 10

After 9th byte, 76:
	1b57d: 10 -> 20
	Countdown: Second row shifts one col to the right

After ath byte, c3:
	2704b: 58 -> 5a, 30 -> 34
	2d882: 00 00 -> 20 10, 00 00 -> 20 20

After bth byte, 87:
	1b57e: 00 00 10 -> 10 00 20
	2704c: 34 -> 3c, 20 -> 38
	Countdown: First row switches 00 10 -> 10 00
	2d889: 00 00 -> 20 20


Alternate reality with only 01's:
	After first 01 loaded:
		270b: 00 50 -> 51 88, 5b -> 60, eb 03 -> 3f 04
	After second 01 loaded:
		1b57e: 00 00 00 00 00 -> e0 e0 00 e0 e0
		27048: 51 -> 52, 00 -> 04
		27650: 00 f0 e0 -> e0 00 f0
		2d650: 00 00 00 -> e0 00 e0
	After third 01 loaded:
		1b57d: e0 -> c0, e0 -> c0
		27048: 52 -> 53, 04 -> 08
		28530: e0 d0 c0 -> c0 e0 d0 (how far in is this? 18 rows from the bottom? It's ee0 into the buffer.)
		2d654: 00 00 00 00 00 00 00 00 -> e0 e0 e0 c0 e0 e0 c0 c0 (hey, that's eight things)
	After fourth 01 loaded:
		2704d: 08 -> 10, 00 00 -> 0c 60
		2d65d: 00 00 00 00 -> e0 e0 c0 c0 (right next to the previous 8 things. Just 4 this time)
	After fifth 01 loaded:
		1b57e: c0 -> a0, c0 -> a0
		27049: 53 -> 55, 10 -> 14
		28510: c0 b0 a0 -> a0 c0 b0         ; 1b57e seems to describe the countdown-shift that occurs? ( this is ec0 into the buffer)
		2d660: 00 x8  -> e0 e0 c0 a0 e0 e0 a0 a0 
	After sixth 01 loaded:
		27040: 14 -> 1c, 0c -> 18
		2d660: 00 x4: e0 e0 a0 a0
	After seventh 01:
		1b570: a0 -> 80, a0 -> 80
		27040: 55 -> 57, 1c -> 20
		Countdown 284f0: a0 90 80 -> 80 a0 90        ( this is ea0 into the buffer.)
		2d660: e0 e0 a0 80 e0 e0 80 80          (kinda the same shift that happened to the thing two bytes ago?
	After eighth 01:
		27040: 20 -> 28, 18 -> 24
		2d670: e0 e0 80 80