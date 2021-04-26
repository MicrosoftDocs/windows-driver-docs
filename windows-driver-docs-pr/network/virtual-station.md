---
title: Virtual Station
description: Virtual Station
keywords:
- Virtual Station WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Station




 

Beginning with NDIS 6.20 (Windows 7), the operating system provides a virtual station (VSTA) that can interact with the 802.11 miniport driver.

An independent hardware vendor (IHV) uses VSTA functionality through the [IHV Extensibility framework](overview-of-ihv-extensibility.md) rather than through Win32 application programming interfaces (APIs).

The creation of the virtual station is initiated when the IHV Extensions DLL calls the [**Dot11ExtRequestVirtualStation**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_request_virtual_station) function. The operating system creates only one virtual station on the computer at a time, and only if an IHV Extensions DLL issues a **Dot11ExtRequestVirtualStation** request.

The operating system calls the [*Dot11ExtIhvInitVirtualStation*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_virtual_station) function to initialize the IHV Extensions DLL for virtual station operations. This call also initializes the user-mode API interface between the operating system and the DLL.

**Note**  To ensure that a virtual station is created in a consistent fashion, a computer should have only one installation of the IHV Extensions DLL that attempts to use Virtual Station functionality. Even if more than one DLL is installed, only one virtual station can be created. The operating system cannot guarantee which DLL will have access to a virtual station after the computer is restarted. Note that if a virtual station already has been created at the request of one DLL and a second DLL then calls **Dot11ExtRequestVirtualStation**, a success code might be returned but a second virtual station will not be created.
An IHV Extensions DLL should set a two-minute timer after it calls the **Dot11ExtRequestVirtualStation** function. If the timer expires before the virtual station adapter arrival event, the DLL should assume that the virtual station was not created.

 

### <a href="" id="extensible-ap-virtual-station-interactions"></a> Extensible AP/Virtual Station Interactions

If your driver implements virtual station functionality but cannot sustain both [Extensible Access Point (ExtAP)](/previous-versions/windows/hardware/wireless/extensible-access-point-operation-mode) and virtual station connections at the same time on different ports, the driver should perform the following actions.

-   Inform the operating system whether a port that is being used for ExtAP can or cannot sustain functionality at all times. In particular, the driver should issue the following status indications on the ExtAP port, using the appropriate status code ( [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)-&gt;**StatusCode**) and reason code:

    <a href="" id="ndis-status-dot11-stop-ap"></a>[NDIS\_STATUS\_DOT11\_STOP\_AP](/previous-versions/windows/hardware/wireless/ndis-status-dot11-stop-ap)  
    Indicates that AP functionality cannot be sustained on the ExtAP port. In this case, set [**DOT11\_STOP\_AP\_PARAMETERS**](/windows-hardware/drivers/ddi/windot11/ns-windot11-_dot11_stop_ap_parameters)-&gt; **ulReason** to a value of DOT11\_STOP\_AP\_REASON\_AP\_ACTIVE. Issue this status indication in the following situations:

    -   Before the virtual station port begins to use the shared resource that would block simultaneous virtual station and ExtAP connections
    -   If the ExtAP port transitions to the ExtAP INIT state, and virtual station resource use would prevent successful initialization of the ExtAP port.

    <a href="" id="---------ndis-status-dot11-can-sustain-ap"></a>[NDIS\_STATUS\_DOT11\_CAN\_SUSTAIN\_AP](/previous-versions/windows/hardware/wireless/ndis-status-dot11-can-sustain-ap)  
    Indicates that the virtual station port is disconnected, or that use of a virtual station resource will not prevent successful transition of the port to the ExtAP INIT state.

-   While connecting to a virtual station port, call the [**Dot11ExtSetVirtualStationAPProperties**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_virtual_station_ap_properties) function to provide information about the AP implementation that is hosted by the virtual station connection.

-   Fail the virtual station port connections if the ExtAP port is running in the OP state and one of the following situations occurs:
    -   One or more clients is on the ExtAP port.
    -   The virtual station attempts to start a connection that duplicates [Wireless Hosted Network](/windows/win32/nativewifi/about-the-wireless-hosted-network) settings.

### <a href="" id="native-802-11-ihv-extensibility-functions-that-support-a-virtual-stati"></a> Native 802.11 IHV Extensibility Functions That Support a Virtual Station

[**Dot11ExtQueryVirtualStationProperties**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_query_virtual_station_properties)

[**Dot11ExtReleaseVirtualStation**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_release_virtual_station)

[**Dot11ExtRequestVirtualStation**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_request_virtual_station)

[**Dot11ExtSetVirtualStationAPProperties**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_virtual_station_ap_properties)

### <a href="" id="structures-that-support-a-virtual-station"></a> Structures That Support a Virtual Station

[**DOT11EXT\_VIRTUAL\_STATION\_AP\_PROPERTY**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_virtual_station_ap_property)

[**DOT11EXT\_VIRTUAL\_STATION\_APIS**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_virtual_station_apis)

 

 
