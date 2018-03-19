---
title: CreatePostScanJobRequest.UserIdentifier
description: CreatePostScanJobRequest.UserIdentifier
ms.assetid: A205CE50-B4B4-4D99-A8E6-61871DF4FEF5
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CreatePostScanJobRequest.UserIdentifier


The **UserIdentifier** element contains an Security Identifier (SID) for the user that is submitting the **CreatePostScanJobRequest**

To create a post-scan job, a DSM device sends a **CreatePostScanJobRequest** message to a DSM scan server. This message contains a **UserIdentifier** element to identify the user for the scan server to use to create the post-scan job.

A **UserIdentifier** element contains a string value in the format of a Security Identifier (SID).

 

 





