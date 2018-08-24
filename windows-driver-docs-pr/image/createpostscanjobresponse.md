---
title: CreatePostScanJobResponse
description: CreatePostScanJobResponse
ms.assetid: 9c3bda26-d306-4fbd-9884-11b404c5e761
keywords: ["CreatePostScanJobResponse"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CreatePostScanJobResponse


The **CreatePostScanJobResponse** element is a response to a request from a client to start a post-scan job.

A DSM scan server sends a message that contains a **CreatePostScanJobResponse** element in response to a **CreatePostScanJobRequest** message received from a DSM device. The message from the scan server acknowledges receipt of the request from the device to create a post-scan job.

If the requested operation fails, the scan server sends the device an error message instead of a **CreatePostScanJobResponse** message. For more information about error messages, see WS-DSP Operation Error Reporting.

The **CreatePostScanJobResponse** element supports the following sub-element:

[CreatePostScanJobResponse.JobToken](createpostscanjobresponse-jobtoken.md)

For an example of using the **CreatePostScanJobResponse** element, see [CreatePostScanJobResponse Example](createpostscanjobresponse-example.md).

 

 





