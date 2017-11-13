---
title: WIA\_IPA\_ICM\_PROFILE\_NAME
description: The WIA\_IPA\_ICM\_PROFILE\_NAME property contains the image color management (ICM) profile name that is needed to properly decode an image.
MS-HAID:
- 'WIA\_PropTable\_2a011d22-29a1-4634-b902-8f772ee8cafd.xml'
- 'image.wia\_ipa\_icm\_profile\_name'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bf4874d9-1f08-4aec-8ee3-2a6a11d63956
keywords: ["WIA_IPA_ICM_PROFILE_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_ICM_PROFILE_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPA\_ICM\_PROFILE\_NAME


The WIA\_IPA\_ICM\_PROFILE\_NAME property contains the image color management (ICM) profile name that is needed to properly decode an image.

## <span id="ddk_wia_ipa_icm_profile_name_si"></span><span id="DDK_WIA_IPA_ICM_PROFILE_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_IPA\_ICM\_PROFILE\_NAME property to determine the ICM profile to use when processing the image. The WIA service creates and maintains this property based on the ICMProfiles entry in the driver installation file.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_ICM_PROFILE_NAME%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




