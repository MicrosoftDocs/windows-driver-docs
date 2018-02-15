---
title: SM\_SendSRL function
description: The SM\_SendSRL WMI method sends a scan remote loop (SRL) command through the indicated port to the indicated domain controller.
ms.assetid: 44090e8d-ffb2-48a9-a574-5bf067ffa952
keywords: ["SM_SendSRL function Storage Devices"]
topic_type:
- apiref
api_name:
- SM_SendSRL
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
---

# SM\_SendSRL function


The SM\_SendSRL WMI method sends a scan remote loop (SRL) command through the indicated port to the indicated domain controller.

Syntax
------

```ManagedCPlusPlus
void SM_SendSRL(
   [in, HBAType("HBA_WWN")] uint8              HbaPortWWN[8],
   [in, HBAType("HBA_WWN")] uint8              WWN[8],
   [in] uint32                                 Domain,
   [in] uint32                                 InRespBufferMaxSize,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS     HBAStatus,
   [out] uint32                                TotalRespBufferSize,
   [out] uint32                                OutRespBufferSize,
   [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
);
```

Parameters
----------

*HbaPortWWN*   
A worldwide name (WWN) for the local port through which the SRL command is sent. This information is delivered to the miniport driver in the HbaPortWWN member of a SM\_SendSRL\_IN structure.

*WWN*   
A worldwide name (WWN) for the port of type FL\_Port whose loop is to be scanned. This information is delivered to the miniport driver in the WWN member of a SM\_SendSRL\_IN structure.

*Domain*   
The domain number for the domain whose loops are to be scanned. This information is delivered to the miniport driver in the Domain member of a SM\_SendSRL\_IN structure.

*InRespBufferMaxSize*   
The maximum size of the response buffer.

*HBAStatus*   
The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the HBAStatus member of a SendRPL\_OUT structure.

*TotalRespBufferSize*   
The size, in bytes, of the results of the RPS command. The miniport driver returns this information in the TotalRespBufferSize member of a SM\_SendRPS\_OUT structure.

*OutRespBufferSize*   
The size, in bytes, of the data that was actually retrieved. The miniport driver returns this information in the OutRespBufferSize member of a SM\_SendRPL\_OUT structure.

*RespBuffer*   
The results of the RPS command. The miniport driver returns this information in the RespBuffer member of a SM\_SendRPS\_OUT structure.

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

[**SM\_SendSRL\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff566326)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SM_SendSRL%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





