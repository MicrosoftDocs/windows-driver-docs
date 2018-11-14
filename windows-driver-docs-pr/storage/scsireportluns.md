---
title: ScsiReportLuns function
description: The ScsiReportLuns WMI method sends a SCSI report LUNs command to the indicated device.
ms.assetid: 12c9138d-41b7-404f-8431-08d7cf9cc330
keywords: ["ScsiReportLuns function Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiReportLuns
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ScsiReportLuns function


The **ScsiReportLuns** WMI method sends a SCSI report LUNs command to the indicated device.

Syntax
------

```ManagedCPlusPlus
void ScsiReportLuns(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS      HBAStatus,
   [in] uint8                                   Cdb[12],
   [in, HBAType("HBA_WWN")] uint8               HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8               DiscoveredPortWWN[8],
   [out] uint32                                 ResponseBufferSize,
   [out] uint32                                 SenseBufferSize,
   [out] uint8                                  ScsiStatus,
   [out, WmiSizeIs("ResponseBufferSize")] uint8 ResponseBuffer[],
   [out, WmiSizeIs("SenseBufferSize")] uint8    SenseBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937) structure.

*Cdb*   
The command descriptor block that holds the SCSI report LUNs command to be sent to the target device. This information is delivered to the miniport driver in the **Cdb** member of a [**ScsiReportLuns\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564932) structure.

*HbaPortWWN*   
A worldwide name for the HBA through which the target is accessed. This information is delivered to the miniport driver in the **HbaPortWWN** member of a [**ScsiReportLuns\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564932) structure.

*DiscoveredPortWWN*   
A worldwide name for the port through which the target device is accessed. This information is delivered to the miniport driver in the **DiscoveredPortWWN** member of a [**ScsiReportLuns\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564932) structure.

*ResponseBufferSize*   
The size in bytes of the buffer that will hold the results of the SCSI report LUNs command. The miniport driver returns this information in the **ResponseBufferSize** member of a [**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937) structure.

*SenseBufferSize*   
The size in bytes of the buffer that will hold the SCSI sense data that results from the SCSI report LUNs command. The miniport driver returns this information in the **SenseBufferSize** member of a [**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937) structure.

*ScsiStatus*   
The status of the SCSI report LUNs command. The miniport driver returns this information in the **ScsiStatus** member of a [**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937) structure.

*ResponseBuffer*   
The results of the SCSI report LUNs command. The miniport driver returns this information in the **ResponseBuffer** member of a [**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937) structure.

*SenseBuffer*   
The SCSI sense data that results from the SCSI report LUNs command. The miniport driver returns this information in the **SenseBuffer** member of a [**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937) structure.

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

[**ScsiReportLuns\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564932)

[**ScsiReportLuns\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564937)

 

 






