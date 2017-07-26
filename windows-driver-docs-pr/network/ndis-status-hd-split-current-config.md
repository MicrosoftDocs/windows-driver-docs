---
title: NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG status indication to notify NDIS and overlying drivers that there has been a change in the header-data split configuration of a miniport adapter.
ms.assetid: 6605d888-bcbe-4898-aa25-4a4352fc50de
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_HD_SPLIT_CURRENT_CONFIG%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


