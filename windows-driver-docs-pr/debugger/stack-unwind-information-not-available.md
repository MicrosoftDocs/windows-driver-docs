---
title: Stack Unwind Information Not Available
description: Stack Unwind Information Not Available
ms.assetid: 82260f85-780b-4f30-bebd-62faed6efeeb
keywords: ["Stack unwind information not available (warning)", "call stack, Stack unwind information not available (warning)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Stack Unwind Information Not Available


## <span id="ddk_stack_unwind_information_not_available_dbg"></span><span id="DDK_STACK_UNWIND_INFORMATION_NOT_AVAILABLE_DBG"></span>


When the debugger is examining the call stack, it may display the message "Stack unwind information not available. Following frames may be wrong."

This warning indicates that the debugger is not certain that the frames in the call stack listed after this message are correct.

To trace the call stack, the debugger examines the stack and analyzes the functions that have used the stack. This lets it identify the chain of return addresses that form the call stack. However, this procedure requires symbol information for each module containing the functions that used the stack.

If this symbol information is not available, the debugger is forced to make a best guess about which frames are return addresses. This warning information is displayed to indicate the uncertain nature of the call stack after this point.

 

 





