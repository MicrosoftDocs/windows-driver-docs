---
title: ndiskd.netring
description: The ndiskd.netring extension displays information about a NET_PACKET_FRAGMENT structure.
keywords: ["ndiskd.netring Windows Debugging"]
ms.date: 06/17/2020
topic_type:
- apiref
api_name:
- ndiskd.netring
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.netring

The **!ndiskd.netring** extension displays information about a [NET\_RING](/windows-hardware/drivers/ddi/ring/ns-ring-_net_ring) structure.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](../netcx/index.md) and [Introduction to net rings](../netcx/introduction-to-net-rings.md).

```console
!ndiskd.netring -handle <x> [-basic] [-dump]
```

## Parameters

*-handle*   
Required. Address of a NET_RING

*-basic*    
Displays basic information

*-dump*    
Displays information about each element

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
6. Click on the handle for that datapath queue's ring buffer. TBD - Does this work with netring?
7. Click on the "List all elements" link at the bottom of the ring buffer details to see the elements it contains. TBD TBD TBD
8. Click on one of the NET\_RING (Collection?) objects TBD.
For details on Steps 1-4 of this procedure, see the examples on the **!ndiskd.cxadapter** topic. For details on Step 5 of this procedure, see the examples on the [**!ndiskd.netqueue**](-ndiskd-netqueue.md) topic. For details on Steps 6-7 of this procedure, see the examples on the [**!ndiskd.netrb**](-ndiskd-netrb.md) topic. TBD TBD  

In the following example, use the [**!ndiskd.cxadapter**](-ndiskd-cxadapter.md) extension to look for TBD .

```console
0: kd> !ndiskd.cxdapter 

TBD

TBD

TBD


```

Use the address of the TBD to display the netring TBD.

```console
0: kd> !ndiskd.netring ffffTBDfffff

TBD

TBD

TBD


```

This example shows the use of the -dump option that displays information about each element.

```console
0: kd> !ndiskd.netring ffffTBDfffff -dump

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

[NET\_RING](/windows-hardware/drivers/ddi/ring/ns-ring-_net_ring)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)

[**!ndiskd.netqueue**](-ndiskd-netqueue.md)

[**!ndiskd.netrb**](-ndiskd-netrb.md)

[**!ndiskd.netpacket**](-ndiskd-netpacket.md)
