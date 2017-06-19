---
title: Windows kernel run-time library obsolete routines
author: windows-driver-content
description: Windows kernel run-time library obsolete routines
ms.assetid: cd9aa441-a7f2-42b1-8319-611bf53c995d
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
<td><p>For better performance, use the [<strong>RtlLongMult</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451490) routine if the result will fit into a 32-bit signed integer. Otherwise, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="even">
<td><strong>RtlEnlargedUnsignedDivide</strong></td>
<td><p>For better performance, use the compiler support for 64-bit integer operations.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlEnlargedUnsignedMultiply</strong></td>
<td><p>For better performance, use the [<strong>RtlULongMult</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451490) routine if the result will fit into a 32-bit unsigned integer. Otherwise, use the compiler support for 64-bit integer operations.</p></td>
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
<td><p>Fills a caller-supplied buffer with the given unsigned character. Use [<strong>RtlFillMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561870) instead.</p></td>
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
<td><p>Fills a block of memory with zeros, given a pointer to the block and the length, in bytes, to be filled. For better performance, use [<strong>RtlZeroMemory</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563610).</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**RtlFillMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561870)  
[**RtlLongMult**](https://msdn.microsoft.com/library/windows/hardware/hh451490)  
[**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20kernel%20run-time%20library%20obsolete%20routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


