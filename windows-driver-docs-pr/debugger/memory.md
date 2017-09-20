---
title: Memory
description: Memory
ms.assetid: 4aa5cf2b-e5f8-4358-b2cc-c677cd012f46
keywords: ["Debugger Engine, memory", "data spaces"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Memory


The [debugger engine](introduction.md#debugger-engine) can directly read and write the target's main memory, registers, and other data spaces. In kernel-mode debugging, all of the target's memory is available, including virtual memory, physical memory, registers, Model Specific Registers (MSRs), System Bus Memory, Control-Space Memory, and I/O Memory. In user-mode debugging, only the virtual memory and registers are available.

The engine exposes, to the clients, all memory in the target using 64-bit addresses. If the target uses 32-bit addresses, when communicating with the target and the clients, the engine will automatically convert between 32-bit and 64-bit addresses, as needed. If a 32-bit address is recovered from the target--for example, by reading from memory or a register--it must be sign-extended to 64 bits before it can be used in the debugger engine API. Sign extension is performed automatically by the **ReadPointersVirtual** method.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For details about reading and writing memory, see [Memory Access](memory-access.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Memory%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




