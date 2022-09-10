---
title: KSDEGRADE structure (ks.h)
description: The KSDEGRADE structure contains specifics of degradation strategies.
ms.date: 07/14/2022
ms.custom: contperf-fy22q1
---

# KSDEGRADE structure

The **KSDEGRADE** structure contains specifics of degradation strategies.

> [!NOTE]
> The **KSDEGRADE** typedef is an alias for the [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structure. As such, their definitions are identical.

## Syntax

``` c++
struct KSDEGRADE {
  GUID Set;
  ULONG Id;
  ULONG Flags;
};
```

## Members

`Set`  

Specifies the globally unique set identifier.

`Id`

Specifies the set-specific identifier for an item within the set.

`Flags`

Contains a ULONG value that specifies either the current percentage of degradation, expressed in parts per thousand (where a value of 1000 represents no degradation), or specifies the amount of time in native units as specified by the interface.

## Remarks

The **Flags** member can contain different values based on the type of signal degradation that the client employs. See [Quality Management](./quality-management.md) for more details on different strategies for solving quality management problems by reducing signal quality.

Because **Flags** contains a ULONG value, multiple Skip requests may be needed to remedy a quality management issue.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSDEGRADE_STANDARD**](/windows-hardware/drivers/ddi/ks/ne-ks-ksdegrade_standard)

[**KSPROPERTY_STREAM_RATECAPABILITY**](./ksproperty-stream-ratecapability.md)

[**KSPROPERTY_STREAM_TIMEFORMAT**](./ksproperty-stream-timeformat.md)

[Quality Management](./quality-management.md)
