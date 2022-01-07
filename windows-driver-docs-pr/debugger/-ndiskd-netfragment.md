---
title: ndiskd.netfragment
description: The ndiskd.netfragment extension displays information about a NET_PACKET_FRAGMENT structure.
keywords: ["ndiskd.netfragment Windows Debugging"]
ms.date: 06/17/2020
topic_type:
- apiref
api_name:
- ndiskd.netfragment
api_type:
- NA
---

# !ndiskd.netfragment

The **!ndiskd.netfragment** extension displays information about a [NET\_PACKET\_FRAGMENT](/windows-hardware/drivers/ddi/fragment/ns-fragment-_net_fragment) structure.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](../netcx/index.md).

```console
!ndiskd.netfragment -handle <x> 
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Address of a NET\_PACKET\_FRAGMENT.

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
6. Click on the handle for that datapath queue's ring buffer.
7. Click on the "List all elements" link at the bottom of the ring buffer details to see the elements it contains.
8. Click on one of the [NET\_PACKET](/windows-hardware/drivers/ddi/packet/ns-packet-_net_packet) objects in the ring buffer's list of elements.

For details on Steps 1-4 of this procedure, see the examples on the **!ndiskd.cxadapter** topic. For details on Step 5 of this procedure, see the examples on the [**!ndiskd.netqueue**](-ndiskd-netqueue.md) topic. For details on Steps 6-7 of this procedure, see the examples on the [**!ndiskd.netrb**](-ndiskd-netrb.md) topic. For details on Step 8 of this procedure, see the examples on the [**!ndiskd.netpacket**](-ndiskd-netpacket.md) topic.
In the following example, look for the handle for the first fragment of this NET\_PACKET, ffffd1022d000040.

```console
0: kd> !ndiskd.netpacket ffffd1022d000040


    NET_PACKET         ffffd1022d000040    Ring Buffer        ffffd1022d000000
    First fragment     ffffd1022d000040    NETTXQUEUE         ffffd1022f512700

    Client Context     ffffd1022d000090

    Show protocol layout
    Show checksum information
    Dump data payload
```

By clicking on the handle for the first fragment or by entering the **!ndiskd.netfragment -handle** command on the command line, you can see details for this NET\_PACKET\_FRAGMENT, including its Virtual Address, capacity, and whether or not it is the last packet in the NET\_PACKET chain of fragments.

```console
0: kd> !ndiskd.netfragment ffffd1022d000040

    NET_PACKET_FRAGMENT ffffd1022d000040

    Virtual Address    ffffd102303e82f8
    Capacity           0n92
    Valid Length       0n34
    Offset             0n58

    Last packet of chain
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Network Adapter WDF Class Extension (Cx)](../netcx/index.md)

[Summary of Objects](../netcx/summary-of-netadaptercx-objects.md)

[NET\_PACKET\_FRAGMENT](/windows-hardware/drivers/ddi/fragment/ns-fragment-_net_fragment)

[NET\_PACKET](/windows-hardware/drivers/ddi/packet/ns-packet-_net_packet)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)

[**!ndiskd.netqueue**](-ndiskd-netqueue.md)

[**!ndiskd.netrb**](-ndiskd-netrb.md)

[**!ndiskd.netpacket**](-ndiskd-netpacket.md)
