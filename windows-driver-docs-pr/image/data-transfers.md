---
title: Data Transfers
description: Data Transfers
ms.assetid: 55ef8125-40d3-44f3-8520-cc3a0912c3d2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Transfers





The main purpose of a WIA minidriver is to transfer data from the device to the application. For a camera, the data may be previously captured pictures, audio, or video clips. For a scanner, the device may need to transfer the data as it acquires it from the scanner.

In operating systems before Windows Vista, WIA had two ways of transferring data from the device to the application, both based on [TYMED](understanding-tymed.md). The first was an in-memory transfer, in which the device returned bands of image data to the WIA service. The second way was a file transfer to the WIA service. Note that the WIA service received the data and forwarded it to the requesting application.

In Windows Vista, a new type of transfer is available: **IStream**-based transfer. This transfer model relies on two interfaces (**IWiaItem2** and **IWiaDevMgr2**) that are new for Windows Vista. (Both of these interfaces are described in the Microsoft Windows SDK documentation.) There is a compatibility layer that allows limited interaction between Windows Vista and legacy drivers and applications. This compatibility layer has some limitations, which are discussed in the [Achieving Compatibility with IStream Transfers](achieving-compatibility-with-istream-transfers.md) section.

This section contains the following topics:

[In-Memory Transfers](in-memory-transfers.md)

[File Transfers](file-transfers.md)

[IStream Data Transfer](istream-data-transfers.md)

For more information about data transfers, see [Transferring Data to a WIA Application](transferring-data-to-a-wia-application.md).

 

 




