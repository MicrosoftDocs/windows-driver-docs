---
title: Uploading Data to a Device
description: Uploading Data to a Device
ms.assetid: 50fc5f56-3758-4151-9748-dd88544006f1
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




