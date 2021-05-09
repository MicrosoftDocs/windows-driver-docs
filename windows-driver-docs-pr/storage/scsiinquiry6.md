---
title: ScsiInquiry function
description: The ScsiInquiry WMI method sends a SCSI inquiry command to the indicated device.
keywords: ["ScsiInquiry function Storage Devices"]
topic_type:
- apiref
api_name:
- ScsiInquiry
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ScsiInquiry function


The **ScsiInquiry** WMI method sends a SCSI inquiry command to the indicated device.

## Syntax

```ManagedCPlusPlus
void ScsiInquiry(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS      HBAStatus,
   [in] uint8                                   Cdb[6],
   [in, HBAType("HBA_WWN")] uint8               HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8               DiscoveredPortWWN[8],
   [in] uint64                                  FcLun,
   [out] uint32                                 ResponseBufferSize,
   [out] uint32                                 SenseBufferSize,
   [out] uint8                                  ScsiStatus,
   [out, WmiSizeIs("ResponseBufferSize")] uint8 ResponseBuffer[],
   [out, WmiSizeIs("SenseBufferSize")] uint8    SenseBuffer[]
);
```

## Parameters

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out) structure.

*Cdb*   
The command descriptor block that holds the SCSI inquiry command to be sent to the target device. This information is delivered to the miniport driver in the **Cdb** member of a [**ScsiInquiry\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_in) structure.

*HbaPortWWN*   
A worldwide name for the HBA through which the target is accessed. This information is delivered to the miniport driver in the **HbaPortWWN** member of a [**ScsiInquiry\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_in) structure.

*DiscoveredPortWWN*   
A worldwide name for the port through which the target device is accessed. This information is delivered to the miniport driver in the **DiscoveredPortWWN** member of a [**ScsiInquiry\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_in) structure.

*FcLun*   
The logical unit number of the logical unit that will receive the SCSI inquiry command. This information is delivered to the miniport driver in the **FcLun** member of a [**ScsiInquiry\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_in) structure.

*ResponseBufferSize*   
The size in bytes of the buffer that will hold the results of the SCSI inquiry command. The miniport driver returns this information in the **ResponseBufferSize** member of a [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out) structure.

*SenseBufferSize*   
The size in bytes of the buffer that will hold the SCSI sense data that results from the SCSI inquiry command. The miniport driver returns this information in the **SenseBufferSize** member of a [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out) structure.

*ScsiStatus*   
The status of the SCSI inquiry command. The miniport driver returns this information in the **ScsiStatus** member of a [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out) structure.

*ResponseBuffer*   
The results of the SCSI inquiry command. The miniport driver returns this information in the **ResponseBuffer** member of a [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out) structure.

*SenseBuffer*   
The SCSI sense data that results from the SCSI inquiry command. The miniport driver returns this information in the **SenseBuffer** member of a [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out) structure.

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

[**ScsiInquiry\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_in)

[**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_scsiinquiry_out)

 

