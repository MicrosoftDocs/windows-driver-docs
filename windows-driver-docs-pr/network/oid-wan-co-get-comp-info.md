---
title: OID_WAN_CO_GET_COMP_INFO
description: The OID_WAN_CO_GET_COMP_INFO OID requests the miniport driver to return information about the capabilities of the NIC or of its driver, in particular whether either supports compression.
ms.assetid: a2525548-ca5a-47a8-ab19-e0469913f6be
ms.date: 08/08/2017
keywords: 
 -OID_WAN_CO_GET_COMP_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WAN\_CO\_GET\_COMP\_INFO


The OID\_WAN\_CO\_GET\_COMP\_INFO OID requests the miniport driver to return information about the capabilities of the NIC or of its driver, in particular whether either supports compression. If so, the values returned are used to negotiate compression with the Point-to-Point Protocol (PPP) Compression Control Protocol. The protocol subsequently negotiates a PPP compression scheme with an [OID\_WAN\_CO\_SET\_COMP\_INFO](oid-wan-co-set-comp-info.md) request. This compression information is specific to a virtual connection (VC).

Compression information is returned in an NDIS\_WAN\_CO\_GET\_COMP\_INFO structure, defined as follows:

```ManagedCPlusPlus
    typedef struct _NDIS_WAN_CO_GET_COMP_INFO {
         OUT NDIS_WAN_COMPRESS_INFO SendCapabilities;
         OUT NDIS_WAN_COMPRESS_INFO RecvCapabilities;
    } NDIS_WAN_CO_GET_COMP_INFO,   *PNDIS_WAN_CO_GET_COMP_INFO;
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


[OID\_WAN\_GET\_COMP\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff561202)

[OID\_WAN\_CO\_SET\_COMP\_INFO](oid-wan-co-set-comp-info.md)








