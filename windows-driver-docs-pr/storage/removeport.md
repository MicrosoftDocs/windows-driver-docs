---
title: RemovePort function
description: The RemovePort WMI method configures the WMI provider so that it stops passing events associated with the indicated port to the WMI client.
ms.assetid: 6e466a89-273b-4ed9-a0fe-5a8df745b28a
keywords: ["RemovePort function Storage Devices"]
topic_type:
- apiref
api_name:
- RemovePort
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# RemovePort function


The **RemovePort** WMI method configures the WMI provider so that it stops passing events associated with the indicated port to the WMI client.

Syntax
------

```ManagedCPlusPlus
void RemovePort(
   [in, HBAType("HBA_WWN")] uint8          PortWWN[8],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*PortWWN*   
A worldwide name that indicates the port that should be removed from the list of ports whose events are reported to the WMI client.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**RemovePort\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564017) structure.

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


[**RemovePort\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564014)

[**RemovePort\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564017)

 

 






