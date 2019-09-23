---
title: OID_PD_QUERY_CURRENT_CONFIG
description: An NDIS protocol or filter driver sends an object identifier (OID) method request of OID_PD_QUERY_CURRENT_CONFIG to a PD-capable miniport driver to retrieve the PD status and capabilities. All PD-capable miniport drivers must handle this OID request.
ms.assetid: 1BF09EAE-9D03-4655-98CD-D3A10BF48A48
ms.date: 08/08/2017
keywords: 
 -OID_PD_QUERY_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PD\_QUERY\_CURRENT\_CONFIG


An NDIS protocol or filter driver sends an object identifier (OID) method request of OID\_PD\_QUERY\_CURRENT\_CONFIG to a PD-capable miniport driver to retrieve the PD status and capabilities. All PD-capable miniport drivers must handle this OID request.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_PD\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_pd_config) structure

Remarks
-------

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportOidRequest*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-miniport_oid_request)

[**NDIS\_PD\_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_pd_config)

[**NDIS\_OID\_REQUEST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_ndis_oid_request)

 

 




