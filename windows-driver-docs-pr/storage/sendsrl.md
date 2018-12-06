---
title: SendSRL function
description: The SendSRL WMI method sends a scan remote loop (SRL) command through the indicated port to the indicated domain controller.
ms.assetid: b191fc8c-2765-4e39-aab7-e950ae1d46b0
keywords: ["SendSRL function Storage Devices"]
topic_type:
- apiref
api_name:
- SendSRL
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendSRL function


The **SendSRL** WMI method sends a scan remote loop (SRL) command through the indicated port to the indicated domain controller.

Syntax
------

```ManagedCPlusPlus
void SendSRL(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                PortWWN[8],
   [in, HBAType("HBA_WWN")] uint8                WWN[8],
   [in] uint32                                   Domain,
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565524) structure.

*PortWWN*   
A worldwide name for the local port through which the SRL command is sent. This information is delivered to the miniport driver in the **PortWWN** member of a SendSRL\_IN structure.

*WWN*   
A worldwide name for the port of type FL\_Port whose loop is to be scanned. This information is delivered to the miniport driver in the **WWN** member of a SendSRL\_IN structure.

*Domain*   
The domain number for the domain whose loops are to be scanned. This information is delivered to the miniport driver in the **Domain** member of a SendSRL\_IN structure.

*TotalRspBufferSize*   
The size in bytes of the results of the SRL command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565524) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565524) structure.

*RspBuffer*   
The results of the SRL command. The miniport driver returns this information in the **RspBuffer** member of a [**SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565524) structure.

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

SendSRL\_IN
[**SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565524)

 

 






