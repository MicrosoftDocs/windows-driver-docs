---
title: ndiskd.netqueue
description: The ndiskd.netqueue extension displays information about a NETTXQUEUE or NETRXQUEUE object.
keywords: ["ndiskd.netqueue Windows Debugging"]
ms.date: 06/17/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.netqueue
api_type:
- NA
---

# !ndiskd.netqueue

The **!ndiskd.netqueue** extension displays information about a NETTXQUEUE or NETRXQUEUE object.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](../netcx/index.md).

```console
!ndiskd.netqueue -handle <x> [-basic]
```

## Parameters

*-handle*   
Required. Handle of a NETTXQUEUE or NETRXQUEUE.

*-basic*   
Displays basic information.

### DLL

Ndiskd.dll

### Examples

**Note**  See [Summary of Objects](../netcx/summary-of-netadaptercx-objects.md) to see a diagram explaining the relationship of the NETTXQUEUE and NETRXQUEUE objects with other objects in the NetAdapterCx.

To obtain a handle for a NETTXQUEUE or NETRXQUEUE, follow these steps:

1. Run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension.
2. Click on the handle for a NetAdapter that has a NetAdapterCx driver installed.
3. Click the "More Information" link to the right of the NetAdapter's NETADAPTER object to run the [**!ndiskd.cxadapter**](-ndiskd-cxadapter.md) extension.
4. Enter the **!ndiskd.cxadapter** command with the *-datapath* parameter to see that NETADAPTER's datapath queues.

For details on this procedure, see the examples on the **!ndiskd.cxadapter** topic.
In the following example, look for the handle for this NETADAPTER's NETTXQUEUE, ffffd1022f512700.

```console
0: kd> !ndiskd.cxadapter ffffd1022f1a0720 -basic -datapath


NETADAPTER

    Miniport           ffffd1022d048030 - Realtek PCIe GBE Family Controller NetAdapter Sample Driver #2
    NETADAPTER         00002efdd0e5f988    
    WDFDEVICE          00002efdcf45f2f8   

    Event Callbacks                        Function pointer   Symbol (if available)
    EvtAdapterCreateTxQueue                fffff80034151508   RtEthSample+1508
    EvtAdapterCreateRxQueue                fffff800341510ec   RtEthSample+10ec


DATAPATH QUEUES

    NETTXQUEUE         ffffd1022f512700
    NETRXQUEUE         ffffd1022cc7b0d0
```

By clicking on the NETTXQUEUE's handle or entering the **!ndiskd.netqueue -handle** command on the command line, you can see details for this queue, including the handle to its companion WDF object, the handle to its ring buffer, and function pointers for its registered callbacks.

```console
0: kd> !ndiskd.netqueue ffffd1022f512700

    NETTXQUEUE         00002efdd0aed9a8
    Ring buffer        ffffd1022d000000

    Switch to EC thread

    Event Callbacks                        Function pointer   Symbol (if available)
    EvtQueueAdvance                        fffff80034152af8   RtEthSample+2af8
    EvtQueueArmNotification                fffff80034159a94   RtEthSample+9a94
    EvtQueueCancel                         fffff800341598d8   RtEthSample+98d8
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Network Adapter WDF Class Extension (Cx)](../netcx/index.md)

[Summary of Objects](../netcx/summary-of-netadaptercx-objects.md)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)
