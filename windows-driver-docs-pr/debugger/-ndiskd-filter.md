---
title: ndiskd.filter
description: The ndiskd.filter extension displays information about an NDIS light-weight filter (LWF). If you run this extension with no parameters, ndiskd will display a list of all LWFs.
ms.assetid: 4cf0f8bc-a15a-49db-b7db-13d60fd0c767
keywords: ["ndiskd.filter Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.filter
api_type:
- NA
---

# !ndiskd.filter


The **!ndiskd.filter** extension displays information about an NDIS light-weight filter (LWF). If you run this extension with no parameters, !ndiskd will display a list of all LWFs.

```
!ndiskd.filter [-handle <x>] [-findname <any>] [-handlers] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NDIS light-weight filter.

<span id="_______-findname______"></span><span id="_______-FINDNAME______"></span> *-findname*   
Filters LWFs by name prefix.

<span id="_______-handlers______"></span><span id="_______-HANDLERS______"></span> *-handlers*   
Displays this LWF's filter handlers.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Enter the **!ndiskd.filter** command with no parameters to get a list of all filters. In this example, look for the ffff8083e14e8460 handle. Note that this handle is for the filter itself and is nested under its associated filter *driver*, the QoS Packet Scheduler.

```
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

```
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

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.filter%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





