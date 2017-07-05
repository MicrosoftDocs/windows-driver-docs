---
title: WSK Socket Options
description: WSK Socket Options
MS-HAID:
- 'wskref\_14c89334-aa7c-4030-bfdd-e789b43c33a3.xml'
- 'netvista.wsk\_socket\_options'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 640681a3-ea68-44c5-be2b-a3bc21bfdb7c
keywords: ["WSK Socket Options Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- WSK Socket Options
api_location:
- Ws2def.h
api_type:
- HeaderDef
---

# WSK Socket Options


The WSK subsystem supports the following socket options at the SOL\_SOCKET level:

[**SO\_BROADCAST**](https://msdn.microsoft.com/library/windows/hardware/ff570828)

[**SO\_CONDITIONAL\_ACCEPT**](https://msdn.microsoft.com/library/windows/hardware/ff570829)

[**SO\_EXCLUSIVEADDRUSE**](https://msdn.microsoft.com/library/windows/hardware/ff570830)

[**SO\_KEEPALIVE**](https://msdn.microsoft.com/library/windows/hardware/ff570831)

[**SO\_RCVBUF**](https://msdn.microsoft.com/library/windows/hardware/ff570832)

[**SO\_REUSEADDR**](https://msdn.microsoft.com/library/windows/hardware/ff570833)

[**SO\_WSK\_EVENT\_CALLBACK**](so-wsk-event-callback.md)

[**SO\_WSK\_SECURITY**](so-wsk-security.md)

The underlying network protocol might support additional socket options.

For more information about each of these socket options, as well as information about socket options at levels other than SOL\_SOCKET, see the "Windows Sockets 2" section of the Microsoft Windows SDK documentation.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ws2def.h (include Wsk.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20WSK%20Socket%20Options%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




