---
title: ndiskd.netpacket
description: The ndiskd.netpacket extension displays information about a NET_PACKET structure.
ms.assetid: 304BA2CF-B6BC-452C-8543-9B872054AA9E
keywords: ["ndiskd.netpacket Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.netpacket
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.netpacket


The **!ndiskd.netpacket** extension displays information about a [NET\_PACKET](https://docs.microsoft.com/windows-hardware/drivers/netcx/net-packet) structure.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx).

```console
!ndiskd.netpacket [-handle <x>] [-basic] [-layout] [-checksum] [-data] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Address of a NET\_PACKET.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information.

<span id="_______-layout______"></span><span id="_______-LAYOUT______"></span> *-layout*   
Displays packet protocol layout.

<span id="_______-checksum______"></span><span id="_______-CHECKSUM______"></span> *-checksum*   
Displays packet checksum information.

<span id="_______-data______"></span><span id="_______-DATA______"></span> *-data*   
Dumps the payload memory.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

**Note**  See [Summary of Objects](https://docs.microsoft.com/windows-hardware/drivers/netcx/summary-of-objects) to see a diagram explaining the relationship of the NET\_PACKET object with other objects in the NetAdapterCx.

 

To obtain a handle for a NET\_PACKET, follow these steps:

1.  Run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension.
2.  Click on the handle for a NetAdapter that has a NetAdapterCx driver installed.
3.  Click the "More Information" link to the right of the NetAdapter's NETADAPTER object to run the [**!ndiskd.cxadapter**](-ndiskd-cxadapter.md) extension.
4.  Enter the **!ndiskd.cxadapter** command with the *-datapath* parameter to see that NETADAPTER's datapath queues.
5.  Click on the handle for one of the datapath queues.
6.  Click on the handle for that datapath queue's ring buffer.
7.  Click on the "List all elements" link at the bottom of the ring buffer details to see the elements it contains.

For details on Steps 1-4 of this procedure, see the examples on the **!ndiskd.cxadapter** topic. For details on Step 5 of this procedure, see the examples on the [**!ndiskd.netqueue**](-ndiskd-netqueue.md) topic. For details on Steps 6-7 of this procedure, see the examples on the [**!ndiskd.netrb**](-ndiskd-netrb.md) topic.
In the following example, look for the handle for the first NET\_PACKET, ffffd1022d000040.

```console
0: kd> !ndiskd.netrb ffffd1022d000000 -dump

    [000] ffffd1022d000040 - NET_PACKET
    [001] ffffd1022d0000c0 - NET_PACKET
    [002] ffffd1022d000140 - NET_PACKET
    [003] ffffd1022d0001c0 - NET_PACKET
    [004] ffffd1022d000240 - NET_PACKET
    [005] ffffd1022d0002c0 - NET_PACKET
    
    ...

    [07b] ffffd1022d003dc0 - NET_PACKET
    [07c] ffffd1022d003e40 - NET_PACKET
    [07d] ffffd1022d003ec0 - NET_PACKET
    [07e] ffffd1022d003f40 - NET_PACKET
    [07f] ffffd1022d003fc0 - NET_PACKET
```

By clicking on the handle for this NET\_PACKET or by entering **!ndiskd.netpacket -handle** on the command line, you can see details for this NET\_PACKET, including the ring buffer that contains it, the datapath queue that contains its ring buffer, and the handle for its first fragment.

```console
0: kd> !ndiskd.netpacket ffffd1022d000040


    NET_PACKET         ffffd1022d000040    Ring Buffer        ffffd1022d000000
    First fragment     ffffd1022d000040    NETTXQUEUE         ffffd1022f512700

    Client Context     ffffd1022d000090

    Show protocol layout
    Show checksum information
    Dump data payload
```

You can now combine the basic description with any of the other **!ndiskd.netpacket** parameters, or all of them, to see specific information for this fragment. The following example uses all parameters.

```console
0: kd> !ndiskd.netpacket ffffd1022d000040 -basic -layout -checksum -data

    NET_PACKET         ffffd1022d000040    Ring Buffer        ffffd1022d000000
    First fragment     ffffd1022d000040    NETTXQUEUE         ffffd1022f512700

    Client Context     ffffd1022d000090


    Protocol Layout                                                             

    Layer 2 Type       ETHERNET
    Header Length      0n14

    Layer 3 Type       IPV4_NO_OPTIONS
    Header Length      0n20

    Layer 4 Type       UDP
    Header Length      8


    Checksum Information                                                        

    Layer 2            TX_PASSTHROUGH
    Layer 3            TX_REQUIRED
    Layer 4            TX_PASSTHROUGH


    Payload data                                                                

    Fragment           ffffd1022d000040
    ffffd102303e8332  00 00 01 02 71 68 0a 89-be 39 e0 00 00 16 94 04  ····qh···9······
    ffffd102303e8342  00 00 22 00 fa 01 00 00-00 01 03 00 00 00 e0 00  ··"·············
    ffffd102303e8352  00 fc   
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx)

[Summary of Objects](https://docs.microsoft.com/windows-hardware/drivers/netcx/summary-of-objects)

[NET\_PACKET](https://docs.microsoft.com/windows-hardware/drivers/netcx/net-packet)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)

[**!ndiskd.netqueue**](-ndiskd-netqueue.md)

[**!ndiskd.netrb**](-ndiskd-netrb.md)

 

 






