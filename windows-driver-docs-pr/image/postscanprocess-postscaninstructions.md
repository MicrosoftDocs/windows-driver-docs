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
---

# PostScanProcess.PostScanInstructions


The **PostScanInstructions** element contains instructions for processing the image files in a post-scan job.

A scan process contains a scan ticket, which specifies image-acquisition settings for the device, and a set of PostScan instructions. These instructions tell the job how to process the image data that it receives from the device. To create a post-scan job, a DSM device sends a **CreatePostScanJobRequest** message to a DSM scan server. The message contains a **PostScanInstructions** element that contains the instructions from the scan process.

The **PostScanInstructions** element supports the following sub-elements:

[PostScanInstructions.ContinueOnError](postscaninstructions-continueonerror.md)

[PostScanInstructions.DocumentRootName](postscaninstructions-documentrootname.md)

[PostScanInstructions.FiltersToProcess](postscaninstructions-filterstoprocess.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PostScanProcess.PostScanInstructions%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




