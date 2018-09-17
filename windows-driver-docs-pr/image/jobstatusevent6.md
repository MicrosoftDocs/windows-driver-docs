---
title: JobStatusEvent
description: JobStatusEvent
ms.assetid: fb9addb9-1a55-4236-a80d-a59c8772ff99
keywords: ["JobStatusEvent"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# JobStatusEvent


The scanner sends the **JobStatusEvent** event to the control point when a scan job's status has changed. The first **JobStatusEvent** message sent will generally have the **JobId** of the scan job and a **JobState** of *Started*. The body of the **JobStatusEvent** message consists of the following data elements:

The **JobStatusEvent** event supports the following sub-element:

[JobStatusEvent.JobStatus](jobstatusevent-jobstatus.md)

 

 





