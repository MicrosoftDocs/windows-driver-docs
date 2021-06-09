---
title: Examining the Stack Trace
description: Examining the Stack Trace
keywords: ["Debugger Engine API, stack trace"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Examining the Stack Trace


A *call stack* contains the data for the functions calls made by a thread. The data for each function call is called a *stack frame* and includes the return address, parameters passed to the function, and the function's local variables. Each time a function call is made a new stack frame is pushed onto the top of the stack. When that function returns, the stack frame is popped off the stack.

Each thread has its own call stack, representing the calls made in that thread.

To get a stack trace, use the methods [**GetStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getstacktrace) and [**GetContextStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-getcontextstacktrace). A stack trace can be printed using [**OutputStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-outputstacktrace) and [**OutputContextStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-outputcontextstacktrace).

 

