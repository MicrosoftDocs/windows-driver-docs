---
title: PostScanProcess.PostScanInstructions
description: PostScanProcess.PostScanInstructions
ms.assetid: fa60df79-4eaf-4cf8-b4f1-38218a47f744
keywords: ["PostScanProcess.PostScanInstructions"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# PostScanProcess.PostScanInstructions


The **PostScanInstructions** element contains instructions for processing the image files in a post-scan job.

A scan process contains a scan ticket, which specifies image-acquisition settings for the device, and a set of PostScan instructions. These instructions tell the job how to process the image data that it receives from the device. To create a post-scan job, a DSM device sends a **CreatePostScanJobRequest** message to a DSM scan server. The message contains a **PostScanInstructions** element that contains the instructions from the scan process.

The **PostScanInstructions** element supports the following sub-elements:

[PostScanInstructions.ContinueOnError](postscaninstructions-continueonerror.md)

[PostScanInstructions.DocumentRootName](postscaninstructions-documentrootname.md)

[PostScanInstructions.FiltersToProcess](postscaninstructions-filterstoprocess.md)

 

 





