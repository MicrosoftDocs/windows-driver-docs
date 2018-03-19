---
title: PostScanJobStatusEvent.JobStatus.JobState
description: PostScanJobStatusEvent.JobStatus.JobState
ms.assetid: b87471eb-c7dc-4235-b9f9-1ce80760f967
keywords: ["PostScanJobStatusEvent.JobStatus.JobState"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PostScanJobStatusEvent.JobStatus.JobState


The **JobState** element contains a value that indicates the current state of a post-scan job.

The **JobState** element supports the following values:

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted**  
The system terminated the post-scan job before it completed.

<span id="Canceled"></span><span id="canceled"></span><span id="CANCELED"></span>**Canceled**  
A control point canceled the post-scan job by sending a **CancelPostScanJobRequest** message or by some method outside of Web Services.

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed**  
The post-scan job completed normally after processing of all the image files sent to the job by the WSD scan device.

<span id="Creating"></span><span id="creating"></span><span id="CREATING"></span>**Creating**  
The post-scan job is currently being initialized.

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>**Pending**  
The post-scan job has been initialized and is waiting to begin processing.

<span id="Pending-Held"></span><span id="pending-held"></span><span id="PENDING-HELD"></span>**Pending-Held**  
The post-scan job is waiting to begin processing but is currently unavailable for scheduling. This state cannot be initiated by Web Services.

<span id="Processing"></span><span id="processing"></span><span id="PROCESSING"></span>**Processing**  
The post-scan job is currently processing image data.

<span id="Started"></span><span id="started"></span><span id="STARTED"></span>**Started**  
The post-scan job has been initialized but has not yet begun processing image data. This state is transient and typically occurs only during an event that causes a **PostScanJobStatusEvent** message to be sent.

<span id="Terminating"></span><span id="terminating"></span><span id="TERMINATING"></span>**Terminating**  
The post-scan job is in the process of being canceled after receiving a **CancelPostScanJobRequest** message or after being canceled by some method outside of Web Services.

Vendors can extend the preceding list of values for this element. Vendors can use a subset of the values in the preceding list.

This element has no sub-elements.

 

 





