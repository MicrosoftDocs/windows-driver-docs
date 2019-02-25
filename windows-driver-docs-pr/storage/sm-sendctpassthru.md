---
title: SM\_SendCTPassThru function
description: The SM\_SendCTPassThru WMI method sends a common transport (CT) pass-through command to the indicated port.
ms.assetid: 437f0c79-78f6-406e-8774-79de4425bfe8
keywords: ["SM_SendCTPassThru function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendCTPassThru
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SendCTPassThru function


The SM\_SendCTPassThru WMI method sends a common transport (CT) pass-through command to the indicated port.

Syntax
------

```ManagedCPlusPlus
void SM_SendCTPassThru(
   [in, HBAType("HBA_WWN")] uint8              HbaPortWWN[8],
   [in] uint32                                 InRespBufferMaxSize,
   [in] uint32                                 RequestBufferSize,
   [in, WmiSizeIs("RequestBufferSize")] uint8  RequestBuffer,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS     HBAStatus,
   [out] uint32                                TotalResponseBufferSize,
   [out] uint32                                ActualResponseBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8 ResponseBuffer[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the HBA through which the target is accessed. This information is delivered to the miniport driver in the PortWWN member of a SendCTPassThru\_IN structure.

*InRespBufferMaxSize*   
The maximum size of the response buffer.

*RequestBufferSize*   
The size, in bytes, of the buffer that will hold the results of the common transport command. The miniport driver returns this information in the RequestBufferSize member of a SM\_SendCTPassThru\_IN structure.

*RequestBuffer*   
The results of the common transport command. The miniport driver returns this information in the RequestBuffer member of a SM\_SendCTPassThru\_IN structure.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_SendCTPassThru\_OUT structure.

*TotalResponseBufferSize*   
The size, in bytes, of the results common transport command. The miniport driver returns this information in the TotalResponseBufferSize member of a SM\_SendCTPassThru\_OUT structure.

*ActualResponseBufferSize*   
The size, in bytes, of the data that was actually retrieved. The miniport driver returns this information in the ActualResponseBufferSize member of a SM\_SendCTPassThru\_OUT structure.

*ResponseBuffer*   
The results of the common transport command. The miniport driver returns this information in the ResponseBuffer member of a SM\_SendCTPassThru\_OUT structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_FabricAndDomainManagementMethods WMI Class.

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

[**SM\_SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566293)

[**SM\_SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566294)

 

 






