---
title: PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedStateReasons
description: PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedStateReasons
ms.assetid: d294c763-a3ef-4e24-b2c5-6066936324d0
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedStateReasons"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedStateReasons


The **JobCompletedStateReasons** element contains a collection of one or more **JobStateReason** elements that indicate the reasons that a post-scan job completed.

When a post-scan job completes, the DSM scan server sends the DSM device a **PostScanJobEndStateEvent** message. This message contains a **JobCompletedStateReasons** element that gives one or more reasons that the job completed.

The **JobCompletedStateReasons** element and **JobStateReasons** element are defined similarly and have the same sub-elements. Whereas the **JobCompletedStateReasons** element contains status information about a post-scan job that has completed, the **JobStateReasons** element contains status information about a job that might not yet have completed.

The **JobCompletedStateReasons** element supports the following sub-element:

[PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedStateReasons.JobStateReason](postscanjobendstateevent-postscanjobendstate-jobcompletedstatereasons-.md)

 

 





