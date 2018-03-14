---
title: Access is denied
description: Access is denied
ms.assetid: 7126a065-aa6a-47c3-9cfb-0c6d5feeb176
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Access is denied


SDV cannot perform the requested operation because it cannot access a required file. Confirm that you have permission to read, edit, and delete files in the driver's sources directory and in the \\tools\\sdv subdirectories of the WDK. These permissions are required to run SDV.

If this message appears when you use a **staticdv /clean** command, confirm that you have permission to edit and delete files in the local driver source directory. If you do, use the **del** command or Windows Explorer to delete the SDV directory in the local driver source directory and then run the **staticdv /clean** command again.

 

 





