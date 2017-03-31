---
title: C28751
description: Warning C28751 Banned usage of ExAllocatePool and its variants.
ms.assetid: A2FBEDA8-FA5D-42A5-B298-FF0A32B1662C
---

# C28751


warning C28751: Banned usage of ExAllocatePool and its variants

This warning indicates that a function is being used that has been banned, and has a more robust and secure replacement.

The kernel memory allocation functions ExAllocatePool and ExAllocatePoolWithQuota do not provide tags to assist in later debugging. There are replacements for these functions that you can use, which make debugging easier.

Replacement

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
<td align="left"><p><span id="ExAllocatePool"></span><span id="exallocatepool"></span><span id="EXALLOCATEPOOL"></span>ExAllocatePool</p></td>
<td align="left"><p>Secure replacement: [<strong>ExAllocatePoolWithTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544520)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="ExAllocatePoolWithQuota"></span><span id="exallocatepoolwithquota"></span><span id="EXALLOCATEPOOLWITHQUOTA"></span>ExAllocatePoolWithQuota</p></td>
<td align="left"><p>Secure replacement: [<strong>ExAllocatePoolWithQuotaTag</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544513) routine</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28751%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




