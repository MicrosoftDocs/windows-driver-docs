---
title: Stack Unwind Information Not Available
description: Stack Unwind Information Not Available
ms.assetid: 82260f85-780b-4f30-bebd-62faed6efeeb
keywords: ["Stack unwind information not available (warning)", "call stack, Stack unwind information not available (warning)"]
---

# Stack Unwind Information Not Available


## <span id="ddk_stack_unwind_information_not_available_dbg"></span><span id="DDK_STACK_UNWIND_INFORMATION_NOT_AVAILABLE_DBG"></span>


When the debugger is examining the call stack, it may display the message "Stack unwind information not available. Following frames may be wrong."

This warning indicates that the debugger is not certain that the frames in the call stack listed after this message are correct.

To trace the call stack, the debugger examines the stack and analyzes the functions that have used the stack. This lets it identify the chain of return addresses that form the call stack. However, this procedure requires symbol information for each module containing the functions that used the stack.

If this symbol information is not available, the debugger is forced to make a best guess about which frames are return addresses. This warning information is displayed to indicate the uncertain nature of the call stack after this point.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Stack%20Unwind%20Information%20Not%20Available%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




