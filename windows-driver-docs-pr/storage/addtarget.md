---
title: AddTarget function
description: The AddTarget WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.
ms.assetid: 9aac339b-a9b4-4de7-99dd-fa5f8889a686
keywords: ["AddTarget function Storage Devices"]
topic_type:
- apiref
api_name:
- AddTarget
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# AddTarget function


The **AddTarget** WMI method configures the WMI provider to inform the WMI client about events that are associated with the indicated targets.

Syntax
------

```ManagedCPlusPlus
void AddTarget(
   [in, HBAType("HBA_WWN")] uint8          HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8          DiscoveredPortWWN[8],
   [in] uint32                             AllTargets,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*HbaPortWWN\[8\]*   
The worldwide name of the local port whose events the WMI client will receive.

*DiscoveredPortWWN\[8\]*   
A worldwide name that specifies the discovered target whose events the WMI client will receive.

*AllTargets*   
The scope of the target events to report. If this member is zero, the WMI client will receive events associated with the port that is indicated by *DiscoveredPortWWN*. If this member is nonzero, the WMI client will receive all events associated with all currently discovered targets as well as targets that are discovered in the future.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**AddTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff550138) structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the [MSFC\_EventControl WMI Class](msfc-eventcontrol-wmi-class.md).

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
</tbody>
</table>

## <span id="see_also"></span>See also


[**AddTarget\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff550137)

[**AddTarget\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff550138)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20AddTarget%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





