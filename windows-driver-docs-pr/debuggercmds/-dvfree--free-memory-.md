---
title: ".dvfree (Free Memory)"
description: "The .dvfree command frees a memory allocation owned by the target process."
keywords: [".dvfree (Free Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .dvfree (Free Memory)
api_type:
- NA
---

# .dvfree (Free Memory)


The **.dvfree** command frees a memory allocation owned by the target process.

```dbgcmd
.dvfree [/d] BaseAddress Size 
```

## <span id="ddk_meta_free_memory_dbg"></span><span id="DDK_META_FREE_MEMORY_DBG"></span>Parameters


<span id="________d______"></span><span id="________D______"></span> **/d**   
Decommits the allocation, but does not actually release the pages containing the allocation. If this option is used, the debugger calls **VirtualFreeEx** with the *dwFreeType* parameter equal to MEM\_DECOMMIT. If this option is not used, the value MEM\_RELEASE is used. See the Microsoft Windows SDK for details.

<span id="_______BaseAddress______"></span><span id="_______baseaddress______"></span><span id="_______BASEADDRESS______"></span> *BaseAddress*   
Specifies the virtual address of the beginning of the allocation.

<span id="_______Size______"></span><span id="_______size______"></span><span id="_______SIZE______"></span> *Size*   
Specifies the amount of memory to be freed, in bytes. The actual memory freed will always be a whole number of memory pages.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Remarks

The **.dvfree** command calls **VirtualFreeEx** to free an existing memory allocation. Unless the **/d** option is specified, the pages containing this memory are released.

This command can be used to free an allocation made by [**.dvalloc (Allocate Memory)**](-dvalloc--allocate-memory-.md). It can also be used to free any block of memory owned by the target process, but freeing memory that was not acquired through **.dvalloc** will naturally pose risks to the stability of the target process.

