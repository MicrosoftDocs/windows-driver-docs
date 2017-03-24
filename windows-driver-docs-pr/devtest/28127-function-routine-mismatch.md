---
title: C28127
description: Warning C28127 The function being used as a routine does not exactly match the type expected.
ms.assetid: ae8f554b-c1e1-42a7-b1ad-c5554af25953
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28127


warning C28127: The function being used as a routine does not exactly match the type expected.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Additional information</strong></p></td>
<td align="left"><p>It is likely that the difference is that the actual function returns a value, and the expected function type is void</p></td>
</tr>
</tbody>
</table>

 

The driver is passing or assigning a function (pointer) of an unexpected type (that is, function signature). This often occurs in C when the expected return type of a function is VOID and a function with an (implied) **int** return value is actually supplied. It can also happen when the parameters are compatible but not identical. In general, callback functions should match the expected type exactly, which is most easily accomplished using a function typedef.

This type mismatch message is designed primarily to verify that the Code Analysis tool can recognize callbacks.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28127%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




