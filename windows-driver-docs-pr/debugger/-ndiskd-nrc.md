---
title: ndiskd.nrc
description: The ndiskd.nrc extension displays information about a NET_PACKET_FRAGMENT structure.
keywords: ["ndiskd.nrc Windows Debugging"]
ms.date: 06/17/2020
topic_type:
- apiref
api_name:
- ndiskd.nrc
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.nrc

The **!ndiskd.nrc** extension displays information about a [NET\_RING\_COLLECTION](/windows-hardware/drivers/ddi/ringcollection/ns-ringcollection-_net_ring_collection) structure.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](../netcx/index.md)
and [Introduction to net rings](../netcx/introduction-to-net-rings.md).

```console
!ndiskd.nrc -handle <x> [-basic] [-packet] [-fragment] [-dump]
```

## Parameters

*-handle*    
Required. Address of NET\_RING\_COLLECTION

*-basic*    
Displays links for packet ring and fragment ring.

*-packet*     
Displays only the packet ring contents.

*-fragment*     
Displays only the fragment ring contents.

*-dump*     
Displays information about each element(packet/fragment).

### DLL

Ndiskd.dll

### Examples

**Note**  See [Summary of Objects](../netcx/summary-of-netadaptercx-objects.md) to see a diagram explaining the relationship of the NET\_PACKET object with other objects in the NetAdapterCx.

To obtain a handle for a NET\_PACKET, follow these steps:

1. Run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension.
2. Click on the handle for a NetAdapter that has a NetAdapterCx driver installed.
3. Click the "More Information" link to the right of the NetAdapter's NETADAPTER object to run the [**!ndiskd.cxadapter**](-ndiskd-cxadapter.md) extension.
4. Enter the **!ndiskd.cxadapter** command with the *-datapath* parameter to see that NETADAPTER's datapath queues.
5. Click on the handle for one of the datapath queues.
6. Click on the handle for that datapath queue's ring buffer. TBD - Does this work with nrc?
7. Click on the "List all elements" link at the bottom of the ring buffer details to see the elements it contains. TBD TBD TBD
8. Click on one of the NET\_RING\_COLLECTION objects TBD.

For details on Steps 1-4 of this procedure, see the examples on the **!ndiskd.cxadapter** topic. For details on Step 5 of this procedure, see the examples on the [**!ndiskd.netqueue**](-ndiskd-netqueue.md) topic. For details on Steps 6-7 of this procedure, see the examples on the [**!ndiskd.netrb**](-ndiskd-netrb.md) topic.

In the following example, look for the handle for the TBD of this NET\_RING\_COLLECTION, ffffffTBDffffffffff.

```console
0: kd> !ndiskd.nrc ffffffTBDffffffffff


TBD

TBD

TBD

```

This example shows the use of the -packet option and shows TBD.

```console
0: kd> !ndiskd.nrc ffffffTBDffffffffff -packet

TBD

TBD

TBD

```

This example shows the use of the -fragment (or dump? TBD) option and shows TBD.

```console
0: kd> !ndiskd.nrc ffffffTBDffffffffff -fragment

TBD

TBD

TBD

```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Network Adapter WDF Class Extension (Cx)](../netcx/index.md)

[Summary of Objects](../netcx/summary-of-netadaptercx-objects.md)

[NET\_RING\_COLLECTION](/windows-hardware/drivers/ddi/ringcollection/ns-ringcollection-_net_ring_collection)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)

[**!ndiskd.netqueue**](-ndiskd-netqueue.md)

[**!ndiskd.netrb**](-ndiskd-netrb.md)

[**!ndiskd.netpacket**](-ndiskd-netpacket.md)
