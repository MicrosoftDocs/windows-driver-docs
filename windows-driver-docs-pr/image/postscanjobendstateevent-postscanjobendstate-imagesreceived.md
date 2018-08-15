---
title: PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived
description: PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived
ms.assetid: b043f34b-e43a-4dcd-a606-0f45a49f66d0
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# PostScanJobEndStateEvent.PostScanJobEndState.ImagesReceived


The **ImagesReceived** element contains an integer count of the image files received by a post-scan job.

The **ImagesReceived** element contains the number of image files that a DSM device has thus far sent to a DSM scan server during the course of a post-scan job.

In response to a message from a DSM device, a DSMscan server sends a message that contains the job elements requested by the device. The device can request a **JobStatus** element that includes an **ImagesReceived** element.

When a post-scan job completes, the DSM scan server sends the WSD Scan device a **PostScanJobEndStateEvent** message that contains information about the completion status of the job. This message contains a **PostScanJobEndState** element that includes an **ImagesReceived** element.

This element has no sub- elements.

 

 





