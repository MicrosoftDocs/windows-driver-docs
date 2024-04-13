---
title: RemoveLink Function
description: The RemoveLink WMI method configures the WMI provider so that it stops passing fabric link event information to the WMI client.
keywords: ["RemoveLink function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- RemoveLink
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# RemoveLink function


The **RemoveLink** WMI method configures the WMI provider so that it stops passing fabric link event information to the WMI client.

## Syntax

```ManagedCPlusPlus
void RemoveLink(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**RemoveLink\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_removelink_out) structure.

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
<td align="left">Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**RemoveLink\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_removelink_out)

 

