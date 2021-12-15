---
title: GDI Floating-Point Services
description: GDI Floating-Point Services
keywords:
- GDI WDK Windows 2000 display , floating-point operations
- graphics drivers WDK Windows 2000 display , floating-point operations
- drawing WDK GDI , floating-point operations
- floating-point operations WDK GDI
ms.date: 04/20/2017
---

# GDI Floating-Point Services


## <span id="ddk_gdi_floating_point_services_gg"></span><span id="DDK_GDI_FLOATING_POINT_SERVICES_GG"></span>


Kernel-mode graphics drivers must do all floating-point operations between calls to the GDI-supplied [**EngSaveFloatingPointState**](/windows/win32/api/winddi/nf-winddi-engsavefloatingpointstate) and [**EngRestoreFloatingPointState**](/windows/win32/api/winddi/nf-winddi-engrestorefloatingpointstate) routines.

If the hardware has a floating-point processor, the driver can do floating-point operations directly. Otherwise, the driver can use the GDI [**FLOATOBJ**](/windows/win32/api/winddi/ns-winddi-floatobj) services shown in the following table to emulate floating-point operations. Regardless of processor type, the driver should use the FLOATL data type when declaring floating-point values.

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
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engrestorefloatingpointstate" data-raw-source="[&lt;strong&gt;EngRestoreFloatingPointState&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engrestorefloatingpointstate)"><strong>EngRestoreFloatingPointState</strong></a></p></td>
<td align="left"><p>Restores the Windows 2000 and later kernel floating-point state after the driver uses any floating-point or MMX hardware instructions.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-engsavefloatingpointstate" data-raw-source="[&lt;strong&gt;EngSaveFloatingPointState&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-engsavefloatingpointstate)"><strong>EngSaveFloatingPointState</strong></a></p></td>
<td align="left"><p>Saves the current Windows 2000 and later kernel floating-point state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_add" data-raw-source="[&lt;strong&gt;FLOATOBJ_Add&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_add)"><strong>FLOATOBJ_Add</strong></a></p></td>
<td align="left"><p>Adds two FLOATOBJs.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_addfloat" data-raw-source="[&lt;strong&gt;FLOATOBJ_AddFloat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_addfloat)"><strong>FLOATOBJ_AddFloat</strong></a></p></td>
<td align="left"><p>Adds a FLOATOBJ and a FLOATL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_addlong" data-raw-source="[&lt;strong&gt;FLOATOBJ_AddLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_addlong)"><strong>FLOATOBJ_AddLong</strong></a></p></td>
<td align="left"><p>Adds a FLOATOBJ and a LONG.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_div" data-raw-source="[&lt;strong&gt;FLOATOBJ_Div&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_div)"><strong>FLOATOBJ_Div</strong></a></p></td>
<td align="left"><p>Divides one FLOATOBJ by another.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_divfloat" data-raw-source="[&lt;strong&gt;FLOATOBJ_DivFloat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_divfloat)"><strong>FLOATOBJ_DivFloat</strong></a></p></td>
<td align="left"><p>Divides a FLOATOBJ by a FLOATL.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_divlong" data-raw-source="[&lt;strong&gt;FLOATOBJ_DivLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_divlong)"><strong>FLOATOBJ_DivLong</strong></a></p></td>
<td align="left"><p>Divides a FLOATOBJ by a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_equal" data-raw-source="[&lt;strong&gt;FLOATOBJ_Equal&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_equal)"><strong>FLOATOBJ_Equal</strong></a></p></td>
<td align="left"><p>Determines whether two FLOATOBJs are equal.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_equallong" data-raw-source="[&lt;strong&gt;FLOATOBJ_EqualLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_equallong)"><strong>FLOATOBJ_EqualLong</strong></a></p></td>
<td align="left"><p>Determines whether a FLOATOBJ and a LONG are equal.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_getfloat" data-raw-source="[&lt;strong&gt;FLOATOBJ_GetFloat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_getfloat)"><strong>FLOATOBJ_GetFloat</strong></a></p></td>
<td align="left"><p>Calculate and return the FLOAT-equivalent value of a FLOATOBJ.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_getlong" data-raw-source="[&lt;strong&gt;FLOATOBJ_GetLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_getlong)"><strong>FLOATOBJ_GetLong</strong></a></p></td>
<td align="left"><p>Calculate and return the LONG-equivalent value of a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_greaterthan" data-raw-source="[&lt;strong&gt;FLOATOBJ_GreaterThan&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_greaterthan)"><strong>FLOATOBJ_GreaterThan</strong></a></p></td>
<td align="left"><p>Determines whether one FLOATOBJ is larger than another.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_greaterthanlong" data-raw-source="[&lt;strong&gt;FLOATOBJ_GreaterThanLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_greaterthanlong)"><strong>FLOATOBJ_GreaterThanLong</strong></a></p></td>
<td align="left"><p>Determines whether a FLOATOBJ is larger than a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_lessthan" data-raw-source="[&lt;strong&gt;FLOATOBJ_LessThan&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_lessthan)"><strong>FLOATOBJ_LessThan</strong></a></p></td>
<td align="left"><p>Determines whether one FLOATOBJ is less than another.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_lessthanlong" data-raw-source="[&lt;strong&gt;FLOATOBJ_LessThanLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_lessthanlong)"><strong>FLOATOBJ_LessThanLong</strong></a></p></td>
<td align="left"><p>Determines whether a FLOATOBJ is less than a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_mul" data-raw-source="[&lt;strong&gt;FLOATOBJ_Mul&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_mul)"><strong>FLOATOBJ_Mul</strong></a></p></td>
<td align="left"><p>Multiplies two FLOATOBJ values.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_mulfloat" data-raw-source="[&lt;strong&gt;FLOATOBJ_MulFloat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_mulfloat)"><strong>FLOATOBJ_MulFloat</strong></a></p></td>
<td align="left"><p>Multiplies a FLOATOBJ by a FLOATL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_mullong" data-raw-source="[&lt;strong&gt;FLOATOBJ_MulLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_mullong)"><strong>FLOATOBJ_MulLong</strong></a></p></td>
<td align="left"><p>Multiplies a FLOATOBJ by a LONG.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_neg" data-raw-source="[&lt;strong&gt;FLOATOBJ_Neg&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_neg)"><strong>FLOATOBJ_Neg</strong></a></p></td>
<td align="left"><p>Changes the sign of a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_setfloat" data-raw-source="[&lt;strong&gt;FLOATOBJ_SetFloat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_setfloat)"><strong>FLOATOBJ_SetFloat</strong></a></p></td>
<td align="left"><p>Sets a FLOATOBJ to a particular FLOATL value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_setlong" data-raw-source="[&lt;strong&gt;FLOATOBJ_SetLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_setlong)"><strong>FLOATOBJ_SetLong</strong></a></p></td>
<td align="left"><p>Sets a FLOATOBJ to a particular LONG value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_sub" data-raw-source="[&lt;strong&gt;FLOATOBJ_Sub&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_sub)"><strong>FLOATOBJ_Sub</strong></a></p></td>
<td align="left"><p>Subtracts one FLOATOBJ from another.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_subfloat" data-raw-source="[&lt;strong&gt;FLOATOBJ_SubFloat&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_subfloat)"><strong>FLOATOBJ_SubFloat</strong></a></p></td>
<td align="left"><p>Subtracts a FLOATL from a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/nf-winddi-floatobj_sublong" data-raw-source="[&lt;strong&gt;FLOATOBJ_SubLong&lt;/strong&gt;](/windows/win32/api/winddi/nf-winddi-floatobj_sublong)"><strong>FLOATOBJ_SubLong</strong></a></p></td>
<td align="left"><p>Subtracts a LONG from a FLOATOBJ.</p></td>
</tr>
</tbody>
</table>

 

