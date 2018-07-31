---
title: CDB and WinDbg
description: CDB and WinDbg
ms.assetid: 840dbe3c-510c-4064-ae6c-bb7525841621
keywords: ["dump file, CDB", "dump file, WinDbg"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CDB and WinDbg


## <span id="ddk_cdb_and_windbg_dbg"></span><span id="DDK_CDB_AND_WINDBG_DBG"></span>


CDB and WinDbg can create user-mode dump files in a variety of ways.

### <span id="creating_a_dump_file_automatically"></span><span id="CREATING_A_DUMP_FILE_AUTOMATICALLY"></span>Creating a Dump File Automatically

When an application error occurs, Windows can respond in several different ways, depending on the postmortem debugging settings. If these settings instruct a debugging tool to create a dump file, a user-mode memory dump file will be created. For more information, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

### <span id="creating_dump_files_while_debugging"></span><span id="CREATING_DUMP_FILES_WHILE_DEBUGGING"></span>Creating Dump Files While Debugging

When CDB or WinDbg is debugging a user-mode application, you can also the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command to create a dump file.

This command does not cause the target application to terminate. By selecting the proper command options, you can create a minidump file that contains exactly the amount of information you wish.

### <span id="shrinking_an_existing_dump_file"></span><span id="SHRINKING_AN_EXISTING_DUMP_FILE"></span>Shrinking an Existing Dump File

CDB and WinDbg can also be used to *shrink* a dump file. To do this, begin debugging an existing dump file, and then use the **.dump** command to create a dump file of smaller size.

 

 





