---
title: KSMETHOD structure (ks.h)
description: The KSMETHOD structure specifies a single kernel streaming method within a method set.
ms.date: 07/14/2022
---

# KSMETHOD structure

The **KSMETHOD** structure specifies a single kernel streaming method within a method set.

The [**KSEVENT**](ksevent-structure.md), **KSMETHOD**, and [**KSPROPERTY**](ksproperty-structure.md) structures are aliases for the [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structure. As such, their definitions are identical.

## Syntax

```cpp
struct KSMETHOD {
  GUID Set;
  ULONG Id;
  ULONG Flags;
};
```

## Members

`Set`

Specifies a GUID that identifies a kernel streaming method set.

For more information about method set GUIDs, see the **Remarks** section below.

`Id`

Specifies the member of the method set.

`Flags`

Specifies the request type. Also, see the *KSMETHOD_TYPE_Xxx* flags for [**KSMETHOD_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_item)).

A request can contain a combination of the values listed in the following table.

| Value | Type of method request |
|--|--|
| KSMETHOD_TYPE_BASICSUPPORT | Indicates to query the minidriver to determine if it supports the specified method of the method set. |
| KSMETHOD_TYPE_SEND | Indicates that the minidriver should execute the specified method. The effect of the method on the given parameters must be known to the client, that is, whether the parameters are read from, written to, both, or neither. The minidriver uses the **KSMETHOD_ITEM** structure to specify the method's effect on the parameters. |
| KSMETHOD_TYPE_SETSUPPORT | Indicates to query the minidriver to determine if it supports the specified method set. |
| KSMETHOD_TYPE_TOPOLOGY | Indicates that the specified method is of type **KSM_NODE**, where the **NodeId** member is the identifier of the topology node. Do not set this flag on its own; instead, OR it with other flags from this list. |

## Remarks

Microsoft provides several system-defined method set GUIDs. Minidrivers specify one of these GUIDs in the **Set** member. Kernel streaming method sets typically begin with a *KSMETHODSETID* prefix. Kernel streaming method sets are defined in *ks.h*, *ksmedia.h*, *bdamedia.h*, and possibly other header files.

For more information about kernel streaming events, see [KS Properties, Events, and Methods](ks-properties--events--and-methods.md).

A client can use the IOCTL_KS_METHOD request along with the KSMETHOD structure to execute methods on a kernel streaming object that the minidriver handles. For more information, see [KS Methods](./ks-methods.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSEVENT**](ksevent-structure.md)

[**KSPROPERTY**](ksproperty-structure.md)

[**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSMETHOD_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmethod_item)

[**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)
