---
title: OID_WAN_CO_SET_COMP_INFO
description: The OID_WAN_CO_SET_COMP_INFO OID notifies the miniport driver of the PPP compression scheme selected by a protocol to which the miniport driver already returned information with a OID_WAN_CO_GET_COMP_INFO query.
ms.assetid: f3b6b846-fa8c-425b-ba05-45927e744d66
ms.date: 08/08/2017
keywords: 
 -OID_WAN_CO_SET_COMP_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WAN\_CO\_SET\_COMP\_INFO


The OID\_WAN\_CO\_SET\_COMP\_INFO OID notifies the miniport driver of the PPP compression scheme selected by a protocol to which the miniport driver already returned information with a [OID\_WAN\_CO\_GET\_COMP\_INFO](oid-wan-co-get-comp-info.md) query. This PPP compression scheme is specific to a virtual connection (VC).

The protocol supplies a specification for the PPP compression scheme it selected in an NDIS\_WAN\_CO\_SET\_COMP\_INFO structure, defined as follows:

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_SET_COMP_INFO {
         IN NDIS_WAN_COMPRESS_INFO SendCapabilities;
         IN NDIS_WAN_COMPRESS_INFO RecvCapabilities;
    } NDIS_WAN_CO_SET_COMP_INFO,   *PNDIS_WAN_CO_SET_COMP_INFO;
```




The members of this structure contain the following information:

<a href="" id="sendcapabilities"></a>**SendCapabilities**  
Specifies a structure containing information about compression capabilities for sending data.

<a href="" id="recvcapabilities"></a>**RecvCapabilities**  
Specifies a structure containing information about compression capabilities for receiving data.

Remarks
-------

For specifics of the NDIS\_WAN\_COMPRESS\_INFO structure, see [OID\_WAN\_GET\_COMP\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff561202).

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
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_WAN\_CO\_GET\_COMP\_INFO](oid-wan-co-get-comp-info.md)








