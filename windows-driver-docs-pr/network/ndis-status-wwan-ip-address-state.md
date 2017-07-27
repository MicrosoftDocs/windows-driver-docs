---
title: NDIS_STATUS_WWAN_IP_ADDRESS_STATE
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_WWAN_IP_ADDRESS_STATE notification to inform the MB service about changes to the IP configuration for an additional PDP context.
ms.assetid: 98E4028D-AD75-4F12-ADA4-41725253166F
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WWAN_IP_ADDRESS_STATE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_IP\_ADDRESS\_STATE


Miniport drivers use the NDIS\_STATUS\_WWAN\_IP\_ADDRESS\_STATE notification to inform the MB service about changes to the IP configuration for an additional PDP context.

This notification uses the [**NDIS\_WWAN\_IP\_ADDRESS\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn449746) structure.

Remarks
-------

This notification must be sent on the NDIS port associated with the additional PDP context session.

Miniport drivers should send this notification after an additional PDP context has been successfully activated and the IP configuration has been acquired for that context. If the device indicates unsolicited IP configuration changes post-context activation, then miniport drivers should send an unsolicited indication with this notification with the updated IP configuration.

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
<td><p>Available in Windows 8.1 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_IP\_ADDRESS\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn449746)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_IP_ADDRESS_STATE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


