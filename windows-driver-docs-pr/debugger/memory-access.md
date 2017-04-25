---
title: Memory Access
description: Memory Access
ms.assetid: a5265f2c-61b9-4f0f-8cff-05da26010c6a
keywords: ["Debugger Engine, memory access", "memory access"]
---

# Memory Access


## <span id="ddk_memory_access_dbx"></span><span id="DDK_MEMORY_ACCESS_DBX"></span>


The [debugger engine](introduction.md#debugger-engine) provides [*interfaces*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-interface) to directly read from and write to the target's main memory, registers, and other data spaces.

In user-mode debugging, only the virtual memory and registers can be accessed; the physical memory and other data spaces cannot be accessed.

The debugger engine API always uses 64-bit addresses when referring to memory locations on the target.

If the target uses 32-bit addresses, the native 32-bit address will automatically be sign-extended by the engine to 64-bit addresses. The engine will automatically convert between 64-bit addresses and native 32-bit addresses when communicating with the target.

This section includes:

[Virtual and Physical Memory](virtual-and-physical-memory.md)

[Registers](registers.md)

[Other Data Spaces](other-data-spaces.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Memory%20Access%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




