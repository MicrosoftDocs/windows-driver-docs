---
title: SM\_AddTarget function
description: The SM\_AddTarget WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.
ms.assetid: 78e19496-1eb0-4d05-8637-f2e6d123208b
keywords: ["SM_AddTarget function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_AddTarget
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_AddTarget function


The SM\_AddTarget WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.

Syntax
------

```ManagedCPlusPlus
void SM_AddTarget(
   [in, HBAType("HBA_WWN")] uint8          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DiscoveredPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DomainPortWWN[8],
   [in] uint32                             AllTargets,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HbaPortWWN*   
The worldwide name (WWN) of the local port whose events the WMI client will receive.

*DiscoveredPortWWN*   
A worldwide name (WWN) that specifies the discovered target whose events the WMI client will receive.

*DomainPortWWN*   
A worldwide name (WWN) that specifies the SAS domain worldwide name of the local port whose events the WMI client will receive.

*AllTargets*   
The scope of the target events to report. If this member is zero, the WMI client receives events that are associated with the port that is indicated by DiscoveredPortWWN. If this member is nonzero, the WMI client receives all events that are associated with all currently discovered targets as well as targets that are discovered in the future.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_AddTarget\_OUT structure.

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

[**SM\_AddTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566218)

[**SM\_AddTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566219)

 

 






