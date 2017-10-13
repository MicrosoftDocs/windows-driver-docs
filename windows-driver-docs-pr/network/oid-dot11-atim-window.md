---
title: OID_DOT11_ATIM_WINDOW
author: windows-driver-content
description: OID\_DOT11\_ATIM\_WINDOW
ms.assetid: 440b3948-6008-4ac7-8ff1-307d5edaa9b5
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_ATIM_WINDOW Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_ATIM\_WINDOW


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_ATIM\_WINDOW object identifier (OID) requests that the miniport driver set the value of the announcement traffic information message (ATIM) window to the specified value.

When queried, OID\_DOT11\_ATIM\_WINDOW requests that the miniport driver return the value of the ATIM window.

The data type for this OID is a ULONG value that specifies the ATIM window in 802.11 time units (TU). One TU is 1024 microseconds.

The ATIM window is a short time period immediately following the transmission of each 802.11 Beacon frame in an independent basic service set (IBSS) network. During the ATIM window, any station in the IBSS network can indicate the need to transfer data to another station during the next data transmission window.

**Note**  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](https://msdn.microsoft.com/library/windows/hardware/hh440289).

 

If the miniport driver is operating in the Extensible Station (ExtSTA) mode, it fails a set request of OID\_DOT11\_ATIM\_WINDOW under the following conditions:

-   The 802.11 station does not support 802.11 ATIM windows. In this situation, the miniport driver returns NDIS\_STATUS\_NOT\_SUPPORTED from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   The desired basic service set (BSS) type had not previously been set to **dot11\_BSS\_type\_independent** through a set of [OID\_DOT11\_DESIRED\_BSS\_TYPE](oid-dot11-desired-bss-type.md). In this situation, the miniport driver returns NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

-   The beacon period was not previously initialized through a set of [OID\_DOT11\_BEACON\_PERIOD](oid-dot11-beacon-period.md). In this situation, the miniport driver returns NDIS\_STATUS\_INVALID\_DATA from its *MiniportOidRequest* function.

-   The specified ATIM window is less than the target beacon transmission time (TBTT). In this situation, the miniport driver returns NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

When queried, the OID\_DOT11\_ATIM\_WINDOW OID requests that the miniport driver return the value of the ATIM window. If the desired BSS type is not **dot11\_BSS\_type\_independent**, the miniport driver must fail the query request by returning NDIS\_STATUS\_INVALID\_DATA from its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.

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


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_ATIM_WINDOW%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


