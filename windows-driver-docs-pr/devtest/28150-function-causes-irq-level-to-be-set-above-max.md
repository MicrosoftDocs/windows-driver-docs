---
title: C28150
description: Warning C28150 The function causes the IRQ Level to be set above the maximum acceptable for the function being analyzed.
ms.assetid: 7ad53801-fa7f-49c1-a1f0-715c9f4951d1
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28150


warning C28150: The function causes the IRQ Level to be set above the maximum acceptable for the function being analyzed

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>The level limits come from annotations on the current function.</p></td>
</tr>
</tbody>
</table>

 

The specified function has raised the IRQL above the maximum IRQL permitted for the current function call.

This warning occurs inside a function that has been annotated with the **\_\_drv\_maxIRQL** annotation and indicates either a coding error in the function or a misunderstanding of the function's contract in the annotations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28150%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




