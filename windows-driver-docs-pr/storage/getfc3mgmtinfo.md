---
title: GetFC3MgmtInfo function
description: The GetFC3MgmtInfo WMI method retrieves FC3 management information that is associated with a Fibre Channel adapter.
ms.assetid: dea5d73f-22e2-4c5e-973a-aa8407955ef8
keywords: ["GetFC3MgmtInfo function Storage Devices"]
topic_type:
- apiref
api_name:
- GetFC3MgmtInfo
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetFC3MgmtInfo function


The **GetFC3MgmtInfo** WMI method retrieves FC3 management information that is associated with a Fibre Channel adapter.

Syntax
------

```ManagedCPlusPlus
void GetFC3MgmtInfo(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
   [out] HBAFC3MgmtInfo                    MgmtInfo
);
```

Parameters
----------

*HBAStatus*   
On return, contains a WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetFC3MgmtInfo\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553946) structure.

*MgmtInfo*   
On return, contains a structure of type [**HBAFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556032) that holds FC3 management information that is associated with a Fibre Channel adapter.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the [MSFC\_HBAAdapterMethods WMI Class](msfc-hbaadaptermethods-wmi-class.md).

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


[**GetFC3MgmtInfo\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553946)

[**HBAFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff556032)

 

 






