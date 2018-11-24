---
title: Setting Presentation Swap Intervals
description: Setting Presentation Swap Intervals
ms.assetid: 01626dbc-d7ac-482a-a07e-0f5ee3ffb05f
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , reporting capabilities
- D3DCAPS8
- presentation swap intervals WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Presentation Swap Intervals


## <span id="ddk_setting_presentation_swap_intervals_gg"></span><span id="DDK_SETTING_PRESENTATION_SWAP_INTERVALS_GG"></span>


A driver should always set the **PresentationIntervals** member of the D3DCAPS8 structure to zero when it reports the capabilities of its Direct3D hardware. The runtime then assigns the D3DPRESENT\_INTERVAL\_ONE value as the default. In addition, the runtime assigns the following presentation swap intervals depending on how the driver specifies capability bits in the **Caps2** member of D3DCAPS8:

-   If the driver specifies the DDCAPS2\_FLIPNOVSYNC bit, the runtime also sets **PresentationIntervals** to D3DPRESENT\_INTERVAL\_IMMEDIATE.

-   If the driver specifies the DDCAPS2\_FLIPINTERVAL bit, the runtime also sets **PresentationIntervals** to D3DPRESENT\_INTERVAL\_TWO, D3DPRESENT\_INTERVAL\_THREE, and D3DPRESENT\_INTERVAL\_FOUR.

 

 





