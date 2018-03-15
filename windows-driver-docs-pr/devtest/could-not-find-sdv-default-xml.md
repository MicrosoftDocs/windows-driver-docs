---
title: Could not find Sdv-default.xml
description: Could not find Sdv-default.xml
ms.assetid: b8d928b0-8e6b-48de-98e2-554eb67c9a0b
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Could not find Sdv-default.xml


SDV reports this error when it cannot find the [global options file](global-and-local-options-files.md), sdv-default.xml, in the \\tools\\sdv\\data\\wdm or \\tools\\sdv\\data\\wdf subdirectories of the WDK. SDV creates the file in those directories when you install SDV and SDV requires that the files remain in those directories.

You can edit the values in the sdv-default.xml file in the \\tools\\sdv\\data\\wdm or \\tools\\sdv\\data\\wdf subdirectories, but you cannot move, delete, or rename them.

To create a custom options file for a particular driver (known as a [local options file](global-and-local-options-files.md)), copy the sdv-default.xml file from the \\tools\\sdv\\data\\wdm or \\tools\\sdv\\data\\wdf subdirectories to the driver's sources directory.

 

 





