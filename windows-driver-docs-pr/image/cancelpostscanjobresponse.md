---
title: CancelPostScanJobResponse
description: CancelPostScanJobResponse
ms.assetid: 5eccaa7d-943b-4269-93b2-b589c03df0a5
keywords: ["CancelPostScanJobResponse"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CancelPostScanJobResponse


The **CancelPostScanJobResponse** element is a scan server's response to a request from a client to cancel a post-scan job.

A DSM scan server sends a message that contains a **CancelPostScanJobResponse** element in response to a **CancelPostScanJobRequest** message received from a DSM device. The message from the scan server acknowledges receipt of the request from the device to cancel a post-scan job.

If the requested operation fails, the scan server sends the device an error message instead of a **CancelPostScanJobResponse** message. For more information about error messages, see [WS-DSP Operation Error Reporting](https://msdn.microsoft.com/library/windows/hardware/ff540619).

This element has no child elements.

For an example of how the **CancelPostScanJobResponse** element can be used in a SOAP message from a DSM scan server, see [CancelPostScanJobResponse Example](cancelpostscanjobresponse-example.md).

 

 





