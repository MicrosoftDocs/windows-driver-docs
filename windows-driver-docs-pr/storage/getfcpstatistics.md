---
title: GetFCPStatistics function
description: The GetFCPStatistics WMI method returns FCP traffic statistics for the indicated SCSI logical unit on the indicated local HBA.
ms.assetid: 566368d7-ee13-449d-97c3-1c214984fee5
keywords: ["GetFCPStatistics function Storage Devices"]
topic_type:
- apiref
api_name:
- GetFCPStatistics
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetFCPStatistics function


The **GetFCPStatistics** WMI method returns FCP traffic statistics for the indicated SCSI logical unit on the indicated local HBA.

Syntax
------

```ManagedCPlusPlus
void GetFCPStatistics(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
   [in] HBAScsiID                          ScsiId,
   [out] MSFC_FC4STATISTICS                FC4Statistics
);
```

Parameters
----------

*HBAStatus*   
On return, contains a WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetFCPStatistics\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554944) structure.

*ScsiId*   
On return, contains a structure of type [**HBAScsiID**](https://msdn.microsoft.com/library/windows/hardware/ff556042) that holds information that identifies the device. This information is delivered to the miniport driver in the **ScsiId** member of a [**GetFCPStatistics\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554942) structure.

*FC4Statistics*   
On return, contains a structure of type [**MSFC\_FC4STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff562492) that holds statistics for the indicated SCSI logical unit. The miniport driver returns this information in the **FC4Statistics** member of a [**GetFCPStatistics\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554944) structure.

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


[**GetFCPStatistics\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554942)

[**GetFCPStatistics\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554944)

[**MSFC\_FC4STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff562492)

 

 






