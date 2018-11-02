---
title: When to Use This Technique
description: When to Use This Technique
ms.assetid: 40c9e2aa-35a3-4169-8305-bddc199a5c98
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# When to Use This Technique


## <span id="ddk_opening_a_crash_dump_dbg"></span><span id="DDK_OPENING_A_CRASH_DUMP_DBG"></span>


There are several situations in which it is useful, or even necessary, to [control user-mode debugging from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md):

-   When you need to perform user-mode debugging, but also need control over the Windows kernel that the user-mode target is running on or need to use some kernel-mode debugging features to analyze the problem.

-   When your user-mode target is a Windows process such as CSRSS or WinLogon. For a detailed description of how to debug these targets, see [Debugging CSRSS](debugging-csrss.md) and [Debugging WinLogon](debugging-winlogon.md).

-   When your user-mode target is a service application. For a detailed description of how to debug these targets, see [Debugging a Service Application](debugging-a-service-application.md).

 

 





