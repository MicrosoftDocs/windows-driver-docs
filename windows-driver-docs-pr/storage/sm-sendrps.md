---
title: SM\_SendRPS function
description: The SM\_SendRPS WMI method sends a read port status block (RPS) request to the indicated port or domain controller.
ms.assetid: a64983ef-c665-43db-ad29-0a6f14421ab8
keywords: ["SM_SendRPS function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendRPS
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SendRPS function


The SM\_SendRPS WMI method sends a read port status block (RPS) request to the indicated port or domain controller.

Syntax
------

```ManagedCPlusPlus
void SM_SendRPS(
   [in, HBAType("HBA_WWN")] uint8              PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8              AgentWWN[8],
   [in, HBAType("HBA_WWN")] uint8              ObjectWWN[8],
   [in] uint32                                 AgentDomain,
   [in] uint32                                 ObjectPortNumber,
   [in] uint32                                 InRespBufferMaxSize,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS     HBAStatus,
   [out] uint32                                TotalRespBufferSize,
   [out] uint32                                OutRespBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
);
```

Parameters
----------

*PortWWN*   
A worldwide name (WWN) for the local port through which the RPS command is sent. This information is delivered to the miniport driver in the PortWWN member of a SM\_SendRPS\_IN structure.

*AgentWWN*   
A worldwide name (WWN) for the port that is to be queried for the status of the port that is indicated by ObjectWWN. This information is delivered to the miniport driver in the AgentWWN member of a SM\_SendRPS\_IN structure.

*ObjectWWN*   
The worldwide name (WWN) of the port for which port status is to be returned. This information is delivered to the miniport driver in the ObjectWWN member of a SM\_SendRPS\_IN structure.

*AgentDomain*   
The domain number of the domain controller to be queried for the status of the port that is indicated by ObjectWWN. This information is delivered to the miniport driver in the AgentDomain member of a SM\_SendRPS\_IN structure.

*ObjectPortNumber*   
The worldwide name (WWN) of the port for which port status is to be returned. This information is delivered to the miniport driver in the ObjectPortNumber member of a SM\_SendRPS\_IN structure.

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

[**SM\_SendRPS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566320)

 

 






