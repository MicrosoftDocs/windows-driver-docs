---
title: GDI User Objects
description: GDI User Objects
keywords:
- GDI WDK Windows 2000 display , user objects
- graphics drivers WDK Windows 2000 display , user objects
- drawing WDK GDI , user objects
- user objects WDK GDI
ms.date: 04/20/2017
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
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-brushobj" data-raw-source="[&lt;strong&gt;BRUSHOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_brushobj)"><strong>BRUSHOBJ</strong></a></p></td>
<td align="left"><p>Defines the brush objects for graphic functions that output lines, text, or fills. Drivers can call <a href="/windows-hardware/drivers/#wdkgloss-brushobj" data-raw-source="&lt;em&gt;BRUSHOBJ&lt;/em&gt;"><em>BRUSHOBJ</em></a> services to realize brushes or to find realizations previously cached by GDI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-clipobj" data-raw-source="[&lt;strong&gt;CLIPOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_clipobj)"><strong>CLIPOBJ</strong></a></p></td>
<td align="left"><p>Provides the driver with access to a <a href="/windows-hardware/drivers/#wdkgloss-clip-region" data-raw-source="&lt;em&gt;clip region&lt;/em&gt;"><em>clip region</em></a> for drawing or filling. This region can be enumerated as a series of rectangles.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-floatobj" data-raw-source="[&lt;strong&gt;FLOATOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_floatobj)"><strong>FLOATOBJ</strong></a></p></td>
<td align="left"><p>Allows graphics drivers to emulate floating-point operations. Floating-point operations are disabled for all other kernel-mode drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-fontobj" data-raw-source="[&lt;strong&gt;FONTOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_fontobj)"><strong>FONTOBJ</strong></a></p></td>
<td align="left"><p>Gives the driver access to information about a particular instance (or realization) of a font.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-palobj" data-raw-source="[&lt;strong&gt;PALOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_palobj)"><strong>PALOBJ</strong></a></p></td>
<td align="left"><p>A structure containing RGB palette colors; accessible via the <a href="/windows/win32/api/winddi/nf-winddi-palobj_cgetcolors" data-raw-source="&lt;strong&gt;PALOBJ_cGetColors&lt;/strong&gt;"><em>PALOBJ</em></a> structure contains no public members.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-pathobj" data-raw-source="[&lt;strong&gt;PATHOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_pathobj)"><strong>PATHOBJ</strong></a></p></td>
<td align="left"><p>Defines a path that specifies what is to be drawn (lines or Bezier curves). A <a href="/windows-hardware/drivers/#wdkgloss-pathobj" data-raw-source="&lt;em&gt;PATHOBJ&lt;/em&gt;"><em>PATHOBJ</em></a> structure is passed to the driver to describe a set of lines and Bezier curves that are to be stroked or filled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-strobj" data-raw-source="[&lt;strong&gt;STROBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_strobj)"><strong>STROBJ</strong></a></p></td>
<td align="left"><p>Enumerates for the driver a list of glyph handles and positions that describe how a text string is to be drawn.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-surfobj" data-raw-source="[&lt;strong&gt;SURFOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_surfobj)"><strong>SURFOBJ</strong></a></p></td>
<td align="left"><p>Identifies a surface, which can be a GDI bitmap, a device-dependent bitmap, or a device-managed surface. See <a href="surface-types.md" data-raw-source="[Surface Types](surface-types.md)">Surface Types</a> for more information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff570618(v=vs.85)" data-raw-source="[&lt;strong&gt;XFORMOBJ&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff570618(v=vs.85))"><strong>XFORMOBJ</strong></a></p></td>
<td align="left"><p>Describes an arbitrary linear two-dimensional transform, such as for geometric wide lines.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/winddi/ns-winddi-xlateobj" data-raw-source="[&lt;strong&gt;XLATEOBJ&lt;/strong&gt;](/windows/win32/api/winddi/ns-winddi-_xlateobj)"><strong>XLATEOBJ</strong></a></p></td>
<td align="left"><p>Defines the translations needed to convert pixels from the source surface format to the destination surface format.</p></td>
</tr>
</tbody>
</table>

 

