---
title: AddPort function
description: The AddPort WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated port.
keywords: ["AddPort function Storage Devices"]
topic_type:
- apiref
api_name:
- AddPort
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# AddPort function


The **AddPort** WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated port.

## Syntax

```ManagedCPlusPlus
void AddPort(
   [in, HBAType("HBA_WWN")] uint8          PortWWN[8],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

## Parameters

*PortWWN\[8\]*   
A worldwide name that indicates the port whose events are to be reported.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**AddPort\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_addport_out) structure.

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


[**AddPort\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_addport_in)

[**AddPort\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_addport_out)

 

