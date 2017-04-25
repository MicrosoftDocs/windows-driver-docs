---
title: Target State
description: Target State
ms.assetid: befd6c0b-dd16-40a1-bc6b-634b354d2a75
keywords: ["Debugger Engine API, targets, state"]
---

# Target State


The method [**OutputCurrentState**](https://msdn.microsoft.com/library/windows/hardware/ff553206) will print the current state of the target to the debugger's output stream.

The current execution status of the target is returned by [**GetExecutionStatus**](https://msdn.microsoft.com/library/windows/hardware/ff546675). If the target is suspended, the method [**SetExecutionStatus**](https://msdn.microsoft.com/library/windows/hardware/ff556693) can be used to resume execution in one of the execution modes.

The method [**GetReturnOffset**](https://msdn.microsoft.com/library/windows/hardware/ff548237) returns the address of the instruction that will execute when the current function returns.

[**GetNearInstruction**](https://msdn.microsoft.com/library/windows/hardware/ff547197) returns the location of an instruction relative to a given address.

### <span id="examining_the_stack_trace"></span><span id="EXAMINING_THE_STACK_TRACE"></span>Examining the Stack Trace

A *call stack* contains the data for the function calls that are made by a thread. The data for each function call is called a *stack frame* and includes the return address, parameters passed to the function, and the function's local variables. Each time a function call is made, a new stack frame is pushed onto the top of the stack. When that function returns, the stack frame is popped off the stack. Each thread has its own call stack, which represents the calls that are made in that thread.

**Note**   Not all of the data for a function call can be stored in the stack frame. Parameters and local variables, at times, can be stored in registers.

 

To retrieve the call stack or *stack trace*, use the methods [**GetStackTrace**](https://msdn.microsoft.com/library/windows/hardware/ff548425) and [**GetContextStackTrace**](https://msdn.microsoft.com/library/windows/hardware/ff545748). The stack trace can be printed using [**OutputStackTrace**](https://msdn.microsoft.com/library/windows/hardware/ff553252) and [**OutputContextStackTrace**](https://msdn.microsoft.com/library/windows/hardware/ff553203).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Target%20State%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




