---
title: WIA\_IPA\_FILENAME\_EXTENSION
description: The WIA\_IPA\_FILENAME\_EXTENSION property contains the file name extension for a particular file format. The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_f7d80007-2973-4ce5-b4e9-a5f831326321.xml'
- 'image.wia\_ipa\_filename\_extension'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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

## <span id="see_also"></span>See also


[**WIA\_IPA\_FORMAT**](wia-ipa-format.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_FILENAME_EXTENSION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





