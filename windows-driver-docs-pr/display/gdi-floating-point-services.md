---
title: GDI Floating-Point Services
description: GDI Floating-Point Services
ms.assetid: 7e32c683-ffad-4a95-9c3a-6716f7ce20cb
keywords:
- GDI WDK Windows 2000 display , floating-point operations
- graphics drivers WDK Windows 2000 display , floating-point operations
- drawing WDK GDI , floating-point operations
- floating-point operations WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>EngRestoreFloatingPointState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565006)</p></td>
<td align="left"><p>Restores the Windows 2000 and later kernel floating-point state after the driver uses any floating-point or MMX hardware instructions.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngSaveFloatingPointState</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565010)</p></td>
<td align="left"><p>Saves the current Windows 2000 and later kernel floating-point state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_Add</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565814)</p></td>
<td align="left"><p>Adds two FLOATOBJs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_AddFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565822)</p></td>
<td align="left"><p>Adds a FLOATOBJ and a FLOATL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_AddLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565826)</p></td>
<td align="left"><p>Adds a FLOATOBJ and a LONG.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_Div</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565835)</p></td>
<td align="left"><p>Divides one FLOATOBJ by another.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_DivFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565841)</p></td>
<td align="left"><p>Divides a FLOATOBJ by a FLOATL.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_DivLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565845)</p></td>
<td align="left"><p>Divides a FLOATOBJ by a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_Equal</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565861)</p></td>
<td align="left"><p>Determines whether two FLOATOBJs are equal.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_EqualLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565870)</p></td>
<td align="left"><p>Determines whether a FLOATOBJ and a LONG are equal.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_GetFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565871)</p></td>
<td align="left"><p>Calculate and return the FLOAT-equivalent value of a FLOATOBJ.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_GetLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565873)</p></td>
<td align="left"><p>Calculate and return the LONG-equivalent value of a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_GreaterThan</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565880)</p></td>
<td align="left"><p>Determines whether one FLOATOBJ is larger than another.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_GreaterThanLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565884)</p></td>
<td align="left"><p>Determines whether a FLOATOBJ is larger than a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_LessThan</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565894)</p></td>
<td align="left"><p>Determines whether one FLOATOBJ is less than another.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_LessThanLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565902)</p></td>
<td align="left"><p>Determines whether a FLOATOBJ is less than a LONG.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_Mul</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565908)</p></td>
<td align="left"><p>Multiplies two FLOATOBJ values.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_MulFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565914)</p></td>
<td align="left"><p>Multiplies a FLOATOBJ by a FLOATL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_MulLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565916)</p></td>
<td align="left"><p>Multiplies a FLOATOBJ by a LONG.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_Neg</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565919)</p></td>
<td align="left"><p>Changes the sign of a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_SetFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565922)</p></td>
<td align="left"><p>Sets a FLOATOBJ to a particular FLOATL value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_SetLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565928)</p></td>
<td align="left"><p>Sets a FLOATOBJ to a particular LONG value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_Sub</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565935)</p></td>
<td align="left"><p>Subtracts one FLOATOBJ from another.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>FLOATOBJ_SubFloat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565938)</p></td>
<td align="left"><p>Subtracts a FLOATL from a FLOATOBJ.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>FLOATOBJ_SubLong</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565941)</p></td>
<td align="left"><p>Subtracts a LONG from a FLOATOBJ.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Floating-Point%20Services%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




