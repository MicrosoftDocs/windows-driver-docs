---
title: C30029
description: Warning C30029 Calling a memory allocating function that requests executable memory.
ms.assetid: E32E6EDB-010A-4E7F-8505-1E7557BB3FDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C30029


warning C30029: Calling a memory allocating function that requests executable memory

BANNED\_MEM\_ALLOCATION\_NOTYPE

Some APIs allocate only executable nonpaged pool. There are no parameters you can supply that will change this behavior. The only way to fix this issue is to use an alternative API that allows for allocation of non-executable nonpaged pool memory.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates warning C30029:

```
MmMapIoSpace(  PhysicalAddress,
        numberOfBytes,
        PAGE_NOCACHE);
```

The following code avoids this warning:

```
MmMapIoSpaceEx(    PhysicalAddress,
        numberOfBytes,
        PAGE_NOCACHE | PAGE_READWRITE);
```

 

 





