---
title: C30029 warning
description: Warning C30029 Calling a memory allocating function that requests executable memory.
ms.date: 08/23/2022
f1_keywords: ["C30029", "BANNED_MEM_ALLOCATION_NOTYPE", "__WARNING_BANNED_MEM_ALLOCATION_NOTYPE"]
---
# C30029

> Warning: Calling a memory allocating function which requests executable memory

This warning indicates that a function is being used that has been banned and has a more robust or secure replacement. This specific error indicates the use of an API that allocates only executable nonpaged pool.

## Remarks

This should only be used if executable memory is required. See [No-Execute (NX) Nonpaged Pool](../kernel/no-execute-nonpaged-pool.md) for more information on this. There are no parameters you can supply that will change this behavior. The only way to fix this issue is to use an alternative function that allows for allocation of non-executable nonpaged pool memory. A list of all banned functions covered by this error and the recommended replacements can be found after the following example.

Code analysis name: BANNED_MEM_ALLOCATION_NOTYPE

## Example

The following code generates this warning. This issue stems from the use of `MmMapIoSpace`:

```cpp
MmMapIoSpace(PhysicalAddress, numberOfBytes, MmNonCached);
```

The following code avoids this warning by replaceing `MmMapIoSpace` with `MmMapIoSpace`:

```cpp
MmMapIoSpaceEx(PhysicalAddress, numberOfBytes, PAGE_NOCACHE | PAGE_READWRITE);
```

## Banned Functions

| Banned API | Replacement(s) | Rationale / Notes |
| -----------|----------------|-------|
|```MmMapIoSpace()```|```MmMapIoSpaceEx()```|
|```MmAllocateContiguousMemorySpecifyCache()```|```MmAllocateContiguousNodeMemory()```|Depending on the cache type, SpecifyCache can be used in a way that limits it to non-executable memory. However, using NodeMemory will ensure this. See [C30030, subsection 'For defects involving cache types'](./30030-parameter-indicates-executable-memory.md#for-defects-involving-cache-types) for more information on this.|
