---
title: OID_GEN_INTERRUPT_MODERATION
description: As a query, NDIS and overlying drivers use the OID_GEN_INTERRUPT_MODERATION OID to determine if interrupt moderation is enabled on a miniport adapter.
ms.assetid: 4d9d2bda-f0b3-42d5-bb49-93a9b256f5ad
ms.date: 08/08/2017
keywords: 
 -OID_GEN_INTERRUPT_MODERATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_INTERRUPT\_MODERATION


As a query, NDIS and overlying drivers use the OID\_GEN\_INTERRUPT\_MODERATION OID to determine if interrupt moderation is enabled on a miniport adapter. If the query succeeds, NDIS returns an [**NDIS\_INTERRUPT\_MODERATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565793) structure that contains the current interrupt moderation settings.

As a set, NDIS and overlying drivers use the OID\_GEN\_INTERRUPT\_MODERATION OID to enable or disable the interrupt moderation on a miniport adapter.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory. Set and query.

Remarks
-------

For a query, if a miniport driver does not support interrupt moderation, the driver must specify **NdisInterruptModerationNotSupported** in the **InterruptModeration** member of the NDIS\_INTERRUPT\_MODERATION\_PARAMETERS structure.

For a set, if the driver reported **NdisInterruptModerationNotSupported** in response to the OID\_GEN\_INTERRUPT\_MODERATION query, the driver should return NDIS\_STATUS\_INVALID\_DATA in response to the set request. The miniport driver receives an [**NDIS\_INTERRUPT\_MODERATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565793) structure. If the **InterruptModeration** member of NDIS\_INTERRUPT\_MODERATION\_PARAMETERS is set to **NdisInterruptModerationEnabled**, the miniport driver should enable interrupt moderation. Otherwise, it should disable interrupt moderation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_INTERRUPT\_MODERATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565793)

 

 




