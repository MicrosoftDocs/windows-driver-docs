---
title: DeleteDevice rule (wdm)
description: The DeleteDevice rule specifies that drivers should not rely on the I/O Manager or PnP Manager to keep the DeviceObject alive after a call to IoDeleteDevice.
ms.assetid: C7068AD1-C9F4-4BB0-8964-24FFB4658AF6
keywords: ["DeleteDevice rule (wdm)"]
topic_type:
- apiref
api_name:
- DeleteDevice
api_type:
- NA
---

# DeleteDevice rule (wdm)


The **DeleteDevice** rule specifies that drivers should not rely on the I/O Manager or PnP Manager to keep the DeviceObject alive after a call to [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083).

Drivers should call [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) after the lower driver has returned. This is the recommended behavior. This rule applies to FDO and FIDO drivers.

When handling an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request, the driver should only call [**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083) after [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) have returned.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DeleteDevice</strong> rule.</p>
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

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





