---
title: NTSC/PAL Conversion
description: NTSC/PAL Conversion
ms.assetid: 2ae22ebd-e75a-4f9c-b50e-d0ddfe05d987
keywords:
- interlaced video WDK video port extensions
- DirectX VPE support WDK DirectDraw , interlaced video
- drawing VPEs WDK DirectDraw , interlaced video
- DirectDraw VPEs WDK Windows 2000 display , interlaced video
- video port extensions WDK DirectDraw , interlaced video
- VPEs WDK DirectDraw , interlaced video
- NTSC/PAL WDK video port extensions
- converting NTSC to PAL
- 3 2 pulldown WDK video port extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NTSC/PAL Conversion


## <span id="ddk_ntsc_pal_conversion_gg"></span><span id="DDK_NTSC_PAL_CONVERSION_GG"></span>


Conversion from NTSC to PAL is done by simply playing the film fast -- at 25 fps. Two sequential fields are created from the same frame and displayed 1/50th of a second apart. Conversion from PAL to NTSC is done by repeating every fifth video field with a process called *3:2 pulldown*. A first film frame is used to create two video fields, and then a second film frame is used to create three video fields. This process is repeated so that odd and even fields are sent in the order Ao Ae Ao Be Bo Ce Co Ce.

Therefore, an interlaced video created from a film contains pairs of fields. But unlike a standard television signal where each field is 1/60th or 1/50th of a second apart; many of these field pairs contain data from the same frame of film. Displaying these field pairs at the same time does not produce any artifacts and provides better results than television monitors do. However, any field pairs not from the same frame will be 1/24 of a second apart and potentially could produce more artifacts.

When the interlaced video is encoded, a flag is set to indicate how the stream should be decoded. This should be enough information to decode and optimally display the decoded pictures because the output of an MPEG-2 or NTSC decoder for DVD or DSS is theoretically always 50 or 60 interlaced fields per second. However, older films and some newer films often have a break in the flag cadence, especially at film reel changeover points. This requires a method for identifying such progressive content in order to select the proper method for displaying the information about a frame-by-frame basis.

 

 





