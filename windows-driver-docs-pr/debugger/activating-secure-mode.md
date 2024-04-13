---
title: Activating Secure Mode
description: Activating Secure Mode
keywords: ["Secure Mode, how to activate"]
ms.date: 05/23/2017
---

# Activating Secure Mode


## <span id="ddk_activating_secure_mode_dbg"></span><span id="DDK_ACTIVATING_SECURE_MODE_DBG"></span>


Secure Mode is only available for kernel-mode debugging. It must be activated before the debugging session has begun -- either on the debugger's command line, or when the debugger is completely dormant and is not yet being used as a server.

To activate Secure Mode, use one of the following methods:

-   The **-secure** [command-line option](command-line-options.md)

-   The [**.secure 1**](../debuggercmds/-secure--activate-secure-mode-.md) command

-   The [**.symopt+0x40000**](../debuggercmds/-symopt--set-symbol-options-.md) command

If you have an existing kernel debugging session and need to discover whether you are already in Secure Mode, use the [**.secure**](../debuggercmds/-secure--activate-secure-mode-.md) command with no arguments. This will tell you the current status of Secure Mode.

After Secure Mode has been activated, it cannot be turned off. Even ending the debugging session will not turn it off. Secure Mode persists as long as the debugger itself is running.

 

 