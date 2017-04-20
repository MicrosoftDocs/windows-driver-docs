---
title: Flatbed Scanner Architecture
author: windows-driver-content
description: Flatbed Scanner Architecture
ms.assetid: 04f7df17-d289-44a1-8c2d-7d0fa618cc97
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Flatbed Scanner Architecture


## <a href="" id="ddk-flatbed-scanner-architecture-si"></a>


If a scanner device supports flatbed platen scanning, it should implement a flatbed scanner item as the first child item, directly off of the root item in its WIA item tree; also, the [**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581) property must be set to WIA\_CATEGORY\_FLATBED. This flatbed item represents a programmable data source and produces an image from the document that is currently placed on the scanner's flatbed platen when a data transfer is requested from this item.

A scanner that supports only flatbed platen scanning has the WIA item tree that the following figure shows.

![diagram illustrating a flatbed scanner with platen-only scanning](images/art-flatbed1.png)

Notice that the WIA flatbed item is located directly off of the root item.

A scanner that supports flatbed platen scanning and document feeder scanning has the WIA item tree that the following figure shows.

![diagram illustrating a flatbed scanner with an automatic document feeder](images/art-flatbed2.png)

The first nonroot item in the WIA item tree must be the WIA flatbed item, if other scanning data sources are implemented. This arrangement makes it easier to support Microsoft Windows XP and Windows Me applications. For more information about compatibility with these operating systems, see [WIA Flatbed Scanner Compatibility for Windows Me and Windows XP](wia-flatbed-scanner-compatibility-for-windows-xp-and-windows-me.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Flatbed%20Scanner%20Architecture%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


