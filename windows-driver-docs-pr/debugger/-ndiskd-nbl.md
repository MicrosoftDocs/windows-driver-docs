---
title: ndiskd.nbl
description: The ndiskd.nbl extension displays information about a NET_BUFFER_LIST (NBL) structure.
ms.assetid: 1806ac7c-b438-4c28-bab0-1b65dba651ea
keywords: ["ndiskd.nbl Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.nbl
api_type:
- NA
---

# !ndiskd.nbl


The **!ndiskd.nbl** extension displays information about a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure) (NBL) structure.

```
    !ndiskd.nbl [-handle <x>] [-basic] [-chain] [-info] [-data] 
    [-netmon] [-capfile <str>] [-launch] [-overwrite] [-log]
    [-stacks] [-NblCurrentOwner]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Address of a **NET\_BUFFER\_LIST** structure.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about an NBL.

<span id="_______-chain______"></span><span id="_______-CHAIN______"></span> *-chain*   
Displays all the NBLs and [**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure)s in an NBL chain.

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

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

In the following example, NBL tracking has been enabled to extract a handle for an NBL from the NBL log. For more information about NBL tracking and the NBL log, see [**!ndiskd.nbllog**](-ndiskd-nbllog.md).

At the time of log collection, the NBL in this example was returned by the TCPIP6 protocol to the WFP Native Mac Layer LightWeight Filter.

```
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

```
2: kd> !ndiskd.nbl ffffdf80149524a0 -data
NET_BUFFER ffffdf8014952610
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)

[**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure)

[**!ndiskd.nbllog**](-ndiskd-nbllog.md)

[**!ndiskd.nb**](-ndiskd-nb.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.nbl%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





