---
title: AddTarget function
description: The AddTarget WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.
ms.assetid: 9aac339b-a9b4-4de7-99dd-fa5f8889a686
keywords: ["AddTarget function Storage Devices"]
topic_type:
- apiref
api_name:
- AddTarget
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# AddTarget function


The **AddTarget** WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.

Syntax
------

```ManagedCPlusPlus
void AddTarget(
   [in, HBAType("HBA_WWN")] uint8          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DiscoveredPortWWN[8],
   [in] uint32                             AllTargets,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HbaPortWWN\[8\]*   
The worldwide name of the local port whose events the WMI client will receive.

*DiscoveredPortWWN\[8\]*   
A worldwide name that specifies the discovered target whose events the WMI client will receive.

*AllTargets*   
The scope of the target events to report. If this member is zero, the WMI client will receive events associated with the port that is indicated by *DiscoveredPortWWN*. If this member is nonzero, the WMI client will receive all events associated with all currently discovered targets as well as targets that are discovered in the future.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**AddTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff550138) structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the [MSFC\_EventControl WMI Class](msfc-eventcontrol-wmi-class.md).

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
<td align="left">Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**AddTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff550137)

[**AddTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff550138)

 

 






