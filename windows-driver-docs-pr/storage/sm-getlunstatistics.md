---
title: SM\_GetLUNStatistics function
description: The SMHBA\_GetLUNStatistics method returns traffic statistics for a specific SCSI logical unit that is provided by using the FCP protocol or SSP protocol on a specific local HBA.
keywords: ["SM_GetLUNStatistics function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_GetLUNStatistics
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# SM\_GetLUNStatistics function


The SMHBA\_GetLUNStatistics method returns traffic statistics for a specific SCSI logical unit that is provided by using the FCP protocol or SSP protocol on a specific local HBA.

## Syntax

```ManagedCPlusPlus
void SM_GetLUNStatistics(
   [in, HBAType("HBA_SCSIID")] HBAScsiID                                     Lunit,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                                   HBAStatus,
   [out, HBAType("MS_SMHBA_PROTOCOLSTATISTICS")] MS_SMHBA_PROTOCOLSTATISTICS ProtocolStatistics
);
```

## Parameters

*Lunit*   
A structure of type [**HBA\_ScsiId**](/previous-versions/ff557191(v=vs.85)) that contains information that is used by the operating system to identify a SCSI logical unit.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_GetLUNStatistics\_OUT structure.

*ProtocolStatistics*   
A structure of type [**MS\_SMHBA\_PROTOCOLSTATISTICS**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_ms_smhba_protocolstatistics) that is used to report protocol traffic statistics on a port.

## Return value

Not applicable to WMI methods.

## Remarks

This WMI method belongs to the MS\_SM\_TargetInformationMethods WMI Class.

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
<td align="left">Hbapiwmi.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SM\_GetLUNStatistics\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sm_getlunstatistics_in)

[**SM\_GetLUNStatistics\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_sm_getlunstatistics_out)

 

