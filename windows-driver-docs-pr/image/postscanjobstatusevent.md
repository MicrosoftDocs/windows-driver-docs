---
title: PostScanJobStatusEvent
description: PostScanJobStatusEvent
ms.assetid: 43368781-c235-4367-b897-22ef8da526e3
keywords: ["PostScanJobStatusEvent"]
---

# PostScanJobStatusEvent


The **PostScanJobStatusEvent** element notifies the DSM device that the status of the current post-scan job has changed.

When the status of the post-scan job changes, the DSM scan server notifies the DSM device of the event by sending the device a message that contains a **PostScanJobStatusEvent** element. This element contains information about the job status change, including the new job state, the reason for the job state change, the status of the scan processing filters, and the job start time.

The **PostScanJobStatusEvent** element supports the following sub-element:

[PostScanJobStatusEvent.JobStatus](postscanjobstatusevent-jobstatus.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PostScanJobStatusEvent%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




