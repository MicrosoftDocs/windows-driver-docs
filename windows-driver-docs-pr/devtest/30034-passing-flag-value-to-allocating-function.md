---
title: C30034 warning
description: Warning C30034 Passing a flag value to an allocating function that could result in executable memory being allocated.
ms.date: 04/20/2017
ms.localizationpriority: medium 
f1_keywords: 
  - "C30034"
---

# C30034


warning C30034: Passing a flag value to an allocating function that could result in executable memory being allocated. Please verify that the allocating function is not requesting a form of executable nonpaged pool.

BANNED\_MEM\_ALLOCATION\_MAYBE\_UNSAFE

A call to a function that results in possible allocation of executable nonpaged pool has been found. There are parameters used that indicate the resulting allocation may actually be non-executable, but it is determined that this is unlikely and executable memory has been allocated. This is most common with a function that takes optional allocating functions as a parameter.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following code generates this warning because it is not known if *pAllocate* allocates the specified type - in this the fourth parameter (0, which is executable) or if the allocation type is set from within *pAllocate.*

```
ExInitializeNPagedLookasideList(   pLookaside,
                pAllocate,
                pFree,
                0,
                size,
                tag,
                depth);
```

The following code avoids this warning:

```
ExInitializeNPagedLookasideList(   pLookaside,
                pAllocate,
                pFree,
                POOL_NX_ALLOCATION,
                size,
                tag,
                depth);
```

 

 





