---
title: SendLIRR function
description: The SendLIRR WMI method sends a link incident record registration (LIRR) command through the indicated local port to the indicated remote port.
ms.assetid: ca54161d-d5fe-4775-a38c-dfaf3fd8c00b
keywords: ["SendLIRR function Storage Devices"]
topic_type:
- apiref
api_name:
- SendLIRR
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
---

# SendLIRR function


The **SendLIRR** WMI method sends a link incident record registration (LIRR) command through the indicated local port to the indicated remote port.

Syntax
------

```ManagedCPlusPlus
void SendLIRR(
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS       HBAStatus,
   [in, HBAType("HBA_WWN")] uint8                SourceWWN[8],
   [in, HBAType("HBA_WWN")] uint8                DestWWN[8],
   [in] uint8                                    Function,
   [in] uint8                                    Type,
   [out] uint32                                  TotalRspBufferSize,
   [out] uint32                                  ActualRspBufferSize,
   [out, WmiSizeIs("ActualRspBufferSize")] uint8 RspBuffer[]
);
```

Parameters
----------

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

*SourceWWN*   
A worldwide name for the local port through which the LIRR command is sent. This information is delivered to the miniport driver in the **SourceWWN** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*DestWWN*   
A worldwide name for the destination port. This information is delivered to the miniport driver in the **DestWWN** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*Function*   
The code that identifies which registration function is to be performed. For an explanation of which values can be assigned to this member, see the T11 committee's *Fibre Channel Framing and Signaling* specification. This information is delivered to the miniport driver in the **Function** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*Type*   
The device type for which link information is requested. For an explanation of which values can be assigned to this member, see the T11 committee's *Fibre Channel Framing and Signaling* specification. This information is delivered to the miniport driver in the **Function** member of a [**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435) structure.

*TotalRspBufferSize*   
The size in bytes of the results of the LIRR command. The miniport driver returns this information in the **TotalRspBufferSize** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

*ActualRspBufferSize*   
The size in bytes of the data that was actually retrieved. The miniport driver returns this information in the **ActualRspBufferSize** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

*RspBuffer*   
The results of the LIRR command. The miniport driver returns this information in the **RspBuffer** member of a [**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439) structure.

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

[**SendLIRR\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565435)

[**SendLIRR\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565439)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SendLIRR%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





