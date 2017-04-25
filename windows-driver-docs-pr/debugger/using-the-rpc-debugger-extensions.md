---
title: Using the RPC Debugger Extensions
description: Using the RPC Debugger Extensions
ms.assetid: 55303052-c5b3-4fe7-96ce-6f41a45a2358
keywords: ["RPC extensions (rpcexts.dll)", "RPC debugging, extensions (rpcexts.dll)", "rpcexts.dll (RPC extensions)"]
---

# Using the RPC Debugger Extensions


## <span id="ddk_using_the_rpc_debugger_extensions_dbg"></span><span id="DDK_USING_THE_RPC_DEBUGGER_EXTENSIONS_DBG"></span>


A variety of RPC debugger extensions are exported from Rpcexts.dll.

The RPC extensions used to display RPC state information will only run in user mode. They can be used from CDB (or NTSD) or from user-mode WinDbg.

The user-mode debugger must have a target application, but the target is irrelevant to the RPC extensions. If the debugger is not already running, you can simply start it with an uninteresting target (for example, **windbg notepad** or **cdb winmine**). Then, use [**CTRL+C**](https://msdn.microsoft.com/library/windows/hardware/ff540312) in CDB or [Debug | Break](https://msdn.microsoft.com/library/windows/hardware/ff541727) in WinDbg to stop the target and access the Debugger Command window.

If you need to analyze RPC state information from a remote computer, you should start the user-mode debugger on the computer that needs to be analyzed, and then use [Remote Debugging](remote-debugging.md).

Accessing RPC state information through the debugger is especially useful in stress environments, or when a debugger already happens to be running.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20RPC%20Debugger%20Extensions%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




