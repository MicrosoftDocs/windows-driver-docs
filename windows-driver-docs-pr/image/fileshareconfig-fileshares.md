---
title: FileShareConfig.FileShares
description: FileShareConfig.FileShares
ms.assetid: 7077cdb3-3d5c-4228-85f1-7c3b648ba672
keywords: ["FileShareConfig.FileShares"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FileShareConfig.FileShares


The **FileShares** element defines the set of network file locations the file share processing filter will use to save the scanned images for the current PostScan job. The **FileShares** element can contain one or more **ShareUNC** elements. The DSM Scan Server will try to save the scanned images to each of the shares specified in a **ShareUNC** element.

The **FileShares** element supports the following sub-element:

[FileShareConfig.FileShares.ShareUNC](fileshareconfig-fileshares-shareunc.md)

 

 





