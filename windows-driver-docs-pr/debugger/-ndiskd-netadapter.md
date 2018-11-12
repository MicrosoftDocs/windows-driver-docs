---
title: ndiskd.netadapter
description: The ndiskd.netadapter extension displays information about NDIS miniports, or network adapters, that are active on the system. 
ms.assetid: 7D55F7CE-5DDB-4C80-8C27-F619F2FB7F15
keywords: ["ndiskd.netadapter Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.netadapter
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.netadapter


The **!ndiskd.netadapter** extension displays information about NDIS miniports, or network adapters, that are active on the system. If you run this command with no parameters, !ndiskd will display a list of all network adapters.

```console
     !ndiskd.netadapter [-handle <x>] [-basic] [-diag] [-state] [-bindings] 
        [-ports] [-offloads] [-filterdb] [-timers] [-rst]
        [-pm] [-ss] [-aoac] [-wol] [-protocoloffloads]
        [-rss] [-hw] [-device] [-wmi] [-customwmi]
        [-ndiswmi] [-ref] [-log] [-grovel] [-findname <any>]
        [-rcvfilter] [-nicswitch] [-rcvqueues] [-nicswitches] [-iov]
        [-vfs] [-vports] [-iftrace] [-ip]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NDIS miniport.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays summary information about the miniport.

<span id="_______-diag______"></span><span id="_______-DIAG______"></span> *-diag*   
Displays auto-diagnostic alerts (if any).

<span id="_______-state______"></span><span id="_______-STATE______"></span> *-state*   
Displays the miniport's current state.

<span id="_______-bindings______"></span><span id="_______-BINDINGS______"></span> *-bindings*   
Displays miniport bindings.

<span id="_______-ports______"></span><span id="_______-PORTS______"></span> *-ports*   
Shows a list of NDIS ports.

<span id="_______-offloads______"></span><span id="_______-OFFLOADS______"></span> *-offloads*   
Shows task offload state and capabilities.

<span id="_______-filterdb______"></span><span id="_______-FILTERDB______"></span> *-filterdb*   
Shows the current packet filter.

<span id="_______-timers______"></span><span id="_______-TIMERS______"></span> *-timers*   
Shows timer objects allocated by the miniport.

<span id="_______-rst______"></span><span id="_______-RST______"></span> *-rst*   
Shows Receive-Side Throttling state.

<span id="_______-pm______"></span><span id="_______-PM______"></span> *-pm*   
Shows power management state and capabilities.

<span id="_______-ss______"></span><span id="_______-SS______"></span> *-ss*   
Shows Selective Suspend state.

<span id="_______-aoac______"></span><span id="_______-AOAC______"></span> *-aoac*   
Shows AOAC (Connected Standby) state.

<span id="_______-wol______"></span><span id="_______-WOL______"></span> *-wol*   
Shows Wake-on-LAN (WoL) configuration.

<span id="_______-protocoloffloads______"></span><span id="_______-PROTOCOLOFFLOADS______"></span> *-protocoloffloads*   
Shows active power management protocol offloads.

<span id="_______-rss______"></span><span id="_______-RSS______"></span> *-rss*   
Shows Receive Side Scaling parameters.

<span id="_______-hw______"></span><span id="_______-HW______"></span> *-hw*   
Displays hardware resources.

<span id="_______-device______"></span><span id="_______-DEVICE______"></span> *-device*   
Shows information about the underlying NT device object.

<span id="_______-wmi______"></span><span id="_______-WMI______"></span> *-wmi*   
Shows WMI GUIDs registered to the adapter.

<span id="_______-customwmi______"></span><span id="_______-CUSTOMWMI______"></span> *-customwmi*   
Shows custom WMI GUIDs registered by the miniport.

<span id="_______-ndiswmi______"></span><span id="_______-NDISWMI______"></span> *-ndiswmi*   
Shows NDIS-provided WMI GUIDs.

<span id="_______-ref______"></span><span id="_______-REF______"></span> *-ref*   
Shows a breakdown of references on the miniport.

<span id="_______-log______"></span><span id="_______-LOG______"></span> *-log*   
Displays a PnP and Power event log.

<span id="_______-grovel______"></span><span id="_______-GROVEL______"></span> *-grovel*   
Forces a search for miniport blocks in memory.

<span id="_______-findname______"></span><span id="_______-FINDNAME______"></span> *-findname*   
Filters miniports by name prefix.

<span id="_______-rcvfilter______"></span><span id="_______-RCVFILTER______"></span> *-rcvfilter*   
Shows receive filtering capabilities.

<span id="_______-nicswitch______"></span><span id="_______-NICSWITCH______"></span> *-nicswitch*   
Shows NIC switch capabilities.

<span id="_______-rcvqueues______"></span><span id="_______-RCVQUEUES______"></span> *-rcvqueues*   
Shows receive queues.

<span id="_______-nicswitches______"></span><span id="_______-NICSWITCHES______"></span> *-nicswitches*   
Shows NIC switches.

<span id="_______-iov______"></span><span id="_______-IOV______"></span> *-iov*   
Shows SR-IOV (Single Root I/O Virtualization) capabilities.

<span id="_______-vfs______"></span><span id="_______-VFS______"></span> *-vfs*   
Shows SR-IOV VFs (Virtual Filters).

<span id="_______-vports______"></span><span id="_______-VPORTS______"></span> *-vports*   
Shows Vports (Virtual ports).

<span id="_______-ifrtrace______"></span><span id="_______-IFRTRACE______"></span> *-ifrtrace*   
Shows the in-flight recorder's trace.

<span id="_______-ip______"></span><span id="_______-IP______"></span> *-ip*   
Shows IP addresses on the network's interface.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

By running **!ndiskd.netadapter** with no parameters, you can get a list of all network adapters on the system along with their associated miniport drivers. In this example output, look for the Microsoft Kernel Debug Network Adapter, whose handle is ffffdf80140c71a0. For more information about what the Kernel Debug Network Adapter is, see [Kernel debugging over the network](https://go.microsoft.com/fwlink/p/?linkid=845868) on the NDIS blog.

```console
3: kd> !ndiskd.netadapter
    Driver             NetAdapter          Name                                 
    ffffdf8015a98380   ffffdf8015aa11a0    Microsoft ISATAP Adapter #2
    ffffdf801418d650   ffffdf80140c71a0    Microsoft Kernel Debug Network Adapter
```

By clicking on the handle for the miniport driver or entering the **!ndiskd.netadapter -handle**, you can now see all of NDIS's state on that device. This can be very helpful as a starting place for troubleshooting a network driver or for figuring out where an issue is in the network stack. For example, you can see the Datapath state for the driver and see whether it is connected or not.

At the bottom of the report for this net adapter, there are many other links you can click on to explore further information, such as any pending OIDs and the state of task offloads. These links correspond to many of the parameters for **!ndiskd.netadapter**.

```console
3: kd> !ndiskd.netadapter ffffdf80140c71a0


MINIPORT

    Microsoft Kernel Debug Network Adapter

    Ndis handle        ffffdf80140c71a0
    Ndis API version   v6.20
    Adapter context    ffffdf80147d7230
    Driver             ffffdf801418d650 - kdnic  v4.2
    Network interface  ffffdf80139b3a20

    Media type         802.3
    Physical medium    NdisPhysicalMediumOther
    Device instance    ROOT\KDNIC\0000
    Device object      ffffdf80140c7050    More information
    MAC address        18-03-73-c1-e8-72


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
    Flags              NOT_BUS_MASTER, ALLOW_BUGCHECK_CALLBACK,
                       BUGCHECK_CALLBACK_REGISTERED, DEFAULT_PORT_ACTIVATED,
                       SUPPORTS_MEDIA_SENSE, DOES_NOT_DO_LOOPBACK,
                       MEDIA_CONNECTED
    PnP flags          VIRTUAL_DEVICE, HIDDEN, NO_HALT_ON_SUSPEND,
                       RECEIVED_START


BINDINGS

    Protocol list      Driver              Open               Context           
    MSLLDP             ffffdf80120a5c10    ffffdf8015a749c0   ffffdf8015d325e0
    TCPIP              ffffdf80131cc010    ffffdf801494a650   ffffdf801494aa50
    NDISUIO            ffffdf8015a58140    ffffdf8015a78c10   ffffdf8015a77e00
    TCPIP6             ffffdf80131c9c10    ffffdf80147875a0   ffffdf801494f010
    (RASPPPOE)         Not running
    RSPNDR             ffffdf80120a0c10    ffffdf8015a79c10   ffffdf8015a79010
    LLTDIO             ffffdf8015a5f9b0    ffffdf801406f010   ffffdf8015a786c0
    (RDMANDK)          ffffdf801406d8f0    Declined with NDIS_STATUS_NOT_RECOGNIZED

    Filter list        Driver              Module             Context           
    WFP 802.3 MAC Layer LightWeight Filter-0000
                       ffffdf80139a5a70    ffffdf801494c670   ffffdf801494a010
    QoS Packet Scheduler-0000
                       ffffdf8014039d90    ffffdf801494dc70   ffffdf80147dc2b0
    WFP Native MAC Layer LightWeight Filter-0000
                       ffffdf80139fcd70    ffffdf8014950c70   ffffdf8014950880



MORE INFORMATION

    Driver handlers                        Task offloads
    Power management                       PM protocol offloads
    Pending OIDs                           Timers
    Pending NBLs                           Receive side throttling
    Wake-on-LAN (WoL)                      Packet filter
    Receive queues                         Receive filtering
    RSS                                    NIC switch
    Hardware resources                     Selective suspend
    NDIS ports                             WMI guids
    Diagnostic log
```

As example of using **!ndiskd.netadapter** as a starting place for further debugging, click on the "Driver handlers" link at the bottom of the report to see a list of all registered driver callback handlers for this net adapter's miniport driver. In the following example, clicking the link causes !ndiskd to run the [**!ndiskd.minidriver**](-ndiskd-minidriver.md) extension with the handle of this net adapter's miniport driver. The miniport driver is the kdnic 4.2 and its handle is ffffdf801418d650.

```console
3: kd> !ndiskd.minidriver ffffdf801418d650 -handlers


HANDLERS

    NDIS Handler                           Function pointer   Symbol (if available)
    InitializeHandlerEx                    fffff80f1fd78230  bp
    SetOptionsHandler                      fffff80f1fd72800  bp
    HaltHandlerEx                          fffff80f1fd78040  bp
    ShutdownHandlerEx                      fffff80f1fd722c0  bp

    CheckForHangHandlerEx                  fffff80f1fd72810  bp
    ResetHandlerEx                         fffff80f1fd72f70  bp

    PauseHandler                           fffff80f1fd78000  bp
    RestartHandler                         fffff80f1fd78940  bp

    OidRequestHandler                      fffff80f1fd71c90  bp
    CancelOidRequestHandler                fffff80f1fd722c0  bp
    DirectOidRequestHandler                [None]
    CancelDirectOidRequestHandler          [None]
    DevicePnPEventNotifyHandler            fffff80f1fd789a0  bp

    SendNetBufferListsHandler              fffff80f1fd71870  bp
    ReturnNetBufferListsHandler            fffff80f1fd71b50  bp
    CancelSendHandler                      fffff80f1fd722c0  bp
```

You can now click the "bp" link to the right of each handler to set a breakpoint on that handler to debug a particular problem. For example, if there is a hang in the datapath, you can investigate the driver's SendNetBufferListsHandler or ReturnNetBufferListsHandler.

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Kernel debugging over the network](https://go.microsoft.com/fwlink/p/?linkid=845868)

[**!ndiskd.minidriver**](-ndiskd-minidriver.md)










