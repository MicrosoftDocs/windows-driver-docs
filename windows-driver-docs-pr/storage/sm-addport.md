---
title: SM\_AddPort function
description: The SM\_AddPort WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated port.
ms.assetid: 1667487e-80b1-47eb-9f3c-2f5e1909c73b
keywords: ["SM_AddPort function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_AddPort
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_AddPort function


The SM\_AddPort WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated port.

Syntax
------

```ManagedCPlusPlus
void SM_AddPort(
   [in, HBAType("HBA_WWN")] uint8          PortWWN[8],
   [in, EVENT_TYPES_QUALIFIERS] uint32     EventType,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*PortWWN*   
A worldwide name (WWN) that indicates the port whose events are to be reported.

*EventType*   
The type of the event. The values that can be assigned to this member are defined by the EVENT\_TYPES\_QUALIFIERS WMI class qualifier.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_AddPort\_OUT structure.

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

[**SM\_AddPort\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566213)

[**SM\_AddPort\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566215)

 

 






