---
title: Security During Postmortem Debugging
description: Security During Postmortem Debugging
ms.assetid: 59c411c4-d829-4d1c-9820-e58188f0656c
keywords: ["security considerations, postmortem debugging", "postmortem debugging, security considerations"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Security During Postmortem Debugging


## <span id="ddk_security_during_postmortem_debugging_dbg"></span><span id="DDK_SECURITY_DURING_POSTMORTEM_DEBUGGING_DBG"></span>


Only an administrator can enable [postmortem debugging](enabling-postmortem-debugging.md).

However, postmortem debugging is enabled for the entire system, not just for one user. Thus, after it has been enabled, any application crash will activate the debugger that has been chosen -- even if the current user does not have administrative privileges.

Also, a postmortem debugger inherits the same privileges as the application that crashed. Thus, if a Windows service such as CSRSS and LSASS crashes, the debugger will have very high-level privileges.

You should take this into account when choosing to enable postmortem debugging.

 

 





