---
title: SM\_SendRNID function
description: The SM\_SendRNID WMI method sends a request node identification data (RNID) command to the indicated port.
ms.assetid: 160e2dc7-8195-4f8a-bc59-854e5283cf6f
keywords: ["SM_SendRNID function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendRNID
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SendRNID function


The SM\_SendRNID WMI method sends a request node identification data (RNID) command to the indicated port.

Syntax
------

```ManagedCPlusPlus
void SM_SendRNID(
   [in, HBAType("HBA_WWN")] uint8              PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8              DestWWN[8],
   [in] uint32                                 DestFCID,
   [in] uint32                                 NodeIdDataFormat,
   [in] uint32                                 InRespBufferMaxSize,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS     HBAStatus,
   [out] uint32                                TotalRespBufferSize,
   [out] uint32                                ResponseBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8 ResponseBuffer[]
);
```

Parameters
----------

*PortWWN*   
A worldwide name (WWN) for the local port through which the RNID command is sent. This information is delivered to the miniport driver in the PortWWN member of a SM\_SendRNID\_IN structure.

*DestWWN*   
A worldwide name (WWN) for the destination port. This information is delivered to the miniport driver in the DestWWN member of a SM\_SendRNID\_IN structure.

*DestFCID*   
An address identifier of the destination port. This information is delivered to the miniport driver in the DestFCID member of a SM\_SendRNID\_IN structure.

*NodeIdDataFormat*   
The node identification data format. For a description of the values that this member can have, see the T11 committee's *Fibre Channel HBA API* specification. This information is delivered to the miniport driver in the NodeIdDataFormat member of a SM\_SendRNID\_IN structure.

*InRespBufferMaxSize*   
The maximum size of the response buffer.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_SendRNID\_OUT structure.

*TotalRespBufferSize*   
The size, in bytes, of the results of the RNID command. The miniport driver returns this information in the TotalRspBufferSize member of a SM\_SendRNID\_OUT structure.

*ResponseBufferSize*   
The size, in bytes, of the results of the RNID command. The miniport driver returns this information in the ResponseBufferSize member of a SM\_SendRNID\_OUT structure.

*ResponseBuffer*   
The results of the RNID command. The miniport driver returns this information in the ResponseBuffer member of a SM\_SendRNID\_OUT structure.

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

[**SM\_SendRNID\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566308)

[**SM\_SendRNID\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566310)

 

 






