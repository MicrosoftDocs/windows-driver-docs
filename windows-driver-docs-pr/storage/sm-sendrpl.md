---
title: SM\_SendRPL function
description: The SM\_SendRPL WMI method sends a read port list (RPL) command through the indicated port to indicated destination port.
ms.assetid: 9297d5eb-f8c4-48f3-8536-a94c66917e66
keywords: ["SM_SendRPL function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendRPL
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_SendRPL function


The SM\_SendRPL WMI method sends a read port list (RPL) command through the indicated port to indicated destination port.

Syntax
------

```ManagedCPlusPlus
void SM_SendRPL(
   [in, HBAType("HBA_WWN")] uint8              PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8              AgentWWN[8],
   [in] uint32                                 AgentDomain,
   [in] uint32                                 PortIndex,
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
A worldwide name (WWN) for the local port through which the read port list (RPL) command is sent. This information is delivered to the miniport driver in the PortWWN member of a SM\_SendRPL\_IN structure.

*AgentWWN*   
A worldwide name (WWN) for the port that is to be queried for a list of ports of type FC\_Port. For a definition of FC\_Port, see the T11 committee's *Fibre Channel HBA API* specification. This information is delivered to the miniport driver in the AgentWWN member of a SM\_SendRPL\_IN structure.

*AgentDomain*   
The domain number for the domain controller that is to be queried for a list of ports of type FC\_Port. For a definition of FC\_Port, see the T11 committee's *Fibre Channel HBA API* specification. This information is delivered to the miniport driver in the agent\_domain member of a SM\_SendRPL\_IN structure.

*PortIndex*   
The port index of the first port in the list of ports of type FC\_Port to be returned. This information is delivered to the miniport driver in the portIndex member of a SM\_SendRPL\_IN structure.

*InRespBufferMaxSize*   
The maximum size of the response buffer.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SendRPL\_OUT structure.

*TotalRespBufferSize*   
The size, in bytes, of the results of the read port list (RPL) command. The miniport driver returns this information in the TotalRespBufferSize member of a SM\_SendRPL\_OUT structure.

*OutRespBufferSize*   
The size, in bytes, of the data that was actually retrieved. The miniport driver returns this information in the OutRespBufferSize member of a SM\_SendRPL\_OUT structure.

*RespBuffer*   
The results of the read port list (RPL) command. The miniport driver returns this information in the RespBuffer member of a SendRPL\_OUT structure.

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

[**SM\_SendRPL\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566314)

[**SM\_SendRPL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566315)

 

 






