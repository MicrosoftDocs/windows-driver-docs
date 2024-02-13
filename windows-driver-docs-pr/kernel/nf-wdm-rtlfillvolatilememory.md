---
title: RtlFillVolatileMemory Function (Wdm.H)
ms.date: 01/04/2024
description: This article describes the RtlFillVolatileMemory function (wdm.h).
---

# RtlFillVolatileMemory function (wdm.h)

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

The **RtlFillVolatileMemory** function provides [**RtlFillMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory) behavior (for example, setting the contents of a buffer) in situations where the developer needs to be sure that the setting operation occurs (for example, isn't subject to compiler optimizations).

## Syntax

```cpp
volatile void * RtlFillVolatileMemory(
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

The **RtlFillVolatileMemory** function has the following properties:

- The function isn't recognized as a compiler intrinsic so the compiler will never optimize away the call (either entirely or replace the call with an equivalent sequence of instructions). This differs from **RtlFillMemory** which is subject to various compiler optimizations.

- When the call returns, the buffer has been overwritten with the desired value. This functions memory accesses to the *Destination* will only be performed within the function (for example, the compiler can't move memory accesses out of this function).

- The function may perform unaligned memory accesses if the platform allows for it.

- The function may access memory locations more than once as part of its operation.

> [!NOTE]
> This function works on all versions of Windows, not just the latest. You need to consume the latest WDK to get the function declaration from the wdm.h header. You also need the library (volatileaccessk.lib) from the latest WDK. However, the resulting driver will run fine on older versions of Windows.

### Example

```cpp
UCHAR SensitiveData[100];

// Imagine we temporarily store some sensitive cryptographic
// material in a buffer.

StoreCryptographicKey(&SensitiveData);

DoCryptographicOperation(&SensitiveData);

// Now that we are done using the sensitive data we want to
// erase it from the stack. We cannot call RtlFillMemory because
// if the compiler realizes that "SensitiveData" is not
// referenced again the compiler can remove the call to RtlFillMemory.
// Instead we can call RtlSecureZeroMemory2, RtlZeroVolatileMemory, or RtlFillVolatileMemory
// (the former two are convenience wrappers around the latter). These
// calls will not be optimized away by the compiler.
// Note that RtlSecureZeroMemory2 performs better than
// RtlSecureZeroMemory function.

RtlFillVolatileMemory(&SensitiveData, sizeof(SensitiveData), 0);
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview

**Header:** wdm.h (include Wdm.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## Related articles

[Bulk memory volatile accessor functions (v3)](bulk-memory-volatile-accessor-functions-v3.md)

[**RtlFillMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory)
