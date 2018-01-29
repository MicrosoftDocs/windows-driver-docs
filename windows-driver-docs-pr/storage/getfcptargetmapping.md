---
title: GetFcpTargetMapping function
description: The GetFcpTargetMapping WMI method retrieves a mapping between the information that uniquely identifies a set of logical units for the operating system and the Fibre Channel protocol (FCP) identifiers for these logical units.
ms.assetid: 2e4b3554-31de-4eaa-9228-844639a219d5
keywords: ["GetFcpTargetMapping function Storage Devices"]
topic_type:
- apiref
api_name:
- GetFcpTargetMapping
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
---

# GetFcpTargetMapping function


The **GetFcpTargetMapping** WMI method retrieves a mapping between the information that uniquely identifies a set of logical units for the operating system and the Fibre Channel protocol (FCP) identifiers for these logical units.

Syntax
------

```ManagedCPlusPlus
void GetFcpTargetMapping(
   [in, HBAType("HBA_WWN")] uint8                    HbaPortWWN[8],
   [in] uint32                                       InEntryCount,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS           HBAStatus,
   [out] uint32                                      TotalEntryCount,
   [out] uint32                                      OutEntryCount,
   [out, WmiSizeIs("OutEntryCount")] HBAFCPScsiEntry Entry[]
);
```

Parameters
----------

*HbaPortWWN\[8\]*   
A worldwide name for the port whose table of mappings is to be retrieved. This information is delivered to the miniport driver in the **HbaPortWWN** member of a [**GetFcpTargetMapping\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554950) structure.

*InEntryCount*   
Indicates the number of binding entries that the WMI provider can report in the *Entry* parameter.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetFcpTargetMapping\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554952) structure.

*TotalEntryCount*   
Indicates the total number of persistent bindings associated with the HBA.

*OutEntryCount*   
Indicates the total number of mappings retrieved by the **GetFcpTargetMapping** method. This value will be less than or equal to *TotalEntryCount*.

*Entry\[\]*   
An array of structures of type [**HBAFCPScsiEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556040) that describe an HBA's bindings between operating system and Fibre Channel protocol (FCP) identifiers.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the [MSFC\_HBAFCPInfo WMI Class](msfc-hbafcpinfo-wmi-class.md).

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

[**GetFcpTargetMapping\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554950)

[**GetFcpTargetMapping\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554952)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20GetFcpTargetMapping%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





