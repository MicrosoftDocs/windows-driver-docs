---
title: "!ndiskd.minidriver"
description: "The !ndiskd.minidriver command displays information about an NDIS miniport driver. "
keywords: ["!ndiskd.minidriver Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.minidriver
api_type:
- NA
---

# !ndiskd.minidriver

The **!ndiskd.minidriver** command displays information about an NDIS miniport driver. If you run this extension with no parameters, !ndiskd will display a list of NDIS miniport drivers that are active on the system.

```console
!ndiskd.minidriver [-handle <x>] [-basic] [-miniports] [-devices] [-handlers]
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Optional handle of an NDIS miniport driver.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about the miniport driver.

<span id="_______-miniports______"></span><span id="_______-MINIPORTS______"></span> *-miniports*   
Displays the miniports associated with this miniport driver.

<span id="_______-devices______"></span><span id="_______-DEVICES______"></span> *-devices*   
Displays devices associated with this miniport driver.

<span id="_______-handlers______"></span><span id="_______-HANDLERS______"></span> *-handlers*   
Displays this driver's miniport handlers.

## DLL

Ndiskd.dll

## Examples

Enter the **!ndiskd.minidriver** command with no parameters to get a list of all NDIS miniport drivers active on the system. In the following example, look for the kdnic adapter's handle, ffffd20d12dec020

```console
1: kd> !ndiskd.minidriver -basic
    ffffd20d173deae0 - tunnel
    ffffd20d12dec020 - kdnic
```

Using the handle for the kdnic adapter, you can now click on the handle or enter the **!ndiskd.minidriver -handle** command to see detailed information for the tunnel miniport driver, as well as a list of miniports associated with it.

```console
1: kd> !ndiskd.minidriver ffffd20d12dec020


MINIPORT DRIVER

    kdnic

    Ndis handle        ffffd20d12dec020    [type it]
    Driver context     fffff80d2fa15100
    DRIVER_OBJECT      ffffd20d12dee540
    Driver image       kdnic.sys
    Registry path      \REGISTRY\MACHINE\SYSTEM\ControlSet001\Services\kdnic
    Reference Count    2
    Flags              [No flags set]


MINIPORTS

    Miniport
    ffffd20d12dd71a0 - Microsoft Kernel Debug Network Adapter

    Handlers
    Device objects
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

