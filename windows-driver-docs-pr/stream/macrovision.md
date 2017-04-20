---
title: Macrovision
author: windows-driver-content
description: Macrovision
ms.assetid: 62bd8d8a-3e58-4bca-a32d-ff792180afbe
keywords:
- DVD decoder minidrivers WDK , copyright protection
- decoder minidrivers WDK DVD , copyright protection
- copyright protection WDK DVD decoder
- Macrovision WDK DVD decoder
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Macrovision


## <a href="" id="ddk-macrovision-ksg"></a>


Macrovision is supported by the last device handling the video data before leaving the computer. In the case of a video port connection to a video card, the video card and the DVD navigator/splitter handle all Macrovision processing. The decoder is not involved.

If the decoder has an NTSC output, Macrovision encoding and Macrovision compliance is the responsibility of the decoder card. The [**KS\_COPY\_MACROVISION**](https://msdn.microsoft.com/library/windows/hardware/ff567316) property indicates the level of Macrovision encoding on the media (levels 0 to 3). The decoder may use this information to enable or disable Macrovision encoding on the NTSC output.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Macrovision%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


