---
title: OID_WWAN_DEVICE_SLOT_MAPPING_INFO
description: OID_WWAN_DEVICE_SLOT_MAPPING_INFO sets or returns the device-slot mappings of the MB device (i.e. the executor-slot mappings).
ms.assetid: 54AF3447-7918-49CE-945A-DC8DC1E78CBF
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_SLOT_MAPPING_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO


OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO sets or returns the device-slot mappings of the MB device (i.e. the executor-slot mappings).

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [**NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782397) status notification containing an [**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782403) structure to provide information on the executor-to-slot mappings.

The following diagram illustrates a query request.

![slot mapping query](images/multi-SIM_8_slotMappingQuery.png)

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [**NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782397) status notification containing an [**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782403) structure, which in turn contains a [**WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt799890) structure to indicate the current mapping status. This holds true even if the set request failed. The structure for set requests for OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO is [**NDIS\_WWAN\_SET\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782405).

The following diagram illustrates a set request.

![slot mapping set](images/multi-SIM_7_slotMappingSet.png)

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

[**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782403)

[**NDIS\_WWAN\_SET\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782405)

 

 




