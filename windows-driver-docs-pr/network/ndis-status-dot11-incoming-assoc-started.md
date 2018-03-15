---
title: NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED
author: windows-driver-content
description: NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED
ms.assetid: 57fd84ea-9f74-40d9-9ce9-1193edd021c9
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_DOT11_INCOMING_ASSOC_STARTED Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_STARTED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_STARTED status indication when the NIC receives the first valid 802.11 authentication request from a peer station on an infrastructure BSS.

A miniport driver can also make this indication when it receives a valid re-association request packet from a peer station that is in an authenticated (class 2) state.

The data type for this indication is the [**DOT11\_INCOMING\_ASSOC\_STARTED\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548663) structure.

The miniport driver must not make this indication when the received association request is not valid, or if the peer station's association state is not valid.

This indication marks the beginning of an *association indication block*, which denotes the time between NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_STARTED and NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_COMPLETION indications when a NIC is operating in ExtAP OP mode. Every NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_STARTED indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_COMPLETION indication.

A peer station cannot have multiple overlapping incoming association indication blocks. Incoming association indication blocks for different peer stations can overlap.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_STARTED indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When the driver makes this indication, it must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_INCOMING\_ASSOC\_STARTED.

-   **StatusBuffer** must be set to the address of a DOT11\_INCOMING\_ASSOC\_STARTED\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_INCOMING\_ASSOC\_STARTED\_PARAMETERS).

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


[**DOT11\_INCOMING\_ASSOC\_STARTED\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff548663)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

 

 




