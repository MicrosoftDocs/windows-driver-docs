---
title: EndPostScanJobResponse
description: EndPostScanJobResponse
ms.assetid: 2433b365-a401-4ce8-a4fd-2aefd3181ddc
keywords: ["EndPostScanJobResponse"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EndPostScanJobResponse


The **EndPostScanJobResponse** element is a response to a request from a client to end a post-scan job.

A DSM scan server sends a message that contains an **EndPostScanJobResponse** element in response to an [EndPostScanJobRequest](endpostscanjobrequest.md) message received from a DSM device. The message from the scan server acknowledges receipt of the request from the device to end a post-scan job.

If the requested operation fails, the scan server sends the device an error message instead of an **EndPostScanJobResponse** message. For more information about error messages, see [WS-DSP Operation Error Reporting](https://msdn.microsoft.com/library/windows/hardware/ff540619).

The **EndPostScanJobResponse** element does not have any child elements.

For an example of using the **EndPostScanJobResponse** element, see [EndPostScanJobResponse Example](endpostscanjobresponse-example.md).

 

 





