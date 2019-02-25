---
title: Macrovision
description: Macrovision
ms.assetid: 62bd8d8a-3e58-4bca-a32d-ff792180afbe
keywords:
- DVD decoder minidrivers WDK , copyright protection
- decoder minidrivers WDK DVD , copyright protection
- copyright protection WDK DVD decoder
- Macrovision WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Macrovision





Macrovision is supported by the last device handling the video data before leaving the computer. In the case of a video port connection to a video card, the video card and the DVD navigator/splitter handle all Macrovision processing. The decoder is not involved.

If the decoder has an NTSC output, Macrovision encoding and Macrovision compliance is the responsibility of the decoder card. The [**KS\_COPY\_MACROVISION**](https://msdn.microsoft.com/library/windows/hardware/ff567316) property indicates the level of Macrovision encoding on the media (levels 0 to 3). The decoder may use this information to enable or disable Macrovision encoding on the NTSC output.

 

 




