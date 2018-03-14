---
title: Full User-Mode Dumps
description: Full User-Mode Dumps
ms.assetid: 7bf69ca0-afee-4c30-b24f-984e5d411f1b
keywords: ["dump file, full user-mode dump", "full user-mode dump"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Full User-Mode Dumps


## <span id="ddk_full_user_mode_dumps_dbg"></span><span id="DDK_FULL_USER_MODE_DUMPS_DBG"></span>


A *full user-mode dump* is the basic user-mode dump file.

This dump file includes the entire memory space of a process, the program's executable image itself, the handle table, and other information that will be useful to the debugger.

It is possible to "shrink" a full user-mode dump file into a minidump. Simply load the dump file into the debugger and then use the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command to save a new dump file in minidump format.

**Note**   Despite their names, the largest "minidump" file actually contains more information than the full user-mode dump. For example, **.dump /mf** or **.dump /ma** will create a larger and more complete file than **.dump /f**.

 

In user mode, **.dump /m\[***MiniOptions***\]** is the best choice. The dump files created with this switch can vary in size from very small to very large. By specifying the proper *MiniOptions* you can control exactly what information is included.

 

 





