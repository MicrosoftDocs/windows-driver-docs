---
title: SetBindingSupport function
description: The SetBindingSupport method sets the binding capabilities that are currently enabled for the indicated port.
ms.assetid: 52a469df-b184-460b-b515-a0b6eb946f1f
keywords: ["SetBindingSupport function Storage Devices"]
topic_type:
- apiref
api_name:
- SetBindingSupport
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SetBindingSupport function


The **SetBindingSupport** method sets the binding capabilities that are currently enabled for the indicated port.

Syntax
------

```ManagedCPlusPlus
void SetBindingSupport(
   [in, HBAType("HBA_WWN")] uint8               PortWWN[8],
   [in, HBA_BIND_TYPE_QUALIFIERS] HBA_BIND_TYPE BindType,
   [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS     HBAStatus
);
```

Parameters
----------

*PortWWN*   
A worldwide name that indicates the port whose persistent bindings will be retrieved.

*BindType*   
A bitmap that indicates the ability of an HBA and its miniport driver to provide a specific set of features related to persistent binding. For a list of values that this parameter can have, see the description of the [HBA\_BIND\_TYPE](hba-bind-type.md) WMI class qualifier.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SetBindingSupport\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565575) structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the [MSFC\_HBAFCPInfo WMI Class](msfc-hbafcpinfo-wmi-class.md).

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
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">Hbaapi.lib</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**SetBindingSupport**](setbindingsupport.md)

[**SetBindingSupport\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565566)

[**SetBindingSupport\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565575)

 

 






