---
title: Accessing Memory by Physical Address
description: Accessing Memory by Physical Address
ms.assetid: 248871dc-dac0-413e-8971-2ee2c2fe5290
keywords: ["physical address, accessing memory"]
---

# Accessing Memory by Physical Address


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


To read from a physical address, use the [**!db**](https://msdn.microsoft.com/library/windows/hardware/ff562317), **!dc**, **!dd**, **!dp**, **!du**, and **!dw** extension commands.

To write to a physical address, use the [**!eb**](https://msdn.microsoft.com/library/windows/hardware/ff562450) and **!ed** extension commands.

The [**fp (Fill Physical Memory)**](https://msdn.microsoft.com/library/windows/hardware/ff545511) command writes a pattern to a physical memory range, repeating it until the range is full.

When you are using WinDbg in kernel mode, you can also read or write to physical memory directly from the [Memory window](memory-window.md).

To search physical memory for a piece of data or a range of data, use the [**!search**](https://msdn.microsoft.com/library/windows/hardware/ff564934) extension command.

Also, for more information about physical addresses, see [Converting Virtual Addresses to Physical Addresses](converting-virtual-addresses-to-physical-addresses.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Accessing%20Memory%20by%20Physical%20Address%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




