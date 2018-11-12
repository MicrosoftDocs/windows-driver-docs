---
title: Security During Kernel-Mode Debugging
description: Security During Kernel-Mode Debugging
ms.assetid: 0dc78f83-a695-4b2c-a5cd-d7f365a9560f
keywords: ["security considerations, kernel-mode debugging", "local kernel debugging, security considerations"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





