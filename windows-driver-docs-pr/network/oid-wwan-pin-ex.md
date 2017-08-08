---
title: OID\_WWAN\_PIN\_EX
author: windows-driver-content
description: OID\_WWAN\_PIN\_EX sets or returns expanded information related to Personal Identification Numbers (PINs).
ms.assetid: 4D3D91B2-7B3C-4C8F-B98F-0F9999D04C03
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_PIN_EX Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_PIN_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


