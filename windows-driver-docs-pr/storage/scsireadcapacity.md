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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20ScsiReadCapacity%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





