---
title: GDI User Objects
description: GDI User Objects
ms.assetid: 25048f14-a46e-49bb-8890-699bf1324007
keywords:
- GDI WDK Windows 2000 display , user objects
- graphics drivers WDK Windows 2000 display , user objects
- drawing WDK GDI , user objects
- user objects WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI User Objects


## <span id="ddk_gdi_user_objects_gg"></span><span id="DDK_GDI_USER_OBJECTS_GG"></span>


GDI maintains important internal data structures, but gives the driver access to the public fields of these structures by passing them down as *user objects*. User objects are intermediate data structures that provide an interface between GDI data structures and the drivers that need access to the information within these structures. The driver can pass the pointer to a user object back to GDI to query for information or to ask for various services. User objects with public fields provide the following advantages:

-   They eliminate problems associated with direct access to internal GDI data structures.

-   They provide a place to hold GDI data for the driver. For example, a PATHOBJ structure can hold all the extra data required to enumerate a complex object like a path.

The following user objects are available:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538261" data-raw-source="[&lt;strong&gt;BRUSHOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538261)"><strong>BRUSHOBJ</strong></a></p></td>
<td align="left"><p>Defines the brush objects for graphic functions that output lines, text, or fills. Drivers can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-brushobj" data-raw-source="[&lt;em&gt;BRUSHOBJ&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-brushobj)"><em>BRUSHOBJ</em></a> services to realize brushes or to find realizations previously cached by GDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff539417" data-raw-source="[&lt;strong&gt;CLIPOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff539417)"><strong>CLIPOBJ</strong></a></p></td>
<td align="left"><p>Provides the driver with access to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region" data-raw-source="[&lt;em&gt;clip region&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-clip-region)"><em>clip region</em></a> for drawing or filling. This region can be enumerated as a series of rectangles.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565804" data-raw-source="[&lt;strong&gt;FLOATOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565804)"><strong>FLOATOBJ</strong></a></p></td>
<td align="left"><p>Allows graphics drivers to emulate floating-point operations. Floating-point operations are disabled for all other kernel-mode drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565974" data-raw-source="[&lt;strong&gt;FONTOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565974)"><strong>FONTOBJ</strong></a></p></td>
<td align="left"><p>Gives the driver access to information about a particular instance (or realization) of a font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568844" data-raw-source="[&lt;strong&gt;PALOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568844)"><strong>PALOBJ</strong></a></p></td>
<td align="left"><p>A structure containing RGB palette colors; accessible via the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568845" data-raw-source="[&lt;strong&gt;PALOBJ_cGetColors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568845)"><strong>PALOBJ_cGetColors</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff556282" data-raw-source="[&lt;strong&gt;DrvSetPalette&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556282)"><strong>DrvSetPalette</strong></a> functions. The <a href="https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palobj" data-raw-source="[&lt;em&gt;PALOBJ&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-palobj)"><em>PALOBJ</em></a> structure contains no public members.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff568849" data-raw-source="[&lt;strong&gt;PATHOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568849)"><strong>PATHOBJ</strong></a></p></td>
<td align="left"><p>Defines a path that specifies what is to be drawn (lines or Bezier curves). A <a href="https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pathobj" data-raw-source="[&lt;em&gt;PATHOBJ&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pathobj)"><em>PATHOBJ</em></a> structure is passed to the driver to describe a set of lines and Bezier curves that are to be stroked or filled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569738" data-raw-source="[&lt;strong&gt;STROBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569738)"><strong>STROBJ</strong></a></p></td>
<td align="left"><p>Enumerates for the driver a list of glyph handles and positions that describe how a text string is to be drawn.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff569901" data-raw-source="[&lt;strong&gt;SURFOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569901)"><strong>SURFOBJ</strong></a></p></td>
<td align="left"><p>Identifies a surface, which can be a GDI bitmap, a device-dependent bitmap, or a device-managed surface. See <a href="surface-types.md" data-raw-source="[Surface Types](surface-types.md)">Surface Types</a> for more information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570618" data-raw-source="[&lt;strong&gt;XFORMOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570618)"><strong>XFORMOBJ</strong></a></p></td>
<td align="left"><p>Describes an arbitrary linear two-dimensional transform, such as for geometric wide lines.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570634" data-raw-source="[&lt;strong&gt;XLATEOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570634)"><strong>XLATEOBJ</strong></a></p></td>
<td align="left"><p>Defines the translations needed to convert pixels from the source surface format to the destination surface format.</p></td>
</tr>
</tbody>
</table>

 

 

 





