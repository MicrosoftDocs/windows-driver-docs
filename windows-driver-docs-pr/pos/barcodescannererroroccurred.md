---
title: BarcodeScannerErrorOccurred
description: BarcodeScannerErrorOccurred
ms.assetid: '38cfbd87-0526-49d1-8580-96f4e1adf7bb'
---

# BarcodeScannerErrorOccurred


This event occurs when there is an error, such as a scanning error.

The data buffer for this event is as follows.

Syntax
------

``` syntax
// Error occurred data should fill the ReadFile buffer in this order:
//    PosBarcodeScannerErrorOccurredEventData structure (length = sizeof(PosBarcodeScannerErrorOccurredEventData))
//    Error Message (length = MessageLength)
//    Scan Data (length = ScanDataLength)
//    Scan Data Label (length = ScanDataLabelLength)

typedef struct _PosBarcodeScannerErrorOccurredEventData
{
    PosEventDataHeader Header;
    LONG IsRetriable;
    UnifiedPosErrorSeverity Severity;
    UINT32 VendorErrorCode;
    UnifiedPosErrorReason Reason;
    UINT32 ExtendedReason;
    UINT32 MessageLength;
    PosBarcodeScannerDataReceivedEventData PartialData;
} PosBarcodeScannerErrorOccurredEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                      | Description                                                                                                                                        |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000006                             | **EventType = PosEventType:: BarcodeScannerTriggerPressed**                                                                             |
| UINT32                                 | **DataLength** = sizeof(**PosBarcodeScannerErrorOccurredData**) + **MessageLength** + **ScanDataLength** + **ScanDataLabelLength**)     |
| BOOL                                   | **IsRetriable**                                                                                                                         |
| 32-bit UnifiedPosErrorSeverity         | **Severity**                                                                                                                            |
| UINT32                                 | **VendorErrorCode**                                                                                                                     |
| 32-bit UnifiedPosErrorReason           | **Reason**                                                                                                                              |
| UINT32                                 | **ExtendedReason**                                                                                                                      |
| UINT32                                 | **MessageLength**                                                                                                                       |
| PosBarcodeScannerDataReceivedEventData | **PartialData**                                                                                                                         |
| UINT32                                 | **EventType** not specified                                                                                                             |
| UINT32                                 | **DataLength** = sizeof(**PosBarcodeScannerDataRecievedEventData**) + **MessageLength** + **ScanDataLength** + **ScanDataLabelLength**) |
| UINT32                                 | **DataType** not specified                                                                                                              |
| UINT32                                 | **ScanDataLength**                                                                                                                      |
| UINT32                                 | **ScanDataLabelLength**                                                                                                                 |
| byte \[\]                              | **MessageLength** bytes of message                                                                                                      |
| byte \[\]                              | **ScanDataLength** bytes of label data                                                                                                  |
| byte \[\]                              | **ScanDataLabelLength** bytes of scan data                                                                                              |



Remarks
-------

If a scanning error occurs, and some scan data was obtained, the event data contains the partial scan data.

Requirements
------------

**Header:** pointofservicedriverinterface.h





[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20BarcodeScannerErrorOccurred%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





