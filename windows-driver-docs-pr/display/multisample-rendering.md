---
title: Multisample Rendering
description: Multisample Rendering
ms.assetid: 7c21b0e0-bdd3-4de3-a5c5-5adc2d2e2b33
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering
- multisample rendering WDK DirectX 8.0
- rendering multisamples WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multisample Rendering


## <span id="ddk_multisample_rendering_gg"></span><span id="DDK_MULTISAMPLE_RENDERING_GG"></span>


DirectX 8.0 introduces support for multisample rendering with the number of samples per pixel under application control. The **IDirect3DDevice8** interface supports multisampling in both fullscreen and windowed modes of operation. Furthermore, there is sufficient flexibility to support hardware that performs the processing of samples into pixels at the back end (directly out of the frame buffer) or at the front end (via a special flip or blt call).For more information about **IDirect3DDevice8**, see the DirectX 8.0 documentation.

 

 





