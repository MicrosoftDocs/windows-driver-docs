---
title: OID\_DOT11\_BEACON\_PERIOD
author: windows-driver-content
description: OID\_DOT11\_BEACON\_PERIOD
ms.assetid: fbb19209-e0dc-44cf-9ebf-60262036ccdc
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_BEACON_PERIOD Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_BEACON\_PERIOD


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_BEACON\_PERIOD object identifier (OID) requests that the miniport driver set the value of the IEEE 802.11 **dot11BeaconPeriod** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **dot11BeaconPeriod** MIB object.

**Note**  If the miniport driver is operating in the Extensible AP (ExtAP) mode, the following requirements apply:
-   Support for this OID is mandatory.

-   The driver must successfully complete a set request. If the **msDot11AutoConfigEnabled** MIB object has the automatic MAC configuration flag DOT11\_MAC\_AUTO\_CONFIG\_ENABLED\_FLAG set, the miniport driver can choose to use a different MAC value.

-   In response to a query request, the miniport driver should return the actual value of the Beacon frame period (the time interval between two Beacons) that the miniport driver uses.

 

The **dot11BeaconPeriod** MIB object is used by the 802.11 station for scheduling the transmission of 802.11 Beacon frames. This value is also specified in the Beacon Interval field of the 802.11 Beacon and Probe Response frames sent by the station.

The data type for OID\_DOT11\_BEACON\_PERIOD is a ULONG value that specifies the beacon period in 802.11 time units (TU). One TU is 1024 microseconds. The **dot11BeaconPeriod** MIB object has a value from 1 through 65535.

**Note**  If the miniport driver is operating in the Extensible Station (ExtSTA) mode, it can only transmit Beacon or Probe Response frames if the desired BSS type is set to **dot11\_BSS\_type\_independent**. For more information about the desired BSS type, see [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md).

 

If the miniport driver is operating in ExtSTA mode, the driver and 802.11 station must do the following when set by OID\_DOT11\_BEACON\_PERIOD:

-   The desired BSS type must have previously been set to **dot11\_BSS\_type\_independent** through [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md). If not, the miniport driver must fail the set request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   After the OID has been set, the 802.11 station uses the specified beacon period only if it starts an IBSS network.

When queried by OID\_DOT11\_BEACON\_PERIOD, the miniport driver must do the following:

-   If the 802.11 station associates with an ESS or joins an IBSS, return the beacon period from the most recently received Beacon or Probe Response.

-   If the 802.11 station starts an IBSS, return the value of **dot11BeaconPeriod** from the previous set of OID\_DOT11\_BEACON\_PERIOD.

**Note**  A Native 802.11 miniport driver that is designed to run on the Windows Vista or Windows Server 2008 operating systems must always reset this 802.11 MIB OID to its default value. This is the case regardless of the value of the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure. This requirement applies to a miniport driver that, in a call to the **NdisMSetMiniportAttributes** function, sets **MiniportAttributes** -&gt; **Native\_802\_11\_Attributes** -&gt; **Header** -&gt; **Revision** to NDIS\_MINIPORT\_ADAPTER\_802\_11\_ATTRIBUTES\_REVISION\_1.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 MIB OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560645)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_BEACON_PERIOD%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


