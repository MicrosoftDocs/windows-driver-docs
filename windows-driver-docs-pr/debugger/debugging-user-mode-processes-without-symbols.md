---
title: Debugging User-Mode Processes Without Symbols
description: Debugging User-Mode Processes Without Symbols
ms.assetid: ac742239-ed6b-4813-80d6-7b8eb84a0cb4
keywords: ["symbols, debugging without symbols"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging User-Mode Processes Without Symbols


## <span id="ddk_debugging_user_mode_processes_without_symbols_dbg"></span><span id="DDK_DEBUGGING_USER_MODE_PROCESSES_WITHOUT_SYMBOLS_DBG"></span>


It is important to have symbols on the faulting machine before starting the debugger for a user-mode failure. However, sometimes the debugger is started without symbols. If the problem is easily reproducible, you can just copy symbols and rerun. If, however, the problem may not occur again, some information can still be gleaned from the failure:

1.  To figure out what the addresses mean, you'll need a computer which matches the one with the error. It should have the same platform (x86 or x64) and be loaded with the same version of Windows.

2.  When you have the computer configured, copy the user-mode symbols and the binaries you want to debug onto the new machine.

3.  Start CDB or WinDbg on the symbol-less machine.

4.  If you don't know which application failed on the symbol-less machine, issue an [**| (Process Status)**](---process-status-.md) command. If that doesn't give you a name, break into KD on the symbol-less machine and do a [**!process 0 0**](-process.md), looking for the process ID given by the CDB command.

5.  When you have the two debuggers set up -- one with symbols which hasn't hit the error, and one which has hit the error but is without symbols -- issue a [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command on the symbol-less machine.

6.  On the machine with symbols, issue a [**u (Unassemble)**](u--unassemble-.md) command for each address given on the symbol-less stack. This will give you the stack trace for the error on the symbol-less machine.

7.  By looking at a stack trace you can see the module and function names involved in the call.

 

 





