---
title: NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION notification to inform the MB Service about a device service subscription in response to an OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS set request.NDIS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION structure.
ms.assetid: E2B839AE-F81A-41EE-8374-F830B79D1E74
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION notification to inform the MB Service about a device service subscription in response to an [OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS](https://msdn.microsoft.com/library/windows/hardware/hh440096) set request.

Miniport drivers cannot use this notification to send unsolicited events.

This indication uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/hh439839) structure.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS](https://msdn.microsoft.com/library/windows/hardware/hh440096)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/hh439839)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_DEVICE_SERVICE_SUBSCRIPTION%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


