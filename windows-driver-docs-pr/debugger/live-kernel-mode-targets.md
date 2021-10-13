---
title: Live Kernel-Mode Targets
description: Live Kernel-Mode Targets
keywords: ["targets, live kernel-mode", "kernel-mode targets"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Live Kernel-Mode Targets


## <span id="ddk_live_kernel_mode_targets_dbx"></span><span id="DDK_LIVE_KERNEL_MODE_TARGETS_DBX"></span>


To attach the [debugger engine](introduction.md#debugger-engine) to a target computer for kernel-mode debugging, use the method [**AttachKernel**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-attachkernel).

**Note**   The engine doesn't completely attach to the kernel until the [**WaitForEvent**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-waitforevent) method has been called. Only after the kernel has generated an event -- for example, the [initial breakpoint](initial-breakpoint.md) -- does it become available in the debugger session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

If the debugger engine is attached to a kernel which is not the local kernel and the connection is not an eXDI connection, the connection options used to find the target computer can be queried using [**GetKernelConnectionOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-getkernelconnectionoptions). The connection can also be re-synchronized or the connection speed changed using [**SetKernelConnectionOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-setkernelconnectionoptions).

The debugger can attach to the local kernel, but only in a limited way and only if the computer was booted with the **/debug** boot switch. (In some Windows installations, local kernel debugging is supported when other switches are used, such as **/debugport**, but this is not a guaranteed feature of Windows and should not be relied on.) [**IsKernelDebuggerEnabled**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugclient5-iskerneldebuggerenabled) is used to determine if the local computer is available for debugging. For more information about kernel debugging on a single machine, see [Performing Local Kernel Debugging](performing-local-kernel-debugging.md).

 

