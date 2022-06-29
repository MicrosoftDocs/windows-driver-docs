---
title: C30029 warning
description: Warning C30029 Calling a memory allocating function that requests executable memory.
ms.date: 12/10/2020
f1_keywords: 
  - "C30029"
---

# C30029


**Warning C30029: Banned Mem Allocation NoType**\
Example output: ```Warning: Calling a memory allocating function which requests executable memory```

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement. This specific error indicates the use of an API that allocates only executable nonpaged pool. This should only be used if executable memory is required. See [this article](/en-us/windows-hardware/drivers/kernel/no-execute-nonpaged-pool) for more information. There are no parameters you can supply that will change this behavior. The only way to fix this issue is to use an alternative function that allows for allocation of non-executable nonpaged pool memory. A list of all banned functions covered by this error and the recommended replacements can be found after the following example: 
## Example

The following code generates warning C30029:
```cpp
MmMapIoSpace(  PhysicalAddress,
        numberOfBytes,
        MmNonCached);
```
The following code avoids this warning:
```cpp
MmMapIoSpaceEx(    PhysicalAddress,
        numberOfBytes,
        PAGE_NOCACHE | PAGE_READWRITE);
```
## Banned Functions
 | Banned API | Replacement(s) | Rationale / Notes |
| -----------|----------------|-------|
|```MM_PAGE_PRIORITY```| <ul><li>```POOL_NX_OPTIN_AUTO``` - This supports creating multiple binaries for different versions of Windows</li><li>```POOL_NX_OPTIN``` (+ ```ExInitializeDriverRuntime(DrvRtPoolNxOptIn)```) - This supports a single binary running on different versions of windows</li><li>```PagePriority``` / ```MdlMappingNoExecute``` - This will work on Windows 8 and later</li></ul> |
|```PAGE_EXECUTE```| ```PAGE_NOACCESS```|
|```PAGE_EXECUTE_READ```| ```PAGE_READONLY``` |
|```PAGE_EXECUTE_READWRITE```| ```PAGE_READWRITE``` | A legitimate use of this would be in a JIT.  Contact your security team with questions. |
|```PAGE_EXECUTE_WRITECOPY```|```PAGE_WRITECOPY```|
|```MmMapIoSpace()```|```MmMapIoSpaceEx()```|
|```ExInitializeNPagedLookasideList()```|<ul><li>Please OR/set the flag parameter with/to ```POOL_NX_ALLOCATION```</li><li>Or by using the ```POOL_NX_OPTIN_AUTO``` / ```POOL_NX_OPTIN``` methods above</li></ul>|
|```MmAllocateContiguousMemorySpecifyCache()```|```MmAllocateContiguousNodeMemory()```|

 





