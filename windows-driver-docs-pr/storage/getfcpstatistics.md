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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20GetFCPStatistics%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





