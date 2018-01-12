---
title: SM\_SendCTPassThru function
description: The SM\_SendCTPassThru WMI method sends a common transport (CT) pass-through command to the indicated port.
ms.assetid: 437f0c79-78f6-406e-8774-79de4425bfe8
keywords: ["SM_SendCTPassThru function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendCTPassThru
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# SM\_SendCTPassThru function


The SM\_SendCTPassThru WMI method sends a common transport (CT) pass-through command to the indicated port.

Syntax
------

```ManagedCPlusPlus
void SM_SendCTPassThru(
   [in, HBAType("HBA_WWN")] uint8              HbaPortWWN[8],
   [in] uint32                                 InRespBufferMaxSize,
   [in] uint32                                 RequestBufferSize,
   [in, WmiSizeIs("RequestBufferSize")] uint8  RequestBuffer,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS     HBAStatus,
   [out] uint32                                TotalResponseBufferSize,
   [out] uint32                                ActualResponseBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8 ResponseBuffer[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the HBA through which the target is accessed. This information is delivered to the miniport driver in the PortWWN member of a SendCTPassThru\_IN structure.

*InRespBufferMaxSize*   
The maximum size of the response buffer.

*RequestBufferSize*   
The size, in bytes, of the buffer that will hold the results of the common transport command. The miniport driver returns this information in the RequestBufferSize member of a SM\_SendCTPassThru\_IN structure.

*RequestBuffer*   
The results of the common transport command. The miniport driver returns this information in the RequestBuffer member of a SM\_SendCTPassThru\_IN structure.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SM\_SendCTPassThru\_OUT structure.

*TotalResponseBufferSize*   
The size, in bytes, of the results common transport command. The miniport driver returns this information in the TotalResponseBufferSize member of a SM\_SendCTPassThru\_OUT structure.

*ActualResponseBufferSize*   
The size, in bytes, of the data that was actually retrieved. The miniport driver returns this information in the ActualResponseBufferSize member of a SM\_SendCTPassThru\_OUT structure.

*ResponseBuffer*   
The results of the common transport command. The miniport driver returns this information in the ResponseBuffer member of a SM\_SendCTPassThru\_OUT structure.

Return value
------------

Not applicable to WMI methods.

Remarks
-------

This WMI method belongs to the MS\_SM\_FabricAndDomainManagementMethods WMI Class.

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
<td align="left">Hbapiwmi.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[HBA\_STATUS](hba-status.md)

[**SM\_SendCTPassThru\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff566293)

[**SM\_SendCTPassThru\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566294)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SM_SendCTPassThru%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





