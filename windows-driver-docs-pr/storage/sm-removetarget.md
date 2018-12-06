---
title: SM\_RemoveTarget function
description: The SM\_RemoveTarget WMI method configures the WMI provider so that it stops passing events that are associated with the indicated target to the WMI client.
ms.assetid: 9be2a40c-299a-4d92-b9a2-ef60eb6d90e9
keywords: ["SM_RemoveTarget function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_RemoveTarget
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_RemoveTarget function


The SM\_RemoveTarget WMI method configures the WMI provider so that it stops passing events that are associated with the indicated target to the WMI client.

Syntax
------

```ManagedCPlusPlus
void SM_RemoveTarget(
   [in, HBAType("HBA_WWN")] uint8          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DiscoveredPortWWN[8],
   [in] uint32                             AllTargets,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HbaPortWWN*   
A 64-bit worldwide name (WWN) that uniquely identifies the local port that should be removed from the list of ports whose events are reported to the WMI client. For more information about worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

*DiscoveredPortWWN*   
A worldwide name (WWN) that indicates the remote discovered port that should be removed from the list of ports whose events are reported to the WMI client.

*AllTargets*   
The events to stop reporting. If this member is zero, the WMI provider client stops reporting events that are associated with the port that is indicated by DiscoveredPortWWN. If this member is nonzero, the WMI provider stops reporting all events associated any target.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_RemoveTarget\_OUT structure.

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

[**SM\_RemoveTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566280)

[**SM\_RemoveTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566283)

 

 






