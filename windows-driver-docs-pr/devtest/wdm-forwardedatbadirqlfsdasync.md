---
title: ForwardedAtBadIrqlFsdAsync rule (wdm)
description: The ForwardedAtBadIrqlFsdAsync rule specifies that the driver call IoCallDriver and PoCallDriver at IRQL DISPATCH\_LEVEL, unless the IRP major function code being forwarded is one of the following IRP\_MJ\_POWERIRP\_MJ\_READIRP\_MJ\_WRITEIRP\_MJ\_DEVICE\_CONTROLIRP\_MJ\_INTERNAL\_DEVICE\_CONTROL.
ms.assetid: 9961AE5F-0B36-4E04-A349-CA0461B3E3DC
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["ForwardedAtBadIrqlFsdAsync rule (wdm)"]
topic_type:
- apiref
api_name:
- ForwardedAtBadIrqlFsdAsync
api_type:
- NA
---

# ForwardedAtBadIrqlFsdAsync rule (wdm)


The **ForwardedAtBadIrqlFsdAsync** rule specifies that the driver call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) and [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) at IRQL&lt;DISPATCH\_LEVEL, unless the IRP major function code being forwarded is one of the following:

-   [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784)
-   [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794)
-   [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819)
-   [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)
-   [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766)

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>ForwardedAtBadIrqlFsdAsync</strong> rule.</p>
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

[**IoBuildAsynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548310)
[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





