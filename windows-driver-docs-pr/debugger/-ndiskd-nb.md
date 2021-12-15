---
title: ndiskd.nb (WinDbg)
description: The ndiskd.nb extension displays information about a NET_BUFFER (NB) structure.
keywords: ["ndiskd.nb Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
api_name:
- ndiskd.nb
api_type:
- NA
---

# !ndiskd.nb

The **!ndiskd.nb** extension displays information about a [**NET\_BUFFER**](../network/net-buffer-structure.md) (NB) structure.

```console
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

### DLL

Ndiskd.dll

### Examples

The **NET\_BUFFER** in the following examples was obtained from the [**NET\_BUFFER\_LIST**](../network/net-buffer-list-structure.md) in the Examples section of the [**!ndiskd.nbl**](-ndiskd-nbl.md) topic. The NB's handle is ffffdf8014952610.

```console
2: kd> !ndiskd.nbl ffffdf80149524a0 -data
NET_BUFFER ffffdf8014952610
```

You can click the **NET\_BUFFER**'s handle or run the **!ndiskd.nb -handle** command to see its details.

```console
2: kd> !ndiskd.nb ffffdf8014952610
    NB                 ffffdf8014952610    Next NB            0
    Length             0                   Source pool        ffffdf80147e4a40
    First MDL          ffffdf8014a37930    DataOffset         0
    Current MDL        [First MDL]         Current MDL offset 0

    View associated NBL
```

Use the **!ndiskd.nb -chain** command to see this **NET\_BUFFER**'s MDL chain in addition to its basic details. In the following example, there is only one MDL. Its handle is ffffdf8014a37930.

```console
2: kd> !ndiskd.nb ffffdf8014952610 -chain
    NB                 ffffdf8014952610    Next NB            0
    Length             0                   Source pool        ffffdf80147e4a40
    First MDL          ffffdf8014a37930    DataOffset         0
    Current MDL        [First MDL]         Current MDL offset 0
        MDL [current]      ffffdf8014a37930    MDL Flags             c
        MappedSystemVa     ffffdf8014bf0024    ByteCount          0n1514
        Process            [System process]    ByteOffset         0n36  
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER**](../network/net-buffer-structure.md)

[**NET\_BUFFER\_LIST**](../network/net-buffer-list-structure.md)

[**!ndiskd.nbl**](-ndiskd-nbl.md)
