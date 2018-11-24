---
title: SendRLS function
description: The SendRLS WMI method sends a read link error status block (RLS) through the indicated local port to the indicated remote port to retrieve a link error status block associated with the remote port.
ms.assetid: 57dcc810-023f-4dbf-a9c2-3062765729c7
keywords: ["SendRLS function Storage Devices"]
topic_type:
- apiref
api_name:
- SendRLS
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendRLS function


The **SendRLS** WMI method sends a read link error status block (RLS) through the indicated local port to the indicated remote port to retrieve a link error status block associated with the remote port.

Syntax
------

```ManagedCPlusPlus
void SendRLS(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                DestWWN[8],
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendRLS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565452) structure.

*PortWWN*   
A worldwide name for the local port through which the RLS command is sent. This information is delivered to the miniport driver in the **PortWWN** member of a [**SendRLS\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565446) structure.

*DestWWN*   
A worldwide name for the destination port. This information is delivered to the miniport driver in the **DestWWN** member of a [**SendRLS\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565446) structure.

*TotalRspBufferSize*   
The size in bytes of the results of the RLS command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendRLS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565452) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendRLS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565452) structure.

*RspBuffer*   
The results of the RLS command. The miniport driver returns this information in the **RspBuffer** member of a [**SendRLS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565452) structure.

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

[**SendRLS\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565446)

[**SendRLS\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565452)

 

 






