---
title: UnSafeAllocatePool Rule (WDM)
description: Learn about the UnSafeAllocatePool rule (wdm). 
ms.date: 01/15/2021
keywords: ["UnSafeAllocatePool rule (wdm)"]
topic_type:
- apiref
ms.topic: reference
api_name:
- UnSafeAllocate
api_type:
- NA
---

# UnSafeAllocatePool rule (wdm)

The **UnSafeAllocatePool** rule is an important security rule that checks that a driver is not using deprecated DDIs to allocate memory.

The UnsafeAllocatePool rule specifies that the driver should not call:

[ExAllocatePool](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool)

[ExAllocatePoolWithTag](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)

[ExAllocatePoolWithQuota](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquota) 

[ExAllocatePoolWithQuotaTag](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)

[ExAllocatePoolWithTagPriority](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtagpriority) 

This rule is available in preview WDK builds 20236 and above.

## Driver updates for versions of Windows 10, version 2004 and later

If you are building a driver that targets Windows 10, version 2004 and later, use the replacement APIs [ExAllocatePool2](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2) and [ExAllocatePool3](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool3) instead.

| Old API                       | New API                                                                     |
|-------------------------------|-----------------------------------------------------------------------------|
| ExAllocatePool                | [ExAllocatePool2](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2) |
| ExAllocatePoolWithTag         | [ExAllocatePool2](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2) |
| ExAllocatePoolWithQuota       | [ExAllocatePool2](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2) |
| ExAllocatePoolWithQuotaTag    | [ExAllocatePool2](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2) |
| ExAllocatePoolWithTagPriority | [ExAllocatePool3](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool3) |

The new APIs will zero pool allocations by default, to help avoid possible memory disclosure bugs.  

### ExAllocatePool/ExAllocatePoolWithTag

```cpp
// Old code
PVOID Allocation = ExAllocatePoolWithTag(PagedPool, 100, 'abcd');
RtlZeroMemory(Allocation, 100);

// New code
PVOID Allocation = ExAllocatePool2(POOL_FLAG_PAGED, 100, 'abcd');
```

The old pool allocation APIs accept a [POOL_TYPE](/windows-hardware/drivers/ddi/wdm/ne-wdm-_pool_type) argument, but the new allocation APIs accept a [POOL_FLAGS](../kernel/pool_flags.md) argument. Update any associated code to use the new [POOL_FLAGS](../kernel/pool_flags.md) argument.

### ExAllocatePoolWithQuota/ExAllocatePoolWithQuotaTag

The new function will now return NULL on allocation failure by default. In order to have the allocator raise an exception on failure instead, the POOL_FLAG_RAISE_ON_FAILURE flag must be passed as discussed in [ExAllocatePool2](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool2).

```cpp
// Old code
PVOID Allocation = ExAllocatePoolWithQuotaTag(PagedPool | POOL_QUOTA_FAIL_INSTEAD_OF_RAISE, 100, 'abcd');
RtlZeroMemory(Allocation, 100);

// New code
PVOID Allocation = ExAllocatePool2(POOL_FLAG_PAGED | POOL_FLAG_USE_QUOTA, 100, 'abcd');
```

### ExAllocatePoolWithTagPriority

```cpp
// Old code
PVOID Allocation = ExAllocatePoolWithTagPriority(PagedPool, 100, 'abcd', HighPoolPriority);
RtlZeroMemory(Allocation, 100);

// New code
POOL_EXTENDED_PARAMETER params = {0};
params.Type = PoolExtendedParameterPriority;
params.Priority = HighPoolPriority;
PVOID Allocation = ExAllocatePool3(POOL_FLAG_PAGED, 100, 'abcd', &params, 1);
```

## Driver updates for versions of Windows earlier than Windows 10, version 2004

If you are building a driver that targets versions of Windows prior to Windows 10, version 2004, you must use the following force inline wrapper functions.

You must also #define POOL_ZERO_DOWN_LEVEL_SUPPORT and call [ExInitializeDriverRuntime](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializedriverruntime) during driver initialization before calling the pool allocation functions.

### Locally defined inline functions

```cpp
PVOID
NTAPI
ExAllocatePoolZero (
    _In_ __drv_strictTypeMatch(__drv_typeExpr) POOL_TYPE PoolType,
    _In_ SIZE_T NumberOfBytes,
    _In_ ULONG Tag
    )

PVOID
NTAPI
ExAllocatePoolQuotaZero (
    _In_ __drv_strictTypeMatch(__drv_typeExpr) POOL_TYPE PoolType,
    _In_ SIZE_T NumberOfBytes,
    _In_ ULONG Tag
    )

PVOID
NTAPI
ExAllocatePoolPriorityZero (
    _In_ __drv_strictTypeMatch(__drv_typeExpr) POOL_TYPE PoolType,
    _In_ SIZE_T NumberOfBytes,
    _In_ ULONG Tag,
    _In_ EX_POOL_PRIORITY Priority
    )
```

Refer to the latest wdm.h header for the implementation code for these code wrappers. For example this is the implementation for ExAllocatePoolPriorityZero, showing the use of [RtlZeroMemory](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory).

```cpp
{
    PVOID Allocation;

    Allocation = ExAllocatePoolWithTagPriority((POOL_TYPE) (PoolType | POOL_ZERO_ALLOCATION),
                                               NumberOfBytes,
                                               Tag,
                                               Priority);

#if defined(POOL_ZERO_DOWN_LEVEL_SUPPORT)

    if ((!ExPoolZeroingNativelySupported) && (Allocation != NULL)) {
        RtlZeroMemory(Allocation, NumberOfBytes);
    }

#endif

    return Allocation;
}
```

### Mapping of old APIs to new APIs

| Old API                       | New API                    |
|-------------------------------|----------------------------|
| ExAllocatePool                | ExAllocatePoolZero         |
| ExAllocatePoolWithTag         | ExAllocatePoolZero         |
| ExAllocatePoolWithQuota       | ExAllocatePoolQuotaZero    |
| ExAllocatePoolWithQuotaTag    | ExAllocatePoolQuotaZero    |
| ExAllocatePoolWithTagPriority | ExAllocatePoolPriorityZero |

### Example

```cpp
// Old code
PVOID Allocation = ExAllocatePoolWithTag(PagedPool, 100, 'abcd');
RtlZeroMemory(Allocation, 100);

// New code

// Before headers are pulled in (or compiler defined)
#define POOL_ZERO_DOWN_LEVEL_SUPPORT

// Once during driver initialization
// Argument can be any value
ExInitializeDriverRuntime(0);

// Replacement for each pool allocation
PVOID Allocation = ExAllocatePoolZero(PagedPool, 100, 'abcd');
```

**Driver model: WDM, Generic**

## How to test

At compile time:

1. Run [Static Driver Verifier](./static-driver-verifier.md) and specify the **UnSafeAllocatePool** rule.
2. Use the following steps (found in [Using Static Driver Verifier to Find Defects in Windows Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)) to run an analysis of your code:

    - [Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)
    - [Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)
    - [View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)

For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md).
