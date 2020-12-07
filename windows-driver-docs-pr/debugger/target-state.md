---
title: Target State
description: Target State
keywords: ["Debugger Engine API, targets, state"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Target State


The method [**OutputCurrentState**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-outputcurrentstate) will print the current state of the target to the debugger's output stream.

The current execution status of the target is returned by [**GetExecutionStatus**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getexecutionstatus). If the target is suspended, the method [**SetExecutionStatus**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setexecutionstatus) can be used to resume execution in one of the execution modes.

The method [**GetReturnOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getreturnoffset) returns the address of the instruction that will execute when the current function returns.

[**GetNearInstruction**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnearinstruction) returns the location of an instruction relative to a given address.

### <span id="examining_the_stack_trace"></span><span id="EXAMINING_THE_STACK_TRACE"></span>Examining the Stack Trace

A *call stack* contains the data for the function calls that are made by a thread. The data for each function call is called a *stack frame* and includes the return address, parameters passed to the function, and the function's local variables. Each time a function call is made, a new stack frame is pushed onto the top of the stack. When that function returns, the stack frame is popped off the stack. Each thread has its own call stack, which represents the calls that are made in that thread.

**Note**   Not all of the data for a function call can be stored in the stack frame. Parameters and local variables, at times, can be stored in registers.

 

To retrieve the call stack or *stack trace*, use the methods [**GetStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getstacktrace) and [**GetContextStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-getcontextstacktrace). The stack trace can be printed using [**OutputStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-outputstacktrace) and [**OutputContextStackTrace**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol4-outputcontextstacktrace).

 

