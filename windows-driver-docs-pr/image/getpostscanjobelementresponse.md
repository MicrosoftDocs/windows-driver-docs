---
title: GetPostScanJobElementResponse
description: GetPostScanJobElementResponse
ms.assetid: 564b2ce5-c041-4a71-b966-7eb0ca3365e6
keywords: ["GetPostScanJobElementResponse"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# GetPostScanJobElementResponse


The **GetPostScanJobElementsResponse** element is a response to a request from a client to obtain a set of job elements from a post-scan job.

A DSM scan server sends a message that contains a **GetPostScanJobElementsResponse** element in response to a [GetPostScanJobElementRequest](getpostscanjobelementrequest.md) message received from a DSM device. The message from the scan server contains the job elements requested by the device.

The **Name** element is used to request Job elements.

If the requested operation fails, the scan server sends the device an error message instead of a **GetPostScanJobElementsResponse** message. For more information about error messages, see [WS-DSP Operation Error Reporting](https://msdn.microsoft.com/library/windows/hardware/ff540619).

The **GetPostScanJobElementsResponse** element supports the following sub-element:

[GetPostScanJobElementsResponse.JobElements](getpostscanjobelementsresponse-jobelements.md)

For an example of using the **GetPostScanJobElementsResponse** element, see [GetPostScanJobElementsResponse Example](getpostscanjobelementsresponse-example.md)

 

 





