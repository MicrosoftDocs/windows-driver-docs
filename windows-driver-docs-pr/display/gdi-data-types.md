---
title: GDI Data Types
description: GDI Data Types
ms.assetid: 2054aa16-6d86-4db3-8b16-4570b0374e23
keywords:
- GDI WDK Windows 2000 display , data types
- graphics drivers WDK Windows 2000 display , data types
- drawing WDK GDI , data types
- data types WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Data Types


## <span id="ddk_gdi_data_types_gg"></span><span id="DDK_GDI_DATA_TYPES_GG"></span>


The data types defined in the following table appear in the device driver interface. Several of the listed data types have already been described in [GDI User Objects](gdi-user-objects.md). Data types that are pointers are marked with an asterisk (\*).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Graphics DDI Data Type</th>
<th align="left">Variable Name Prefix</th>
<th align="left">Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>BOOL</p></td>
<td align="left"><p>b</p></td>
<td align="left"><p>A 32-bit value that can be either <strong>TRUE</strong> or <strong>FALSE</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>BYTE</p></td>
<td align="left"><p>j</p></td>
<td align="left"><p>An 8-bit unsigned integer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>BRUSHOBJ<em></p></td>
<td align="left"><p>pbo</p></td>
<td align="left"><p>A pointer to a brush object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CLIPLINE</p></td>
<td align="left"><p>cl</p></td>
<td align="left"><p>A clipline object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CLIPOBJ</em></p></td>
<td align="left"><p>pco</p></td>
<td align="left"><p>A pointer to a clipping object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DHPDEV</p></td>
<td align="left"><p>dhpdev</p></td>
<td align="left"><p>A 32-bit handle, defined by the device driver, that identifies a physical device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DHSURF</p></td>
<td align="left"><p>dhsurf</p></td>
<td align="left"><p>A 32-bit handle, defined by the device driver, that identifies a device-managed surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FIX</p></td>
<td align="left"><p>fix</p></td>
<td align="left"><p>A fixed-point number.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FLOATL</p></td>
<td align="left"><p>e</p></td>
<td align="left"><p>A floating-point number.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FLOAT_LONG</p></td>
<td align="left"><p>el</p></td>
<td align="left"><p>A 32-bit overloaded value that is interpreted as either a LONG or FLOATL, depending on context.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FLONG</p></td>
<td align="left"><p>fl</p></td>
<td align="left"><p>A set of 32-bit flags.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FONTOBJ<em></p></td>
<td align="left"><p>pfo</p></td>
<td align="left"><p>A pointer to a font object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FSHORT</p></td>
<td align="left"><p>fs</p></td>
<td align="left"><p>A set of 16-bit flags.</p></td>
</tr>
<tr class="even">
<td align="left"><p>FWORD</p></td>
<td align="left"><p>fw</p></td>
<td align="left"><p>A 16-bit signed integer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HBM</p></td>
<td align="left"><p>hbm</p></td>
<td align="left"><p>A 32-bit handle, defined by GDI, that identifies a bitmap.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HPAL</p></td>
<td align="left"><p>hpal</p></td>
<td align="left"><p>A 32-bit handle, defined by GDI, that identifies a palette.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HSURF</p></td>
<td align="left"><p>hsurf</p></td>
<td align="left"><p>A 32-bit handle, defined by GDI, that identifies a surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LONG</p></td>
<td align="left"><p>l</p></td>
<td align="left"><p>A 32-bit signed integer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MIX</p></td>
<td align="left"><p>mix</p></td>
<td align="left"><p>A 32-bit quantity, whose lower 16 bits define foreground and background mix modes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PALOBJ</em></p></td>
<td align="left"><p>ppalo</p></td>
<td align="left"><p>A pointer to a palette object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PATHOBJ<em></p></td>
<td align="left"><p>ppo</p></td>
<td align="left"><p>A pointer to a path object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>POINTE</p></td>
<td align="left"><p>pte</p></td>
<td align="left"><p>A point structure that consists of {FLOATL <strong>x</strong>, <strong>y</strong>;}.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>POINTFIX</p></td>
<td align="left"><p>ptfx</p></td>
<td align="left"><p>A point structure that consists of {FIX <strong>x</strong>, <strong>y</strong>;}.</p></td>
</tr>
<tr class="even">
<td align="left"><p>POINTQF</p></td>
<td align="left"><p>ptq</p></td>
<td align="left"><p>A point structure that consists of {LARGE_INTEGER <strong>x</strong>, <strong>y</strong>;}. Each member of this structure is a 64-bit coordinate in 28.36 format.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PWSZ</p></td>
<td align="left"><p>pwsz</p></td>
<td align="left"><p>A pointer to a null-terminated Unicode string.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PVOID</p></td>
<td align="left"><p>pv</p></td>
<td align="left"><p>A pointer to a VOID, an undefined data type.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RECTFX</p></td>
<td align="left"><p>rcfx</p></td>
<td align="left"><p>A rectangle structure that consists of {FIX <strong>xLeft</strong>, <strong>yTop</strong>, <strong>xRight</strong>, <strong>yBottom</strong>;}.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ROP4</p></td>
<td align="left"><p>rop4</p></td>
<td align="left"><p>A 32-bit value that specifies how source, destination, pattern, and mask pixels are to be mixed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SHORT</p></td>
<td align="left"><p>s</p></td>
<td align="left"><p>A 16-bit signed integer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SIZEL</p></td>
<td align="left"><p>sizl</p></td>
<td align="left"><p>A structure that consists of {LONG <strong>cx</strong>, <strong>cy</strong>;}.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STROBJ</em></p></td>
<td align="left"><p>pstro</p></td>
<td align="left"><p>A pointer to a text string object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SURFOBJ<em></p></td>
<td align="left"><p>pso</p></td>
<td align="left"><p>A pointer to a surface object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ULONG</p></td>
<td align="left"><p>ul</p></td>
<td align="left"><p>A 32-bit unsigned integer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>USHORT</p></td>
<td align="left"><p>us</p></td>
<td align="left"><p>A 16-bit unsigned integer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>XFORMOBJ</em></p></td>
<td align="left"><p>pxo</p></td>
<td align="left"><p>A pointer to a coordinate transform object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>XLATEOBJ*</p></td>
<td align="left"><p>pxlo</p></td>
<td align="left"><p>A pointer to a color translation object.</p></td>
</tr>
</tbody>
</table>

 

The parameter prefixes listed in the next table are used to modify variable name prefixes in accordance with their usage.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Prefix</th>
<th align="left">Parameter Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>i</p></td>
<td align="left"><p>An enumerated index</p></td>
</tr>
<tr class="even">
<td align="left"><p>c</p></td>
<td align="left"><p>A count</p></td>
</tr>
<tr class="odd">
<td align="left"><p>p</p></td>
<td align="left"><p>A pointer</p></td>
</tr>
</tbody>
</table>

 

 

 





