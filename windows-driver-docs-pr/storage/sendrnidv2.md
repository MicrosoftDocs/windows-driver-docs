---
title: SendRNIDV2 function
description: The SendRNIDV2 WMI method sends a version 2 RNID command to the indicated port.
keywords: ["SendRNIDV2 function Storage Devices"]
topic_type:
- apiref
api_name:
- SendRNIDV2
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendRNIDV2 function


The **SendRNIDV2** WMI method sends a version 2 RNID command to the indicated port.

## Syntax

```ManagedCPlusPlus
void SendRNIDV2(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                DestWWN[8],
   [in] uint32                                   DestFCID,
   [in] uint32                                   NodeIdDataFormat,
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendRNIDV2\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_out) structure.

*PortWWN*   
A worldwide name for the local port through which the version 2 RNID command is sent. This information is delivered to the miniport driver in the **PortWWN** member of a [**SendRNIDV2\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_in) structure.

*DestWWN*   
A worldwide name for the destination port. This information is delivered to the miniport driver in the **DestWWN** member of a [**SendRNIDV2\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_in) structure.

*DestFCID*   
An address identifier of the destination port. This information is delivered to the miniport driver in the **DestFCID** member of a [**SendRNIDV2\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_in) structure.

*NodeIdDataFormat*   
The node identification data format. For a description of the values that this member can have, see the T11 committee's *Fibre Channel HBA API* specification. This information is delivered to the miniport driver in the **NodeIdDataFormat** member of a [**SendRNIDV2\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_in) structure.

*TotalRspBufferSize*   
The size in bytes of the results of the version 2 RNID command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendRNIDV2\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_out) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendRNIDV2\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_out) structure.

*RspBuffer*   
The results of the version 2 RNID command. The miniport driver returns this information in the **RspBuffer** member of a [**SendRNIDV2\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_out) structure.

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

[**SendRNIDV2\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_in)

[**SendRNIDV2\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sendrnidv2_out)

 

