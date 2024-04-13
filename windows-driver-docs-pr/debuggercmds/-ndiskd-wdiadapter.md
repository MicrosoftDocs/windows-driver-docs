---
title: "!ndiskd.wdiadapter"
description: "The !ndiskd.wdiadapter extension displays information about a WDIWiFi CAdapter structure. If you run this extension with no parameters, ndiskd will display a list of all WDIWiFi CAdapter structures."
keywords: ["!ndiskd.wdiadapter Windows Debugging"]
ms.date: 06/26/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.wdiadapter
api_type:
- NA
---

# !ndiskd.wdiadapter

The **!ndiskd.wdiadapter** extension displays information about a WDIWiFi!CAdapter structure. If you run this extension with no parameters, !ndiskd will display a list of all WDIWiFi!CAdapter structures.

For more information about WDI miniport drivers, see the [WDI Miniport Driver Design Guide](../network/wdi-miniport-driver-design-guide.md).

For more information about WDI miniport driver reference, see [WDI Miniport Driver Reference](/windows-hardware/drivers/ddi/_netvista/).

```console
!ndiskd.wdiadapter [-handle <x>] [-pm] [-rcvfilter] 
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Optional handle of a CAdapter object.

<span id="_______-pm______"></span><span id="_______-PM______"></span> *-pm*   
Shows power management state and capabilities.

<span id="_______-rcvfilter______"></span><span id="_______-RCVFILTER______"></span> *-rcvfilter*   
Shows receive filtering capabilities.

### DLL

Ndiskd.dll

### Examples

Run the **!ndiskd.wdiadapter** extension with no parameters to see a list of all CAdapter objects, along with details for each of their WDI Adapters. In the following example, there is only one CAdapter structure. The handle for its associated WDI Adapter is ffffc804af396000.

```console
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

```console
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

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[WDI Miniport Driver Design Guide](../network/wdi-miniport-driver-design-guide.md)

[WDI Miniport Driver Reference](/windows-hardware/drivers/ddi/_netvista/)

