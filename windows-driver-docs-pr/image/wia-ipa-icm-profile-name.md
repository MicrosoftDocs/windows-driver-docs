---
title: WIA\_IPA\_ICM\_PROFILE\_NAME
description: The WIA\_IPA\_ICM\_PROFILE\_NAME property contains the image color management (ICM) profile name that is needed to properly decode an image.
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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





