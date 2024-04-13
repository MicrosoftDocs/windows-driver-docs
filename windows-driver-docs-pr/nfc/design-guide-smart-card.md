---
title: Smart Card Design Guide
description: Smart card design guide
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Smart card design guide

The smart card DDI allows callers to the NFC device driver to perform low level smart card operations on NFC contactless smart cards. This includes listening on card arrival/departure notifications, reading meta-data of the smart card like ATR, UID and Historical Bytes information as well as performing read/write operations on the specific NFC card using APDUs. For non-ISO14443-4 compliant cards (known as storage cards), the translation of APDUs to low-level primitive commands supported by the storage card is documented in section 4.3.7. The IOCTLs make up the SMARTCARD device driver interface and all of them use FILE_ANY_ACCESS and METHOD_BUFFERED. The smart card DDI below are the minimum subset of the Smart Card driver IOCTLs specified by Windows \[1\] to support accessing NFC contactless smart card.

``` syntax
GUID_DEVINTERFACE_SMARTCARD_READER
"{50DD5230-BA8A-11D1-BF5D-0000F805F530}"
```

## Unsupported IOCTLs

The following IOCTLs are not supported for NFC smart card operation because they aren't applicable for contactless smart card operation, so the driver might return an unsupported error code:

- IOCTL_SMARTCARD_EJECT
- IOCTL_SMARTCARD_GET_LAST_ERROR
- IOCTL_SMARTCARD_SWALLOW

## Smart card attributes

The Windows smart card DDI includes IOCTL requests for Get and Set attributes. In order to meet the minimum requirement to support NFC contactless reader, we only support the GET_ATTRIBUTE for the minimum set of Reader and ICC State. For more information, see [Supported smart card attributes](smart-card-attributes.md).

## In this section

- [Functional flow](functional-flow.md)
- [Example sequence](example-sequence.md)
- [Storage card requirements](storage-card-requirements.md)
- [Supported smart card attributes](smart-card-attributes.md)
- [PC/SC interface](pc-sc-interface.md)

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [Smart card DDI and command reference](/previous-versions/dn905601(v=vs.85))
