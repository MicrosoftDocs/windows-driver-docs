---
title: RemoveTarget function
description: The RemoveTarget WMI method configures the WMI provider so that it stops passing events associated with the indicated target to the WMI client.
ms.assetid: 413cee3c-5e3a-4012-925b-b4699fbd2e1b
keywords: ["RemoveTarget function Storage Devices"]
topic_type:
- apiref
api_name:
- RemoveTarget
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# RemoveTarget function


The **RemoveTarget** WMI method configures the WMI provider so that it stops passing events associated with the indicated target to the WMI client.

Syntax
------

```ManagedCPlusPlus
void RemoveTarget(
   [in, HBAType("HBA_WWN")] uint8          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DiscoveredPortWWN[8],
   [in] uint32                             AllTargets,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HbaPortWWN*   
A 64 bit worldwide name (WWN) that uniquely identifies the local port that should be removed from the list of ports whose events are reported to the WMI client. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

*DiscoveredPortWWN*   
A WWN that indicates the remote discovered port that should be removed from the list of ports whose events are reported to the WMI client.

*AllTargets*   
The events to stop reporting. If this member is zero, the WMI provider client will stop reporting events associated with the port that is indicated by *DiscoveredPortWWN*. If this member is nonzero, the WMI provider will cease reporting all events associated any target.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**RemoveTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564039) structure.

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


[**RemoveTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564033)

[**RemoveTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564039)

 

 






