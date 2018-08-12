---
title: PostScanJobEndStateEvent
description: PostScanJobEndStateEvent
ms.assetid: 686068cd-aa42-43d6-aa56-865243eca020
keywords: ["PostScanJobEndStateEvent"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# PostScanJobEndStateEvent


The **PostScanJobEndStateEvent** element notifies the DSM device that a post-scan job has completed.

When a post-scan job completes, the DSM scan server notifies the DSM device of the event by sending the device a message that contains a **PostScanJobEndStateEvent** element. This element contains information about the final status of the job, including the job token, the job state, the reason for the job state, the status of the [scan processing filters](https://msdn.microsoft.com/library/windows/hardware/ff547945) in the job, and the job start and end times.

The **PostScanJobEndStateEvent** supports the following sub-element:

[PostScanJobEndStateEvent.PostScanJobEndState](postscanjobendstateevent-postscanjobendstate.md)

 

 





