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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

## <span id="see_also"></span>See also


[**WIA\_IPA\_MIN\_BUFFER\_SIZE**](wia-ipa-min-buffer-size.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPA_BUFFER_SIZE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





