---
title: SendRPS function
description: The SendRPS WMI method sends a read port status block (RPS) request to the indicated port or domain controller.
keywords: ["SendRPS function Storage Devices"]
topic_type:
- apiref
api_name:
- SendRPS
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendRPS function


The **SendRPS** WMI method sends a read port status block (RPS) request to the indicated port or domain controller.

## Syntax

```ManagedCPlusPlus
void SendRPS(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                AgentWWN[8],
   [in, HBAType("HBA_WWN")] uint8                ObjectWWN[8],
   [in] uint32                                   AgentDomain,
   [in] uint32                                   ObjectPortNumber,
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendRPS\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_out) structure.

*PortWWN*   
A worldwide name for the local port through which the RPS command is sent. This information is delivered to the miniport driver in the **PortWWN** member of a [**SendRPS\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_in) structure.

*AgentWWN*   
A worldwide name for the port that is to be queried for the status of the port indicated by *ObjectWWN*. This information is delivered to the miniport driver in the **AgentWWN** member of a [**SendRPS\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_in) structure.

*ObjectWWN*   
The worldwide name of the port for which port status is to be returned. This information is delivered to the miniport driver in the **ObjectWWN** member of a [**SendRPS\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_in) structure.

*AgentDomain*   
The domain number of the domain controller to be queried for the status of the port indicated by *ObjectWWN*. This information is delivered to the miniport driver in the **AgentDomain** member of a [**SendRPS\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_in) structure.

*ObjectPortNumber*   
The worldwide name of the port for which port status is to be returned. This information is delivered to the miniport driver in the **ObjectPortNumber** member of a [**SendRPS\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_in) structure.

*TotalRspBufferSize*   
The size in bytes of the results of the RPS command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendRPS\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_out) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendRPS\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_out) structure.

*RspBuffer*   
The results of the RPS command. The miniport driver returns this information in the **RspBuffer** member of a [**SendRPS\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_out) structure.

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

[**SendRPS\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_in)

[**SendRPS\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrps_out)

 

