---
title: Scan Processing Filters
author: windows-driver-content
description: Scan Processing Filters
ms.assetid: 9c654af4-9492-4aca-95fb-4301084eefa7
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Scan Processing Filters


A DSM scan server uses software modules called *scan processing filters* to process image files received from a DSM device. The Distributed Scan Server in Windows Server 2008 R2 provides the following three filters:

<a href="" id="e-mail-filter"></a>*E-mail filter*  
This filter attaches the image data, as files, to an email message. The filter sends the messages to the user's email address or to a list of email addresses provided in the scan process or by the user.

<a href="" id="sharepoint-filter"></a>*SharePoint filter*  
This filter sends image data to one or more SharePoint sites specified in a scan process.

<a href="" id="file-share-filter"></a>*File share filter*  
This filter sends image data to one or more file shares specified in a scan process.

The three filters in the preceding list are supplied with the operating system. An administrator can create a scan process that uses one, two, or all of these filters to process the image files in a post-scan job.

After a user selects a scan process, the DSM device creates a post-scan job that uses only the filters specified in the scan process. See [CreatePostScanJobRequest](https://msdn.microsoft.com/library/windows/hardware/ff540230) for an example of a SOAP message that creates a post-scan job that uses all three of the available filters.

The current implementation of the Distributed Scan Server does not support the use of additional filters from third parties.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Scan%20Processing%20Filters%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


