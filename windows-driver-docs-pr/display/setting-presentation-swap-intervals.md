---
title: Setting Presentation Swap Intervals
description: Setting Presentation Swap Intervals
ms.assetid: 01626dbc-d7ac-482a-a07e-0f5ee3ffb05f
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities
- D3DCAPS8
- presentation swap intervals WDK DirectX 8.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Presentation Swap Intervals


## <span id="ddk_setting_presentation_swap_intervals_gg"></span><span id="DDK_SETTING_PRESENTATION_SWAP_INTERVALS_GG"></span>


A driver should always set the **PresentationIntervals** member of the D3DCAPS8 structure to zero when it reports the capabilities of its Direct3D hardware. The runtime then assigns the D3DPRESENT\_INTERVAL\_ONE value as the default. In addition, the runtime assigns the following presentation swap intervals depending on how the driver specifies capability bits in the **Caps2** member of D3DCAPS8:

-   If the driver specifies the DDCAPS2\_FLIPNOVSYNC bit, the runtime also sets **PresentationIntervals** to D3DPRESENT\_INTERVAL\_IMMEDIATE.

-   If the driver specifies the DDCAPS2\_FLIPINTERVAL bit, the runtime also sets **PresentationIntervals** to D3DPRESENT\_INTERVAL\_TWO, D3DPRESENT\_INTERVAL\_THREE, and D3DPRESENT\_INTERVAL\_FOUR.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20Presentation%20Swap%20Intervals%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




