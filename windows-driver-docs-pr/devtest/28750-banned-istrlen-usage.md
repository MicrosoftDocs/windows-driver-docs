---
title: C28750
description: Warning C28750 Banned usage of lstrlen and its variants.
ms.assetid: 5057FE71-286A-4710-922F-DFC639717C75
---

# C28750


warning C28750: Banned usage of lstrlen and its variants

This warning indicates that a function is being used that has been banned, and has better replacements.

The lstrlen function and related variations fail to transmit exceptions that occur during operation. This can cause error conditions to happen much later, potentially on a different thread, making the error conditions harder to diagnose. In addition, equivalent substitute functions can be optimized by the compiler, and avoid the performance overhead of exception handlers (**\_try** and **\_except** blocks).

The lstrlen function and its variants are banned because they fail to transmit exceptions. The correct mitigation is to convert them to another string length function (usually strlen, wcslen, \_tcslen). However, while you review the lstrlen changes, you should confirm that the string buffer is coming from trusted code. If you are dealing with untrusted data, you should instead switch from the strlen family of functions to the strnlen family (or StringCchLength family), which will ensure they don't go past the bounds of the untrusted data block.

Unlike lstrlen, none of the replacements catch exceptions. In addition, lstrlen allows NULL pointers, so if NULL pointers are possible at that point in the code, an explicit NULL check is required when replacing lstrlen with strlen or strnlen.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">API</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="lstrlen"></span><span id="LSTRLEN"></span>lstrlen</p></td>
<td align="left"><p>Trusted data replacement options: _tcslen</p>
<p>Untrusted data replacement: _tcsnlen, StringCchLength</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="lstrlenA"></span><span id="lstrlena"></span><span id="LSTRLENA"></span>lstrlenA</p></td>
<td align="left"><p>Trusted data replacement options: strlen</p>
<p>Untrusted data replacement: strnlen, StringCchLengthA</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="lstrlenW"></span><span id="lstrlenw"></span><span id="LSTRLENW"></span>lstrlenW</p></td>
<td align="left"><p>Trusted data replacement options: wcslen</p>
<p>Untrusted data replacement: wcsnlen, StringCchLengthW</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28750%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




