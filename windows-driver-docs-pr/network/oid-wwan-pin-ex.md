---
title: OID_WWAN_PIN_EX
description: OID_WWAN_PIN_EX sets or returns expanded information related to Personal Identification Numbers (PINs).
ms.assetid: 4D3D91B2-7B3C-4C8F-B98F-0F9999D04C03
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_PIN_EX Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_PIN\_EX


OID\_WWAN\_PIN\_EX sets or returns expanded information related to Personal Identification Numbers (PINs).

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PIN\_INFO**](ndis-status-wwan-pin-info.md) status notification when they have completed the set or query request.

Miniport drivers should send [**NDIS\_STATUS\_WWAN\_PIN\_INFO**](ndis-status-wwan-pin-info.md) status notifications containing an [**NDIS\_WWAN\_PIN\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567911) structure to return PIN-type and PIN-entry state information, primarily to indicate whether a PIN is required to unlock the MB device or Subscriber Identity Module (SIM card) when completing query requests.

Callers requesting to set information related to PINs provide an [**NDIS\_WWAN\_SET\_PIN\_EX**](https://msdn.microsoft.com/library/windows/hardware/hh439842) structure to the miniport driver to send a PIN to the MB device, enable or disable PIN settings, or to change a PIN on the SIM.

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
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 




