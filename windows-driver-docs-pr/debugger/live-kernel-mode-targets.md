---
title: Live Kernel-Mode Targets
description: Live Kernel-Mode Targets
ms.assetid: 88820097-4a47-428d-88dd-d0a08e5debdc
keywords: ["targets, live kernel-mode", "kernel-mode targets"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Live Kernel-Mode Targets


## <span id="ddk_live_kernel_mode_targets_dbx"></span><span id="DDK_LIVE_KERNEL_MODE_TARGETS_DBX"></span>


To attach the [debugger engine](introduction.md#debugger-engine) to a target computer for kernel-mode debugging, use the method [**AttachKernel**](https://msdn.microsoft.com/library/windows/hardware/ff538145).

**Note**   The engine doesn't completely attach to the kernel until the [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) method has been called. Only after the kernel has generated an event -- for example, the [initial breakpoint](initial-breakpoint.md) -- does it become available in the debugger session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

If the debugger engine is attached to a kernel which is not the local kernel and the connection is not an eXDI connection, the connection options used to find the target computer can be queried using [**GetKernelConnectionOptions**](https://msdn.microsoft.com/library/windows/hardware/ff546970). The connection can also be re-synchronized or the connection speed changed using [**SetKernelConnectionOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556729).

The debugger can attach to the local kernel, but only in a limited way and only if the computer was booted with the **/debug** boot switch. (In some Windows installations, local kernel debugging is supported when other switches are used, such as **/debugport**, but this is not a guaranteed feature of Windows and should not be relied on.) [**IsKernelDebuggerEnabled**](https://msdn.microsoft.com/library/windows/hardware/ff551088) is used to determine if the local computer is available for debugging. For more information about kernel debugging on a single machine, see [Performing Local Kernel Debugging](performing-local-kernel-debugging.md).

 

 





