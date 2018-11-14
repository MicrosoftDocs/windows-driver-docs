---
title: Debugging a User-Mode Failure with KD
description: Debugging a User-Mode Failure with KD
ms.assetid: c7ef3c04-45bf-4e7b-bcc6-35fe2ffa43d1
keywords: ["KD, user-mode debugging with KD"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging a User-Mode Failure with KD


## <span id="ddk_debugging_user_mode_failures_with_kd_dbg"></span><span id="DDK_DEBUGGING_USER_MODE_FAILURES_WITH_KD_DBG"></span>


To properly debug user-mode failures, you need CDB or WinDbg. However, sometimes a user-mode exception will break into KD because no user-mode debugger is present. There are also times when it is helpful to monitor what specific user-mode processes are doing while debugging a kernel-mode problem.

By default, the kernel debugger attempts to load the first user-mode symbol that matches the address specified (for a **k**, **u**, or **ln** command).

Unfortunately, user-mode symbols are often not specified in the symbol path or the first symbol is not the correct one. If the symbols are not there, either copy them into the symbol path or use a [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command to point to the full symbol tree, and then use the [**.reload (Reload Module)**](-reload--reload-module-.md) command. If the wrong symbol is loaded, you can explicitly load a symbol by doing a **.reload &lt;binary.ext&gt;**.

Most of the Windows DLLs are rebased so they load at different addresses, but there are exceptions. Video adapters are the most common exceptions. There are dozens of video adapters that all load at the same base address, so KD will almost always find ati.dll (the first video symbol, alphabetically). For video, there is also a .sys file loaded that can be identified by using a [**!drivers**](-drivers.md) extension. With that information, you can issue a **.reload** to get the correct video DLLs. There are also times when the debugger gets confused and reloading specific symbols will help give the correct stack. Unassemble the functions to see if the symbols look correct.

Similar to the video DLLs, almost all executables load at the same address, so KD will report access. If you see a stack trace in access, do a [**!process**](-process.md) and then a **.reload** of the executable name given. If the executable does not have symbols in the symbol path, copy them there and do the **.reload** again.

Sometimes KD or WinDbg has trouble loading the correct user-mode symbols even when the full symbol tree is in the symbol path. In this case, ntdll.dll and kernel32.dll are two of the most common symbols that would be required. In the case of debugging CSRSS from KD, winsrv.dll and csrsrv.dll are also common DLLs to load.

 

 





