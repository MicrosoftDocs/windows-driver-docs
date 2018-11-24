---
title: SM\_SetPersistentBinding function
description: The SM\_SetPersistentBinding method sets the bindings that are used by the HBA miniport driver to map the OS-specific LUN information to the fibre channel protocol (FCP) identifiers for the logical units.
ms.assetid: 722f7216-9ff4-4f12-a4fe-e1f8f9e594e1
keywords: ["SM_SetPersistentBinding function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SetPersistentBinding
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SetPersistentBinding function


The SM\_SetPersistentBinding method sets the bindings that are used by the HBA miniport driver to map the OS-specific LUN information to the fibre channel protocol (FCP) identifiers for the logical units.

Syntax
------

```ManagedCPlusPlus
void SM_SetPersistentBinding(
   [in, HBAType("HBA_WWN")] uint8                        HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                        DomainPortWWN[8],
   [in] uint32                                           InEntryCount,
   [in, WmiSizeIs("InEntryCount")] MS_SMHBA_BINDINGENTRY Entry[],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS               HBAStatus,
   [out] uint32                                          OutStatusCount,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS               EntryStatus
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the port whose persistent bindings will be set.

*DomainPortWWN*   
The worldwide name (WWN) for the callback. It is the Port\_Identifier that has the smallest value of any Port\_Identifier of an SMP port that is discovered by using the physical fibre channel port. It has a value of zero if no SMP port has been discovered by using the physical fibre channel port.

*InEntryCount*   
The number of binding entries that the WMI provider can report in the Entry parameter.

*Entry*   
An array of structures of type SMHBA\_SCSIENTRY that describes an HBA's bindings between the operating system and the SAS identifiers.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a GetPersistentBinding\_OUT structure.

*OutStatusCount*   
The total number of persistent bindings that are retrieved by the SM\_GetPersistentBinding method. This value will be less than or equal to TotalEntryCount.

*EntryStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a GetPersistentBinding\_OUT structure.

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

[**SM\_SetPersistentBinding\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566334)

[**SM\_SetPersistentBinding\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566335)

 

 






