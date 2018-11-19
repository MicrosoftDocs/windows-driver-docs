---
title: SM\_SetRNIDMgmtInfo function
description: The SM\_SetRNIDMgmtInfo WMI method sets FC3 management information that is associated with a fibre channel adapter.
ms.assetid: 235beb52-0e09-402d-ace1-0543ad3ee74f
keywords: ["SM_SetRNIDMgmtInfo function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SetRNIDMgmtInfo
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SetRNIDMgmtInfo function


The SM\_SetRNIDMgmtInfo WMI method sets FC3 management information that is associated with a fibre channel adapter.

Syntax
------

```ManagedCPlusPlus
void SM_SetRNIDMgmtInfo(
   [in] HBAFC3MgmtInfo                     MgmtInfo,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*MgmtInfo*   
A structure of type HBAFC3MgmtInfo that holds FC3 management information that is associated with a fibre channel adapter.

*HBAStatus*   
A WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_GetRNIDMgmtInfo\_OUT structure.

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

[**SM\_SetRNIDMgmtInfo\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566337)

[**SM\_SetRNIDMgmtInfo\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566338)

 

 






