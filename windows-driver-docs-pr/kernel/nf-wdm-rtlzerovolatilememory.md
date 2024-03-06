---
title:  RtlZeroVolatileMemory Function (Wdm.H)
ms.date: 01/04/2024
description: This article describes the RtlZeroVolatileMemory function (wdm.h).
---

# RtlZeroVolatileMemory function (wdm.h)

> [!IMPORTANT]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

The **RtlZeroVolatileMemory** function is a convenience wrapper around [**RtlFillVolatileMemory**](nf-wdm-rtlfillvolatilememory.md).

## Syntax

```cpp
volatile void * RtlZeroVolatileMemory(
    [out] volatile void *Destination,
    [in]  size_t        Length
);
```

## Parameters

### Destination [out]

A pointer to the starting address of the block of memory to fill with zeros.

### Length [in]

The size of the block of memory to fill with zeros, in bytes.

## Returns

Returns the value of *Destination*.

## Remarks

The **RtlZeroVolatileMemory** function is a convenience wrapper around **RtlFillVolatileMemory**.

For more information, see the remarks section of [**RtlFillVolatileMemory**](nf-wdm-rtlfillvolatilememory.md).

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
// Note that RtlSecureZeroMemory2 performs better than the
// RtlSecureZeroMemory function.

RtlZeroVolatileMemory(&SensitiveData, sizeof(SensitiveData));
```

## Requirements

**Minimum supported client:** Windows 11 Insider Preview

**Header:** wdm.h (include Wdm.h)

**Kernel-mode library:** volatileaccessk.lib

**User-mode library:** volatileaccessu.lib

## Related articles

[Bulk memory volatile accessor functions (v3)](bulk-memory-volatile-accessor-functions-v3.md)

[**RtlFillVolatileMemory**](nf-wdm-rtlfillvolatilememory.md)
