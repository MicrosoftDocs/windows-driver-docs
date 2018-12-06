---
title: KSPROPERTY\_BDA\_CA\_MODULE\_STATUS
description: Clients use KSPROPERTY\_BDA\_CA\_MODULE\_STATUS to determine status on the CA module associated with an ECM map node.
ms.assetid: 4bd8a423-7a76-4702-a769-0de88fcc5772
keywords: ["KSPROPERTY_BDA_CA_MODULE_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_CA_MODULE_STATUS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_CA\_MODULE\_STATUS


Clients use KSPROPERTY\_BDA\_CA\_MODULE\_STATUS to determine status on the CA module associated with an ECM map node.

## <span id="ddk_ksproperty_bda_ca_module_status_ks"></span><span id="DDK_KSPROPERTY_BDA_CA_MODULE_STATUS_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The returned value specifies the CA module status.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSEVENT\_BDA\_CA\_MODULE\_STATUS\_CHANGED**](ksevent-bda-ca-module-status-changed.md)

[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






