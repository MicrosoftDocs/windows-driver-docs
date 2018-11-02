---
title: SM\_GetPersistentBinding function
description: The SM\_GetPersistentBinding method retrieves the bindings that an HBA miniport driver uses. These bindings map the OS-specific LUN information to the fibre channel protocol (FCP) identifiers for the logical units.
ms.assetid: 74a67e91-c3b3-462a-8810-a9eae64e02a7
keywords: ["SM_GetPersistentBinding function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_GetPersistentBinding
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_GetPersistentBinding function


The SM\_GetPersistentBinding method retrieves the bindings that an HBA miniport driver uses. These bindings map the OS-specific LUN information to the fibre channel protocol (FCP) identifiers for the logical units.

Syntax
------

```ManagedCPlusPlus
void SM_GetPersistentBinding(
   [in, HBAType("HBA_WWN")] uint8                          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                          DomainPortWWN[8],
   [in] uint32                                             InEntryCount,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                 HBAStatus,
   [out] uint32                                            TotalEntryCount,
   [out] uint32                                            OutEntryCount,
   [out, WmiSizeIs("OutEntryCount")] MS_SMHBA_BINDINGENTRY Bindings[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the port whose persistent bindings will be retrieved.

*DomainPortWWN*   
The worldwide name (WWN) for the callback. It is the Port\_Identifier that has the smallest value of any Port\_Identifier of an SMP port that was discovered by using the physical fibre channel port. It has a value of zero if no SMP port has been discovered by using the physical fibre channel port.

*InEntryCount*   
The number of binding entries that the WMI provider can report in the Entry parameter.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see the [HBA\_STATUS](hba-status.md) structure. The miniport driver returns this information in the HBAStatus member of a GetPersistentBinding\_OUT structure.

*TotalEntryCount*   
The total number of persistent bindings that are associated with the HBA.

*OutEntryCount*   
The total number of persistent bindings that are retrieved by the SM\_GetPersistentBinding method. This value will be less than or equal to TotalEntryCount.

*Bindings*   
An array of structures of type MS\_SMHBA\_BINDINGENTRY that describe an HBA's bindings between the operating system and the fibre channel protocol (FCP) identifiers.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_TargetInformationMethods WMI Class.

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
<td align="left">Hbapiwmi.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SM\_GetPersistentBinding\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566246)

[**SM\_GetPersistentBinding\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566248)

 

 






