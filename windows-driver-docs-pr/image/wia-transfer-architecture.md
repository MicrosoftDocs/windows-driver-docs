---
title: WIA Transfer Architecture
description: WIA Transfer Architecture
ms.assetid: d8a11440-efdb-4590-9261-2b424c11186d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Transfer Architecture


Stream-based transfers simplify transfers for drivers and driver developers. With in-memory and file transfers, the caller had to specify which transfer type to use and the driver had to perform different actions depending on which transfer type was chosen. With stream-based transfers, the caller does not need to specify memory or file transfers; the caller specifies only which stream to use, and the driver behaves the same way whether this stream is a file stream or memory stream. Using streams also provides easy integration with the [WIA Image Processing Filter](wia-image-processing-filter.md).

Like the other WIA application programming interfaces (APIs) and device driver interfaces (DDIs), **IStream** is based on the Component Object Model (COM). To ensure that stream transfers are compatible with other streams, the **IWiaTransfer** interface must be exposed.

The **IWiaTransfer** interface has methods that enable progress display during a transfer, transfer cancellation, integration of error and status reporting, and uploads and downloads of data from a device. The **IWiaTransfer** interface is available only through the **IWiaItem2** interface. For more information about the **IWiaItem2** or **IWiaTransfer** interfaces and their methods, see the Microsoft Windows SDK documentation.

This section includes:

[IStream Data Transfer Driver Changes](istream-data-transfer-driver-changes.md)

[IStream Transfer Driver Example](istream-transfer-driver-example.md)

 

 




