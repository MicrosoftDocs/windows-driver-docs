---
title: Features of Secure Mode
description: Features of Secure Mode
keywords: ["Secure Mode, overview"]
ms.date: 05/23/2017
---

# Features of Secure Mode


## <span id="ddk_features_of_secure_mode_dbg"></span><span id="DDK_FEATURES_OF_SECURE_MODE_DBG"></span>


When Secure Mode is active, all commands that could be used to affect the *host* computer are deactivated, and there are some restrictions on symbol servers and debugger extensions.

The specific effects of Secure Mode are as follows:

-   The [**.attach (Attach to Process)**](../debuggercmds/-attach--attach-to-process-.md), [**.create (Create Process)**](../debuggercmds/-create--create-process-.md), [**.detach (Detach from Process)**](../debuggercmds/-detach--detach-from-process-.md), [**.abandon (Abandon Process)**](../debuggercmds/-abandon--abandon-process-.md), [**.kill (Kill Process)**](../debuggercmds/-kill--kill-process-.md), [**.tlist (List Process IDs)**](../debuggercmds/-tlist--list-process-ids-.md), [**.dump (Create Dump File)**](../debuggercmds/-dump--create-dump-file-.md), [**.opendump (Open Dump File)**](../debuggercmds/-opendump--open-dump-file-.md), [**.writemem (Write Memory to File)**](../debuggercmds/-writemem--write-memory-to-file-.md), [**.netuse (Control Network Connections)**](../debuggercmds/-netuse--control-network-connections-.md), and [**.quit\_lock (Prevent Accidental Quit)**](../debuggercmds/-quit-lock--prevent-accidental-quit-.md) commands are not available.

-   The **File | Attach to a Process**, **File | Open Executable**, **Debug | Detach Debuggee**, **Debug | Stop Debugging**, **File | Open Crash Dump** WinDbg menu commands are not available.

-   The [**.shell (Command Shell)**](../debuggercmds/-shell--command-shell-.md) command is not available.

-   Extension DLLs must be loaded from a local disk; they cannot be loaded from UNC paths.

-   Only the two standard types of extension DLLs (wdbgexts.h and dbgeng.h) are permitted. Other types of DLLs cannot be loaded as extensions.

-   If you are using a symbol server, there are several restrictions. Only SymSrv (symsrv.dll) is permitted; other symbol server DLLs will not be accepted. You may not use a downstream store for your symbols, and any existing downstream store will be ignored. HTTP and HTTPS connections are not permitted.

After it has been activated, Secure Mode cannot be turned off. For more information see, [Activating Secure Mode](activating-secure-mode.md).

 

 