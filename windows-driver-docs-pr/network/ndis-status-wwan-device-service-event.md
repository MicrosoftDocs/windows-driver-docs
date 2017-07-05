---
title: NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT indication to notify the MB Service of device service changes.NDIS\_WWAN\_DEVICE\_SERVICE\_EVENT structure.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2414F63D-756F-4057-974C-A363CEB6399B
keywords: ["NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT
api_location:
- ndis.h
api_type:
- HeaderDef
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT


Miniport drivers use the NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_EVENT indication to notify the MB Service of device service changes.

Miniport drivers can only use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SERVICE\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/hh439837) structure.

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


[**NDIS\_WWAN\_DEVICE\_SERVICE\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/hh439837)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_DEVICE_SERVICE_EVENT%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





