---
title: SendRNID function
description: The SendRNID WMI method sends a request node identification data (RNID) command to the indicated port.
ms.assetid: 70c9655c-aaa8-45bb-ae5b-7428d9cdd4b2
keywords: ["SendRNID function Storage Devices"]
topic_type:
- apiref
api_name:
- SendRNID
api_location:
- Hbaapi.lib
- Hbaapi.dll
api_type:
- LibDef
---

# SendRNID function


The **SendRNID** WMI method sends a request node identification data (RNID) command to the indicated port.

Syntax
------

```ManagedCPlusPlus
void SendRNID(
   [in, HBAType("HBA_WWN")] uint8                                                          wwn[8],
   [in, HBAType("HBA_WWNTYPE"), Values{"NODE_WWN", "PORT_WWN"}, ValueMap{"0", "1"}] uint32 wwntype,
   [out, HBA_STATUS_QUALIFIERS] HBA_STATUS                                                 HBAStatus,
   [out] uint32                                                                            ResponseBufferCount,
   [out, WmiSizeIs("ResponseBufferCount")] uint8                                           ResponseBuffer[]
);
```

Parameters
----------

*wwn*   
A worldwide name for the port to which the RNID command is sent. This information is delivered to the miniport driver in the **wwn** member of a [**SendRNID\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565485) structure.

*wwntype*   
Deprecated. Do not use.

*HBAStatus*   
On return, contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](hba-status.md). The miniport driver returns this information in the **HBAStatus** member of a [**SendRNID\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565486) structure.

*ResponseBufferCount*   
The size in bytes of the results of the RNID command. The miniport driver returns this information in the **ResponseBufferCount** member of a [**SendRNID\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565486) structure.

*ResponseBuffer*   
The results of the RNID command. The miniport driver returns this information in the **ResponseBuffer** member of a [**SendRNID\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565486) structure.

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

[**SendRNID\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff565485)

[**SendRNID\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff565486)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SendRNID%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





