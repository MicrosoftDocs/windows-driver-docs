---
title: SM\_RemovePersistentBinding function
description: The SM\_RemovePersistentBinding method removes one or more persistent bindings to the specified SCSI IDs for the specified adapter port.
ms.assetid: 475c2f5f-4a1c-48b4-9a43-81d03b1b737d
keywords: ["SM_RemovePersistentBinding function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_RemovePersistentBinding
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_RemovePersistentBinding function


The SM\_RemovePersistentBinding method removes one or more persistent bindings to the specified SCSI IDs for the specified adapter port.

Syntax
------

```ManagedCPlusPlus
void SM_RemovePersistentBinding(
   [in, HBAType("HBA_WWN")] uint8                      HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                      DomainPortWWN[8],
   [in] uint32                                         EntryCount,
   [in, WmiSizeIs("EntryCount")] MS_SMHBA_BINDINGENTRY Entry[],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS             HBAStatus
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the port whose persistent bindings will be removed.

*DomainPortWWN*   
The worldwide name (WWN) for the callback. It is the Port\_Identifier that has the smallest value of any Port\_Identifier of an SMP port that was discovered by using the physical fibre channel port. It has a value of zero if no SMP port has been discovered by using the physical fibre channel port.

*EntryCount*   
The number of binding entries that the WMI provider can report in the Entry parameter.

*Entry*   
A list of MS\_SMHBA\_BINDINGENTRY types for persistent binding.

*HBAStatus*   
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

[**SM\_RemovePersistentBinding\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566269)

[**SM\_RemovePersistentBinding\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566271)

 

 






