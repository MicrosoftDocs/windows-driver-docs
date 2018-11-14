---
title: Accessing Memory by Physical Address
description: Accessing Memory by Physical Address
ms.assetid: 248871dc-dac0-413e-8971-2ee2c2fe5290
keywords: ["physical address, accessing memory"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Accessing Memory by Physical Address


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


To read from a physical address, use the [**!db**](-db---dc---dd---dp---dq---du---dw.md), **!dc**, **!dd**, **!dp**, **!du**, and **!dw** extension commands.

To write to a physical address, use the [**!eb**](-eb---ed.md) and **!ed** extension commands.

The [**fp (Fill Physical Memory)**](f--fp--fill-memory-.md) command writes a pattern to a physical memory range, repeating it until the range is full.

When you are using WinDbg in kernel mode, you can also read or write to physical memory directly from the [Memory window](memory-window.md).

To search physical memory for a piece of data or a range of data, use the [**!search**](-search.md) extension command.

Also, for more information about physical addresses, see [Converting Virtual Addresses to Physical Addresses](converting-virtual-addresses-to-physical-addresses.md).

 

 





