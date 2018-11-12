---
title: Supporting Nonstandard Display Modes
description: Supporting Nonstandard Display Modes
ms.assetid: 33a10aed-dfc9-4b64-97fb-e4b7c744dc0d
keywords:
- nonstandard display modes WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Nonstandard Display Modes


## <span id="ddk_supporting_nonstandard_display_modes_gg"></span><span id="DDK_SUPPORTING_NONSTANDARD_DISPLAY_MODES_GG"></span>


A DirectX 9.0 version driver for a device that supports any nonstandard display modes, such as the 10-bits-per-channel (10:10:10:2) display and render target format, must respond to requests to enumerate these extended nonstandard display modes. In addition, the DirectX 9.0 driver must be able to perform operations that enable switching between standard and nonstandard display modes. The following sections describe how drivers support nonstandard display modes:

[Enumerating Extended Formats](enumerating-extended-formats.md)

[Switching Between Standard and Nonstandard Modes](switching-between-standard-and-nonstandard-modes.md)

[Handling Nonstandard Display Modes](handling-nonstandard-display-modes.md)

 

 





