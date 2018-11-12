---
title: Using the RPC Debugger Extensions
description: Using the RPC Debugger Extensions
ms.assetid: 55303052-c5b3-4fe7-96ce-6f41a45a2358
keywords: ["RPC extensions (rpcexts.dll)", "RPC debugging, extensions (rpcexts.dll)", "rpcexts.dll (RPC extensions)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using the RPC Debugger Extensions


## <span id="ddk_using_the_rpc_debugger_extensions_dbg"></span><span id="DDK_USING_THE_RPC_DEBUGGER_EXTENSIONS_DBG"></span>


A variety of RPC debugger extensions are exported from Rpcexts.dll.

The RPC extensions used to display RPC state information will only run in user mode. They can be used from CDB (or NTSD) or from user-mode WinDbg.

The user-mode debugger must have a target application, but the target is irrelevant to the RPC extensions. If the debugger is not already running, you can simply start it with an uninteresting target (for example, **windbg notepad** or **cdb winmine**). Then, use [**CTRL+C**](ctrl-c--break-.md) in CDB or [Debug | Break](debug---break.md) in WinDbg to stop the target and access the Debugger Command window.

If you need to analyze RPC state information from a remote computer, you should start the user-mode debugger on the computer that needs to be analyzed, and then use [Remote Debugging](remote-debugging.md).

Accessing RPC state information through the debugger is especially useful in stress environments, or when a debugger already happens to be running.

 

 





