---
title: Hardware Emulation Layer
description: Hardware Emulation Layer
ms.assetid: 79ca4e7f-f335-4e71-8abb-811d98976cc9
keywords:
- drawing WDK DirectDraw , hardware emulation layer
- DirectDraw WDK Windows 2000 display , hardware emulation layer
- hardware emulation layer WDK DirectDraw
- HEL WDK DirectDraw
- emulation WDK DirectDraw
- transparent blts WDK DirectDraw
- capability bits WDK DirectDraw
- caps bits WDK DirectDraw
- surfaces WDK DirectDraw , capability bits
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Emulation Layer


## <span id="ddk_hardware_emulation_layer_gg"></span><span id="DDK_HARDWARE_EMULATION_LAYER_GG"></span>


The DirectDraw hardware emulation layer (HEL) performs emulation for the DirectDraw driver. The HEL (written by Microsoft as part of DirectDraw) performs this emulation in user mode.

For example, if the DirectDraw driver has capability (*caps*) bits set for blts but not for transparent blts, the DirectDraw driver is called for blts and the HEL for transparent blts. In the case of a transparent blt, the HEL is passed a display memory pointer and it compares each byte from a backing surface to the color key. If the byte does not match the color key, the HEL copies it to the destination surface using the CPU. This emulation also occurs for other unsupported operations or if the card is out of display memory.

DirectDraw does not pass failed DirectDraw driver operations to the HEL. If either the HEL or the DirectDraw driver fails a particular operation, an error code is returned to the application.

 

 





