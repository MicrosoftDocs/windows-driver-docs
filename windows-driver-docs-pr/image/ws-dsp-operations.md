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
ms.localizationpriority: medium
---

# WS-DSP Operations


The following operations are defined for WS-DSP and must be supported by conforming DSM Device and DSM Scan Server implementations:

**CancelPostScanJob -** cancels a post-scan job that is identified by the **JobToken**.

**CreatePostScanJob -** requests that the DSM Scan Server create a new post-scan job.

**EndPostScanJob** - indicates to the DSM Scan Server that all images of a specific post-scan job have been sent to the DSM Scan Server and that the DSM Scan Server can begin processing the images.

**GetPostScanJobElements -** requests that the DSM Scan Server return a specific set of data elements from the specified post-scan job.

**SendImage -** contains the image data of a single scan document that is sent by the DSM Device to the DSM Scan Server for processing as part of the specified post-scan job.

 

 




