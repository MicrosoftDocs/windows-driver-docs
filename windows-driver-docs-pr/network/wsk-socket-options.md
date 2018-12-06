---
title: WSK Socket Options
description: WSK Socket Options
ms.assetid: 640681a3-ea68-44c5-be2b-a3bc21bfdb7c
ms.date: 07/18/2017
keywords:
 - WSK Socket Options Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




