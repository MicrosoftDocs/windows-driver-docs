---
title: SetPersistentEntry function
description: The SetPersistentEntry method adds a binding to the list of bindings associated with the indicated port.
ms.assetid: 52680641-9f63-4c8e-9538-4c725b9074a3
keywords: ["SetPersistentEntry function Storage Devices"]
topic_type:
- apiref
api_name:
- SetPersistentEntry
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SetPersistentEntry function


The **SetPersistentEntry** method adds a binding to the list of bindings associated with the indicated port.

Syntax
------

```ManagedCPlusPlus
void SetPersistentEntry(
   [in, HBAType("HBA_WWN")] uint8                            PortWWN[8],
   [in, HbaType("HBA_FCPBINDINGENTRY2")] HBAFCPBindingEntry2 Binding,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                   HBAStatus
);
```

Parameters
----------

*PortWWN*   
A worldwide name that indicates the port whose persistent bindings will be changed.

*Binding*   
A structure of type [**HBAFCPBindingEntry2**](https://msdn.microsoft.com/library/windows/hardware/ff556035) that indicates the binding to be removed from the indicated port's list of bindings.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SetPersistentEntry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565795) structure.

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
</tbody>
</table>

## <span id="see_also"></span>See also


[**SetPersistentEntry\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565790)

[**SetPersistentEntry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565795)

 

 






