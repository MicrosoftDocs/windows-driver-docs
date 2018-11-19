---
title: What Does the Zw Prefix Mean
description: What Does the Zw Prefix Mean
ms.assetid: 9529cce9-9c46-4906-854d-d0aef9118a90
ms.localizationpriority: medium
ms.date: 10/17/2018
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff541921" data-raw-source="[&lt;strong&gt;CmRegisterCallbackEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541921)"><strong>CmRegisterCallbackEx</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Ex</strong></p></td>
<td><p>Executive</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544501" data-raw-source="[&lt;strong&gt;ExAllocatePool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544501)"><strong>ExAllocatePool</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Hal</strong></p></td>
<td><p>Hardware abstraction layer</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff546596" data-raw-source="[&lt;strong&gt;HalGetAdapter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546596)"><strong>HalGetAdapter</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Io</strong></p></td>
<td><p>I/O manager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548257" data-raw-source="[&lt;strong&gt;IoAllocateIrp&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548257)"><strong>IoAllocateIrp</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Ke</strong></p></td>
<td><p>Kernel core</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553253" data-raw-source="[&lt;strong&gt;KeSetEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553253)"><strong>KeSetEvent</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Mm</strong></p></td>
<td><p>Memory manager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556381" data-raw-source="[&lt;strong&gt;MmUnlockPages&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556381)"><strong>MmUnlockPages</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Ob</strong></p></td>
<td><p>Object manager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff558678" data-raw-source="[&lt;strong&gt;ObReferenceObject&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff558678)"><strong>ObReferenceObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Po</strong></p></td>
<td><p>Power manager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559765" data-raw-source="[&lt;strong&gt;PoSetPowerState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559765)"><strong>PoSetPowerState</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Tm</strong></p></td>
<td><p>Transaction manager</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564665" data-raw-source="[&lt;strong&gt;TmCommitTransaction&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564665)"><strong>TmCommitTransaction</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Nt</strong> and <strong>Zw</strong></p></td>
<td><p>Native system services</p></td>
<td><p><a href="http://go.microsoft.com/fwlink/p/?linkid=157250" data-raw-source="[NtCreateFile](http://go.microsoft.com/fwlink/p/?linkid=157250)">NtCreateFile</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424" data-raw-source="[&lt;strong&gt;ZwCreateFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566424)"><strong>ZwCreateFile</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 




