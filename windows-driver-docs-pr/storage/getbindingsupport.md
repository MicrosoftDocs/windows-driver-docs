---
title: GetBindingSupport function
description: The GetBindingSupport method retrieves the binding capabilities that are currently enabled for the indicated port.
ms.assetid: 50c90379-613f-42f1-80fe-7bc1b77a53bf
keywords: ["GetBindingSupport function Storage Devices"]
topic_type:
- apiref
api_name:
- GetBindingSupport
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetBindingSupport function


The **GetBindingSupport** method retrieves the binding capabilities that are currently enabled for the indicated port.

Syntax
------

```ManagedCPlusPlus
void GetBindingSupport(
   [in, HBAType("HBA_WWN")] uint8                PortWWN[8],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [out, HBA_BIND_TYPE_QUALIFIERS] HBA_BIND_TYPE BindType
);
```

Parameters
----------

*PortWWN\[8\]*   
A worldwide name that indicates the port whose persistent bindings will be retrieved.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetBindingSupport\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553917) structure.

*BindType*   
A bitmap that indicates the ability of an HBA and its miniport driver to provide a specific set of features related to persistent binding. For a list of values that this parameter can have, see the description of the [HBA\_BIND\_TYPE](hba-bind-type.md) WMI class qualifier.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This **GetBindingSupport** method returns the binding capability that is currently enabled, whereas the [**GetBindingCapability**](getbindingcapability.md) method indicates the binding capability of the port without reference to whether particular bindings are enabled or not.

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


[**GetBindingCapability**](getbindingcapability.md)

[**GetBindingSupport**](getbindingsupport.md)

[**GetBindingSupport\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff553914)

[**GetBindingSupport\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553917)

 

 






