---
title: Live Kernel-Mode Targets
description: Live Kernel-Mode Targets
ms.assetid: 88820097-4a47-428d-88dd-d0a08e5debdc
keywords: ["targets, live kernel-mode", "kernel-mode targets"]
---

# Live Kernel-Mode Targets


## <span id="ddk_live_kernel_mode_targets_dbx"></span><span id="DDK_LIVE_KERNEL_MODE_TARGETS_DBX"></span>


To attach the [debugger engine](introduction.md#debugger-engine) to a target computer for kernel-mode debugging, use the method [**AttachKernel**](https://msdn.microsoft.com/library/windows/hardware/ff538145).

**Note**   The engine doesn't completely attach to the kernel until the [**WaitForEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561229) method has been called. Only after the kernel has generated an event -- for example, the [initial breakpoint](initial-breakpoint.md) -- does it become available in the debugger session. See [Debugging Session and Execution Model](debugging-session-and-execution-model.md) for more details.

 

If the debugger engine is attached to a kernel which is not the local kernel and the connection is not an eXDI connection, the connection options used to find the target computer can be queried using [**GetKernelConnectionOptions**](https://msdn.microsoft.com/library/windows/hardware/ff546970). The connection can also be re-synchronized or the connection speed changed using [**SetKernelConnectionOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556729).

The debugger can attach to the local kernel, but only in a limited way and only if the computer was booted with the **/debug** boot switch. (In some Windows installations, local kernel debugging is supported when other switches are used, such as **/debugport**, but this is not a guaranteed feature of Windows and should not be relied on.) [**IsKernelDebuggerEnabled**](https://msdn.microsoft.com/library/windows/hardware/ff551088) is used to determine if the local computer is available for debugging. For more information about kernel debugging on a single machine, see [Performing Local Kernel Debugging](performing-local-kernel-debugging.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Live%20Kernel-Mode%20Targets%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




