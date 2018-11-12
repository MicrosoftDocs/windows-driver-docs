---
title: SM\_GetTargetMapping function
description: The SM\_GetTargetMapping WMI method retrieves a mapping between the information that uniquely identifies a set of logical units for the operating system and the fibre channel protocol (FCP) identifiers for these logical units.
ms.assetid: db18920c-327d-4349-8821-6d7fb68eccbd
keywords: ["SM_GetTargetMapping function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_GetTargetMapping
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_GetTargetMapping function


The SM\_GetTargetMapping WMI method retrieves a mapping between the information that uniquely identifies a set of logical units for the operating system and the fibre channel protocol (FCP) identifiers for these logical units.

Syntax
------

```ManagedCPlusPlus
void SM_GetTargetMapping(
   [in, HBAType("HBA_WWN")] uint8                       HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                       DomainPortWWN[8],
   [in] uint32                                          InEntryCount,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS              HBAStatus,
   [out] uint32                                         TotalEntryCount,
   [out] uint32                                         OutEntryCount,
   [out, WmiSizeIs("OutEntryCount")] MS_SMHBA_SCSIENTRY Entry[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the port whose table of mappings is to be retrieved. This information is delivered to the miniport driver in the HbaPortWWN member of a GetTargetMapping\_IN structure.

*DomainPortWWN*   
The worldwide name (WWN) for the callback. It is the Port\_Identifier with the smallest value of any Port\_Identifier of an SMP port that is discovered by using the physical fibre channel port. It has a value of zero if no SMP port has been discovered by using the physical fibre channel port.

*InEntryCount*   
The number of binding entries that the WMI provider can report in the Entry parameter.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see the [HBA\_STATUS](hba-status.md) structure. The miniport driver returns this information in the HBAStatus member of a GetFcpTargetMapping\_OUT structure.

*TotalEntryCount*   
The total number of persistent bindings that are associated with the HBA.

*OutEntryCount*   
The total number of mappings that are retrieved by the SM\_GetTargetMapping method. This value will be less than or equal to TotalEntryCount.

*Entry*   
An array of structures of type MS\_SMHBA\_SCSIENTRY that describe an HBA's bindings between the operating system and the fibre channel protocol (FCP) identifiers.

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

[**SM\_GetTargetMapping\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566256)

[**SM\_GetTargetMapping\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566258)

 

 






