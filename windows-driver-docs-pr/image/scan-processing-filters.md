---
title: Scan Processing Filters
author: windows-driver-content
description: Scan Processing Filters
ms.assetid: 9c654af4-9492-4aca-95fb-4301084eefa7
ms.author: windowsdriverdev
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

 

 




