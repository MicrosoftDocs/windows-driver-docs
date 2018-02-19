---
title: BarcodeScannerDataReceived
description: BarcodeScannerDataReceived
ms.assetid: '3dd7699a-5e2b-484b-bd83-c37ee7f0e851'
---

# BarcodeScannerDataReceived


This event occurs after a successful scan event.

The scanned data is variable length and consists of the [PosBarcodeScannerDataReceivedEventData](https://msdn.microsoft.com/library/windows/hardware/dn772207) structure followed by **ScanDataLength** bytes of raw scan data followed by **ScanDataLabelLength** bytes of decoded scan data in which the header and footer information is removed, leaving only the scanner data. The data buffer for this event is as follows.

Syntax
------

``` syntax
typedef struct _PosBarcodeScannerDataReceivedEventData
{
    PosEventDataHeader Header;
    UINT32 DataType;
    UINT32 ScanDataLength;
    UINT32 ScanDataLabelLength;
} PosBarcodeScannerDataReceivedEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                            | Description                                                                                                                          |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000005<br/>                                   | **Header.EventType = PosEventType::BarcodeScannerDataReceived**<br/>                                                           |
| 0000020+Scan data length + label data length<br/> | **Header.DataLength** = sizeof(**PosBarcodeScannerDataReceivedEventData**) + **ScanDataLength** + **ScanDataLabelLength**<br/> |
| UINT32<br/>                                       | **PosBarcodeScannerDataReceivedEventData.DataType**<br/>                                                                       |
| UINT32<br/>                                       | **PosBarcodeScannerDataReceivedEventData.ScanDataLength**<br/>                                                                 |
| UINT32<br/>                                       | **PosBarcodeScannerDataReceivedEventData.ScanDataLabelLength**<br/>                                                            |
| byte \[\]<br/>                                    | **ScanDataLength** bytes of raw scan data<br/>                                                                                 |
| byte \[\]<br/>                                    | **ScanDataLabelLength** bytes of decoded scan data<br/>                                                                        |

 

Requirements
------------

**Header:** pointofservicedriverinterface.h

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20BarcodeScannerDataReceived%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





