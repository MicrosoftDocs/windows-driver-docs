---
title: WIA\_IPS\_CUR\_INTENT
description: The WIA\_IPS\_CUR\_INTENT property contains the current settings for an application's intended use of an image. The WIA minidriver creates and maintains this property.
ms.assetid: 9fa732bb-9281-441e-91b5-ce6eec67ea8f
keywords: ["WIA_IPS_CUR_INTENT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_CUR_INTENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_CUR\_INTENT


The WIA\_IPS\_CUR\_INTENT property contains the current settings for an application's intended use of an image. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_cur_intent_si"></span><span id="DDK_WIA_IPS_CUR_INTENT_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_FLAG

Access Rights: Read/write

Remarks
-------

A driver uses the intent settings to pre-set item properties based on an application's intended use of an image. These properties might include, for example, maximum quality and minimum size.

The following table contains the image-type flags and their definitions. These flags are used to set which type of image is intended: color, grayscale, and so on.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Image type flags</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_INTENT_IMAGE_TYPE_COLOR</p></td>
<td><p>The application intends to prepare the device for a color scan.</p></td>
</tr>
<tr class="even">
<td><p>WIA_INTENT_IMAGE_TYPE_GRAYSCALE</p></td>
<td><p>The application intends to prepare the device for a grayscale scan.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_INTENT_IMAGE_TYPE_TEXT</p></td>
<td><p>The application intends to prepare the device for scanning text.</p></td>
</tr>
<tr class="even">
<td><p>WIA_INTENT_IMAGE_TYPE_MASK</p></td>
<td><p>This flag is a mask for all of the image-type flags.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_INTENT_NONE</p></td>
<td><p>Default value. No intent is specified.</p></td>
</tr>
</tbody>
</table>

 

The following table contains the image size and quality flags and their definitions. These flags are used to set the size and quality of an image scan.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Image size/quality Flags</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_INTENT_BEST_PREVIEW</p></td>
<td><p>The application intends to prepare the device for scanning a preview.</p></td>
</tr>
<tr class="even">
<td><p>WIA_INTENT_MAXIMIZE_QUALITY</p></td>
<td><p>The application intends to prepare the device for scanning a high-quality image.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_INTENT_MINIMIZE_SIZE</p></td>
<td><p>The application intends to prepare the device for scanning an image that results in a small scan.</p></td>
</tr>
<tr class="even">
<td><p>WIA_INTENT_SIZE_MASK</p></td>
<td><p>This flag is a mask for all of the size and quality flags.</p></td>
</tr>
</tbody>
</table>

 

The driver chooses the bit depth, in dots per inch, and other settings that it determines are appropriate for the selected intent. The application must read the current settings to determine which properties were changed.

An application sets the WIA\_IPS\_CUR\_INTENT property to auto-set the WIA properties for specific acquisition intent. Note that flags can be combined with a bitwise OR operator, but an image cannot be both grayscale and color.

WIA\_IPS\_CUR\_INTENT is required for all image acquisition enabled items; it is not available for storage items or stored image items.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





