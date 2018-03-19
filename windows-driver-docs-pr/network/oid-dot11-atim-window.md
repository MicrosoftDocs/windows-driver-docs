---
title: OID_DOT11_ATIM_WINDOW
author: windows-driver-content
description: OID_DOT11_ATIM_WINDOW
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

 

 




