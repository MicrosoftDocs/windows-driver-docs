---
title: WIA Transfer Architecture
author: windows-driver-content
description: WIA Transfer Architecture
ms.assetid: d8a11440-efdb-4590-9261-2b424c11186d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Transfer Architecture


Stream-based transfers simplify transfers for drivers and driver developers. With in-memory and file transfers, the caller had to specify which transfer type to use and the driver had to perform different actions depending on which transfer type was chosen. With stream-based transfers, the caller does not need to specify memory or file transfers; the caller specifies only which stream to use, and the driver behaves the same way whether this stream is a file stream or memory stream. Using streams also provides easy integration with the [WIA Image Processing Filter](wia-image-processing-filter.md).

Like the other WIA application programming interfaces (APIs) and device driver interfaces (DDIs), **IStream** is based on the Component Object Model (COM). To ensure that stream transfers are compatible with other streams, the **IWiaTransfer** interface must be exposed.

The **IWiaTransfer** interface has methods that enable progress display during a transfer, transfer cancellation, integration of error and status reporting, and uploads and downloads of data from a device. The **IWiaTransfer** interface is available only through the **IWiaItem2** interface. For more information about the **IWiaItem2** or **IWiaTransfer** interfaces and their methods, see the Microsoft Windows SDK documentation.

This section includes:

[IStream Data Transfer Driver Changes](istream-data-transfer-driver-changes.md)

[IStream Transfer Driver Example](istream-transfer-driver-example.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Transfer%20Architecture%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


