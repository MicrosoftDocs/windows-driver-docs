---
title: Sys_error("slam.bp Permission denied") Exception
description: Sys_error("slam.bp Permission denied") Exception
ms.assetid: d7b2da9c-792f-4cdc-9945-2877f48f775f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sys\_error("slam.bp: Permission denied") Exception


SDV might encounter this exception and display this error message when an antivirus program is running on your computer and the driver source code directory is not excluded from runtime scanning. The simultaneous access of the same file might cause the permission denied exception during the driver verification process.

To avoid this error, configure your antivirus program so that it does not scan the driver source code directories when you run SDV.

 

 





