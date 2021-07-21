---
title: KSPIN_MEDIUM structure (ks.h)
description: The KSPIN_MEDIUM structure identifies a specific connection on a communication bus.
ms.date: 07/07/2021
ms.localizationpriority: medium
---


# KSPIN_MEDIUM structure

The **KSPIN_MEDIUM** structure identifies a specific connection on a communication bus.

## Syntax

```cpp
struct KSPIN_MEDIUM {
  GUID  Set;
  ULONG Id;
  ULONG Flags;
};
```

## Members

`Set`

Specifies a GUID that specifies this communication bus.

`Id`

Identifies a unique connection on the bus.

`Flags`

Reserved for system use.

## Remarks

The **KSPIN_MEDIUM** structure is an alias for the [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structure. As such, their definitions are identical.

The **KSPIN_MEDIUM** structure identifies a medium, with a unique medium GUID and instance identifier, which is generated in a bus-specific manner. There is a reserved identifier value **KSMEDIUM_TYPE_ANYINSTANCE** that is used when bus instances are not of concern. For example, the **KSMEDIUMSETID_Standard** refers to the system bus, of which there should only be one. So this instance identifier is always used just as a convenience.

A pin may support multiple mediums and interfaces on those mediums. The way in which a pin is described implies that the list of interfaces is supported on all mediums enumerated for a pin. If there is a case in which this is not true, another pin may be used to describe each subset of interfaces for the specific mediums.

The medium is also cached by kernel streaming to speed up the search for a possible connection.

An example of use of this structure can be found in a tuner sample, in which **KSPIN_MEDIUM** represents unique connections between tuners, crossbars, and other tuner components.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSPROPERTY_PIN_MEDIUMS**](/windows-hardware/drivers/stream/ksproperty-pin-mediums)

[**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)
