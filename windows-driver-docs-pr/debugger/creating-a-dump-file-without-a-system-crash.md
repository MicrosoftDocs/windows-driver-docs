---
title: Creating a Dump File Without a System Crash
description: Creating a Dump File Without a System Crash
ms.assetid: 747194d0-0aac-487a-acdc-ff27721606d4
keywords: ["dump file, creating without a system crash"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Creating a Dump File Without a System Crash


## <span id="ddk_creating_a_dump_file_without_a_system_crash_dbg"></span><span id="DDK_CREATING_A_DUMP_FILE_WITHOUT_A_SYSTEM_CRASH_DBG"></span>


If KD or WinDbg is performing kernel-mode debugging, it can cause a kernel-mode dump file to be written without crashing the target computer.

This dump file can be either a Complete Memory Dump or a Small Memory Dump. The Control Panel settings are not relevant to this action.

Whereas dump files caused by a system crash are written to the computer that has crashed, this dump file will be written to the host computer.

For details, see the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command.

 

 





