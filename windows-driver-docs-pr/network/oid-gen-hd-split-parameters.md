---
title: OID_GEN_HD_SPLIT_PARAMETERS
description: As a set, NDIS and overlying drivers or user-mode applications use the OID_GEN_HD_SPLIT_PARAMETERS OID to set the current header-data split settings of a miniport adapter.
ms.assetid: 1b33c601-4302-4f63-8265-b75889b42d42
ms.date: 08/08/2017
keywords: 
 -OID_GEN_HD_SPLIT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_HD\_SPLIT\_PARAMETERS


As a set, NDIS and overlying drivers or user-mode applications use the OID\_GEN\_HD\_SPLIT\_PARAMETERS OID to set the current header-data split settings of a miniport adapter. NDIS 6.1 and later miniport drivers that provide header-data split services must support this OID. Otherwise, this OID is optional.

Remarks
-------

The **InformationBuffer** member of [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701) structure.

NDIS might set the OID\_GEN\_HD\_SPLIT\_PARAMETERS OID when an NDIS 5.*x* protocol driver binds to an NDIS 6.1 miniport. NDIS processes this OID before passing it to the miniport driver and updates the miniport adapter's **\*HeaderDataSplit** standardized keyword, if required. If header-data split is disabled, NDIS does not send this OID to the miniport adapter.

NDIS will send this OID to the miniport driver only if header-data split was enabled with the NDIS\_HD\_SPLIT\_ENABLE\_HEADER\_DATA\_SPLIT flag in the [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure during miniport initialization.

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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694)

[**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 




