---
title: SM\_SendRLS function
description: The SM\_SendRLS WMI method sends a read link status (RLS) through the indicated local port. This RLS is sent to the indicated remote port to retrieve a link error status block that is associated with the remote port.
ms.assetid: 4498edde-1249-43b8-b581-37e24f8bd2d3
keywords: ["SM_SendRLS function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendRLS
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SendRLS function


The SM\_SendRLS WMI method sends a read link status (RLS) through the indicated local port. This RLS is sent to the indicated remote port to retrieve a link error status block that is associated with the remote port.

Syntax
------

```ManagedCPlusPlus
void SM_SendRLS(
   [in, HBAType("HBA_WWN")] uint8              HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8              DestWWN[8],
   [in] uint32                                 InRespBufferMaxSize,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS     HBAStatus,
   [out] uint32                                TotalRespBufferSize,
   [out] uint32                                OutRespBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the local port through which the RLS command is sent. This information is delivered to the miniport driver in the HbaPortWWN member of a SM\_SendRLS\_IN structure.

*DestWWN*   
A worldwide name (WWN) for the destination port. This information is delivered to the miniport driver in the DestWWN member of a SM\_SendRLS\_IN structure.

*InRespBufferMaxSize*   
The maximum size, in bytes, of the response buffer.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_SendRLS\_OUT structure.

*TotalRespBufferSize*   
The size, in bytes, of the results of the RLS command. The miniport driver returns this information in the TotalRespBufferSize member of a SM\_SendRLS\_OUT structure.

*OutRespBufferSize*   
The size, in bytes, of the data that was actually retrieved. The miniport driver returns this information in the OutRespBufferSize member of a SM\_SendRLS\_OUT structure.

*RespBuffer*   
The results of the RLS command. The miniport driver returns this information in the RespBuffer member of a SM\_SendRLS\_OUT structure.

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

[**SM\_SendRLS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566305)

 

 






