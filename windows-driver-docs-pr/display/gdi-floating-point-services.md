---
title: GDI Floating-Point Services
description: GDI Floating-Point Services
ms.assetid: 7e32c683-ffad-4a95-9c3a-6716f7ce20cb
keywords:
- GDI WDK Windows 2000 display , floating-point operations
- graphics drivers WDK Windows 2000 display , floating-point operations
- drawing WDK GDI , floating-point operations
- floating-point operations WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Floating-Point Services


## <span id="ddk_gdi_floating_point_services_gg"></span><span id="DDK_GDI_FLOATING_POINT_SERVICES_GG"></span>


Kernel-mode graphics drivers must do all floating-point operations between calls to the GDI-supplied [**EngSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565010) and [**EngRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565006) routines.

If the hardware has a floating-point processor, the driver can do floating-point operations directly. Otherwise, the driver can use the GDI [**FLOATOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff565804) services shown in the following table to emulate floating-point operations. Regardless of processor type, the driver should use the FLOATL data type when declaring floating-point values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565006" data-raw-source="[&lt;strong&gt;EngRestoreFloatingPointState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565006)"><strong>EngRestoreFloatingPointState</strong></a></p></td>
<td align="left"><p>Restores the Windows 2000 and later kernel floating-point state after the driver uses any floating-point or MMX hardware instructions.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565010" data-raw-source="[&lt;strong&gt;EngSaveFloatingPointState&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565010)"><strong>EngSaveFloatingPointState</strong></a></p></td>
<td align="left"><p>Saves the current Windows 2000 and later kernel floating-point state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565814" data-raw-source="[&lt;strong&gt;FLOATOBJ_Add&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565814)"><strong>FLOATOBJ_Add</strong></a></p></td>
<td align="left"><p>Adds two FLOATOBJs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565822" data-raw-source="[&lt;strong&gt;FLOATOBJ_AddFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565822)"><strong>FLOATOBJ_AddFloat</strong></a></p></td>
<td align="left"><p>Adds a FLOATOBJ and a FLOATL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565826" data-raw-source="[&lt;strong&gt;FLOATOBJ_AddLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565826)"><strong>FLOATOBJ_AddLong</strong></a></p></td>
<td align="left"><p>Adds a FLOATOBJ and a LONG.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565835" data-raw-source="[&lt;strong&gt;FLOATOBJ_Div&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565835)"><strong>FLOATOBJ_Div</strong></a></p></td>
<td align="left"><p>Divides one FLOATOBJ by another.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565841" data-raw-source="[&lt;strong&gt;FLOATOBJ_DivFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565841)"><strong>FLOATOBJ_DivFloat</strong></a></p></td>
<td align="left"><p>Divides a FLOATOBJ by a FLOATL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565845" data-raw-source="[&lt;strong&gt;FLOATOBJ_DivLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565845)"><strong>FLOATOBJ_DivLong</strong></a></p></td>
<td align="left"><p>Divides a FLOATOBJ by a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565861" data-raw-source="[&lt;strong&gt;FLOATOBJ_Equal&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565861)"><strong>FLOATOBJ_Equal</strong></a></p></td>
<td align="left"><p>Determines whether two FLOATOBJs are equal.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565870" data-raw-source="[&lt;strong&gt;FLOATOBJ_EqualLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565870)"><strong>FLOATOBJ_EqualLong</strong></a></p></td>
<td align="left"><p>Determines whether a FLOATOBJ and a LONG are equal.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565871" data-raw-source="[&lt;strong&gt;FLOATOBJ_GetFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565871)"><strong>FLOATOBJ_GetFloat</strong></a></p></td>
<td align="left"><p>Calculate and return the FLOAT-equivalent value of a FLOATOBJ.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565873" data-raw-source="[&lt;strong&gt;FLOATOBJ_GetLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565873)"><strong>FLOATOBJ_GetLong</strong></a></p></td>
<td align="left"><p>Calculate and return the LONG-equivalent value of a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565880" data-raw-source="[&lt;strong&gt;FLOATOBJ_GreaterThan&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565880)"><strong>FLOATOBJ_GreaterThan</strong></a></p></td>
<td align="left"><p>Determines whether one FLOATOBJ is larger than another.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565884" data-raw-source="[&lt;strong&gt;FLOATOBJ_GreaterThanLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565884)"><strong>FLOATOBJ_GreaterThanLong</strong></a></p></td>
<td align="left"><p>Determines whether a FLOATOBJ is larger than a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565894" data-raw-source="[&lt;strong&gt;FLOATOBJ_LessThan&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565894)"><strong>FLOATOBJ_LessThan</strong></a></p></td>
<td align="left"><p>Determines whether one FLOATOBJ is less than another.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565902" data-raw-source="[&lt;strong&gt;FLOATOBJ_LessThanLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565902)"><strong>FLOATOBJ_LessThanLong</strong></a></p></td>
<td align="left"><p>Determines whether a FLOATOBJ is less than a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565908" data-raw-source="[&lt;strong&gt;FLOATOBJ_Mul&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565908)"><strong>FLOATOBJ_Mul</strong></a></p></td>
<td align="left"><p>Multiplies two FLOATOBJ values.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565914" data-raw-source="[&lt;strong&gt;FLOATOBJ_MulFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565914)"><strong>FLOATOBJ_MulFloat</strong></a></p></td>
<td align="left"><p>Multiplies a FLOATOBJ by a FLOATL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565916" data-raw-source="[&lt;strong&gt;FLOATOBJ_MulLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565916)"><strong>FLOATOBJ_MulLong</strong></a></p></td>
<td align="left"><p>Multiplies a FLOATOBJ by a LONG.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565919" data-raw-source="[&lt;strong&gt;FLOATOBJ_Neg&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565919)"><strong>FLOATOBJ_Neg</strong></a></p></td>
<td align="left"><p>Changes the sign of a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565922" data-raw-source="[&lt;strong&gt;FLOATOBJ_SetFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565922)"><strong>FLOATOBJ_SetFloat</strong></a></p></td>
<td align="left"><p>Sets a FLOATOBJ to a particular FLOATL value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565928" data-raw-source="[&lt;strong&gt;FLOATOBJ_SetLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565928)"><strong>FLOATOBJ_SetLong</strong></a></p></td>
<td align="left"><p>Sets a FLOATOBJ to a particular LONG value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565935" data-raw-source="[&lt;strong&gt;FLOATOBJ_Sub&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565935)"><strong>FLOATOBJ_Sub</strong></a></p></td>
<td align="left"><p>Subtracts one FLOATOBJ from another.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565938" data-raw-source="[&lt;strong&gt;FLOATOBJ_SubFloat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565938)"><strong>FLOATOBJ_SubFloat</strong></a></p></td>
<td align="left"><p>Subtracts a FLOATL from a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565941" data-raw-source="[&lt;strong&gt;FLOATOBJ_SubLong&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565941)"><strong>FLOATOBJ_SubLong</strong></a></p></td>
<td align="left"><p>Subtracts a LONG from a FLOATOBJ.</p></td>
</tr>
</tbody>
</table>

 

 

 





