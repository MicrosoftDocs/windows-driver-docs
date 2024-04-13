---
title: Windows Kernel Run-Time Library Obsolete Routines
description: Windows kernel run-time library obsolete routines
ms.date: 10/17/2018
---

# Windows kernel run-time library obsolete routines


The following run-time library obsolete routines are exported to support existing driver binaries:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Obsolete routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RtlEnlargedIntegerMultiply</strong></td>
<td><p>For better performance, use the <a href="/windows-hardware/drivers/ddi/ntintsafe/nf-ntintsafe-rtlulongmult" data-raw-source="[&lt;strong&gt;RtlLongMult&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntintsafe/nf-ntintsafe-rtlulongmult)"><strong>RtlLongMult</strong></a> routine if the result will fit into a 32-bit signed integer. Otherwise, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlEnlargedUnsignedDivide</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlEnlargedUnsignedMultiply</strong></td>
<td><p>For better performance, use the <a href="/windows-hardware/drivers/ddi/ntintsafe/nf-ntintsafe-rtlulongmult" data-raw-source="[&lt;strong&gt;RtlULongMult&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntintsafe/nf-ntintsafe-rtlulongmult)"><strong>RtlULongMult</strong></a> routine if the result will fit into a 32-bit unsigned integer. Otherwise, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlExtendedIntegerMultiply</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlExtendedLargeIntegerDivide</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlExtendedMagicDivide</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlFillBytes</strong></td>
<td><p>Fills a caller-supplied buffer with the given unsigned character. Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory" data-raw-source="[&lt;strong&gt;RtlFillMemory&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory)"><strong>RtlFillMemory</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerAdd</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerAnd</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerArithmeticShift</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerDivide</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerEqualTo</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerEqualToZero</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerGreaterOrEqualToZero</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerGreaterThan</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerGreaterThanOrEqualTo</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerGreaterThanZero</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerLessOrEqualToZero</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerLessThan</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerLessThanOrEqualTo</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerLessThanZero</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerNegate</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerNotEqualTo</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerNotEqualToZero</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerShiftLeft</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlLargeIntegerShiftRight</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlLargeIntegerSubtract</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlZeroBytes</strong></td>
<td><p>Fills a block of memory with zeros, given a pointer to the block and the length, in bytes, to be filled. For better performance, use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory" data-raw-source="[&lt;strong&gt;RtlZeroMemory&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory)"><strong>RtlZeroMemory</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**RtlFillMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlfillmemory)  
[**RtlLongMult**](/windows-hardware/drivers/ddi/ntintsafe/nf-ntintsafe-rtlulongmult)  
[**RtlZeroMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlzeromemory)
