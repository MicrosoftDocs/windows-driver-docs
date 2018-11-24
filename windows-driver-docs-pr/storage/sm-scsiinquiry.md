---
title: SM\_ScsiInquiry function
description: The SM\_ScsiInquiry WMI method sends a SCSI inquiry command to the indicated device.
ms.assetid: 7af1c25a-1823-49e0-a2c5-6533bd22f606
keywords: ["SM_ScsiInquiry function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_ScsiInquiry
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_ScsiInquiry function


The SM\_ScsiInquiry WMI method sends a SCSI inquiry command to the indicated device.

Syntax
------

```ManagedCPlusPlus
void SM_ScsiInquiry(
   [in, HBAType("HBA_WWN")] uint8               HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8               DiscoveredPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8               DomainPortWWN[8],
   [in, HBAType("HBA_SCSILUN")] uint64          SmhbaLUN,
   [in] uint8                                   Cdb[6],
   [in] uint32                                  InRespBufferMaxSize,
   [in] uint32                                  InSenseBufferMaxSize,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS      HBAStatus,
   [out] uint8                                  ScsiStatus,
   [out] uint32                                 OutRespBufferSize,
   [out] uint32                                 OutSenseBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8  RespBuffer[],
   [out, WmiSizeIs("OutSenseBufferSize")] uint8 SenseBuffer[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the HBA through which the target is accessed. This information is delivered to the miniport driver in the HbaPortWWN member of a [**ScsiInquiry\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564593) structure.

*DiscoveredPortWWN*   
A worldwide name (WWN) for the port through which the target device is accessed. This information is delivered to the miniport driver in the DiscoveredPortWWN member of a [**ScsiInquiry\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564593) structure.

*DomainPortWWN*   
The worldwide name (WWN) for the callback. It is the Port\_Identifier that has the smallest value of any Port\_Identifier of an SMP port that was discovered by using the physical port. It has a value of zero if no SMP port has been discovered by using the physical port.

*SmhbaLUN*   
The logical unit number of the logical unit that will receive the SCSI inquiry command. This information is delivered to the miniport driver in the SmhbaLUN member of a [**ScsiInquiry\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564593) structure.

*Cdb*   
The command descriptor block that holds the SCSI inquiry command to be sent to the target device. This information is delivered to the miniport driver in the Cdb member of a [**ScsiInquiry\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564593) structure.

*InRespBufferMaxSize*   
The maximum size, in bytes, of the response buffer.

*InSenseBufferMaxSize*   
The maximum size, in bytes, for the sense buffer in the response.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structure.

*ScsiStatus*   
The status of the SCSI inquiry command. The miniport driver returns this information in the ScsiStatus member of a [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structure.

*OutRespBufferSize*   
The size, in bytes, of the buffer that will hold the results of the SCSI inquiry command. The miniport driver returns this information in the ResponseBufferSize member of a [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structure.

*OutSenseBufferSize*   
The size, in bytes, of the buffer that will hold the SCSI sense data that results from the SCSI inquiry command. The miniport driver returns this information in the SenseBufferSize member of a [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structure.

*RespBuffer*   
The results of the SCSI inquiry command. The miniport driver returns this information in the ResponseBuffer member of a [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structure.

*SenseBuffer*   
The SCSI sense data that results from the SCSI inquiry command. The miniport driver returns this information in the SenseBuffer member of a [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_ScsiInformationMethods WMI Class.

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
<td align="left">Hbapiwmi.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

 

 






