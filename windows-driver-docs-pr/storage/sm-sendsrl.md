---
title: SM\_SendSRL function
description: The SM\_SendSRL WMI method sends a scan remote loop (SRL) command through the indicated port to the indicated domain controller.
ms.assetid: 44090e8d-ffb2-48a9-a574-5bf067ffa952
keywords: ["SM_SendSRL function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendSRL
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SendSRL function


The SM\_SendSRL WMI method sends a scan remote loop (SRL) command through the indicated port to the indicated domain controller.

Syntax
------

```ManagedCPlusPlus
void SM_SendSRL(
   [in, HBAType("HBA_WWN")] uint8              HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8              WWN[8],
   [in] uint32                                 Domain,
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
A worldwide name (WWN) for the local port through which the SRL command is sent. This information is delivered to the miniport driver in the HbaPortWWN member of a SM\_SendSRL\_IN structure.

*WWN*   
A worldwide name (WWN) for the port of type FL\_Port whose loop is to be scanned. This information is delivered to the miniport driver in the WWN member of a SM\_SendSRL\_IN structure.

*Domain*   
The domain number for the domain whose loops are to be scanned. This information is delivered to the miniport driver in the Domain member of a SM\_SendSRL\_IN structure.

*InRespBufferMaxSize*   
The maximum size of the response buffer.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SendRPL\_OUT structure.

*TotalRespBufferSize*   
The size, in bytes, of the results of the RPS command. The miniport driver returns this information in the TotalRespBufferSize member of a SM\_SendRPS\_OUT structure.

*OutRespBufferSize*   
The size, in bytes, of the data that was actually retrieved. The miniport driver returns this information in the OutRespBufferSize member of a SM\_SendRPL\_OUT structure.

*RespBuffer*   
The results of the RPS command. The miniport driver returns this information in the RespBuffer member of a SM\_SendRPS\_OUT structure.

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

[**SM\_SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566326)

 

 






