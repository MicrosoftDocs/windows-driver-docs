---
title: .dvalloc (Allocate Memory)
description: The .dvalloc command causes Windows to allocate additional memory to the target process.
keywords: [".dvalloc (Allocate Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .dvalloc (Allocate Memory)
api_type:
- NA
---

# .dvalloc (Allocate Memory)


The **.dvalloc** command causes Windows to allocate additional memory to the target process.

```dbgcmd
.dvalloc [Options] Size 
```

## <span id="ddk_meta_allocate_memory_dbg"></span><span id="DDK_META_ALLOCATE_MEMORY_DBG"></span>Parameters


*Options*
Can be any number of the following options:

<span id="_b_BaseAddress"></span><span id="_b_baseaddress"></span><span id="_B_BASEADDRESS"></span>**/b** **** *BaseAddress*  
Specifies the virtual address of the beginning of the allocation.

<span id="_r"></span><span id="_R"></span>**/r**  
Reserves the memory in the virtual address space but does not actually allocate any physical memory. If this option is used, the debugger calls **VirtualAllocEx** with the *flAllocationType* parameter equal to MEM\_RESERVE. If this option is not used, the value MEM\_COMMIT | MEM\_RESERVE is used. See the Microsoft Windows SDK for details.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Specifies the amount of memory to be allocated, in bytes. The amount of memory available to the program will equal *Size*. The amount of memory actually used may be slightly larger, since it is always a whole number of pages.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Remarks

The **.dvalloc** command calls **VirtualAllocEx** to allocate new memory for the target process. The allocated memory permits reading, writing, and execution.

To free this memory, use [**.dvfree (Free Memory)**](-dvfree--free-memory-.md).

 

 





