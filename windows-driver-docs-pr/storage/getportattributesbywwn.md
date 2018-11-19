---
title: GetPortAttributesByWWN function
description: The GetPortAttributesByWWN method retrieves the attributes for the port specified by Port Name.
ms.assetid: 24b62b1c-9f47-40f1-aa72-849fabcbfbae
keywords: ["GetPortAttributesByWWN function Storage Devices"]
topic_type:
- apiref
api_name:
- GetPortAttributesByWWN
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetPortAttributesByWWN function


The **GetPortAttributesByWWN** method retrieves the attributes for the port specified by Port Name.

Syntax
------

```ManagedCPlusPlus
void GetPortAttributesByWWN(
   [in, HBAType("HBA_WWN")] uint8                                     wwn[8],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                            HBAStatus,
   [out, HBAType("HBA_PORTATTRIBUTES")] MSFC_HBAPortAttributesResults PortAttributes
);
```

Parameters
----------

*wwn\[8\]*   
The name of the port whose attributes are to be queried. This information is delivered to the miniport driver in the **wwn** member of a [**GetPortAttributesByWWN\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554967) structure.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetPortAttributesByWWN\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554969) structure.

*PortAttributes*   
A structure of type [**MSFC\_HBAPortAttributesResults**](https://msdn.microsoft.com/library/windows/hardware/ff562510) in which attributes for the discovered FC\_Port may be returned. The miniport driver returns this information in the **PortAttributes** member of a [**GetDiscoveredPortAttributes\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553930) structure.

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


[**GetPortAttributesByWWN\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff554967)

[**GetPortAttributesByWWN\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff554969)

[**MSFC\_HBAPortAttributesResults**](https://msdn.microsoft.com/library/windows/hardware/ff562510)

 

 






