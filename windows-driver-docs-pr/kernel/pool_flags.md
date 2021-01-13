---
title: POOL_FLAGS
description: Flags that indicate the type of pool memory, attributes the memory is required to have, and attributes the memory can optionally have.
keywords: ["memory management WDK kernel , system-allocated space", "system-allocated space WDK kernel", "allocating system-space memory", "allocating I/O buffer memory", "I/O buffer memory allocations WDK kernel", "buffer memory allocations WDK kernel"]
ms.date: 06/16/2020
ms.localizationpriority: medium
---

# POOL_FLAGS

A ULONG64-typed value specifying the type of pool memory along with required and optional attributes. Multiple flag values can be combined using bit-wise OR.

```cpp
//
// POOL_FLAG values
//
// Low 32-bits of ULONG64 are for required parameters (allocation fails if they
// cannot be satisfied).
// High 32-bits of ULONG64 is for optional parameters (allocation succeeds if
// they cannot be satisfied or are unrecognized).
//

#define POOL_FLAG_REQUIRED_START          0x0000000000000001UI64
#define POOL_FLAG_USE_QUOTA               0x0000000000000001UI64     // Charge quota
#define POOL_FLAG_UNINITIALIZED           0x0000000000000002UI64     // Don't zero-initialize allocation
#define POOL_FLAG_SESSION                 0x0000000000000004UI64     // Use session specific pool
#define POOL_FLAG_CACHE_ALIGNED           0x0000000000000008UI64     // Cache aligned allocation
#define POOL_FLAG_RESERVED1               0x0000000000000010UI64     // Reserved for system use
#define POOL_FLAG_RAISE_ON_FAILURE        0x0000000000000020UI64     // Raise exception on failure
#define POOL_FLAG_NON_PAGED               0x0000000000000040UI64     // Non paged pool NX
#define POOL_FLAG_NON_PAGED_EXECUTE       0x0000000000000080UI64     // Non paged pool executable
#define POOL_FLAG_PAGED                   0x0000000000000100UI64     // Paged pool
#define POOL_FLAG_RESERVED2               0x0000000000000200UI64     // Reserved for system use
#define POOL_FLAG_RESERVED3               0x0000000000000400UI64     // Reserved for system use
#define POOL_FLAG_REQUIRED_END            0x0000000080000000UI64
#define POOL_FLAG_OPTIONAL_START          0x0000000100000000UI64
#define POOL_FLAG_SPECIAL_POOL            0x0000000100000000UI64     // Make special pool allocation
#define POOL_FLAG_OPTIONAL_END            0x8000000000000000UI64
```

## Required Flags

Required flags must be recognized and satisfied by the pool allocator. If the allocator does not recognize the flag or cannot make an allocation satisfying all required flags the allocation fails.

|Name|Description|
|-|-|
|POOL_FLAG_USE_QUOTA|This flag is passed by highest-level drivers that allocate memory to satisfy a request in the context of the process that originally made the I/O request. Lower-level drivers need not specify this flag.|
|POOL_FLAG_UNINITIALIZED|Leave the allocation uninitialized. The contents of the allocation are indeterminant. The driver must be extremely careful never to copy uninitialized memory to untrusted destinations (user-mode, over the network, etc.).|
|POOL_FLAG_SESSION|Reserved for the operating system.|
|POOL_FLAG_CACHE_ALIGNED|Cache align the pool allocation. Warning: this flag is treated as a best effort and it should not be used if cache aligned allocations are required for program correctness.|
|POOL_FLAG_RESERVED1|Reserved for internal use.|
|POOL_FLAG_RAISE_ON_FAILURE|Raise an exception if the allocation cannot be satisfied.|
|POOL_FLAG_NON_PAGED|Make allocation in the non-paged pool.|
|POOL_FLAG_NON_PAGED_EXECUTE|Make allocation in the non-paged executable pool.|
|POOL_FLAG_PAGED|Make allocation in the paged pool. This is executable on x86, non-executable on all other platforms.|
|POOL_FLAG_RESERVED2|Reserved for internal use.|
|POOL_FLAG_RESERVED3|Reserved for internal use.|

## Optional Flags

Optional flags are satisfied by the pool allocator opportunistically. If the allocator does not recognize an optional flag it ignores it. If the allocator cannot satisfy an optional flag it may or may not succeed depending on the semantics of the specific flag.

|Name|Description|
|-|-|
|POOL_FLAG_SPECIAL_POOL|Make allocation in the special pool (used for debugging). If the special pool cannot be used the allocator will attempt to use the normal pool.|

## Requirements

**Header**: wdm.h (include Wdm.h, Ntddk.h, Ntifs.h, Wudfwdm.h)

## See Also

[**ExAllocatePool2**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2)
