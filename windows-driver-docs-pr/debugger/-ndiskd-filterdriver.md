---
title: ndiskd.filterdriver
description: The ndiskd.filterdriver extension displays information about an NDIS filter driver. If you run this extension with no parameters, ndiskd will display a list of all filter drivers.
ms.assetid: 9FE3E885-98BC-4FCC-9E1C-DBECD070F92A
keywords: ["ndiskd.filterdriver Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.filterdriver
api_type:
- NA
---

# !ndiskd.filterdriver


The **!ndiskd.filterdriver** extension displays information about an NDIS filter driver. If you run this extension with no parameters, !ndiskd will display a list of all filter drivers.

```
!ndiskd.filterdriver [-handle <x>] [-filters] [-handlers] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NDIS filter driver.

<span id="_______-filters______"></span><span id="_______-FILTERS______"></span> *-filters*   
Displays instances of this driver's filters.

<span id="_______-handlers______"></span><span id="_______-HANDLERS______"></span> *-handlers*   
Displays this driver's filter handlers.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run **!ndiskd.filterdriver** with no parameters to see a list of all filter drivers on the system. In the following example, look for the Virtual WiFi Filter Driver, whose handle is ffffbc064cc83be0.

```
0: kd> !ndiskd.filterdriver
    ffffbc064ccd4900 - QoS Packet Scheduler
    ffffbc064cc83be0 - Virtual WiFi Filter Driver
    ffffbc064cb91a10 - WFP vSwitch Layers LightWeight Filter
    ffffbc064cb8fd70 - WFP Native MAC Layer LightWeight Filter
    ffffbc064cb59b00 - WFP 802.3 MAC Layer LightWeight Filter
```

By clicking the filter driver handle from the previous example or by using it to enter the **!ndiskd.filterdriver -handle** command in the command window, you can get see more detailed information about that filter driver. In this case, for example, there are no filter modules for this filter driver.

```
0: kd> !ndiskd.filterdriver ffffbc064cc83be0


FILTER DRIVER

    Virtual WiFi Filter Driver

    Ndis handle        ffffbc064cc83be0
    Driver context     ffffbc064cc8e9d0
    Ndis API version   v6.50
    Driver version     v1.0
    Driver object      ffffbc064cc8e9d0
    Driver image       vwififlt.sys

    Bind flags         Optional, Modifying
    Class              [Zero-length string]
    References         1


FILTER MODULES

    Filter module                                                               
    [No filter modules were found]


HANDLERS

    Filter handler                         Function pointer   Symbol (if available)
    SetOptionsHandler                      [None]
    SetFilterModuleOptionsHandler          [None]
    AttachHandler                          fffff80787d83b60  bp
    DetachHandler                          fffff80787d84800  bp
    RestartHandler                         fffff80787d86e20  bp
    PauseHandler                           fffff80787d863e0  bp
    SendNetBufferListsHandler              fffff80787d814d0  bp
    SendNetBufferListsCompleteHandler      fffff80787d81940  bp
    CancelSendNetBufferListsHandler        fffff80787d842f0  bp
    ReceiveNetBufferListsHandler           fffff80787d817e0  bp
    ReturnNetBufferListsHandler            fffff80787d81a80  bp
    OidRequestHandler                      fffff80787d85ae0  bp
    OidRequestCompleteHandler              fffff80787d85fd0  bp
    DirectOidRequestHandler                fffff80787d84af0  bp
    DirectOidRequestCompleteHandler        fffff80787d84e80  bp
    CancelDirectOidRequestHandler          fffff80787d841d0  bp
    DevicePnPEventNotifyHandler            fffff80787d849e0  bp
    NetPnPEventHandler                     fffff80787d85a40  bp
    StatusHandler                          fffff80787d877c0  bp
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.filterdriver%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





