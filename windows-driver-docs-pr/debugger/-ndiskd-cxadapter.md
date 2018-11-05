---
title: ndiskd.cxadapter
description: The ndiskd.cxadapter extension displays information about a NETADAPTER object.
ms.assetid: 5BE91B1C-9795-4E2C-834A-B7424FF1FCDB
keywords: ["ndiskd.cxadapter Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.cxadapter
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.cxadapter


The **!ndiskd.cxadapter** extension displays information about a NETADAPTER object.

For more information about the Network Adapter WDF Class Extension (NetAdapterCx), see [Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx).

```console
!ndiskd.cxadapter [-handle <x>] [-basic] [-power] [-datapath] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of a NETADAPTER.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information.

<span id="_______-power______"></span><span id="_______-POWER______"></span> *-power*   
Displays information about the NETPOWERSETTINGS object of the NETADAPTER.

<span id="_______-datapath______"></span><span id="_______-DATAPATH______"></span> *-datapath*   
Displays information about the datapath queues.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

To obtain a handle for a NETADAPTER object, first run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) command to see a list of all NIC drivers and NetAdapters on the system. In the following example, look for the handle for the NetAdapter named Realtek PCIe GBE Family Controller NetAdapter Sample Driver \#2. Its handle is ffffd1022d048030.

```console
0: kd> !ndiskd.netadapter
    Driver             NetAdapter          Name                                 
    ffffd1022e8ecae0   ffffd1022d048030    Realtek PCIe GBE Family Controller NetAdapter Sample Driver #2
    ffffd1022ed908e0   ffffd1022e8611a0    Microsoft Kernel Debug Network Adapter
```

By clicking on this NetAdapter's handle or by entering the **!ndiskd.netadapter -handle** command with its handle on the command line, you can see details for this NetAdapter, including its NETADAPTER object. The Realtek PCIe GBE Family Controller NetAdapter Sample Driver \#2's NETADAPTER handle is 00002efdd0e5f988.

```console
0: kd> !ndiskd.netadapter ffffd1022d048030


NETADAPTER

    Realtek PCIe GBE Family Controller NetAdapter Sample Driver #2

    Ndis handle        ffffd1022d048030    
    NETADAPTER         00002efdd0e5f988    More information
    WDFDEVICE          00002efdcf45f2f8
    Driver             ffffd1022e8ecae0 - RtEthSample  v0.0
    Network interface  ffffd1022e395a20

    Media type         802.3
    Device instance    PCI\VEN_10EC&DEV_8168&SUBSYS_816810EC&REV_03\4&22bb23f1&0&0038
    Device object      ffffd1022de127f0    More information
    MAC address        00-e0-4c-68-00-8b


STATE

    Miniport           Running
    Device PnP         Started             Show state history
    Datapath           Normal
    Interface          Up
    Media              Connected
    Power              D0
    References         0n10                Show detail
    Total resets       0
    Pending OID        None
    Flags              NOT_BUS_MASTER, WDF, DEFAULT_PORT_ACTIVATED,
                       SUPPORTS_MEDIA_SENSE, DOES_NOT_DO_LOOPBACK,
                       MEDIA_CONNECTED
    PnP flags          PM_SUPPORTED, DEVICE_POWER_ENABLED,
                       DEVICE_POWER_WAKE_ENABLE, HARDWARE_DEVICE,
                       NDIS_WDM_DRIVER, WAKE_CAPABLE


IP ADDRESS SUMMARY

    10.137.188.169                         See all IP addresses on this adapter
    fe80::3cad:81bb:5dad:1066


BINDINGS

    Protocol list      Driver              Open               Context           
    MSLLDP             ffffd1023043f6a0    ffffd1022e786a90   ffffd102307465c0
    LLTDIO             ffffd1022c6b7830    ffffd1022ef8cc00   ffffd1022f1e5730
    TCPIP6             ffffd1022e2c7c10    ffffd10230b98310   ffffd102304d9010
    (RASPPPOE)         Not running
    (RDMANDK)          ffffd1022d574a70    Declined with NDIS_STATUS_NOT_RECOGNIZED
    RSPNDR             ffffd1022c71a830    ffffd1022de0cc00   ffffd1022d03f6a0
    TCPIP              ffffd1022e2cbc10    ffffd1022de067f0   ffffd1022d03f010
    NDISUIO            ffffd1022de07670    ffffd1022cd648d0   ffffd10231131970

    Filter list        Driver              Module             Context           
    WFP 802.3 MAC Layer LightWeight Filter-0000
                       ffffd1022e384d70    ffffd1022f271660   ffffd10230cfe2c0
    QoS Packet Scheduler-0000
                       ffffd1022d56f220    ffffd1022f26d660   ffffd10231778700
    WFP Native MAC Layer LightWeight Filter-0000
                       ffffd1022e384ad0    ffffd1022f26b660   ffffd1022ed59c20



MORE INFORMATION

    Driver handlers                        Task offloads
    Power management                       PM protocol offloads
    Pending OIDs
    Pending NBLs                           Receive side throttling
    Wake-on-LAN (WoL)                      Packet filter
    Receive queues                         Receive filtering
    RSS                                    NIC switch
                                           Selective suspend
    NDIS ports                             WMI guids
    Diagnostic log
```

Because the NETADAPTER object is a WDF object, clicking its handle will cause the debugger to run the [**!wdfkd.wdfhandle**](-wdfkd-wdfhandle.md) command which will give you more information about it from a WDF perspective. To see more detailed information about the NETADAPTER from a networking perspective, click the "More Information" link to the right of the NETADAPTER's handle to run the **!ndiskd.cxadapter** command with its handle.

```console
0: kd> !ndiskd.cxadapter ffffd1022f1a0720


NETADAPTER

    Miniport           ffffd1022d048030 - Realtek PCIe GBE Family Controller NetAdapter Sample Driver #2
    NETADAPTER         00002efdd0e5f988    
    WDFDEVICE          00002efdcf45f2f8    

    Event Callbacks                        Function pointer   Symbol (if available)
    EvtAdapterCreateTxQueue                fffff80034151508   RtEthSample+1508
    EvtAdapterCreateRxQueue                fffff800341510ec   RtEthSample+10ec

    Show datapath info
    Show NETPOWERSETTINGS info
```

You can also combine this command other parameters such as *-datapath* to see more information for this NETADAPTER.

```console
0: kd> !ndiskd.cxadapter ffffd1022f1a0720 -basic -datapath


NETADAPTER

    Miniport           ffffd1022d048030 - Realtek PCIe GBE Family Controller NetAdapter Sample Driver #2
    NETADAPTER         00002efdd0e5f988    
    WDFDEVICE          00002efdcf45f2f8    

    Event Callbacks                        Function pointer   Symbol (if available)
    EvtAdapterCreateTxQueue                fffff80034151508   RtEthSample+1508
    EvtAdapterCreateRxQueue                fffff800341510ec   RtEthSample+10ec


DATAPATH QUEUES

    NETTXQUEUE         ffffd1022f512700
    NETRXQUEUE         ffffd1022cc7b0d0
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!wdfkd.wdfhandle**](-wdfkd-wdfhandle.md)

 

 






