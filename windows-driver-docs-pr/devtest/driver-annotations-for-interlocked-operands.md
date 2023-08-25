---
title: Driver annotations for interlocked operands
description: Driver annotations for interlocked operands
ms.date: 08/24/2023
---

# Driver annotations for interlocked operands


A large family of functions takes as one of their parameters the address of a variable that should be accessed by using an interlocked processor instruction. These are cache read-through atomic instructions, and if the operands are used incorrectly, very subtle bugs result.

Use the following annotation for function parameters to identify it as an interlocked operand.

|Interlocked operand annotation|Description|
|----------------------------- |---------- |
|\_Interlocked_operand_|The annotated function parameter is the target operand of one of the interlocked functions. Those operands must have specific additional properties.|

Function parameters annotated with the \_Interlocked\_operand\_ are expected to be shared between processes. Variables used with this annotation must:

- Be declared **volatile.**

- Not be a local variable. Use of a local variable usually indicates a misunderstanding of the function's intent. Even if a local variable is somehow shared, system paging requirements make addressing variables in another process problematic.

- Not be accessed except by an interlocked function. Without the explicit use of an interlocked function, the operation might access stale data, might occur only in a single processor’s cache, or might be delayed in reaching the rest of the system.

System-supplied functions are already annotated for interlocked operands.

The following example shows the annotation for the [**InterlockedExchange**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedexchange) function. This annotation specifies that the Target parameter must always be accessed by using an interlocked operation.

```cpp
LONG  
InterlockedExchange (  
    _Inout_ _Interlocked_operand_ LONG volatile *Target,  
    _In_ LONG Value  
    );  
```

## <span id="related_topics"></span>Related topics

[SAL 2.0 Annotations for Drivers](sal-2-annotations-for-windows-drivers.md)
