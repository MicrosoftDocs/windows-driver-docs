---
title: PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState
description: PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState
ms.assetid: 38819dd3-4689-423b-b9ff-1ecc83e32842
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState


The **JobCompletedState** element contains information about the state of a post-scan job that has completed.

When a post-scan job completes, the DSM scan server sends the DSM device a **PostScanJobEndStateEvent** message. This message contains a **JobCompletedState** element that indicates the status of the job at completion.

The **JobCompletedState** element and **JobState** element are defined similarly, but the text values defined for the **JobCompletedState** element are a subset of those defined for **JobState** element. Whereas the **JobCompletedState** element contains state information about a post-scan job that has completed, the **JobStateReasons** element contains information about a job that might not yet have completed.

This element can have the following values:

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted**  
The system terminated the post-scan job before it completed.

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>**Canceled**  
A control point canceled the post-scan job by sending a **CancelPostScanJobRequest** message or by some method that originated outside of Web Services.

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed**  
The post-scan job completed normally after processing of all the image data received from the WSD scan device.

Vendors can extend the preceding list of values for this element. Vendors can also use only a subset of the values in the preceding list.

This element has no sub-elements.

 

 





