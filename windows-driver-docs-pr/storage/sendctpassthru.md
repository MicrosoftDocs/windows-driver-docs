---
title: SendCTPassThru function
description: The SendCTPassThru WMI method sends a common transport (CT) passthrough command to the indicated port.
ms.assetid: 7f512980-5aff-4359-b52e-7fcef9627e1f
keywords: ["SendCTPassThru function Storage Devices"]
topic_type:
- apiref
api_name:
- SendCTPassThru
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
---

# SendCTPassThru function


The **SendCTPassThru** WMI method sends a common transport (CT) passthrough command to the indicated port.

Syntax
------

```ManagedCPlusPlus
void SendCTPassThru(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS             HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                      PortWWN[8],
   [in] uint32                                         RequestBufferCount,
   [in, WmiSizeIs("RequestBufferCount")] uint8         RequestBuffer[],
   [out] uint32                                        TotalResponseBufferCount,
   [out] uint32                                        ActualResponseBufferCount,
   [out, WmiSizeIs("ActualResponseBufferCount")] uint8 ResponseBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

*PortWWN*   
A worldwide name for the HBA through which the target is accessed. This information is delivered to the miniport driver in the **PortWWN** member of a [**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412) structure.

*RequestBufferCount*   
The size in bytes of the buffer that will hold the results of the common transport command. The miniport driver returns this information in the **RequestBufferCount** member of a [**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412) structure.

*RequestBuffer*   
The results of the common transport command. The miniport driver returns this information in the **RequestBuffer** member of a [**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412) structure.

*TotalResponseBufferCount*   
The size in bytes of the results common transport command. The miniport driver returns this information in the **TotalResponseBufferCount** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

*ActualResponseBufferCount*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualResponseBufferCount** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

*ResponseBuffer*   
The results of the common transport command. The miniport driver returns this information in the **ResponseBuffer** member of a [**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413) structure.

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


[HBA\_STATUS](hba-status.md)

[**SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565412)

[**SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565413)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SendCTPassThru%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





