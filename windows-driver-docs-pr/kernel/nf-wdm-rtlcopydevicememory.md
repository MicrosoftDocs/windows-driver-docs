---
title: RtlCopyDeviceMemory Function (Wdm.H)
ms.date: 01/04/2024
description: This article describes the RtlCopyDeviceMemory function.
---

# RtlCopyDeviceMemory function (wdm.h)

The **RtlCopyDeviceMemory** function provides [**RtlCopyVolatileMemory**](nf-wdm-rtlcopyvolatilememory.md) behavior (for example, copying memory from one location to another without interference from compiler optimizations) in situations where the developer needs to additionally be sure that alignment faults won't be generated when accessing device memory.

## Syntax

```cpp
volatile void * RtlCopyDeviceMemory(
    [out] volatile void       *Destination,
    [in]  volatile const void *Source,
    [in]  size_t              Length
);
```

## Parameters

### Destination [out]

A pointer to the starting address of the copied block's destination.

### Source [in]

A pointer to the starting address of the block of memory to copy.

### Length [in]

The size of the block of memory to copy, in bytes.

## Returns

Returns the value of *Destination*.

## Remarks

The **RtlCopyDeviceMemory** function has the following properties:

- The function isn't recognized as a compiler intrinsic so the compiler will never optimize away the call (either entirely, or replace the call with an equivalent sequence of instructions). This differs from [**RtlCopyMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcopymemory) which is subject to various compiler optimizations.

- When the call returns, the data has been copied from Source to Destination. This functions memory accesses to the *Source* and *Destination* will only be performed within the function (for example, the compiler can't move memory accesses out of this function).

- The function may perform unaligned memory accesses only if the CPU supports unaligned memory accesses on device memory. If the CPU doesn't support unaligned device memory accesses, only aligned accesses will be performed.

- The function may access memory locations more than once as part of its copy operation.

- Doesn't support copy operations when *Source* and *Destination* overlap each other. If overlapping buffers are provided, fast-fails with the error code FAST_FAIL_INVALID_ARG.

> [!NOTE]
> This function only guarantees that the CPU's requirements for accessing memory mapped as device memory are respected. If a specific device has its own specific requirements for being accessed, this function should not be used (and instead, the developer must implement their own accessor functions). For example, this function makes no guarantee about the size of memory accesses generated (unless the CPU itself enforces these requirements).

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest WDK to get the function declaration from the wdm.h header. You also need the library (volatileaccessk.lib) from the latest WDK. However, the resulting driver will run fine on older versions of Windows.

### Example

```cpp
UCHAR* CopyBuffer;

// In this scenario we are copying data from memory mapped
// as "device memory" (for example, memory not backed by RAM). On
// some platforms like ARM64, device memory cannot tolerate
// memory accesses that are not naturally aligned (for example, a 4-byte
// load must be 4-byte aligned). Functions like memcpy, RtlCopyMemory,
// and even RtlCopyVolatileMemory may perform unaligned memory accesses
// because it is typically faster to do this.
// To ensure only naturally aligned accesses happen, use RtlCopyDeviceMemory.

RtlCopyDeviceMemory(CopyBuffer, DeviceMemoryBuffer, 100);
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview

**Header:** wdm.h (include Wdm.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## Related articles

[Bulk memory volatile accessor functions (v3)](bulk-memory-volatile-accessor-functions-v3.md)

[**RtlCopyMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcopymemory)

[**RtlCopyVolatileMemory**](nf-wdm-rtlcopyvolatilememory.md)
