---
title: WIA\_IPA\_BUFFER\_SIZE
description: The WIA\_IPA\_BUFFER\_SIZE property contains the size of the buffer, in bytes, that is used during a data transfer. The WIA minidriver creates and maintains this property.
ms.assetid: 2feb26fa-674d-4dc2-b8bb-51942cb48737
keywords: ["WIA_IPA_BUFFER_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_BUFFER_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_BUFFER\_SIZE


The WIA\_IPA\_BUFFER\_SIZE property contains the size of the buffer, in bytes, that is used during a data transfer. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_buffer_size_si"></span><span id="DDK_WIA_IPA_BUFFER_SIZE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA\_IPA\_BUFFER\_SIZE property is identical to the [**WIA\_IPA\_MIN\_BUFFER\_SIZE**](wia-ipa-min-buffer-size.md) property.

An application can read WIA\_IPA\_BUFFER\_SIZE to determine the driver-specified buffer size for data transfers. The WIA service also reads this property to allocate memory for the minidriver during the data transfer.

**Note**   The value that the WIA\_IPA\_BUFFER\_SIZE property contains is the minimum amount of data that an application can request at any given time. The larger the buffer size, the larger the requests to the device will be. This larger buffer size can make the device seem slow and unresponsive, can slow the overall computer performance, and can consume excessive resources. Buffer sizes that are too small can slow performance of the data transfer by requiring many smaller requests. Choose a reasonable buffer size by considering the typical size of a data request to your device, the number of requests, and the size of those requests.

 

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
<td><p>Optional for Windows Vista drivers for all transfer-enabled items. If you implement this property, applications that are designed for Windows Server 2003, Windows XP, and previous versions of Windows can estimate the transfer buffer size and, therefore, the transfer rate will be optimal.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPA\_MIN\_BUFFER\_SIZE**](wia-ipa-min-buffer-size.md)

 

 






