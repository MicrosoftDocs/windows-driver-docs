---
title: NDIS_STATUS_WWAN_SLOT_INFO
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_WWAN_SLOT_INFO notification to inform the MB service about the completion of a previous OID_WWAN_SLOT_INFO query request.
ms.assetid: FA1E16E4-56A3-4401-875F-D75DD01FE75D
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WWAN_SLOT_INFO Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_SLOT\_INFO


Miniport drivers use the **NDIS\_STATUS\_WWAN\_SLOT\_INFO** notification to inform the MB service about the completion of a previous [OID\_WWAN\_SLOT\_INFO](https://msdn.microsoft.com/library/windows/hardware/mt799832) query request.

Miniport drivers can send a **NDIS\_STATUS\_WWAN\_SLOT\_INFO** notification as an unsolicited event when the slot/card state changes.

This notification uses the [**NDIS\_WWAN\_SLOT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782408) structure.

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
<td><p>Windows 10, version 1703</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_SLOT\_INFO](https://msdn.microsoft.com/library/windows/hardware/mt799832)

[**NDIS\_WWAN\_SLOT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782408)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_SLOT_INFO%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


