---
title: Features of Secure Mode
description: Features of Secure Mode
ms.assetid: bf40d018-7804-47df-9064-fb6f86da4b33
keywords: ["Secure Mode, overview"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Features of Secure Mode


## <span id="ddk_features_of_secure_mode_dbg"></span><span id="DDK_FEATURES_OF_SECURE_MODE_DBG"></span>


When Secure Mode is active, all commands that could be used to affect the *host* computer are deactivated, and there are some restrictions on symbol servers and debugger extensions.

The specific effects of Secure Mode are as follows:

-   The [**.attach (Attach to Process)**](-attach--attach-to-process-.md), [**.create (Create Process)**](-create--create-process-.md), [**.detach (Detach from Process)**](-detach--detach-from-process-.md), [**.abandon (Abandon Process)**](-abandon--abandon-process-.md), [**.kill (Kill Process)**](-kill--kill-process-.md), [**.tlist (List Process IDs)**](-tlist--list-process-ids-.md), [**.dump (Create Dump File)**](-dump--create-dump-file-.md), [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md), [**.writemem (Write Memory to File)**](-writemem--write-memory-to-file-.md), [**.netuse (Control Network Connections)**](-netuse--control-network-connections-.md), and [**.quit\_lock (Prevent Accidental Quit)**](-quit-lock--prevent-accidental-quit-.md) commands are not available.

-   The [File | Attach to a Process](file---attach-to-a-process.md), [File | Open Executable](file---open-executable.md), [Debug | Detach Debuggee](debug---detach-debuggee.md), [Debug | Stop Debugging](debug---stop-debugging.md), [File | Open Crash Dump](file---open-crash-dump.md) WinDbg menu commands are not available.

-   The [**.shell (Command Shell)**](-shell--command-shell-.md) command is not available.

-   Extension DLLs must be loaded from a local disk; they cannot be loaded from UNC paths.

-   Only the two standard types of extension DLLs (wdbgexts.h and dbgeng.h) are permitted. Other types of DLLs cannot be loaded as extensions.

-   If you are using a symbol server, there are several restrictions. Only SymSrv (symsrv.dll) is permitted; other symbol server DLLs will not be accepted. You may not use a downstream store for your symbols, and any existing downstream store will be ignored. HTTP and HTTPS connections are not permitted.

After it has been activated, Secure Mode cannot be turned off. For more information see, [Activating Secure Mode](activating-secure-mode.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Features%20of%20Secure%20Mode%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




