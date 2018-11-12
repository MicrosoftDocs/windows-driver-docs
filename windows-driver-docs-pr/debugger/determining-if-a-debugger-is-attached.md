---
title: Determining if a Debugger is Attached
description: Determining if a Debugger is Attached
ms.assetid: 78f7d90a-459c-4967-a980-3f8d6339eb77
keywords: ["determining if a debugger is attached", "KdRefreshDebuggerNotPresent function", "KD_DEBUGGER_ENABLED global variable", "KD_DEBUGGER_NOT_PRESENT global variable"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Determining if a Debugger is Attached


## <span id="ddk_determining_if_a_debugger_is_attached_dbg"></span><span id="DDK_DETERMINING_IF_A_DEBUGGER_IS_ATTACHED_DBG"></span>


Kernel-mode code can determine the status of kernel debugging by using the following variables and routines:

-   (Windows XP and later) The KD\_DEBUGGER\_ENABLED global kernel variable indicates whether kernel debugging is enabled.

-   (Windows XP and later) The KD\_DEBUGGER\_NOT\_PRESENT global kernel variable indicates whether a kernel debugger is currently attached.

-   (Windows Server 2003 and later) The **KdRefreshDebuggerNotPresent** routine refreshes the value of KD\_DEBUGGER\_NOT\_PRESENT.

For complete documentation, see the Windows Driver Kit.

 

 





