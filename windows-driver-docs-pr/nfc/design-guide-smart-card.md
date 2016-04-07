---
title: Smart card design guide
author: windows-driver-content
description: Smart card design guide
ms.assetid: 721A1530-B7B4-4373-9006-356A0A601349
---

# Smart card design guide


The smart card DDI allows callers to the NFC device driver to perform low level smart card operations on NFC contactless smart cards. This includes listening on card arrival/departure notifications, reading meta-data of the smart card like ATR, UID and Historical Bytes information as well as performing read/write operations on the specific NFC card using APDUs. For non-ISO14443-4 compliant cards (known as storage cards), the translation of APDUs to low-level primitive commands supported by the storage card is documented in section 4.3.7. The IOCTLs make up the SMARTCARD device driver interface and all of them use FILE\_ANY\_ACCESS and METHOD\_BUFFERED. The smart card DDI below are the minimum subset of the Smart Card driver IOCTLs specified by Windows \[1\] to support accessing NFC contactless smart card.

``` syntax
GUID_DEVINTERFACE_SMARTCARD_READER
“{50DD5230-BA8A-11D1-BF5D-0000F805F530}”
```

## Unsupported IOCTLs


The following IOCTLs are not supported for NFC smart card operation because they aren't applicable for contactless smart card operation, so the driver might return an unsupported error code:

-   IOCTL\_SMARTCARD\_EJECT
-   IOCTL\_SMARTCARD\_GET\_LAST\_ERROR
-   IOCTL\_SMARTCARD\_SWALLOW

## In this section


-   [Functional flow](functional-flow.md)
-   [Example sequence](example-sequence.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Smart%20card%20design%20guide%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




