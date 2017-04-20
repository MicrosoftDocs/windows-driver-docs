---
title: Non-Duplex-Capable Document Feeder
author: windows-driver-content
description: Non-Duplex-Capable Document Feeder
ms.assetid: e22ec1bb-623e-45c6-88f4-d3b6a45fa175
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Non-Duplex-Capable Document Feeder


## <a href="" id="ddk-non-duplex-capable-document-feeder-si"></a>


The following figure illustrates the WIA item tree for a flatbed scanner that supports simple (non-duplex) document feeder scanning.

![diagram illustrating the wia item tree for a flatbed scanner that supports non-duplex document feeder scanning](images/wia-feeder-tree4.png)

A scanner with a feeder (or automatic document feeder) does not have to have a flatbed. The following figure illustrates the item tree for a feeder scanner without a flatbed or duplexer.

![diagram illustrating the item tree for a feeder scanner without a flatbed or duplexer](images/wia-feeder-tree2.png)

The flatbed item can be omitted only if no flatbed is present on the scanner. Similarly, the feeder item must be present in the item tree for any scanner that has a feeder. The feeder item is used to control settings such as basic scans (no duplexing or Simplex), simple duplex (identical front and back items), and advanced duplex scans (independent front and back items).

### Scanning

Applications navigate to the feeder item to perform document feeder scans. This item is where applications configure the number of pages to scan and the settings for each page. Notice that scanning three documents results in three pages.

### Image Acquisition

In standard acquisition and folder acquisition, the WIA feeder item property settings are used for all front pages. For more information about standard acquisition and folder acquisition, see [Advanced Duplex-Capable Document Feeder](advanced-duplex-capable-document-feeder.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Non-Duplex-Capable%20Document%20Feeder%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


