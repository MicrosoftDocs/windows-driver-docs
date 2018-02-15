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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20GetEventBuffer%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





