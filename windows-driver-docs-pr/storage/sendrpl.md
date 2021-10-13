---
title: SendRPL function
description: The SendRPL WMI method sends a read port list (RPL) command through the indicated port to indicated destination port.
keywords: ["SendRPL function Storage Devices"]
topic_type:
- apiref
api_name:
- SendRPL
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendRPL function


The **SendRPL** WMI method sends a read port list (RPL) command through the indicated port to indicated destination port.

## Syntax

```ManagedCPlusPlus
void SendRPL(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                AgentWWN[8],
   [in] uint32                                   agent_domain,
   [in] uint32                                   portIndex,
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendRPL\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_out) structure.

*PortWWN*   
A worldwide name for the local port through which the read port list (RPL) command is sent. This information is delivered to the miniport driver in the **PortWWN** member of a [**SendRPL\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_in) structure.

*AgentWWN*   
A worldwide name for the port that is to be queried for a list of ports of type FC\_Port. For a definition of FC\_Port, see the T11 committee's *Fibre Channel HBA API* specification. This information is delivered to the miniport driver in the **AgentWWN** member of a [**SendRPL\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_in) structure.

*agent\_domain*   
The domain number for the domain controller that is to be queried for a list of ports of type FC\_Port. For a definition of FC\_Port, see the T11 committee's *Fibre Channel HBA API* specification. This information is delivered to the miniport driver in the **agent\_domain** member of a [**SendRPL\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_in) structure.

*portIndex*   
The port index of the first port in the list of ports of type FC\_Port to be returned. This information is delivered to the miniport driver in the **portIndex** member of a [**SendRPL\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_in) structure.

*TotalRspBufferSize*   
The size in bytes of the results of the read port list (RPL) command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendRPL\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_out) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendRPL\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_out) structure.

*RspBuffer*   
The results of the read port list (RPL) command. The miniport driver returns this information in the **RspBuffer** member of a [**SendRPL\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_out) structure.

## Return value

Not applicable to WMI methods.

## Remarks

This WMI method belongs to the [MSFC\_HBAAdapterMethods WMI Class](msfc-hbaadaptermethods-wmi-class.md).

## Requirements

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
<td align="left">Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">Hbaapi.lib</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SendRPL\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_in)

[**SendRPL\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrpl_out)

 

