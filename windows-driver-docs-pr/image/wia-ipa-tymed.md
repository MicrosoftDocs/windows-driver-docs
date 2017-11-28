---
title: WIA\_IPA\_TYMED
description: The WIA\_IPA\_TYMED property contains the method setting for image transfer . The WIA minidriver creates and maintains this property.
ms.assetid: 3490f4b8-a1ed-4ab3-b621-ed87ce8ae9ea
keywords: ["WIA_IPA_TYMED Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_TYMED
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPA\_TYMED


The WIA\_IPA\_TYMED property contains the method setting for image transfer . The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_tymed_si"></span><span id="DDK_WIA_IPA_TYMED_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_IPA\_TYMED property to determine the minidriver's method of data transfer.

The following table describes the constants that are valid with WIA\_IPA\_TYMED.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TYMED_CALLBACK</p></td>
<td><p>Transfer an image to memory, in bands.</p>
<p>This constant is obsolete for Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>TYMED_FILE</p></td>
<td><p>Transfer an image to a file.</p></td>
</tr>
<tr class="odd">
<td><p>TYMED_MULTIPAGE_CALLBACK</p></td>
<td><p>Transfer multiple images to memory, in bands.</p>
<p>This constant is obsolete for Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>TYMED_MULTIPAGE_FILE</p></td>
<td><p>Transfer multiple images to a file.</p></td>
</tr>
</tbody>
</table>

 

All WIA 2.0 minidrivers must set the initial value of this property to its default value, which is TYMED\_FILE.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_TYMED%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




