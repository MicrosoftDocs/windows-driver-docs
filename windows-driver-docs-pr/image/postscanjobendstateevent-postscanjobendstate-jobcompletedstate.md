---
title: PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState
description: PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState
MS-HAID:
- 'dsm\_ref\_dsp\_6765b8dc-2c65-42b2-95ea-8db42cd47241.xml'
- 'image.postscanjobendstateevent\_postscanjobendstate\_jobcompletedstate'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 38819dd3-4689-423b-b9ff-1ecc83e32842
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PostScanJobEndStateEvent.PostScanJobEndState.JobCompletedState%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




