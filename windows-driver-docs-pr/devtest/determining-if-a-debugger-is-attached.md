---
title: Determining if a Debugger is Attached
description: Determining if a Debugger is Attached
ms.assetid: b40482c4-7186-4632-b1d9-3c91a415b7c8
keywords:
- debugging code WDK , attached debuggers
- attached debuggers WDK
- status information WDK debugging
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining if a Debugger is Attached


## <span id="ddk_determining_if_a_debugger_is_attached_tools"></span><span id="DDK_DETERMINING_IF_A_DEBUGGER_IS_ATTACHED_TOOLS"></span>


You may wish to take certain actions with your driver if a kernel debugger is currently attached.

To determine the status of kernel debugging, the following variables and routines are useful:

-   (Microsoft Windows XP and later) The [**KD\_DEBUGGER\_ENABLED**](https://msdn.microsoft.com/library/windows/hardware/ff548118) global kernel variable indicates whether kernel debugging is enabled.

-   (Windows XP and later) The [**KD\_DEBUGGER\_NOT\_PRESENT**](https://msdn.microsoft.com/library/windows/hardware/ff548125) global kernel variable indicates whether a kernel debugger is currently attached.

-   (Microsoft Windows Server 2003 and later) The [**KdRefreshDebuggerNotPresent**](https://msdn.microsoft.com/library/windows/hardware/ff548109) routine refreshes the value of KD\_DEBUGGER\_NOT\_PRESENT.

 

 





