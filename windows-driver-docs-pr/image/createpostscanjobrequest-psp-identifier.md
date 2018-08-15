---
title: CreatePostScanJobRequest.PSP\_Identifier
description: CreatePostScanJobRequest.PSP\_Identifier
ms.assetid: 07a17b6a-7fcf-4734-9a8e-caf62e398553
keywords: ["CreatePostScanJobRequest.PSP_Identifier"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CreatePostScanJobRequest.PSP\_Identifier


The **PSP\_Identifier** element contains an identifier for a scan process.

To create a post-scan job, a DSM device sends a **CreatePostScanJobRequest** message to a DSM scan server. This message contains a **PSP\_Identifier** element to identify the scan process for the scan server to use to create the post-scan job. The scan process specifies how the job is to process the image data that it receives from the device.

When an IT administrator creates a scan process, the scan-management console (SMC) generates a GUID value to uniquely identify the scan process. A **PSP\_Identifier** element contains this GUID value.

 

 





