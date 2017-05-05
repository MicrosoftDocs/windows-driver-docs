---
title: Data Transfers
author: windows-driver-content
description: Data Transfers
ms.assetid: 55ef8125-40d3-44f3-8520-cc3a0912c3d2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data Transfers


## <a href="" id="ddk-data-transfers-si"></a>


The main purpose of a WIA minidriver is to transfer data from the device to the application. For a camera, the data may be previously captured pictures, audio, or video clips. For a scanner, the device may need to transfer the data as it acquires it from the scanner.

In operating systems before Windows Vista, WIA had two ways of transferring data from the device to the application, both based on [TYMED](understanding-tymed.md). The first was an in-memory transfer, in which the device returned bands of image data to the WIA service. The second way was a file transfer to the WIA service. Note that the WIA service received the data and forwarded it to the requesting application.

In Windows Vista, a new type of transfer is available: **IStream**-based transfer. This transfer model relies on two interfaces (**IWiaItem2** and **IWiaDevMgr2**) that are new for Windows Vista. (Both of these interfaces are described in the Microsoft Windows SDK documentation.) There is a compatibility layer that allows limited interaction between Windows Vista and legacy drivers and applications. This compatibility layer has some limitations, which are discussed in the [Achieving Compatibility with IStream Transfers](achieving-compatibility-with-istream-transfers.md) section.

This section contains the following topics:

[In-Memory Transfers](in-memory-transfers.md)

[File Transfers](file-transfers.md)

[IStream Data Transfer](istream-data-transfers.md)

For more information about data transfers, see [Transferring Data to a WIA Application](transferring-data-to-a-wia-application.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Data%20Transfers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


