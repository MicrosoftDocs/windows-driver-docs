---
title: What Does the Zw Prefix Mean
author: windows-driver-content
description: What Does the Zw Prefix Mean
ms.assetid: 9529cce9-9c46-4906-854d-d0aef9118a90
---

# What Does the Zw Prefix Mean?


The Windows native system services routines have names that begin with the prefixes **Nt** and **Zw**. The **Nt** prefix is an abbreviation of Windows NT, but the **Zw** prefix has no meaning. **Zw** was selected partly to avoid potential naming conflicts with other APIs, and partly to avoid using any potentially useful two-letter prefixes that might be needed in the future.

Many of the [Windows driver support routines](https://msdn.microsoft.com/library/windows/hardware/ff544200) have names that begin with two- or three-letter prefixes. These prefixes indicate which kernel-mode system components implement the routines. The following table contains some examples.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Prefix</th>
<th>Kernel component</th>
<th>Example routine</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Cm</strong></p></td>
<td><p>Configuration manager</p></td>
<td><p>[<strong>CmRegisterCallbackEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541921)</p></td>
</tr>
<tr class="even">
<td><p><strong>Ex</strong></p></td>
<td><p>Executive</p></td>
<td><p>[<strong>ExAllocatePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544501)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Hal</strong></p></td>
<td><p>Hardware abstraction layer</p></td>
<td><p>[<strong>HalGetAdapter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546596)</p></td>
</tr>
<tr class="even">
<td><p><strong>Io</strong></p></td>
<td><p>I/O manager</p></td>
<td><p>[<strong>IoAllocateIrp</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548257)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Ke</strong></p></td>
<td><p>Kernel core</p></td>
<td><p>[<strong>KeSetEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553253)</p></td>
</tr>
<tr class="even">
<td><p><strong>Mm</strong></p></td>
<td><p>Memory manager</p></td>
<td><p>[<strong>MmUnlockPages</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556381)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Ob</strong></p></td>
<td><p>Object manager</p></td>
<td><p>[<strong>ObReferenceObject</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558678)</p></td>
</tr>
<tr class="even">
<td><p><strong>Po</strong></p></td>
<td><p>Power manager</p></td>
<td><p>[<strong>PoSetPowerState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559765)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Tm</strong></p></td>
<td><p>Transaction manager</p></td>
<td><p>[<strong>TmCommitTransaction</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564665)</p></td>
</tr>
<tr class="even">
<td><p><strong>Nt</strong> and <strong>Zw</strong></p></td>
<td><p>Native system services</p></td>
<td><p>[NtCreateFile](http://go.microsoft.com/fwlink/p/?linkid=157250) and [<strong>ZwCreateFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566424)</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20What%20Does%20the%20Zw%20Prefix%20Mean?%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


