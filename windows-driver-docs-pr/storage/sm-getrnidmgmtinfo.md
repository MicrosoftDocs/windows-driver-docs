---
title: SM\_GetRNIDMgmtInfo function
description: The SM\_GetRNIDMgmtInfo WMI method retrieves FC3 management information that is associated with a Fibre Channel adapter.
ms.assetid: 0d414701-6e60-4d9d-85ae-f82b742ee907
keywords: ["SM_GetRNIDMgmtInfo function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_GetRNIDMgmtInfo
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_GetRNIDMgmtInfo function


The SM\_GetRNIDMgmtInfo WMI method retrieves FC3 management information that is associated with a Fibre Channel adapter.

Syntax
------

```ManagedCPlusPlus
void SM_GetRNIDMgmtInfo(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
   [out] HBAFC3MgmtInfo                    MgmtInfo
);
```

Parameters
----------

*HBAStatus*   
A WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_GetRNIDMgmtInfo\_OUT structure.

*MgmtInfo*   
A structure of type HBAFC3MgmtInfo that holds FC3 management information that is associated with a fibre channel adapter.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_FabricAndDomainManagementMethods WMI Class.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Hbapiwmi.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SM\_GetRNIDMgmtInfo\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566252)

 

 






