---
title: WIA\_IPA\_FILENAME\_EXTENSION
description: The WIA\_IPA\_FILENAME\_EXTENSION property contains the file name extension for a particular file format. The WIA minidriver creates and maintains this property.
ms.assetid: 08abb3f2-73a2-42cd-ae69-1607eda63d1e
keywords: ["WIA_IPA_FILENAME_EXTENSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_FILENAME_EXTENSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_FILENAME\_EXTENSION


The WIA\_IPA\_FILENAME\_EXTENSION property contains the file name extension for a particular file format. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_filename_extension_si"></span><span id="DDK_WIA_IPA_FILENAME_EXTENSION_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The minidriver updates the WIA\_IPA\_FILENAME\_EXTENSION property to reflect the current value of the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) property.

For example, if WIA\_IPA\_FORMAT is WiaImgFmt\_JPEG, WIA\_IPA\_FILENAME\_EXTENSION should be "jpg". If WIA\_IPA\_FORMAT is WiaImgFmt\_BMP, WIA\_IPA\_FILENAME\_EXTENSION should be "bmp". Note that the file name extension does not include the period (".").

The WIA\_IPA\_FILENAME\_EXTENSION property is recommended for drivers that support standard formats and is required for drivers that implement custom-defined formats. WIA\_IPA\_FILENAME\_EXTENSION informs the application of the correct file name extension to use during the transfer of privately formatted files. For example, if the A. Datum Corporation created a WIA driver that transferred a file in a new format, the company could specify an extension of "adc". This extension enables applications to transfer data in that format to a file and to create a file name such as *Myfile.adc*, which is useful to others who understand the new extension.

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

## See also


[**WIA\_IPA\_FORMAT**](wia-ipa-format.md)

 

 






