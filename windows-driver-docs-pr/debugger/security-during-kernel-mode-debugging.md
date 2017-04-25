---
title: Security During Kernel-Mode Debugging
description: Security During Kernel-Mode Debugging
ms.assetid: 0dc78f83-a695-4b2c-a5cd-d7f365a9560f
keywords: ["security considerations, kernel-mode debugging", "local kernel debugging, security considerations"]
---

# Security During Kernel-Mode Debugging


## <span id="ddk_security_during_kernel_mode_debugging_dbg"></span><span id="DDK_SECURITY_DURING_KERNEL_MODE_DEBUGGING_DBG"></span>


Security during kernel-mode debugging is never about protecting the *target* computer. The target is completely vulnerable to the debugger -- this is the very nature of debugging.

If a debugging connection was enabled during boot, it will remain vulnerable through the debugging port until its next boot.

However, you should be concerned about security on the *host* computer. In an ideal situation, the debugger runs as an application on your host computer, but does not interact with other applications on this computer. There are three possible ways in which security problems could arise:

-   If you use corrupt or destructive extension DLLs, they could cause your debugger to take unexpected actions, possibly affecting the host computer.

-   It is possible that corrupt or destructive symbol files could also cause your debugger to take unexpected actions, possibly affecting the host computer.

-   If you are running a remote debugging session, an unexpected client might attempt to link to your server. Or perhaps the client you are expecting might attempt to perform actions that you do not anticipate.

If you want to prevent a remote user from performing actions on your host computer, use [Secure Mode](secure-mode.md).

For suggestions on how to guard against unexpected remote connections, see [Security During Remote Debugging](security-during-remote-debugging.md).

If you are not performing remote debugging, you should still beware of bad symbol files and extension DLLs. Do not load symbols or extensions that you distrust!

### <span id="local_kernel_debugging"></span><span id="LOCAL_KERNEL_DEBUGGING"></span>Local Kernel Debugging

Only users who have debug privileges can start a local kernel debugging session. If you are the administrator of a machine that has multiple user accounts, you should be aware that any user with these privileges can start a local kernel debugging session, effectively giving them control of all processes on the computer -- and therefore giving them access to all peripherals as well.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Security%20During%20Kernel-Mode%20Debugging%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




