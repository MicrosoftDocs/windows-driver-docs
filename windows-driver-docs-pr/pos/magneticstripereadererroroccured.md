---
title: MagneticStripeReaderErrorOccured
description: MagneticStripeReaderErrorOccured
ms.assetid: 'c2402411-1bbf-44c1-bf7f-813f6d967822'
---

# MagneticStripeReaderErrorOccured


This event occurs when there is a magnetic stripe reader (MSR) error, such as a scanning error.

Syntax
------

``` syntax
typedef struct _MSR_ERROR_EVENT
{
    PosEventDataHeader Header;
    MsrTrackErrorType Track1Status;
    MsrTrackErrorType Track2Status;
    MsrTrackErrorType Track3Status;
    MsrTrackErrorType Track4Status;
    UnifiedPosErrorSeverity Severity;
    UnifiedPosErrorReason Reason;
    UINT32 ExtendedReason;
    MSR_DATA_RECEIVED CardData;
    wchar_t Message[MSR_ERROR_MAX_MESSAGE_LENGTH];
} MSR_ERROR_EVENT, *PMSR_ERROR_EVENT;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                                                   | Description                                                                                                                               |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000009                                                          | **EventType = PosEventType:: MagneticStripeReaderErrorOccurred**                                                               |
| UINT32                                                              | **DataLength** = sizeof(**PosEventDataHeader**) + sizeof(**MSR\_ERROR\_EVENT**)                                                |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)                   | **Track1Status**                                                                                                               |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)                   | **Track2Status**                                                                                                               |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)                   | **Track3Status**                                                                                                               |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)                   | **Track4Status**                                                                                                               |
| 32-bit [UnifiedPosErrorSeverity](https://msdn.microsoft.com/library/windows/hardware/dn790053)       | **Severity**                                                                                                                   |
| 32-bit [UnifiedPosErrorReason](https://msdn.microsoft.com/library/windows/hardware/dn790050)           | **Reason**                                                                                                                     |
| UINT32                                                              | **Extended Reason**                                                                                                            |
| 32-bit [MsrCardType](https://msdn.microsoft.com/library/windows/hardware/dn772167)                               | **CardType**                                                                                                                   |
| unsigned char                                                       | **Track1EncryptedDataLength**                                                                                                  |
| unsigned char                                                       | **Track2EncryptedDataLength**                                                                                                  |
| unsigned char                                                       | **Track3EncryptedDataLength**                                                                                                  |
| unsigned char                                                       | **Track4EncryptedDataLength**                                                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track1EncryptedDataLength** bytes of encrypted track 1 data                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track2EncryptedDataLength** bytes of encrypted track 2 data                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track3EncryptedDataLength** bytes of encrypted track 3 data                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track4EncryptedDataLength** bytes of encrypted track 4 data                                                                  |
| unsigned char                                                       | **Track1MaskedDataLength**                                                                                                     |
| unsigned char                                                       | **Track2MaskedDataLength**                                                                                                     |
| unsigned char                                                       | **Track3MaskedDataLength**                                                                                                     |
| unsigned char                                                       | **Track4MaskedDataLength**                                                                                                     |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track1MaskedDataLength** bytes of masked track 1 data                                                                        |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track2MaskedDataLength** bytes of masked track 2 data                                                                        |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track3MaskedDataLength** bytes of masked track 3 data                                                                        |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track4MaskedDataLength** bytes of masked track 4 data                                                                        |
| unsigned char                                                       | **Track1DiscretionaryDataLength**                                                                                              |
| unsigned char                                                       | **Track2DiscretionaryDataLength**                                                                                              |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track1DiscretionaryDataLength** bytes of discretionary track 1 data                                                          |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track2DiscretionaryDataLength** bytes of discretionary track 2 data                                                          |
| unsigned char                                                       | **CardAuthenicationDataLength** - length of the data after encryption, including padding                                       |
| unsigned char                                                       | **CardAuthenticationDataAbsoluteLength** - length of data before encryption (may be needed to strip padding during decryption) |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_DATA\_SIZE\] | **CardAuthenticationDataAbsoluteLength** bytes of card authentication data                                                     |
| unsigned char                                                       | **AdditionalSecurityInformationLength**                                                                                        |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_SIZE\]       | **AdditionalSecurityInformationLength** bytes of additional security information                                               |
| wchar\_T \[MSR\_ERROR\_MAX\_MESSAGE\_LENGTH\]                       | Up to **MSR\_ERROR\_MAX\_MESSAGE\_LENGTH** wchar\_t of error **Null**-terminated message text                                  |



Remarks
-------

If a scanning error occurs, and some scan data was obtained, the event data contains the partial scan data.

Requirements
------------

**Header:** pointofservicedriverinterface.h





[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20MagneticStripeReaderErrorOccured%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





