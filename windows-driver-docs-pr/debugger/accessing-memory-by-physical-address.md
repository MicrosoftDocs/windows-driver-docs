---
title: Accessing Memory by Physical Address
description: Accessing Memory by Physical Address
keywords: ["physical address, accessing memory"]
ms.date: 05/23/2017
---

# Accessing Memory by Physical Address


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


To read from a physical address, use the [**!db**](../debuggercmds/-db---dc---dd---dp---dq---du---dw.md), **!dc**, **!dd**, **!dp**, **!du**, and **!dw** extension commands.

To write to a physical address, use the [**!eb**](../debuggercmds/-eb---ed.md) and **!ed** extension commands.

The [**fp (Fill Physical Memory)**](../debuggercmds/f--fp--fill-memory-.md) command writes a pattern to a physical memory range, repeating it until the range is full.

When you are using WinDbg in kernel mode, you can also read or write to physical memory directly from the [Memory window](memory-window.md).

To search physical memory for a piece of data or a range of data, use the [**!search**](../debuggercmds/-search.md) extension command.

Also, for more information about physical addresses, see [Converting Virtual Addresses to Physical Addresses](converting-virtual-addresses-to-physical-addresses.md).

 

 





