---
title: CreatePostScanJobResponse.JobToken
description: CreatePostScanJobResponse.JobToken
ms.assetid: 00aae6a7-ed3d-46e0-9453-4010df840eb0
keywords: ["CreatePostScanJobResponse.JobToken"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CreatePostScanJobResponse.JobToken


The **JobToken** element contains a GUID value that uniquely identifies a post-scan job.

A DSM device sends a DSMscan server a **CreatePostScanJobRequest** message to request the creation of a post-scan job. If the request succeeds, the scan server generates a new job token and sends the device a **CreatePostScanJobResponse** message that contains the job token. The device and server use the job token to identify the job in subsequent communications.

This element has no child elements.

 

 





