---
title: NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG
description: Miniport drivers use the NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG status indication to notify NDIS and overlying drivers that there has been a change in the header-data split configuration of a miniport adapter.
ms.assetid: 6605d888-bcbe-4898-aa25-4a4352fc50de
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG


Miniport drivers use the NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG status indication to notify NDIS and overlying drivers that there has been a change in the header-data split configuration of a miniport adapter.

Remarks
-------

When a miniport driver receives an [OID\_GEN\_HD\_SPLIT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569587) set request, the driver must use the contents of the [**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701) structure to update the current configuration of the miniport adapter. After the update, the miniport driver must report the changes with the NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG status indication. The status indication ensures that all of the overlying drivers are updated with the new information.

The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains an [**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696) structure. This structure specifies the current header-data split configuration of a miniport adapter.

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_HD\_SPLIT\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff565696)

[**NDIS\_STATUS\_HD\_SPLIT\_CURRENT\_CONFIG**](ndis-status-hd-split-current-config.md)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_GEN\_HD\_SPLIT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569587)

 

 




