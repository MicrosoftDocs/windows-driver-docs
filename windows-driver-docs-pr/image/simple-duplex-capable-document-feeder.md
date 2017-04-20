---
title: Simple Duplex-Capable Document Feeder
author: windows-driver-content
description: Simple Duplex-Capable Document Feeder
ms.assetid: 0807f02a-5bbf-4ed1-b381-63e1f37a0e2e
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Simple Duplex-Capable Document Feeder


## <a href="" id="ddk-simple-duplex-capable-document-feeder-si"></a>


Simple duplex scanning uses the same page settings for both front and back pages. Scanners that support duplexing should set the DUPLEX flag in the [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384) property.

The following figure illustrates the WIA item tree of a flatbed scanner that supports simple duplex-capable document feeder scanning.

![diagram illustrating the item tree of a flatbed scanner that supports simple duplex-capable document feeder scanning](images/wia-feeder-tree3.png)

Note that the front and back of the page that is being scanned are represented by separate child items in the item tree. This differentiation includes separate categories in the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property: WIA\_CATEGORY\_FRONT and WIA\_CATEGORY\_BACK. In a scanner that performs basic duplex scanning, the front and back items will not be set separately; they will be set to the exact same values.

### Scanning

Applications navigate to the feeder item to perform document feeder scans. This item is where they will configure the number of pages to scan and the settings of each page and set [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384) to the DUPLEX setting. A page corresponds to a single side of a document. Notice that scanning two documents results in four pages.

### Image Acquisition

In standard acquisition and folder acquisition, the WIA feeder item property settings are used for both front and back pages. For more information about standard acquisition and folder acquisition, see [Advanced Duplex-Capable Document Feeder](advanced-duplex-capable-document-feeder.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Simple%20Duplex-Capable%20Document%20Feeder%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


