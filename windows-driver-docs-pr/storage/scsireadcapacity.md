---
title: ScsiReadCapacity function
description: The ScsiReadCapacity WMI method sends a SCSI read capacity command to the indicated device.
ms.assetid: 2e865ed8-a835-40e7-8ba3-babb9d18eb23
keywords: ["ScsiReadCapacity function Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiReadCapacity
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ScsiReadCapacity function


The **ScsiReadCapacity** WMI method sends a SCSI read capacity command to the indicated device.

Syntax
------

```ManagedCPlusPlus
void ScsiReadCapacity(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS      HBAStatus,
   [in] uint8                                   Cdb[10],
   [in, HBAType("HBA_WWN")] uint8               HbaPortWWN[10],
   [in, HBAType("HBA_WWN")] uint8               DiscoveredPortWWN[10],
   [in] uint64                                  FcLun,
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
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910) structure.

*Cdb*   
The command descriptor block that holds the SCSI read capacity command to be sent to the target device. This information is delivered to the miniport driver in the **Cdb** member of a [**ScsiReadCapacity\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564901) structure.

*HbaPortWWN*   
A worldwide name for the HBA through which the target is accessed. This information is delivered to the miniport driver in the **HbaPortWWN** member of a [**ScsiReadCapacity\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564901) structure.

*DiscoveredPortWWN*   
A worldwide name for the port through which the target device is accessed. This information is delivered to the miniport driver in the **DiscoveredPortWWN** member of a [**ScsiReadCapacity\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564901) structure.

*FcLun*   
The logical unit number of the logical unit that will receive the SCSI read capacity command. This information is delivered to the miniport driver in the **FcLun** member of a [**ScsiReadCapacity\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564901) structure.

*ResponseBufferSize*   
The size in bytes of the buffer that will hold the results of the read capacity command. The miniport driver returns this information in the **ResponseBufferSize** member of a [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910) structure.

*SenseBufferSize*   
The size in bytes of the buffer that will hold the SCSI sense data that results from the SCSI inquiry command. The miniport driver returns this information in the **SenseBufferSize** member of a [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910) structure.

*ScsiStatus*   
The status of the SCSI read capacity command. The miniport driver returns this information in the **ScsiStatus** member of a [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910) structure.

*ResponseBuffer*   
The results of the SCSI read capacity command. The miniport driver returns this information in the **ResponseBuffer** member of a [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910) structure.

*SenseBuffer*   
The SCSI sense data that results from the SCSI read capacity command. The miniport driver returns this information in the **SenseBuffer** member of a [**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910) structure.

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

[**ScsiReadCapacity\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564901)

[**ScsiReadCapacity\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564910)

 

 






