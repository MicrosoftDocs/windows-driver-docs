---
title: Post-Scan Job Execution
author: windows-driver-content
description: Post-Scan Job Execution
ms.assetid: 3ce8eee6-0aaa-43da-b3ca-d12063c01d7d
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Post-Scan Job Execution


After the DSM Device has scanned an image, the DSM Device creates a post-scan job on the DSM Scan Server and uses Distributed Scan Processing Web Service (WS-DSP) to send the scanned image data to a DSM Scan Server for post-scan processing. The DSM Scan Server performs the post-scan processing that is described in the post-scan instructions of the selected scan process. The post-scan job ends when the DSM Scan Server has processed all image data sent by the DSM Device for the post-scan job.

Distributed scan management supports only device initiated scan jobs. This means that a scan job must be initiated by a user who interacts directly with a DSM Device. The DSM Device must retrieve a scan process from a directory service. The DSM Device must include the post-scan instructions from the scan process with the image data that is transferred to the DSM Scan Server.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Post-Scan%20Job%20Execution%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


