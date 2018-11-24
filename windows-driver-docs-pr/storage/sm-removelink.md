---
title: SM\_RemoveLink function
description: The SM\_RemoveLink WMI method configures the WMI provider so that it stops passing fabric link event information to the WMI client.
ms.assetid: 25f6b807-f921-44b6-b087-e5c6ec8c72ec
keywords: ["SM_RemoveLink function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_RemoveLink
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_RemoveLink function


The SM\_RemoveLink WMI method configures the WMI provider so that it stops passing fabric link event information to the WMI client.

Syntax
------

```ManagedCPlusPlus
void SM_RemoveLink(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_RemoveLink\_OUT structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_EventControl WMI Class.

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

[**SM\_RemoveLink\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566265)

 

 






