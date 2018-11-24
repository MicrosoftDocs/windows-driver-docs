---
title: WIA\_IPA\_MIN\_BUFFER\_SIZE
description: The WIA\_IPA\_MIN\_BUFFER\_SIZE property specifies the minimum buffer size that is used in data transfers.
ms.assetid: 0d289645-666c-4b67-8971-cdeff3caef3e
keywords: ["WIA_IPA_MIN_BUFFER_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_MIN_BUFFER_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_MIN\_BUFFER\_SIZE


The WIA\_IPA\_MIN\_BUFFER\_SIZE property specifies the minimum buffer size that is used in data transfers.

## <span id="ddk_wia_ipa_min_buffer_size_si"></span><span id="DDK_WIA_IPA_MIN_BUFFER_SIZE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

If a data transfer is performed through a callback mechanism, the WIA\_IPA\_MIN\_BUFFER\_SIZE property value can be as small as 64 KB. However, if the transfer is to file, the property value is the number of bytes that are needed to transfer one page of data at a time. The WIA minidriver creates and maintains this WIA property.

WIA\_IPA\_MIN\_BUFFER\_SIZE is identical to the [**WIA\_IPA\_BUFFER\_SIZE**](wia-ipa-buffer-size.md) property.

An application can read WIA\_IPA\_MIN\_BUFFER\_SIZE to determine the driver-specified buffer size for data transfers. The WIA service also reads this property to allocate memory for the minidriver during the data transfer.

**Note**   The value that the WIA\_IPA\_MIN\_BUFFER\_SIZE property contains is the minimum amount of data that an application can request at any given time. The larger the buffer size, the larger the requests to the device will be. This larger buffer size can make the device appear slow and unresponsive, can slow the overall computer performance, and can consume excessive resources. Buffer sizes that are too small can slow performance of the data transfer by requiring many smaller requests. Choose a reasonable buffer size by considering the typical size of a data request to your device, the number of requests, and the size of those requests.

 

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
<td><p>Optional for Windows Vista drivers for all transfer-enabled items. If this property is implemented, applications written for Windows Server 2003, Windows XP, and previous Windows versions can estimate the transfer buffer size, and, therefore, the transfer rate will be optimal.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPA\_BUFFER\_SIZE**](wia-ipa-buffer-size.md)

 

 






