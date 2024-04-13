---
title: "!ndiskd.rcvqueue"
description: "The !ndiskd.rcvqueue command displays information about a receive queue."
keywords: ["!ndiskd.rcvqueue Windows Debugging"]
ms.date: 06/26/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.rcvqueue
api_type:
- NA
---

# !ndiskd.rcvqueue

The **!ndiskd.rcvqueue** command displays information about a receive queue.

```console
!ndiskd.rcvqueue -handle <x> [-filters] [-mem] [-verbose] [-rcvqueueverbosity <x>] 
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of a receive queue.

<span id="_______-filters______"></span><span id="_______-FILTERS______"></span> *-filters*   
Shows filters on the queue.

<span id="_______-mem______"></span><span id="_______-MEM______"></span> *-mem*   
Shows shared memory allocations.

<span id="_______-verbose______"></span><span id="_______-VERBOSE______"></span> *-verbose*   
Shows additional details.

<span id="_______-rcvqueueverbosity______"></span><span id="_______-RCVQUEUEVERBOSITY______"></span> *-rcvqueueverbosity*   
Level of detail to display.

## DLL

Ndiskd.dll

## Examples

To obtain the receive queue handle, first enter the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) command with no parameters to see the list of net adapters, their drivers, and their handles. In the following example, look for the Microsoft ISATAP Adapter \#2's NetAdapter handle, ffff8083e02ce1a0.

```console
3: kd> !ndiskd.netadapter
    Driver             NetAdapter          Name                                 
    ffff8083e2668970   ffff8083e02ce1a0    Microsoft ISATAP Adapter #2
    ffff8083e210fae0   ffff8083e0f501a0    Microsoft Kernel Debug Network Adapter
```

Next, with the net adapter's handle, use the **!ndiskd.netadapter -handle -rcvqueues** command to obtain a list of receive queues for this net adapter along with their handles. In this example, there is only one receive queue (the default one) with a handle of ffff8083e3a3d3a0.

```console
3: kd> !ndiskd.netadapter ffff8083e02ce1a0 -rcvqueues


RECEIVE QUEUES

    QueueId            Queue Handle        Processor Affinity                   
    0 [Default]        ffff8083e3a3d3a0    0:0000000000000000 (group:mask)
                       Queue Name:         [Zero-length string]
                       VM Name:            [Zero-length string]
```

Now you can use the queue handle to examine the receive queue details with the **!ndiskd.rcvqueue** command.

```console
3: kd> !ndiskd.rcvqueue ffff8083e3a3d3a0


RECEIVE QUEUE

    [Zero-length string]

    VM name            [Zero-length string]
    QueueId            0
    Ndis handle        ffff8083e3a3d3a0

    Miniport           ffff8083e02ce1a0 - Microsoft ISATAP Adapter #2
    Open               [No associated Open]

    Type               Unspecified
    Flags              [No flags set]
    Allocated          Yes
    References         1

    Num filters        0
    Num buffers hint   0
    MSI-X entry        0
    Lookahead size     0
    Processor affinity 0:0000000000000000 (group:mask)

    Receive filter list
    Shared memory allocations
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

