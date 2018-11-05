---
title: ndiskd.netqueue
description: The ndiskd.netqueue extension displays information about a NETTXQUEUE or NETRXQUEUE object.
ms.assetid: 101F29AA-5CEE-41F8-A3EC-AA2E74B8E074
keywords: ["ndiskd.netqueue Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.netqueue
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.netqueue


The **!ndiskd.netqueue** extension displays information about a NETTXQUEUE or NETRXQUEUE object.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx).

```console
!ndiskd.netqueue [-handle <x>] [-basic] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of a NETTXQUEUE or NETRXQUEUE.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

**Note**  See [Summary of Objects](https://docs.microsoft.com/windows-hardware/drivers/netcx/summary-of-objects) to see a diagram explaining the relationship of the NETTXQUEUE and NETRXQUEUE objects with other objects in the NetAdapterCx.

 

To obtain a handle for a NETTXQUEUE or NETRXQUEUE, follow these steps:

1.  Run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension.
2.  Click on the handle for a NetAdapter that has a NetAdapterCx driver installed.
3.  Click the "More Information" link to the right of the NetAdapter's NETADAPTER object to run the [**!ndiskd.cxadapter**](-ndiskd-cxadapter.md) extension.
4.  Enter the **!ndiskd.cxadapter** command with the *-datapath* parameter to see that NETADAPTER's datapath queues.

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

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx)

[Summary of Objects](https://docs.microsoft.com/windows-hardware/drivers/netcx/summary-of-objects)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.cxadapter**](-ndiskd-cxadapter.md)

 

 






