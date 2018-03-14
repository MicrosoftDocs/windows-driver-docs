---
title: FileShareConfig.FileShares.ShareUNC
description: FileShareConfig.FileShares.ShareUNC
ms.assetid: 8bcc73e1-7764-42d4-b0da-a2662e09a83a
keywords: ["FileShareConfig.FileShares.ShareUNC"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FileShareConfig.FileShares.ShareUNC


The **ShareUNC** element defines a single network file location that the file share processing filter will use to save the scanned images for the current post-scan job.

The DSM Scan Server will try to save the scanned images to a directory in the share contained in this element. The directory name is *user@domain* based on the submitting user for the current PostScan job.

This element has no sub-elements.

 

 





