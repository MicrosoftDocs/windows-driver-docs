---
title: OID_DOT11_WPS_ENABLED
author: windows-driver-content
description: OID_DOT11_WPS_ENABLED
ms.assetid: 84dd7496-19e4-4c0c-8208-9ad4d1797154
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WPS_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WPS\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_WPS\_ENABLED object identifier (OID) requests that the miniport driver set the value of the Boolean **msDot11WpsEnabled** management information base (MIB) object. If **msDot11WpsEnabled** is set to **TRUE**, WiFi Protected Setup (WPS) is enabled on the NIC. Otherwise WPS is disabled. The NIC must complete the set request regardless of whether the Extensible AP is in the INIT or OP states.

When queried, this OID requests that the miniport driver return the value of the Boolean **msDot11WpsEnabled** MIB object. If **msDot11AdditionalIEs** is **TRUE**, WiFi Protected Setup (WPS) is enabled on the NIC. Otherwise WPS is disabled.

The **msDot11WpsEnabled** object is only applicable to the Extensible AP.

**Note**  Support for this OID is mandatory.

 

The default value of **msDot11WpsEnabled** is **FALSE**. It is reset to the default value whenever an [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) request is received.

If WPS is enabled on a NIC that is operating in Extensible AP mode, the miniport driver must allow peer stations to associate with the Extensible AP by using [Open System Authentication](https://msdn.microsoft.com/library/windows/hardware/ff569852) or [Wired Equivalent Privacy (WEP)](https://msdn.microsoft.com/library/windows/hardware/ff571060) algorithms, regardless of the enabled authorization and cipher algorithms. For these peer stations, the miniport driver must enforce the following:

-   For inbound packets, only unicast 802.1X packets are accepted. Other data packets will be dropped.

-   For outbound packets, only unicast 802.1X packets are allowed to be sent to the stations. Broadcast and multicast packets are not affected.

-   No encryption or decryption is allowed on unicast data packets. Inbound encrypted data packets are dropped.

When WPS is disabled, the miniport driver must disassociate all peer stations that were associated by using Open System Authentication or WEP algorithms if they were not among the enabled authorization and cipher algorithms.

The 802.11 miniport driver should allow only the following pairs of [**DOT11\_AUTH\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547655) and [**DOT11\_CIPHER\_ALGORITHM**](https://msdn.microsoft.com/library/windows/hardware/ff547672) authentication and cipher algorithms, depending on whether WPS is enabled or disabled.

<a href="" id="wps-is-enabled-------"></a>**WPS is enabled**   
-   **DOT11\_AUTH\_ALGO\_WPA\_PSK/DOT11\_CIPHER\_ALGO\_CCMP**

-   **DOT11\_AUTH\_ALGO\_80211\_OPEN/DOT11\_CIPHER\_ALGO\_WEPXXX**

-   **DOT11\_AUTH\_ALGO\_80211\_OPEN/DOT11\_CIPHER\_ALGO\_NONE**

<a href="" id="wps-is-disabled-------"></a>**WPS is disabled**   
-   **DOT11\_AUTH\_ALGO\_WPA\_PSK/DOT11\_CIPHER\_ALGO\_CCMP**

**Note**  The NIC's response to 802.11 Beacon or Probe Response frames must not change when WPS is enabled with this OID, even if some peer stations were associated by using Open System Authentication or WEP algorithms.

 

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
<td><p>Available in Windows 7 and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_WPS_ENABLED%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


