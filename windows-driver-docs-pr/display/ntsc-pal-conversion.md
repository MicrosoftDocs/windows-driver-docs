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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NTSC/PAL Conversion


## <span id="ddk_ntsc_pal_conversion_gg"></span><span id="DDK_NTSC_PAL_CONVERSION_GG"></span>


Conversion from NTSC to PAL is done by simply playing the film fast -- at 25 fps. Two sequential fields are created from the same frame and displayed 1/50th of a second apart. Conversion from PAL to NTSC is done by repeating every fifth video field with a process called *3:2 pulldown*. A first film frame is used to create two video fields, and then a second film frame is used to create three video fields. This process is repeated so that odd and even fields are sent in the order Ao Ae Ao Be Bo Ce Co Ce.

Therefore, an interlaced video created from a film contains pairs of fields. But unlike a standard television signal where each field is 1/60th or 1/50th of a second apart; many of these field pairs contain data from the same frame of film. Displaying these field pairs at the same time does not produce any artifacts and provides better results than television monitors do. However, any field pairs not from the same frame will be 1/24 of a second apart and potentially could produce more artifacts.

When the interlaced video is encoded, a flag is set to indicate how the stream should be decoded. This should be enough information to decode and optimally display the decoded pictures because the output of an MPEG-2 or NTSC decoder for DVD or DSS is theoretically always 50 or 60 interlaced fields per second. However, older films and some newer films often have a break in the flag cadence, especially at film reel changeover points. This requires a method for identifying such progressive content in order to select the proper method for displaying the information about a frame-by-frame basis.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20NTSC/PAL%20Conversion%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




