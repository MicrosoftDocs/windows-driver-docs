---
title: Image Geometry Properties
author: windows-driver-content
description: Image Geometry Properties
ms.assetid: d1343ad4-3a54-414c-bc08-e07e0fb079cd
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Image Geometry Properties


## <a href="" id="ddk-image-geometry-properties-si"></a>


The ImgPixHeight and ImgPixWidth image geometry properties (see the PIMA 15740 standard) are optional in PTP. For cameras that do not implement these properties, the Microsoft PTP minidriver downloads the entire image and calculates the correct values for these properties. You can prevent this from occurring by implementing these optional PTP properties.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Image%20Geometry%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


