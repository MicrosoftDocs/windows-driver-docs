---
title: Uploading Data to a Device
author: windows-driver-content
description: Uploading Data to a Device
ms.assetid: 50fc5f56-3758-4151-9748-dd88544006f1
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Uploading Data to a Device


To transfer data from the application to the device, you must use the **IWiaTransfer::Upload** method. The application provides the data stream, which is used as the data source rather than the destination. Similarly, the driver calls **IStream::Read** instead of **IStream::Write** in the upload situation.

Notice that this upload procedure can be performed only on an item that already exists. This procedure cannot be completed if the application attempts to upload a new file to a device with storage, because there is no item to represent that file yet.

To create new content on the device, such as a new file on the device storage, the application should:

1.  Create a WIA item by calling **IWiaItem2::CreateChildItem** on the folder that will be the item's parent.

2.  Call **QueryInterface** for **IWiaTransfer**, and then call **IWiaTransfer::Upload**.

The driver should process the call to **IWiaTransfer::Upload** accordingly. For example, if the WIA item is a new item, the driver should create the file and save the contents of the source stream that is provided in **IWiaTransfer::Upload** to the device storage.

The **IWiaTransfer**, **IWiaItem2**, **IwiaDataTransfer**, and **IStream** interfaces are described in the Microsoft Windows SDK documentation.

This section includes:

[Driver Behavior on Upload](driver-behavior-on-upload.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Uploading%20Data%20to%20a%20Device%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


