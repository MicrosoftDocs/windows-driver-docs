---
title: Timing a Flip
description: Timing a Flip
ms.assetid: abd3188e-0f75-401a-88e3-e2a9c5788ad5
keywords:
- drawing page flips WDK DirectDraw , timing
- DirectDraw flipping WDK Windows 2000 display , timing
- page flipping WDK DirectDraw , timing
- flipping WDK DirectDraw , timing
- timing flips WDK DirectDraw
- display duration WDK DirectDraw
- tears WDK DirectDraw
- scan lines WDK DirectDraw
- surfaces WDK DirectDraw , flipping
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Timing a Flip


## <span id="ddk_timing_a_flip_gg"></span><span id="DDK_TIMING_A_FLIP_GG"></span>


Timing a flip is very easy if a flip register is available and the scan line is known. Simply check the flip register to see whether the last flip has occurred, then make sure the scan line is not in the vertical blank before doing the flip. If the scan line and flip register are not available, however, use one or more of the algorithms described in the following paragraphs.

-   If the hardware does not have a bit for checking whether the scan line has been through a refresh cycle, more than one method should be used to time the flip. The alternative method is based on elapsed time. It is okay to flip if adequate time for drawing the entire surface has elapsed since the last flip. This amount of time is determined empirically (unless the monitor refresh rate is known) at driver initialization and on mode changes by polling until the display is in vertical sync, and then polling until it is not in vertical sync. This is done for 20 iterations, with the thread execution priority set to maximum. The result is divided by 20 to give *display duration*. This is the maximum time to wait before allowing access to the back buffer. (If the display duration is already known, it does not need to be calculated.) In most cases, a much shorter period is required before doing a flip, but display duration is used as a fallback because it is completely reliable.

-   If only the line number of the scan line is available, the fastest method is to record the time and scan line. Then, when the scan line is less than it was before, it has been through a refresh cycle. For instance, if the scan line is at line 300 the first time it is polled and at line 50 the next time, then the entire surface has been displayed at least once. However, the scan line is not completely reliable on all display cards. In some cases a register can be read from and written to at the same time, giving half of two different numbers. In these cases, the register must be read twice to verify that it is reporting a correct number. In some cases the scan line may be inaccurate as it passes through the horizontal sync. The flag that indicates whether the scan line is currently in display often returns a false negative result while the scan line is in horizontal blank.

-   If the line number of the scan line is not available, it may be possible to verify that the scan line has passed from display through vertical blank and back into display. By tracking when the scan line passes into and out of display, you can determine when an entire refresh cycle has been completed. The ability to check whether the scan line is in display or in vertical blank should be available on all display cards, but the scan-line number may not be.

A few adjustments may be required to get the last bit of flicker out of the display, such as making sure no calculations are occurring after the address is read (for example, shifting right two places to get the true address because the address is on a DWORD boundary). To avoid tearing, make sure that the scan line is not in vertical blank, is just above the vertical sync, and is in display before writing to the flip register.

Although display cards are based on the original IBM video graphics card (VGA) specifications, Super VGAs vary considerably (see *Programmer's Guide to the EGA, VGA, and Super VGA Cards* by Richard F. Ferraro - Addison-Wesley, latest edition). Some cards provide no straightforward way of determining whether the scan line is in vertical blank, or if it is even in display. These deficiencies become more important as the competition to meet the demand for advanced display capabilities increases. In the meantime, driver writers must use creativity to compensate for these deficiencies.

Once it is okay to flip, the reference to the surface to display next is loaded in the flip register. Nothing happens until the scan line gets past the vertical sync and is back into the display area. Then the flip register is read once. If something else is stored in the flip register before that time, or if the surface is being written to at the same time it is being read, a tear occurs. Once the register is read, the surface should not be locked or written to while it is still being drawn.

Checking whether the register has been read is just a matter of checking a flag in most newer cards. In older cards, however, a hardware interrupt was often used for this purpose. When a certain point was crossed that read in the flip register, whatever function was hooked to that interrupt would be called. The problem is that this interrupt may be used for other purposes in some newer hardware.

 

 





