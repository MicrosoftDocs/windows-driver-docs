---
title: ndiskd.nb
description: The ndiskd.nb extension displays information about a NET\_BUFFER (NB) structure.
ms.assetid: 7351264c-4adc-43ac-9eca-41deb3d35983
keywords: ["ndiskd.nb Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.nb
api_type:
- NA
---

# !ndiskd.nb


The **!ndiskd.nb** extension displays information about a [**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure) (NB) structure.

```
!ndiskd.nb [-handle <x>] [-verbosity <x>] [-basic] [-chain] [-data] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Address of a **NET\_BUFFER** structure.

<span id="_______-verbosity______"></span><span id="_______-VERBOSITY______"></span> *-verbosity*   
Level of detail to display.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about an NB.

<span id="_______-chain______"></span><span id="_______-CHAIN______"></span> *-chain*   
Displays all the MDLs associated with an NB.

<span id="_______-data______"></span><span id="_______-DATA______"></span> *-data*   
Dumps the actual data payload of an NB.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

The **NET\_BUFFER** in the following examples was obtained from the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure) in the Examples section of the [**!ndiskd.nbl**](-ndiskd-nbl.md) topic. The NB's handle is ffffdf8014952610.

```
2: kd> !ndiskd.nbl ffffdf80149524a0 -data
NET_BUFFER ffffdf8014952610
```

You can click the **NET\_BUFFER**'s handle or run the **!ndiskd.nb -handle** command to see its details.

```
2: kd> !ndiskd.nb ffffdf8014952610
    NB                 ffffdf8014952610    Next NB            0
    Length             0                   Source pool        ffffdf80147e4a40
    First MDL          ffffdf8014a37930    DataOffset         0
    Current MDL        [First MDL]         Current MDL offset 0

    View associated NBL
```

Use the **!ndiskd.nb -chain** command to see this **NET\_BUFFER**'s MDL chain in addition to its basic details. In the following example, there is only one MDL. Its handle is ffffdf8014a37930.

```
2: kd> !ndiskd.nb ffffdf8014952610 -chain
    NB                 ffffdf8014952610    Next NB            0
    Length             0                   Source pool        ffffdf80147e4a40
    First MDL          ffffdf8014a37930    DataOffset         0
    Current MDL        [First MDL]         Current MDL offset 0
        MDL [current]      ffffdf8014a37930    MDL Flags             c
        MappedSystemVa     ffffdf8014bf0024    ByteCount          0n1514
        Process            [System process]    ByteOffset         0n36  
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)

[**!ndiskd.nbl**](-ndiskd-nbl.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.nb%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





