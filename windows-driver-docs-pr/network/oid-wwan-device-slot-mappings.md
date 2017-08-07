---
title: OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO
author: windows-driver-content
description: OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO sets or returns the device-slot mappings of the MB device (i.e. the executor-slot mappings).
ms.assetid: 54AF3447-7918-49CE-945A-DC8DC1E78CBF
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WWAN_DEVICE_SLOT_MAPPING_INFO Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO


OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO sets or returns the device-slot mappings of the MB device (i.e. the executor-slot mappings).

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [**NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782397) status notification containing an [**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](ndis-wwan-device-slot-mappings.md) structure to provide information on the executor-to-slot mappings.

The following diagram illustrates a query request.

![slot mapping query](images/multi-sim-8-slotmappingquery.png)

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [**NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782397) status notification containing an [**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](ndis-wwan-device-slot-mappings.md) structure, which in turn contains a [**WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](wwan-device-slot-mappings.md) structure to indicate the current mapping status. This holds true even if the set request failed. The structure for set requests for OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO is [**NDIS\_WWAN\_SET\_DEVICE\_SLOT\_MAPPING\_INFO**](ndis-wwan-set-device-slot-mappings.md).

The following diagram illustrates a set request.

![slot mapping set](images/multi-sim-7-slotmappingset.png)

Remarks
-------

The host expects that on first boot, the modem would have a default mapping between slots and executors. The host performs a SET operation with OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO to define the slot that is bound to each executor. The host expects the modem to maintain the mapping across reboots and removals/insertions. This OID is not executor-specific and may be sent to any NDIS instance on the device. It may also query the current mapping as shown above.

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782397)

[**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](ndis-wwan-device-slot-mappings.md)

[**NDIS\_WWAN\_SET\_DEVICE\_SLOT\_MAPPING\_INFO**](ndis-wwan-set-device-slot-mappings.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_SLOT_MAPPING_INFO%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


