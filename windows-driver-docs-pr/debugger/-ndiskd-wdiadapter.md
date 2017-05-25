---
title: ndiskd.wdiadapter
description: The ndiskd.wdiadapter extension displays information about a WDIWiFi CAdapter structure. If you run this extension with no parameters, ndiskd will display a list of all WDIWiFi CAdapter structures.
ms.assetid: 1AC069E8-CF87-459B-9C56-DDC1A6F765A8
keywords: ["ndiskd.wdiadapter Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.wdiadapter
api_type:
- NA
---

# !ndiskd.wdiadapter


The **!ndiskd.wdiadapter** extension displays information about a WDIWiFi!CAdapter structure. If you run this extension with no parameters, !ndiskd will display a list of all WDIWiFi!CAdapter structures.

For more information about WDI miniport drivers, see the [WDI Miniport Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/wdi-miniport-driver-design-guide).

For more information about WDI miniport driver reference, see [WDI Miniport Driver Reference](https://msdn.microsoft.com/library/windows/hardware/dn926075).

``` syntax
    !ndiskd.wdiadapter [-handle <x>] [-pm] [-rcvfilter] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of a CAdapter object.

<span id="_______-pm______"></span><span id="_______-PM______"></span> *-pm*   
Shows power management state and capabilities.

<span id="_______-rcvfilter______"></span><span id="_______-RCVFILTER______"></span> *-rcvfilter*   
Shows receive filtering capabilities.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run the **!ndiskd.wdiadapter** extension with no parameters to see a list of all CAdapter objects, along with details for each of their WDI Adapters. In the following example, there is only one CAdapter structure. The handle for its associated WDI Adapter is ffffc804af396000.

```cmd
1: kd> !ndiskd.wdiadapter
    CAdapter                                                                    
    ffffc804af396000 - WDI Adapter


WDI ADAPTER

    Object             ffffc804af396000
    Miniport           ffffc804b9e6f1a0
    WDI driver         ffffc804b8ce7c40 - WDI MiniDriver
    NetGuid            47cb3aa5-e29c-4628-80bd-5023c53fcccb
    Power              D0

    CCtlPlane          ffffc804af396080
    CTxMgr             ffffc804af399790


DEVICE COMMANDS

    Scheduler state    DeviceCommandSchedulerStateInit
    [No queued device commands found]

Device Command Scheduler


SERIALIZED JOBS

    Job                State               Type               Child             
    ffffc804b9f33000   StepPending         WiFiJobMiniportInitialize



ACTIVE JOBS

    Job                State               Type               Child             
    ffffc804b9f33000   StepPending         WiFiJobMiniportInitialize



EVENTS

    Processing?        No

    Event              Status              Type                                 
    [No events found]

Event Queue


MORE INFORMATION

    Power management                       Receive filtering
```

Now you can either click on the "Power management" and "Receive filtering" links at the bottom of the CAdapter structure's description, or you can enter the **!ndiskd.wdiadapter -handle** command with either the *-pm* or *-rcvfilter* option. The following example shows output for the *-rcvfilter* option.

```cmd
1: kd> !ndiskd.wdiadapter ffffc804af396000 -rcvfilter


RECEIVE FILTER

    Current Configuration

    Revision                               0
    Flags                                  0
    Enabled filter types                   [No flags set]
    Enabled queue types                    [No flags set]
    Max Queues                             0
    Queue properties                       [No flags set]
    Filter tests                           [No flags set]
    Header types                           [No flags set]
    MAC header fields                      [No flags set]
    Max MAC header filters                 0
    Max queue groups                       0
    Max queues per group                   0
    Min lookahead split size               0
    Max lookahead split size               0
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[WDI Miniport Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/wdi-miniport-driver-design-guide)

[WDI Miniport Driver Reference](https://msdn.microsoft.com/library/windows/hardware/dn926075)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.wdiadapter%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





