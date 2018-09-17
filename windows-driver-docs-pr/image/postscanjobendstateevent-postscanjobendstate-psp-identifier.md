---
title: PostScanJobEndStateEvent.PostScanJobEndState.PSP\_Identifier
description: PostScanJobEndStateEvent.PostScanJobEndState.PSP\_Identifier
ms.assetid: 57b7f75a-b2ef-4d8a-a620-82348b6d28e5
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.PSP_Identifier"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# PostScanJobEndStateEvent.PostScanJobEndState.PSP\_Identifier


The **PSP\_Identifier** element contains an identifier for a scan process.

To create a post-scan job, a DSM device sends a **CreatePostScanJobRequest** message to a DSM scan server. This message contains a **PSP\_Identifier** element to identify the scan process for the scan server to use to create the post-scan job. The scan process specifies how the job is to process the image data that it receives from the device.

When an IT administrator creates a scan process, the scan-management console (SMC) generates a GUID value to uniquely identify the scan process. A **PSP\_Identifier** element contains this GUID value.

In contrast to a **PSP\_Identifier** element, which identifies a scan process, a **JobToken** element identifies a post-scan job. A post-scan job is an instance of a scan process.

This element has no sub-elements.

 

 





