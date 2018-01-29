---
title: ndiskd.netpacket
description: The ndiskd.netpacket extension displays information about a NET_PACKET structure.
ms.assetid: 304BA2CF-B6BC-452C-8543-9B872054AA9E
keywords: ["ndiskd.netpacket Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.netpacket
api_type:
- NA
---

# !ndiskd.netpacket


The **!ndiskd.netpacket** extension displays information about a [NET\_PACKET](https://docs.microsoft.com/windows-hardware/drivers/netcx/net-packet) structure.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx).

```
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

```
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

```
0: kd> !ndiskd.netpacket ffffd1022d000040


    NET_PACKET         ffffd1022d000040    Ring Buffer        ffffd1022d000000
    First fragment     ffffd1022d000040    NETTXQUEUE         ffffd1022f512700

    Client Context     ffffd1022d000090

    Show protocol layout
    Show checksum information
    Dump data payload
```

You can now combine the basic description with any of the other **!ndiskd.netpacket** parameters, or all of them, to see specific information for this fragment. The following example uses all parameters.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.netpacket%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





