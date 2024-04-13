---
title: GetDiscoveredPortAttributes Function
description: The GetDiscoveredPortAttributes WMI method retrieves the attributes for a specified remote Fibre Channel port.
keywords: ["GetDiscoveredPortAttributes function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- GetDiscoveredPortAttributes
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.date: 10/17/2018
---

# GetDiscoveredPortAttributes function


The **GetDiscoveredPortAttributes** WMI method retrieves the attributes for a specified remote Fibre Channel port.

## Syntax

```ManagedCPlusPlus
void GetDiscoveredPortAttributes(
   [in] uint32                                                        PortIndex,
   [in] uint32                                                        DiscoveredPortIndex,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                            HBAStatus,
   [out, HBAType("HBA_PORTATTRIBUTES")] MSFC_HBAPortAttributesResults PortAttributes
);
```

## Parameters

*PortIndex*   
The index of the local port of type Nx\_Port through which to query the discovered remote port. This information is delivered to the miniport driver in the **PortIndex** member of a [**GetDiscoveredPortAttributes\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getdiscoveredportattributes_in) structure.

*DiscoveredPortIndex*   
The index of the remote port to be queried. This information is delivered to the miniport driver in the **DiscoveredPortIndex** member of a [**GetDiscoveredPortAttributes\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getdiscoveredportattributes_in) structure.

*HBAStatus*   
On return, contains a WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetDiscoveredPortAttributes\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getdiscoveredportattributes_out) structure.

*PortAttributes*   
A structure of type [**MSFC\_HBAPortAttributesResults**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_msfc_hbaportattributesresults) in which attributes for the discovered FC\_Port may be returned. The miniport driver returns this information in the **PortAttributes** member of a [**GetDiscoveredPortAttributes\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getdiscoveredportattributes_out) structure.

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


[**GetDiscoveredPortAttributes\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getdiscoveredportattributes_in)

[**GetDiscoveredPortAttributes\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getdiscoveredportattributes_out)

[**MSFC\_HBAPortAttributesResults**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_msfc_hbaportattributesresults)

 

