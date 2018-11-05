---
title: Memory
description: Memory
ms.assetid: 4aa5cf2b-e5f8-4358-b2cc-c677cd012f46
keywords: ["Debugger Engine, memory", "data spaces"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Memory


The [debugger engine](introduction.md#debugger-engine) can directly read and write the target's main memory, registers, and other data spaces. In kernel-mode debugging, all of the target's memory is available, including virtual memory, physical memory, registers, Model Specific Registers (MSRs), System Bus Memory, Control-Space Memory, and I/O Memory. In user-mode debugging, only the virtual memory and registers are available.

The engine exposes, to the clients, all memory in the target using 64-bit addresses. If the target uses 32-bit addresses, when communicating with the target and the clients, the engine will automatically convert between 32-bit and 64-bit addresses, as needed. If a 32-bit address is recovered from the target--for example, by reading from memory or a register--it must be sign-extended to 64 bits before it can be used in the debugger engine API. Sign extension is performed automatically by the **ReadPointersVirtual** method.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about reading and writing memory, see [Memory Access](memory-access.md).

 

 





