---
title: GetPersistentBinding2 function
description: The GetPersistentBinding2 method retrieves the bindings that an HBA miniport driver uses to map the information that an operating system uses to identify its logical units to the Fibre Channel protocol (FCP) identifiers for the logical units.
ms.assetid: 17734973-fa82-4f54-b882-d9a2f5ce2066
keywords: ["GetPersistentBinding2 function Storage Devices"]
topic_type:
- apiref
api_name:
- GetPersistentBinding2
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetPersistentBinding2 function


The **GetPersistentBinding2** method retrieves the bindings that an HBA miniport driver uses to map the information that an operating system uses to identify its logical units to the Fibre Channel protocol (FCP) identifiers for the logical units.

Syntax
------

```ManagedCPlusPlus
void GetPersistentBinding2(
   [in, HBAType("HBA_WWN")] uint8                        PortWWN[8],
   [in] uint32                                           InEntryCount,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS               HBAStatus,
   [out] uint32                                          TotalEntryCount,
   [out] uint32                                          OutEntryCount,
   [out, WmiSizeIs("OutEntryCount")] HBAFCPBindingEntry2 Bindings[]
);
```

Parameters
----------

*PortWWN\[8\]*   
A worldwide name that indicates the port whose persistent bindings will be retrieved.

*InEntryCount*   
Indicates the number of binding entries that the WMI provider can report in the *Entry* parameter.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetFcpPersistentBinding\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554936) structure.

*TotalEntryCount*   
Indicates the total number of persistent bindings associated with the HBA.

*OutEntryCount*   
Indicates the total number of persistent bindings retrieved by the **GetPersistentBinding2** method.. This value will be less than or equal to *TotalEntryCount*.

*Bindings\[\]*   
An array of structures of type [**HBAFCPBindingEntry2**](https://msdn.microsoft.com/library/windows/hardware/ff556035) that describe an HBA's bindings between operating system and Fibre Channel protocol (FCP) identifiers.

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


[**GetFcpPersistentBinding\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554933)

[**GetFcpPersistentBinding\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554936)

[**HBAFCPBindingEntry2**](https://msdn.microsoft.com/library/windows/hardware/ff556035)

 

 






