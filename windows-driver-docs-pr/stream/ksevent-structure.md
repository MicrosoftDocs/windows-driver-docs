---
title: KSEVENT structure (ks.h)
description: The KSEVENT structure specifies a single kernel streaming event within a kernel streaming event set.
ms.date: 07/07/2021
ms.custom: contperf-fy22q1
---

# KSEVENT structure

The **KSEVENT** structure specifies a single kernel streaming event within a kernel streaming event set.

The **KSEVENT**, [**KSMETHOD**](ksmethod-structure.md), and [**KSPROPERTY**](ksproperty-structure.md) structures are aliases for the [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) structure. As such, their definitions are identical.

## Syntax

```cpp
struct KSEVENT {
  GUID  Set;
  ULONG Id;
  ULONG Flags;
};
```

## Members

`Set`  

Specifies a GUID that identifies a kernel streaming event set.

For more information about event set GUIDs, see the **Remarks** section below.

`Id`

Specifies the member of the event set.

`Flags`

Specifies the request type.

This flag should be one of the values listed in the following table.

| Value | Description |
|--|--|
| KSEVENT_TYPE_ENABLE | Enables event notification for this event type. The driver continues event notification until the client explicitly disables it. |
| KSEVENT_TYPE_ONESHOT | Enables event notification for the next occurrence of this event only. The client does not need to (and should not) disable the event once it has occurred. |
| KSEVENT_TYPE_SETSUPPORT | Queries for the list of event sets, or for support of a particular event set. |
| KSEVENT_TYPE_BASICSUPPORT | Queries for support of a particular event type. |
| KSEVENT_TYPE_ENABLEBUFFERED | Instead of notifying the client, the driver queues event notifications. The client then issues a second **IOCTL_KS_ENABLE_EVENT** request with the *KSEVENT_TYPE_QUERYBUFFER* to receive the queued event notifications. |
| KSEVENT_TYPE_TOPOLOGY | Indicates that the event passed is of type [**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node), where **NodeId** indicates the numeric ID of the topology node. Do not set this flag on its own; instead, OR it with other flags from this list. |
| KSEVENT_TYPE_QUERYBUFFER | Retrieves the next buffered event notification. |

## Remarks

Microsoft provides several system-defined event set GUIDs. Minidrivers specify one of these GUIDs in the **Set** member. Kernel streaming event sets typically begin with a *KSEVENTSETID* prefix. Kernel streaming event sets are defined in *ks.h*, *ksmedia.h*, *bdamedia.h*, and possibly other header files.

For more information about kernel streaming events, see [KS Properties, Events, and Methods](ks-properties--events--and-methods.md).

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)

[**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSMETHOD**](ksmethod-structure.md)

[**KSPROPERTY**](ksproperty-structure.md)
