---
title: BarcodeScannerImagePreviewReceived
description: BarcodeScannerImagePreviewReceived
ms.assetid: 'ec05bffb-95e6-4d9c-b632-adee1cbd5bad'
---

# BarcodeScannerImagePreviewReceived


This event occurs when the device receives a bitmap image of the scan.

The data buffer for this event is as follows.

Syntax
------

``` syntax
typedef struct _PosEventDataHeader
{
    // Event enumeration value
    PosEventType EventType;

    // Size of buffer required to read entire event (including header)
    UINT32 DataLength;
} PosEventDataHeader;

typedef struct _PosEventDataHeader PosBarcodeScannerImagePreviewEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                 | Description                                                                                                 |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| 0x00000007<br/>                        | **EventType** = **PosEventType:: BarcodeScannerImagePreviewReceived**<br/>                            |
| 0x00000008 + length of image data<br/> | sizeof(**PosBarcodeScannerImagePreviewEventData**) + the size of the image preview data in bytes<br/> |
| Image data<br/>                        | The preview image data<br/>                                                                           |

 

Requirements
------------

**Header:** pointofservicedriverinterface.h

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20BarcodeScannerImagePreviewReceived%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





