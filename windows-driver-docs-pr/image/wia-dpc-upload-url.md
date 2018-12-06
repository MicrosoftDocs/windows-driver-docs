---
title: WIA\_DPC\_UPLOAD\_URL
description: The WIA\_DPC\_UPLOAD\_URL property describes a standard Internet URL.
ms.assetid: 5fc36640-32e3-4e51-845f-dabaecd39472
keywords: ["WIA_DPC_UPLOAD_URL Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_UPLOAD_URL
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_UPLOAD\_URL


The WIA\_DPC\_UPLOAD\_URL property describes a standard Internet URL.

## <span id="ddk_wia_dpc_upload_url_si"></span><span id="DDK_WIA_DPC_UPLOAD_URL_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/write

Remarks
-------

The WIA\_DPC\_UPLOAD\_URL property describes a URL that images or objects, after they are acquired from a device, can be uploaded to in one of the following scenarios:

-   A WIA application reads WIA\_DPC\_UPLOAD\_URL and allows a user to automatically upload images to the URL.

-   An application sets the URL, and other devices (for example, kiosks) use WIA\_DPC\_UPLOAD\_URL.

The Microsoft Windows operating system does not upload images.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





