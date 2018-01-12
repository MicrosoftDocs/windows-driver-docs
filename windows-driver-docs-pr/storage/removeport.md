---
title: RemovePort function
description: The RemovePort WMI method configures the WMI provider so that it stops passing events associated with the indicated port to the WMI client.
ms.assetid: 6e466a89-273b-4ed9-a0fe-5a8df745b28a
keywords: ["RemovePort function Storage Devices"]
topic_type:
- apiref
api_name:
- RemovePort
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# RemovePort function


The **RemovePort** WMI method configures the WMI provider so that it stops passing events associated with the indicated port to the WMI client.

Syntax
------

```ManagedCPlusPlus
void RemovePort(
   [in, HBAType("HBA_WWN")] uint8          PortWWN[8],
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS HBAStatus
);
```

Parameters
----------

*PortWWN*   
A worldwide name that indicates the port that should be removed from the list of ports whose events are reported to the WMI client.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**RemovePort\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564017) structure.

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


[**RemovePort\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564014)

[**RemovePort\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564017)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20RemovePort%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





