---
title: Hardware Emulation Layer
description: Hardware Emulation Layer
ms.assetid: 79ca4e7f-f335-4e71-8abb-811d98976cc9
keywords: ["drawing WDK DirectDraw , hardware emulation layer", "DirectDraw WDK Windows 2000 display , hardware emulation layer", "hardware emulation layer WDK DirectDraw", "HEL WDK DirectDraw", "emulation WDK DirectDraw", "transparent blts WDK DirectDraw", "capability bits WDK DirectDraw", "caps bits WDK DirectDraw", "surfaces WDK DirectDraw , capability bits"]
---

# Hardware Emulation Layer


## <span id="ddk_hardware_emulation_layer_gg"></span><span id="DDK_HARDWARE_EMULATION_LAYER_GG"></span>


The DirectDraw hardware emulation layer (HEL) performs emulation for the DirectDraw driver. The HEL (written by Microsoft as part of DirectDraw) performs this emulation in user mode.

For example, if the DirectDraw driver has capability (*caps*) bits set for blts but not for transparent blts, the DirectDraw driver is called for blts and the HEL for transparent blts. In the case of a transparent blt, the HEL is passed a display memory pointer and it compares each byte from a backing surface to the color key. If the byte does not match the color key, the HEL copies it to the destination surface using the CPU. This emulation also occurs for other unsupported operations or if the card is out of display memory.

DirectDraw does not pass failed DirectDraw driver operations to the HEL. If either the HEL or the DirectDraw driver fails a particular operation, an error code is returned to the application.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Hardware%20Emulation%20Layer%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




