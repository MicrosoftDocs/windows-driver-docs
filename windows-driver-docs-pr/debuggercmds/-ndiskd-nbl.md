---
title: "!ndiskd.nbl"
description: "The !ndiskd.nbl extension displays information about a NET_BUFFER_LIST (NBL) structure."
keywords: ["!ndiskd.nbl Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.nbl
api_type:
- NA
---

# !ndiskd.nbl


The **!ndiskd.nbl** extension displays information about a [**NET\_BUFFER\_LIST**](../network/net-buffer-list-structure.md) (NBL) structure.

```console
    !ndiskd.nbl [-handle <x>] [-basic] [-chain] [-info] [-data] 
    [-netmon] [-capfile <str>] [-launch] [-overwrite] [-log]
    [-stacks] [-NblCurrentOwner]
```

## Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Address of a **NET\_BUFFER\_LIST** structure.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about an NBL.

<span id="_______-chain______"></span><span id="_______-CHAIN______"></span> *-chain*   
Displays all the NBLs and [**NET\_BUFFER**](../network/net-buffer-structure.md)s in an NBL chain.

<span id="_______-info______"></span><span id="_______-INFO______"></span> *-info*   
Displays all the out-of-band information that is associated with an NBL.

<span id="_______-data______"></span><span id="_______-DATA______"></span> *-data*   
Displays the actual data payload of an NBL.

<span id="_______-netmon______"></span><span id="_______-NETMON______"></span> *-netmon*   
Views the NBL chain in Microsoft Network Monitor.

<span id="_______-capfile______"></span><span id="_______-CAPFILE______"></span> *-capfile*   
Specifies the path to which a netmon capture is saved.

<span id="_______-launch______"></span><span id="_______-LAUNCH______"></span> *-launch*   
Automatically launches netmon.exe after saving the capture file.

<span id="_______-overwrite______"></span><span id="_______-OVERWRITE______"></span> *-overwrite*   
Allows overwriting the capture file if it already exists.

<span id="_______-log______"></span><span id="_______-LOG______"></span> *-log*   
Shows NBL log if NBL history logging is enabled.

<span id="_______-stacks______"></span><span id="_______-STACKS______"></span> *-stacks*   
Includes callstacks with NBL log (use with -log).

<span id="_______-NblCurrentOwner______"></span><span id="_______-nblcurrentowner______"></span><span id="_______-NBLCURRENTOWNER______"></span> *-NblCurrentOwner*   
Shows the current owner of the NBL.

## DLL

Ndiskd.dll

## Examples

In the following example, NBL tracking has been enabled to extract a handle for an NBL from the NBL log. For more information about NBL tracking and the NBL log, see [**!ndiskd.nbllog**](-ndiskd-nbllog.md).

At the time of log collection, the NBL in this example was returned by the TCPIP6 protocol to the WFP Native Mac Layer LightWeight Filter.

```console
2: kd> !ndiskd.nbl ffffdf80149524a0
    NBL                ffffdf80149524a0    Next NBL           NULL
    First NB           ffffdf8014952610    Source             ffffdf80140c71a0 - Microsoft Kernel Debug Network Adapter
    Flags              INDICATED, RETURNED, NBL_ALLOCATED, PROTOCOL_020_0,
                       PROTOCOL_200_0

    Walk the NBL chain                     Dump data payload
    Show out-of-band information
    Review NBL history
```

By clicking on the "Dump data payload" link from the previous example or by entering the **!ndiskd.nbl -handle -data** command, you can see the data payload of this NBL. In the following example, the NBL contains only one **NET\_BUFFER** structure. To further explore the contents of that **NET\_BUFFER** structure, run the [**!ndiskd.nb -handle**](-ndiskd-nb.md) command with its handle.

```console
2: kd> !ndiskd.nbl ffffdf80149524a0 -data
NET_BUFFER ffffdf8014952610
```

## See also


[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER\_LIST**](../network/net-buffer-list-structure.md)

[**NET\_BUFFER**](../network/net-buffer-structure.md)

[**!ndiskd.nbllog**](-ndiskd-nbllog.md)

[**!ndiskd.nb**](-ndiskd-nb.md)

 


