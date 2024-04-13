---
title: AddLink Function
description: The AddLink WMI method configures the WMI provider to inform the WMI client of fabric link events.
keywords: ["AddLink function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- AddLink
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# AddLink function


The **AddLink** WMI method configures the WMI provider to inform the WMI client of fabric link events.

## Syntax

```ManagedCPlusPlus
void AddLink(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**AddLink\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_addlink_out) structure.

## Return value

Not applicable to WMI methods.

## Remarks

This WMI method belongs to the [MSFC\_EventControl WMI Class](msfc-eventcontrol-wmi-class.md).

## Requirements

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
<td align="left">Hbapiwmi.h (include Hbaapi.h or Hbapiwmi.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**AddLink\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_addlink_out)

 

