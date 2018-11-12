---
title: Using Debugger Extensions
description: This topic describes using debugger extensions
ms.assetid: 55de0cbd-c6ba-40af-a932-2f9e57f1e8ec
keywords: extension commands, debugger extensions
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Debugger Extensions


## <span id="ddk_debugger_extensions_dbg"></span><span id="DDK_DEBUGGER_EXTENSIONS_DBG"></span>


Visual Studio, WinDbg, KD, and CDB all allow the use of debugger extension commands. These extensions give these three Microsoft debuggers a great degree of power and flexibility.

Debugger extension commands are used much like the standard debugger commands. However, while the built-in debugger commands are part of the debugger binaries themselves, debugger extension commands are exposed by DLLs distinct from the debugger.

This allows you to write new debugger commands which are tailored to your specific need. In addition, a number of debugger extension DLLs are shipped with the debugging tools themselves.

This section includes:

[Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md)

[Using Debugger Extension Commands](using-debugger-extension-commands.md)

[Writing New Debugger Extensions](writing-new-debugger-extensions.md)

 

 





