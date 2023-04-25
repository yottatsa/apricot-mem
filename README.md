# Apricot Xi Memory and IO Card 

Additional 640KB RAM

[Schematics](https://kicanvas.org/?github=https%3A%2F%2Fgithub.com%2Fyottatsa%2Fapricot-mem%2Fblob%2Fmain%2Fpcb%2Fapricot-mem.kicad_sch), 
[PCB](https://kicanvas.org/?github=https%3A%2F%2Fgithub.com%2Fyottatsa%2Fapricot-mem%2Fblob%2Fmain%2Fpcb%2Fapricot-mem.kicad_pcb)


    make -C gal
    minipro -p ATF16V8C --write gal/chip_enable.jed -P

## ToDo

* Loading caps on signal lines
* Board a bit tight near the floppy, trim the right side
* Move GAL to the left so it will be accessible without pulling the card
* Move testpoints to the bottom/make them THT, as it will make it more accessible from the case
* 3D-print a frame to hold the card in place

## Board verification

- GAL is compilable and flash-able
- pins 12, 19 can not be used as input in registered mode

## Alternative options

* [Apricot F Series expandable SRAM board](https://github.com/stephen-usher/Apricot-RAM-Expansion) by S.R.Usher
