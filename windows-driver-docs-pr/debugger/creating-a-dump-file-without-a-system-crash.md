---
title: Creating a Dump File Without a System Crash
description: Creating a Dump File Without a System Crash
keywords: ["dump file, creating without a system crash"]
ms.date: 05/23/2017
---

# Creating a Dump File Without a System Crash


## <span id="ddk_creating_a_dump_file_without_a_system_crash_dbg"></span><span id="DDK_CREATING_A_DUMP_FILE_WITHOUT_A_SYSTEM_CRASH_DBG"></span>


If KD or WinDbg is performing kernel-mode debugging, it can cause a kernel-mode dump file to be written without crashing the target computer.

This dump file can be either a Complete Memory Dump or a Small Memory Dump. The Control Panel settings are not relevant to this action.

Whereas dump files caused by a system crash are written to the computer that has crashed, this dump file will be written to the host computer.

For details, see the [**.dump (Create Dump File)**](../debuggercmds/-dump--create-dump-file-.md) command.

 

 