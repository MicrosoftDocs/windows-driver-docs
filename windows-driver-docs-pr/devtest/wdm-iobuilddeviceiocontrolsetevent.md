---
title: IoBuildDeviceIoControlSetEvent rule (wdm)
description: The IoBuildDeviceIoControlSetEvent rule specifies that a driver that calls IoBuildDeviceIoControlRequest must not call KeSetEvent if the driver supplies a pointer to a caller-allocated and initialized event object.
ms.assetid: F9721484-3156-4AF5-8C60-AF68644E602D
ms.date: 05/21/2018
keywords: ["IoBuildDeviceIoControlSetEvent rule (wdm)"]
topic_type:
- apiref
api_name:
- IoBuildDeviceIoControlSetEvent
api_type:
- NA
ms.localizationpriority: medium
---

# IoBuildDeviceIoControlSetEvent rule (wdm)


The **IoBuildDeviceIoControlSetEvent** rule specifies that a driver that calls [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) must not call [**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253) if the driver supplies a pointer to a caller-allocated and initialized event object. The **KeSetEvent** does not need to be called by the driver for this IRP.

|              |     |
|--------------|-----|
| Driver model | WDM |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>IoBuildDeviceIoControlSetEvent</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
[**KeClearEvent**](https://msdn.microsoft.com/library/windows/hardware/ff551980)
[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)
[**KeSetEvent**](https://msdn.microsoft.com/library/windows/hardware/ff553253)
 

 





