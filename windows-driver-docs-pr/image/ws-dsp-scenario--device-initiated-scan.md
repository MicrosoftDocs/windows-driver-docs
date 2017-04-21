---
title: WS-DSP Scenario Device-Initiated Scan
author: windows-driver-content
description: WS-DSP Scenario Device-Initiated Scan
ms.assetid: aa301f2c-64f6-4b4f-bb48-f3b2a10ea08d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WS-DSP Scenario: Device-Initiated Scan


An end-user wants to scan a document for storage in a shared folder. From the directory service, the DSM Device retrieves the scan processes that are associated with the user and displays them to the user. Using a user interface on the DSM Device, the user selects the appropriate scan process for the scan job, places the document on the DSM Device and presses the scan button on the DSM Device.

The DSM Device scans the document using the settings specified in the scan ticket of the selected scan process. After scanning an image of the document, the DSM Device submits a **CreatePostScanJob** operation to the DSM Scan Server for post-scan processing of the scanned images. The **CreatePostScanJob** operation contains the post-scan instructions from the scan process. The DSM Device submits the image data of each scanned document to the DSM Scan Server in a **SendImage** operation and sends an **EndPostScanJob** operation after the last **SendImage** operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WS-DSP%20Scenario:%20Device-Initiated%20Scan%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


