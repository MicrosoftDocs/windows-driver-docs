---
title: WIA_IPA_MIN_BUFFER_SIZE
description: The WIA_IPA_MIN_BUFFER_SIZE property specifies the minimum buffer size that is used in data transfers.
keywords: ["WIA_IPA_MIN_BUFFER_SIZE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_MIN_BUFFER_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
---

# WIA_IPA_MIN_BUFFER_SIZE

The WIA_IPA_MIN_BUFFER_SIZE property specifies the minimum buffer size that is used in data transfers.

Property Type: VT_I4

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

If a data transfer is performed through a callback mechanism, the WIA_IPA_MIN_BUFFER_SIZE property value can be as small as 64 KB. However, if the transfer is to file, the property value is the number of bytes that are needed to transfer one page of data at a time. The WIA minidriver creates and maintains this WIA property.

WIA_IPA_MIN_BUFFER_SIZE is identical to the [**WIA_IPA_BUFFER_SIZE**](wia-ipa-buffer-size.md) property.

An application can read WIA_IPA_MIN_BUFFER_SIZE to determine the driver-specified buffer size for data transfers. The WIA service also reads this property to allocate memory for the minidriver during the data transfer.

> [!NOTE]
> The value that the WIA_IPA_MIN_BUFFER_SIZE property contains is the minimum amount of data that an application can request at any given time. The larger the buffer size, the larger the requests to the device will be. This larger buffer size can make the device appear slow and unresponsive, can slow the overall computer performance, and can consume excessive resources. Buffer sizes that are too small can slow performance of the data transfer by requiring many smaller requests. Choose a reasonable buffer size by considering the typical size of a data request to your device, the number of requests, and the size of those requests.

## Requirements

**Version:** Optional for Windows Vista drivers for all transfer-enabled items. If this property is implemented, applications written for Windows Server 2003, Windows XP, and previous Windows versions can estimate the transfer buffer size, and, therefore, the transfer rate will be optimal.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_BUFFER_SIZE**](wia-ipa-buffer-size.md)
