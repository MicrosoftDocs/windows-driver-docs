---
title: What Does the Zw Prefix Mean
description: What Does the Zw Prefix Mean
ms.date: 10/17/2018
---

# What Does the Zw Prefix Mean?


The Windows native system services routines have names that begin with the prefixes **Nt** and **Zw**. The **Nt** prefix is an abbreviation of Windows NT, but the **Zw** prefix has no meaning. **Zw** was selected partly to avoid potential naming conflicts with other APIs, and partly to avoid using any potentially useful two-letter prefixes that might be needed in the future.

Many of the Windows driver support routines have names that begin with two- or three-letter prefixes. These prefixes indicate which kernel-mode system components implement the routines. The following table contains some examples.

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
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex" data-raw-source="[&lt;strong&gt;CmRegisterCallbackEx&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex)"><strong>CmRegisterCallbackEx</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Ex</strong></p></td>
<td><p>Executive</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool" data-raw-source="[&lt;strong&gt;ExAllocatePool&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool)"><strong>ExAllocatePool</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Hal</strong></p></td>
<td><p>Hardware abstraction layer</p></td>
<td><p><a href="/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)" data-raw-source="[&lt;strong&gt;HalGetAdapter&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85))"><strong>HalGetAdapter</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Io</strong></p></td>
<td><p>I/O manager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp" data-raw-source="[&lt;strong&gt;IoAllocateIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)"><strong>IoAllocateIrp</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Ke</strong></p></td>
<td><p>Kernel core</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent" data-raw-source="[&lt;strong&gt;KeSetEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesetevent)"><strong>KeSetEvent</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Mm</strong></p></td>
<td><p>Memory manager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpages" data-raw-source="[&lt;strong&gt;MmUnlockPages&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpages)"><strong>MmUnlockPages</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Ob</strong></p></td>
<td><p>Object manager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject" data-raw-source="[&lt;strong&gt;ObReferenceObject&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject)"><strong>ObReferenceObject</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Po</strong></p></td>
<td><p>Power manager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-posetpowerstate" data-raw-source="[&lt;strong&gt;PoSetPowerState&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-posetpowerstate)"><strong>PoSetPowerState</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>Tm</strong></p></td>
<td><p>Transaction manager</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-tmcommittransaction" data-raw-source="[&lt;strong&gt;TmCommitTransaction&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-tmcommittransaction)"><strong>TmCommitTransaction</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>Nt</strong> and <strong>Zw</strong></p></td>
<td><p>Native system services</p></td>
<td><p><a href="/windows/win32/api/winternl/nf-winternl-ntcreatefile" data-raw-source="[NtCreateFile](/windows/win32/api/winternl/nf-winternl-ntcreatefile)">NtCreateFile</a> and <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile" data-raw-source="[&lt;strong&gt;ZwCreateFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile)"><strong>ZwCreateFile</strong></a></p></td>
</tr>
</tbody>
</table>

