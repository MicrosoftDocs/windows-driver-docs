---
title: NDIS_STATUS_DOT11_PHY_FREQUENCY_ADOPTED
author: windows-driver-content
description: NDIS_STATUS_DOT11_PHY_FREQUENCY_ADOPTED
ms.assetid: f723fa8d-702c-48dd-9a66-7532cc476257
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_PHY_FREQUENCY_ADOPTED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_PHY\_FREQUENCY\_ADOPTED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_PHY\_FREQUENCY\_ADOPTED status indication after it has adopted a channel or frequency to communicate with a peer station on an infrastructure BSS. This indication must be made any time the NIC adopts a new channel or frequency or has started an AP.

The data type for this indication is the [**DOT11\_PHY\_FREQUENCY\_ADOPTED\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548735) structure.

The NIC should treat the available operating channels or frequencies returned by [OID\_DOT11\_AVAILABLE\_CHANNEL\_LIST](oid-dot11-available-channel-list.md) and [OID\_DOT11\_AVAILABLE\_FREQUENCY\_LIST](oid-dot11-available-frequency-list.md) as suggestions. The NIC is free to adopt its own channel or frequency that meets the local regulatory domain.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_PHY\_FREQUENCY\_ADOPTED indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When the driver makes this indication, it must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_PHY\_FREQUENCY\_ADOPTED.

-   **StatusBuffer** must be set to the address of a DOT11\_PHY\_FREQUENCY\_ADOPTED\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_PHY\_FREQUENCY\_ADOPTED\_PARAMETERS).

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


[**DOT11\_PHY\_FREQUENCY\_ADOPTED\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548735)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

[OID\_DOT11\_AVAILABLE\_CHANNEL\_LIST](oid-dot11-available-channel-list.md)

[OID\_DOT11\_AVAILABLE\_FREQUENCY\_LIST](oid-dot11-available-frequency-list.md)

 

 




