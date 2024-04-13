---
title: GetFC4Statistics Function
description: The GetFC4Statistics WMI method reports traffic statistics on a port of type Nx\_Port for the indicated FC-4 protocol.
keywords: ["GetFC4Statistics function Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- GetFC4Statistics
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.date: 10/17/2018
---

# GetFC4Statistics function


The **GetFC4Statistics** WMI method reports traffic statistics on a port of type Nx\_Port for the indicated FC-4 protocol.

## Syntax

```ManagedCPlusPlus
void GetFC4Statistics(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus,
   [in, HBAType("HBA_WWN")] uint8          PortWWN,
   [in] uint8                              FC4Type,
   [out] MSFC_FC4STATISTICS                FC4Statistics
);
```

## Parameters

*HBAStatus*   
On return, contains a WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetFC4Statistics\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc4statistics_out) structure.

*PortWWN*   
The worldwide name for the local port of type Nx\_Port whose traffic statistics are to be reported. This information is delivered to the miniport driver in the **PortWWN** member of a [**GetFC4Statistics\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc4statistics_in) structure.

*FC4Type*   
A value that indicates the type FC-4 protocol. For an explanation of FC4 types, see the T11 committee's *Fibre Channel Generic Services - 4* specification. This information is delivered to the miniport driver in the **FC4Type** member of a [**GetFC4Statistics\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc4statistics_in) structure.

*FC4Statistics*   
On return, contains a structure of type [**MSFC\_FC4STATISTICS**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_msfc_fc4statistics) that holds statistics for the specified FC-4 protocol. The miniport driver returns this information in the **FC4Statistics** member of a [**GetFC4Statistics\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc4statistics_out) structure.

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


[**GetFC4Statistics\_IN**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc4statistics_in)

[**GetFC4Statistics\_OUT**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_getfc4statistics_out)

[HBA\_STATUS](hba-status.md)

[**MSFC\_FC4STATISTICS**](/windows-hardware/drivers/ddi/hbapiwmi/ns-hbapiwmi-_msfc_fc4statistics)

 

