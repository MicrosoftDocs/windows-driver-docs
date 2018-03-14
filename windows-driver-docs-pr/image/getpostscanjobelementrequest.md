---
title: GetPostScanJobElementRequest
description: GetPostScanJobElementRequest
ms.assetid: 37f6e28f-57c8-4f49-baed-2ba83dfdeda7
keywords: ["GetPostScanJobElementRequest"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetPostScanJobElementRequest


The **GetPostScanJobElementsRequest** element requests a set of job elements from a post-scan job.

A DSM device sends a message that contains a **GetPostScanJobElementRequest** element to the DSM scan server to obtain a collection of job elements. In response, the scan server sends the device a message that contains a [GetPostScanJobElementResponse](getpostscanjobelementresponse.md) element. The response from the scan server contains the job elements requested in the message from the device.

The **Name** element is used to request Job elements.

The **GetPostScanJobElementsRequest** supports the following sub-elements:

[GetPostScanJobElementsRequest.JobToken](getpostscanjobelementsrequest-jobtoken.md)

[GetPostScanJobElementsRequest.RequestedElements](getpostscanjobelementsrequest-requestedelements.md)

For an example of using the **GetPostScanJobElementsRequest** element, see [GetPostScanJobElementsRequest Example](getpostscanjobelementsrequest-example.md).

 

 





