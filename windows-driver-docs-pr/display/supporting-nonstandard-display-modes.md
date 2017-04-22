---
title: Supporting Nonstandard Display Modes
description: Supporting Nonstandard Display Modes
ms.assetid: 33a10aed-dfc9-4b64-97fb-e4b7c744dc0d
keywords:
- nonstandard display modes WDK DirectX 9.0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Nonstandard Display Modes


## <span id="ddk_supporting_nonstandard_display_modes_gg"></span><span id="DDK_SUPPORTING_NONSTANDARD_DISPLAY_MODES_GG"></span>


A DirectX 9.0 version driver for a device that supports any nonstandard display modes, such as the 10-bits-per-channel (10:10:10:2) display and render target format, must respond to requests to enumerate these extended nonstandard display modes. In addition, the DirectX 9.0 driver must be able to perform operations that enable switching between standard and nonstandard display modes. The following sections describe how drivers support nonstandard display modes:

[Enumerating Extended Formats](enumerating-extended-formats.md)

[Switching Between Standard and Nonstandard Modes](switching-between-standard-and-nonstandard-modes.md)

[Handling Nonstandard Display Modes](handling-nonstandard-display-modes.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Nonstandard%20Display%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




