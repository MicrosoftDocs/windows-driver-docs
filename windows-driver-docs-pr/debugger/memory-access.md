---
title: Memory Access
description: Memory Access
keywords: ["Debugger Engine, memory access", "memory access"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Memory Access


## <span id="ddk_memory_access_dbx"></span><span id="DDK_MEMORY_ACCESS_DBX"></span>


The [debugger engine](introduction.md#debugger-engine) provides *interfaces* to directly read from and write to the target's main memory, registers, and other data spaces.

In user-mode debugging, only the virtual memory and registers can be accessed; the physical memory and other data spaces cannot be accessed.

The debugger engine API always uses 64-bit addresses when referring to memory locations on the target.

If the target uses 32-bit addresses, the native 32-bit address will automatically be sign-extended by the engine to 64-bit addresses. The engine will automatically convert between 64-bit addresses and native 32-bit addresses when communicating with the target.

This section includes:

[Virtual and Physical Memory](virtual-and-physical-memory.md)

[Registers](registers.md)

[Other Data Spaces](other-data-spaces.md)

 

 





