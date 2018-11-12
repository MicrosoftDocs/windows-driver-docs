---
title: Forcing a System Crash from the Debugger
description: Forcing a System Crash from the Debugger
ms.assetid: 7d7d9b07-00a3-4f87-8eb9-01b3f2fa312f
keywords: ["system crash, causing from debugger", "bug check, causing from debugger", "forcing system crash from debugger"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Forcing a System Crash from the Debugger


## <span id="ddk_forcing_a_system_crash_from_the_debugger_dbg"></span><span id="DDK_FORCING_A_SYSTEM_CRASH_FROM_THE_DEBUGGER_DBG"></span>


If KD or WinDbg is performing kernel-mode debugging, it can force a system crash to occur. This is done by entering the [**.crash (Force System Crash)**](-crash--force-system-crash-.md) command at the command prompt. (If the target computer does not crash immediately, follow this with the [**g (Go)**](g--go-.md) command.)

When this command is issued, the system will call **KeBugCheck** and issue [**bug check 0xE2**](bug-check-0xe2--manually-initiated-crash.md) (MANUALLY\_INITIATED\_CRASH). Unless crash dumps have been disabled, a crash dump file is written at this point.

After the crash dump file has been written, the kernel debugger on the host computer will be alerted and can be used to actively debug the crashed target.

 

 





