---
title: GetEventBuffer function
description: The GetEventBuffer WMI method retrieves the next events in the HBA's event queue.
ms.assetid: 9eee93e0-2661-4777-8c02-a87c4e1d744c
keywords: ["GetEventBuffer function Storage Devices"]
topic_type:
- apiref
api_name:
- GetEventBuffer
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# GetEventBuffer function


The **GetEventBuffer** WMI method retrieves the next events in the HBA's event queue.

Syntax
------

```ManagedCPlusPlus
void GetEventBuffer(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS         HBAStatus,
   [out] uint32                                    EventCount,
   [out, WmiSizeIs("EventCount")] MSFC_EventBuffer Events[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains a WMI qualifier value that indicates the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**GetEventBuffer\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553937) structure.

*EventCount*   
On return, indicates the number of events whose information was retrieved. The miniport driver returns this information in the **EventCount** member of a [**GetEventBuffer\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553937) structure.

*Events\[\]*   
An array of structures of type [**MSFC\_EventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562480) that contain information about the next events in the HBA event queue. The miniport driver returns this information in the **Events** member of a [**GetEventBuffer\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553937) structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

The **GetEventBuffer** method removes events from the queue after retrieving their information.

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


[**GetEventBuffer\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff553937)

[**MSFC\_EventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff562480)

 

 






