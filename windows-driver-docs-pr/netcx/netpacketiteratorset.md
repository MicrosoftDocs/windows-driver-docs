---
title: NetPacketIteratorSet function
description: The NetPacketIteratorSet method completes a client driver's post or drain operation on the packet ring. 
ms.assetid: DE28AAFC-BDD9-4025-B0A5-3778CA4581DB
keywords:
- NetAdapterCx NetPacketIteratorSet, NetCx NetPacketIteratorSet
ms.date: 01/10/2019
ms.localizationpriority: medium
---

# NetPacketIteratorSet function

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The **NetPacketIteratorSet** method completes a client driver's post or drain operation on the packet ring. 

## Syntax

```cpp
void NetPacketIteratorSet(
    NET_RING_PACKET_ITERATOR const * Iterator
);
```

## Parameters

`Iterator`

A pointer to a [**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md) structure.

## Return Value

None.

## Remarks

**NetPacketIteratorSet** sets the packet iterator's **IndexToSet** to its **Index**, which indicates to the OS that the client driver has finished processing the packets from **IndexToSet** to **Index - 1** inclusive. Client drivers call this method to finish posting packets to hardware, or to finish draining completed packets to the OS. 

For an animation and code example of draining packets back to the OS, see [Net rings and net ring iterators](net-rings-and-net-ring-iterators.md).

## Requirements

|  |  |
| --- | --- |
| Target Platform | Universal |
| Header | netringiterator.h |
| IRQL | Any level as long as target memory is resident |

## See Also

[Net rings and net ring iterators](net-rings-and-net-ring-iterators.md)

[**NET_RING_PACKET_ITERATOR**](net-ring-packet-iterator.md)