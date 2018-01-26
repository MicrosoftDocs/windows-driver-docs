---
title: Security During Postmortem Debugging
description: Security During Postmortem Debugging
ms.assetid: 59c411c4-d829-4d1c-9820-e58188f0656c
keywords: ["security considerations, postmortem debugging", "postmortem debugging, security considerations"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security During Postmortem Debugging


## <span id="ddk_security_during_postmortem_debugging_dbg"></span><span id="DDK_SECURITY_DURING_POSTMORTEM_DEBUGGING_DBG"></span>


Only an administrator can enable [postmortem debugging](enabling-postmortem-debugging.md).

However, postmortem debugging is enabled for the entire system, not just for one user. Thus, after it has been enabled, any application crash will activate the debugger that has been chosen -- even if the current user does not have administrative privileges.

Also, a postmortem debugger inherits the same privileges as the application that crashed. Thus, if a Windows service such as CSRSS and LSASS crashes, the debugger will have very high-level privileges.

You should take this into account when choosing to enable postmortem debugging.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Security%20During%20Postmortem%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




