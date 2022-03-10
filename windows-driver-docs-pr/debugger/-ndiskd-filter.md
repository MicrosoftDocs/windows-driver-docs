---
title: ndiskd.filter
description: The ndiskd.filter extension displays information about an NDIS light-weight filter (LWF). If you run this extension with no parameters, ndiskd will display a list of all LWFs.
keywords: ["ndiskd.filter Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
api_name:
- ndiskd.filter
api_type:
- NA
---

# !ndiskd.filter

The **!ndiskd.filter** extension displays information about an NDIS light-weight filter (LWF). If you run this extension with no parameters, !ndiskd will display a list of all LWFs.

```console
!ndiskd.filter [-handle <x>] [-findname <any>] [-handlers]
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Optional handle of an NDIS light-weight filter.

<span id="_______-findname______"></span><span id="_______-FINDNAME______"></span> *-findname*   
Filters LWFs by name prefix.

<span id="_______-handlers______"></span><span id="_______-HANDLERS______"></span> *-handlers*   
Displays this LWF's filter handlers.

### DLL

Ndiskd.dll

### Examples

Enter the **!ndiskd.filter** command with no parameters to get a list of all filters. In this example, look for the ffff8083e14e8460 handle. Note that this handle is for the filter itself and is nested under its associated filter *driver*, the QoS Packet Scheduler.

```console
3: kd> !ndiskd.filter
ffff8083e1a7fd90 - QoS Packet Scheduler
  Filter ffff8083e14e8460, Miniport ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
ffff8083e1a96b80 - Virtual WiFi Filter Driver
ffff8083e19c4b70 - WFP vSwitch Layers LightWeight Filter
ffff8083e19a6ad0 - WFP Native MAC Layer LightWeight Filter
  Filter ffff8083e43df8f0, Miniport ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
ffff8083e19a6d70 - WFP 802.3 MAC Layer LightWeight Filter
  Filter ffff8083e0d89c70, Miniport ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
```

By using this filter handle we can now see more detailed information about it, such as it State, Higher filter handle, and Lower filter handle.

```console
3: kd> !ndiskd.filter ffff8083e14e8460


FILTER

    Microsoft Kernel Debug Network Adapter-QoS Packet Scheduler-0000

    Ndis handle        ffff8083e14e8460
    Filter driver      ffff8083e1a7fd90 - QoS Packet Scheduler
    Module context     ffff8083e26953e0
    Miniport           ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
    Network interface  ffff8083e200f010

    State              Running
    Datapath           Send only
    References         1
    Flags              RUNNING
    More flags         OID_TOP

    Higher filter      ffff8083e0d89c70 - Microsoft Kernel Debug Network Adapter-WFP 802.3 MAC Layer LightWeight Filter-0000
    Lower filter       ffff8083e43df8f0 - Microsoft Kernel Debug Network Adapter-WFP Native MAC Layer LightWeight Filter-0000

    Driver handlers
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)
