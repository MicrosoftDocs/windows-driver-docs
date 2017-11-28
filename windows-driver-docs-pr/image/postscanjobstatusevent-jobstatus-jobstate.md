---
title: PostScanJobStatusEvent.JobStatus.JobState
description: PostScanJobStatusEvent.JobStatus.JobState
ms.assetid: b87471eb-c7dc-4235-b9f9-1ce80760f967
keywords: ["PostScanJobStatusEvent.JobStatus.JobState"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PostScanJobStatusEvent.JobStatus.JobState%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




