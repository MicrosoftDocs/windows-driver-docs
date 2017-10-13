---
title: OID_GEN_INTERRUPT_MODERATION
author: windows-driver-content
description: As a query, NDIS and overlying drivers use the OID\_GEN\_INTERRUPT\_MODERATION OID to determine if interrupt moderation is enabled on a miniport adapter.
ms.assetid: 4d9d2bda-f0b3-42d5-bb49-93a9b256f5ad
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_INTERRUPT_MODERATION Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_INTERRUPT_MODERATION%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


