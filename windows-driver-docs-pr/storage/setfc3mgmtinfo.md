---
title: SetFC3MgmtInfo function
description: The SetFC3MgmtInfo WMI method sets FC3 management information that is associated with a Fibre Channel adapter.
keywords: ["SetFC3MgmtInfo function Storage Devices"]
topic_type:
- apiref
api_name:
- SetFC3MgmtInfo
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SetFC3MgmtInfo function


The **SetFC3MgmtInfo** WMI method sets FC3 management information that is associated with a Fibre Channel adapter.

## Syntax

```ManagedCPlusPlus
void SetFC3MgmtInfo(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
   [in] HBAFC3MgmtInfo                     MgmtInfo
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SetFC3MgmtInfo\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_setfc3mgmtinfo_out) structure.

*MgmtInfo*   
A structure of type [**HBAFC3MgmtInfo**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_hbafc3mgmtinfo) that holds FC3 management information that will be used to configure the fibre channel adapter. This information is delivered to the miniport driver in the **PortWWN** member of a [**SetFC3MgmtInfo\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_setfc3mgmtinfo_in) structure.

## Return value

Not applicable to WMI methods.

## Remarks

This WMI method belongs to the [MSFC\_HBAAdapterMethods WMI Class](msfc-hbaadaptermethods-wmi-class.md).

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


[HBA\_STATUS](hba-status.md)

[**GetFC3MgmtInfo\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc3mgmtinfo_out)

[**HBAFC3MgmtInfo**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_hbafc3mgmtinfo)

[**SetFC3MgmtInfo\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_setfc3mgmtinfo_in)

[**SetFC3MgmtInfo\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_setfc3mgmtinfo_out)

 

