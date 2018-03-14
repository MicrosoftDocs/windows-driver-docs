---
title: PostScanJobStatusEvent
description: PostScanJobStatusEvent
ms.assetid: 43368781-c235-4367-b897-22ef8da526e3
keywords: ["PostScanJobStatusEvent"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PostScanJobStatusEvent


The **PostScanJobStatusEvent** element notifies the DSM device that the status of the current post-scan job has changed.

When the status of the post-scan job changes, the DSM scan server notifies the DSM device of the event by sending the device a message that contains a **PostScanJobStatusEvent** element. This element contains information about the job status change, including the new job state, the reason for the job state change, the status of the scan processing filters, and the job start time.

The **PostScanJobStatusEvent** element supports the following sub-element:

[PostScanJobStatusEvent.JobStatus](postscanjobstatusevent-jobstatus.md)

 

 





