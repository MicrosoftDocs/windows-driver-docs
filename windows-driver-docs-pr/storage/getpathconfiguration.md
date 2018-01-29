---
title: GetPathConfiguration function
description: The GetPathConfiguration method is used to retrieve the device information for each path.
ms.assetid: 1661746f-5a5a-48af-b876-c57f19de4923
keywords: ["GetPathConfiguration function Storage Devices"]
topic_type:
- apiref
api_name:
- GetPathConfiguration
api_location:
- MPIOwmi.h
api_type:
- HeaderDef
---

# GetPathConfiguration function


The GetPathConfiguration method is used to retrieve the device information for each path.

Syntax
------

```ManagedCPlusPlus
void GetPathConfiguration(
   [in, Description("64-bit Path Identifier"):amended] uint64 PathID,
   [out] uint32                                               EntryCount,
   [out, WmiSizeIs("EntryCount")] SCSI_ADDR                   Address[]
);
```

Parameters
----------

*PathID*   
A 64-bitfield that specifies the path that is associated with the device.

*EntryCount*   
A 32-bitfield that indicates the number of entries that the output contains.

*Address\[\]*   
An array that contains as many SCSI\_ADDR structures as specified by the *EntryCount* parameter.

Return value
------------

None

Remarks
-------

This WMI method belongs to the MPIO\_WMI\_METHODS WMI class.

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
<td align="left">MPIOwmi.h (include MPIOwmi.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20GetPathConfiguration%20function%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




