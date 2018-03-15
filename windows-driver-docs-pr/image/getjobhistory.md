---
title: GetJobHistory
description: GetJobHistory
ms.assetid: 330351fd-8a75-4e3c-b3f0-3211144393e9
keywords: ["GetJobHistory"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GetJobHistory


The **GetJobHistory** operation requests a summary list of the scan jobs that the scanner has recently completed. The returned list contains information about the scan jobs such as **JobId**, **JobOriginatingUserName***,* and the **JobName**.

The amount of data returned in this operation is device specific and depends on the amount of scan job history data that the scanner maintains.

To retrieve more detailed information about a scan job, use the **GetJobElements** operation.

The **GetJobHistory** operation supports the following sub-elements:

[GetJobHistoryRequest](getjobhistoryrequest2.md)

[GetJobHistoryResponse](getjobhistoryresponse4.md)

 

 





