---
title: Understanding TYMED
description: Understanding TYMED
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Understanding TYMED





TYMED specifies the type of data transfer. The value of this member is derived from the [**WIA\_IPA\_TYMED**](./wia-ipa-tymed.md) common item property. The data transfer specified can be either a memory-callback transfer or a file transfer. See the Microsoft Windows SDK documentation for more information about the TYMED\_XXX constants.

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

 

