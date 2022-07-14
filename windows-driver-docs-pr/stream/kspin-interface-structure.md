---
title: KSPIN_INTERFACE structure (ks.h)
description: The KSPIN_INTERFACE structure describes a specific interface within an interface set.
ms.date: 07/14/2022
ms.custom: contperf-fy22q1
---

# KSPIN_INTERFACE structure

The **KSPIN_INTERFACE** structure describes a specific interface within an interface set.

## Syntax

```cpp
struct KSPIN_INTERFACE {
  GUID Set;
  ULONG Id;
  ULONG Flags;
};
```

## Members

`Set`

Specifies the GUID that specifies this interface set.

`Id`

Specifies the ID number of this particular interface within the interface set.

`Flags`

Reserved for system use.

## Remarks

The **KSPIN_INTERFACE** structure is an alias for the [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structure. As such, their definitions are identical.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)
