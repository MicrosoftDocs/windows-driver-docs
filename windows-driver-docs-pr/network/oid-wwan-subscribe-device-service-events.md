---
title: OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS
author: windows-driver-content
description: OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS sets information about the list of device services for which the MB device must send NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT notifications.
ms.assetid: 34D38A28-0E81-47B0-9232-F89927DA4B2B
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS


OID\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS sets information about the list of device services for which the MB device must send [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/hh846204) notifications. The MB device should not indicate events for any device service which is not in this list.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/hh846209) status notification that contains the current list of event subscriptions on the MB device.

Callers requesting to set the MB device service event subscription list provide a [**NDIS\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/hh439843) structure to the miniport driver with the appropriate information.

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

## See also


[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/hh846204)

[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_SUBSCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/hh846209)

[**NDIS\_WWAN\_SUBSCRIBE\_DEVICE\_SERVICE\_EVENTS**](https://msdn.microsoft.com/library/windows/hardware/hh439843)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_SUBSCRIBE_DEVICE_SERVICE_EVENTS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


