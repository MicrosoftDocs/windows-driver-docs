---
title: Understanding TYMED
author: windows-driver-content
description: Understanding TYMED
ms.assetid: 36110923-c346-4367-8b7d-ef4d003ed88c
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Understanding TYMED


## <a href="" id="ddk-understanding-tymed-si"></a>


TYMED specifies the type of data transfer. The value of this member is derived from the [**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656) common item property. The data transfer specified can be either a memory-callback transfer or a file transfer. See the Microsoft Windows SDK documentation for more information about the TYMED\_XXX constants.

### File Transfer TYMED

In a file transfer, the following values are used:

<a href="" id="tymed-file"></a>TYMED\_FILE  
Indicates one file containing a single image.

<a href="" id="tymed-multipage-file"></a>TYMED\_MULTIPAGE\_FILE  
Indicates one file containing multiple images, such as multipage TIF and similar formats. This is used primarily in document feeder acquisition.

### Memory Transfer TYMED

In a memory transfer, the following values are used:

<a href="" id="tymed-callback"></a>TYMED\_CALLBACK  
Indicates one buffer containing a single image or multiple images separated by IT\_MSG\_NEW\_PAGE messages.

<a href="" id="tymed-multipage-callback"></a>TYMED\_MULTIPAGE\_CALLBACK  
Indicates one buffer containing multiple images separated by IT\_MSG\_NEW\_PAGE messages. This results in a single file containing multiple images. This is used primarily in document feeder acquisition.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Understanding%20TYMED%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


