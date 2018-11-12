---
title: SendCTPassThru function
description: The SendCTPassThru WMI method sends a common transport (CT) passthrough command to the indicated port.
ms.assetid: 7f512980-5aff-4359-b52e-7fcef9627e1f
keywords: ["SendCTPassThru function Storage Devices"]
topic_type:
- apiref
api_name:
- SendCTPassThru
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SendCTPassThru function


The **SendCTPassThru** WMI method sends a common transport (CT) passthrough command to the indicated port.

Syntax
------

```ManagedCPlusPlus
void SendCTPassThru(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS             HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                      PortWWN[8],
   [in] uint32                                         RequestBufferCount,
   [in, WmiSizeIs("RequestBufferCount")] uint8         RequestBuffer[],
   [out] uint32                                        TotalResponseBufferCount,
   [out] uint32                                        ActualResponseBufferCount,
   [out, WmiSizeIs("ActualResponseBufferCount")] uint8 ResponseBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

*PortWWN*   
A worldwide name for the HBA through which the target is accessed. This information is delivered to the miniport driver in the **PortWWN** member of a [**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412) structure.

*RequestBufferCount*   
The size in bytes of the buffer that will hold the results of the common transport command. The miniport driver returns this information in the **RequestBufferCount** member of a [**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412) structure.

*RequestBuffer*   
The results of the common transport command. The miniport driver returns this information in the **RequestBuffer** member of a [**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412) structure.

*TotalResponseBufferCount*   
The size in bytes of the results common transport command. The miniport driver returns this information in the **TotalResponseBufferCount** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

*ActualResponseBufferCount*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualResponseBufferCount** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

*ResponseBuffer*   
The results of the common transport command. The miniport driver returns this information in the **ResponseBuffer** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

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

[**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412)

[**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413)

 

 






