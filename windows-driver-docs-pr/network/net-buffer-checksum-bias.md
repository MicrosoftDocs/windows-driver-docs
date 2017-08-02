---
title: NET_BUFFER_CHECKSUM_BIAS macro
author: windows-driver-content
description: NET_BUFFER_CHECKSUM_BIAS is a macro that NDIS drivers use to get the ChecksumBias member of a NET_BUFFER structure.
ms.assetid: 8fd4aafc-c095-4026-8c6b-8f739e429285
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_CHECKSUM_BIAS macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_CHECKSUM\_BIAS macro


NET\_BUFFER\_CHECKSUM\_BIAS is a macro that NDIS drivers use to get the **ChecksumBias** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
USHORT NET_BUFFER_CHECKSUM_BIAS(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_CHECKSUM\_BIAS returns the value of the **ChecksumBias** member of the indicated NET\_BUFFER structure.

Remarks
-------

The return value specifies the number of bytes of data to skip over at the beginning of the data buffer when computing a checksum. This value is used by the TCP/IP protocol.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_CHECKSUM_BIAS%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


