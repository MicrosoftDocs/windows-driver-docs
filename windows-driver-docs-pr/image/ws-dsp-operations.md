---
title: WS-DSP Operations
author: windows-driver-content
description: WS-DSP Operations
ms.assetid: abbf00c2-2448-40c4-a296-9e5c1d0810a5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WS-DSP Operations


The following operations are defined for WS-DSP and must be supported by conforming DSM Device and DSM Scan Server implementations:

**CancelPostScanJob -** cancels a post-scan job that is identified by the **JobToken**.

**CreatePostScanJob -** requests that the DSM Scan Server create a new post-scan job.

**EndPostScanJob** - indicates to the DSM Scan Server that all images of a specific post-scan job have been sent to the DSM Scan Server and that the DSM Scan Server can begin processing the images.

**GetPostScanJobElements -** requests that the DSM Scan Server return a specific set of data elements from the specified post-scan job.

**SendImage -** contains the image data of a single scan document that is sent by the DSM Device to the DSM Scan Server for processing as part of the specified post-scan job.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WS-DSP%20Operations%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


