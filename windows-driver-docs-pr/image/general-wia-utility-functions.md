---
title: General WIA Utility Functions
description: General WIA Utility Functions
ms.date: 04/20/2017
---

# General WIA Utility Functions





You can use the following functions to retrieve the driver item context, retrieve information from the system registry, and copy a string.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetdrvitemcontext" data-raw-source="[&lt;strong&gt;wiauGetDrvItemContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetdrvitemcontext)"><strong>wiauGetDrvItemContext</strong></a></p></td>
<td><p>Gets the driver item context and, optionally, the driver item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetresourcestring" data-raw-source="[&lt;strong&gt;wiauGetResourceString&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetresourcestring)"><strong>wiauGetResourceString</strong></a></p></td>
<td><p>Gets a resource string, storing it as a <strong>BSTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetvalidformats" data-raw-source="[&lt;strong&gt;wiauGetValidFormats&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetvalidformats)"><strong>wiauGetValidFormats</strong></a></p></td>
<td><p>Calls the <a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetWiaFormatInfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo)"><strong>IWiaMiniDrv::drvGetWiaFormatInfo</strong></a> method and makes a list of valid formats, using a specified TYMED value.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaupropinpropspec" data-raw-source="[&lt;strong&gt;wiauPropInPropSpec&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaupropinpropspec)"><strong>wiauPropInPropSpec</strong></a></p></td>
<td><p>Determines whether a specified property specification identifier (ID) is contained in an array of such values. The function optionally gets the index where the property specification ID was found.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaupropsinpropspec" data-raw-source="[&lt;strong&gt;wiauPropsInPropSpec&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaupropsinpropspec)"><strong>wiauPropsInPropSpec</strong></a></p></td>
<td><p>Determines whether any of a list of property specification IDs is contained within an array of such values.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaureggetdwordw" data-raw-source="[&lt;strong&gt;wiauRegGetDword&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaureggetdwordw)"><strong>wiauRegGetDword</strong></a></p></td>
<td><p>Gets a <strong>DWORD</strong> value from the <strong>DeviceData</strong> section of the registry.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaureggetstrw" data-raw-source="[&lt;strong&gt;wiauRegGetStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaureggetstrw)"><strong>wiauRegGetStr</strong></a></p></td>
<td><p>Gets a string value from the <strong>DeviceData</strong> section of the registry.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiauregopendataw" data-raw-source="[&lt;strong&gt;wiauRegOpenData&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiauregopendataw)"><strong>wiauRegOpenData</strong></a></p></td>
<td><p>Opens the <strong>DeviceData</strong> registry key.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiausetimageitemsize" data-raw-source="[&lt;strong&gt;wiauSetImageItemSize&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiausetimageitemsize)"><strong>wiauSetImageItemSize</strong></a></p></td>
<td><p>Calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (defined in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrc2c" data-raw-source="[&lt;strong&gt;wiauStrC2C&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrc2c)"><strong>wiauStrC2C</strong></a></p></td>
<td><p>Copies an ANSI character string to another ANSI character string.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrc2w" data-raw-source="[&lt;strong&gt;wiauStrC2W&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrc2w)"><strong>wiauStrC2W</strong></a></p></td>
<td><p>Converts an ANSI character string to a Unicode string.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrw2c" data-raw-source="[&lt;strong&gt;wiauStrW2C&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrw2c)"><strong>wiauStrW2C</strong></a></p></td>
<td><p>Converts a Unicode string to an ANSI character string.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrw2w" data-raw-source="[&lt;strong&gt;wiauStrW2W&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrw2w)"><strong>wiauStrW2W</strong></a></p></td>
<td><p>Copies a Unicode string to another Unicode string.</p></td>
</tr>
</tbody>
</table>

 

