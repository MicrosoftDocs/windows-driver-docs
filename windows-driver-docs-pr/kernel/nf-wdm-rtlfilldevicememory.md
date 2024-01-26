---
title: RtlFillDeviceMemory function (wdm.h)
ms.date: 01/04/2024
description: This article describes the RtlFillDeviceMemory function (wdm.h).
---

# RtlFillDeviceMemory function (wdm.h)

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

The **RtlFillDeviceMemory** function provides [**RtlFillVolatileMemory**](nf-wdm-rtlfillvolatilememory.md) behavior (for example, setting the contents of a buffer without interference from compiler optimizations) in situations where the developer needs to additionally be sure that alignment faults won't be generated when accessing device memory.

## Syntax

```cpp
volatile void * RtlFillDeviceMemory(
    [out] volatile void *Destination,
    [in]  size_t        Length,
    [in]  int           Fill
);
```

## Parameters

### Destination [out]

A pointer to the starting address of the block of memory to fill.

### Length [in]

The size of the block of memory to fill, in bytes. This value must be less than the size of the *Destination* buffer.

### Fill [in]

The byte value with which to fill the memory block.

## Returns

Returns the value of *Destination*.

## Remarks

The **RtlFillDeviceMemory** function has the following properties:

- The function isn't recognized as a compiler intrinsic so the compiler will never optimize away the call (either entirely or replace the call with an equivalent sequence of instructions). This differs from [**RtlFillMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory) which is subject to various compiler optimizations.

- When the call is complete, the buffer has been overwritten with the desired value. This functions memory accesses to the *Destination* will only be performed within the function (for example, the compiler can't move memory accesses out of this function).

- The function may perform unaligned memory accesses only if the CPU supports unaligned memory accesses on device memory. If the CPU doesn't support unaligned device memory accesses, only aligned accesses will be performed.

- The function may access memory locations more than once as part of its operation.

> [!NOTE]
> This function only guarantees that the CPU's requirements for accessing memory mapped as device memory are respected. If a specific device has its own specific requirements for being accessed, this function should not be used (and instead, the developer must implement their own accessor functions). For example, this function makes no guarantee about the size of memory accesses generated (unless the CPU itself enforces these requirements).

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest WDK to get the function declaration from the wdm.h header. You also need the library (volatileaccessk.lib) from the latest WDK. However, the resulting driver will run fine on older versions of Windows.

### Example

```cpp
// In this scenario we are setting data on memory mapped
// as "device memory" (for example, memory not backed by RAM). 
// On some platforms like ARM64, device memory cannot tolerate
// memory accesses that are not naturally aligned (for example, a 4-byte
// load must be 4-byte aligned). Functions like memset, RtlFillMemory,
// and even RtlFillVolatileMemory may perform unaligned memory accesses
// because it is typically faster to do this.
// To ensure only naturally aligned accesses happen, use RtlFillDeviceMemory.

RtlFillDeviceMemory(DeviceMemoryBuffer, 100, 0xAA);
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview

**Header:** wdm.h (include Wdm.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## Related articles

[Bulk memory volatile accessor functions (v3)](bulk-memory-volatile-accessor-functions-v3.md)

[**RtlFillMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory)

[**RtlFillVolatileMemory**](nf-wdm-rtlfillvolatilememory.md)
