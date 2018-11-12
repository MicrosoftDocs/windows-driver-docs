---
title: SendLIRR function
description: The SendLIRR WMI method sends a link incident record registration (LIRR) command through the indicated local port to the indicated remote port.
ms.assetid: ca54161d-d5fe-4775-a38c-dfaf3fd8c00b
keywords: ["SendLIRR function Storage Devices"]
topic_type:
- apiref
api_name:
- SendLIRR
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendLIRR function


The **SendLIRR** WMI method sends a link incident record registration (LIRR) command through the indicated local port to the indicated remote port.

Syntax
------

```ManagedCPlusPlus
void SendLIRR(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                SourceWWN[8],
   [in, HBAType("HBA_WWN")] uint8                DestWWN[8],
   [in] uint8                                    Function,
   [in] uint8                                    Type,
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

*SourceWWN*   
A worldwide name for the local port through which the LIRR command is sent. This information is delivered to the miniport driver in the **SourceWWN** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*DestWWN*   
A worldwide name for the destination port. This information is delivered to the miniport driver in the **DestWWN** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*Function*   
The code that identifies which registration function is to be performed. For an explanation of which values can be assigned to this member, see the T11 committee's *Fibre Channel Framing and Signaling* specification. This information is delivered to the miniport driver in the **Function** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*Type*   
The device type for which link information is requested. For an explanation of which values can be assigned to this member, see the T11 committee's *Fibre Channel Framing and Signaling* specification. This information is delivered to the miniport driver in the **Function** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*TotalRspBufferSize*   
The size in bytes of the results of the LIRR command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

*RspBuffer*   
The results of the LIRR command. The miniport driver returns this information in the **RspBuffer** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the [MSFC\_HBAAdapterMethods WMI Class](msfc-hbaadaptermethods-wmi-class.md).

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

[**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435)

[**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439)

 

 






