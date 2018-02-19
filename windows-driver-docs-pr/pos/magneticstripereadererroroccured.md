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
| 0x00000009<br/>                                                          | **EventType = PosEventType:: MagneticStripeReaderErrorOccurred**<br/>                                                               |
| UINT32<br/>                                                              | **DataLength** = sizeof(**PosEventDataHeader**) + sizeof(**MSR\_ERROR\_EVENT**)<br/>                                                |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)<br/>                   | **Track1Status**<br/>                                                                                                               |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)<br/>                   | **Track2Status**<br/>                                                                                                               |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)<br/>                   | **Track3Status**<br/>                                                                                                               |
| 32-bit [MsrTrackErrorType](https://msdn.microsoft.com/library/windows/hardware/dn772173)<br/>                   | **Track4Status**<br/>                                                                                                               |
| 32-bit [UnifiedPosErrorSeverity](https://msdn.microsoft.com/library/windows/hardware/dn790053)<br/>       | **Severity**<br/>                                                                                                                   |
| 32-bit [UnifiedPosErrorReason](https://msdn.microsoft.com/library/windows/hardware/dn790050)<br/>           | **Reason**<br/>                                                                                                                     |
| UINT32<br/>                                                              | **Extended Reason**<br/>                                                                                                            |
| 32-bit [MsrCardType](https://msdn.microsoft.com/library/windows/hardware/dn772167)<br/>                               | **CardType**<br/>                                                                                                                   |
| unsigned char<br/>                                                       | **Track1EncryptedDataLength**<br/>                                                                                                  |
| unsigned char<br/>                                                       | **Track2EncryptedDataLength**<br/>                                                                                                  |
| unsigned char<br/>                                                       | **Track3EncryptedDataLength**<br/>                                                                                                  |
| unsigned char<br/>                                                       | **Track4EncryptedDataLength**<br/>                                                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track1EncryptedDataLength** bytes of encrypted track 1 data<br/>                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track2EncryptedDataLength** bytes of encrypted track 2 data<br/>                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track3EncryptedDataLength** bytes of encrypted track 3 data<br/>                                                                  |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track4EncryptedDataLength** bytes of encrypted track 4 data<br/>                                                                  |
| unsigned char<br/>                                                       | **Track1MaskedDataLength**<br/>                                                                                                     |
| unsigned char<br/>                                                       | **Track2MaskedDataLength**<br/>                                                                                                     |
| unsigned char<br/>                                                       | **Track3MaskedDataLength**<br/>                                                                                                     |
| unsigned char<br/>                                                       | **Track4MaskedDataLength**<br/>                                                                                                     |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track1MaskedDataLength** bytes of masked track 1 data<br/>                                                                        |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track2MaskedDataLength** bytes of masked track 2 data<br/>                                                                        |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track3MaskedDataLength** bytes of masked track 3 data<br/>                                                                        |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track4MaskedDataLength** bytes of masked track 4 data<br/>                                                                        |
| unsigned char<br/>                                                       | **Track1DiscretionaryDataLength**<br/>                                                                                              |
| unsigned char<br/>                                                       | **Track2DiscretionaryDataLength**<br/>                                                                                              |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track1DiscretionaryDataLength** bytes of discretionary track 1 data<br/>                                                          |
| unsigned char \[MSR\_TRACK\_SIZE\]<br/>                                  | **Track2DiscretionaryDataLength** bytes of discretionary track 2 data<br/>                                                          |
| unsigned char<br/>                                                       | **CardAuthenicationDataLength** - length of the data after encryption, including padding<br/>                                       |
| unsigned char<br/>                                                       | **CardAuthenticationDataAbsoluteLength** - length of data before encryption (may be needed to strip padding during decryption)<br/> |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_DATA\_SIZE\]<br/> | **CardAuthenticationDataAbsoluteLength** bytes of card authentication data<br/>                                                     |
| unsigned char<br/>                                                       | **AdditionalSecurityInformationLength**<br/>                                                                                        |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_SIZE\]<br/>       | **AdditionalSecurityInformationLength** bytes of additional security information<br/>                                               |
| wchar\_T \[MSR\_ERROR\_MAX\_MESSAGE\_LENGTH\]<br/>                       | Up to **MSR\_ERROR\_MAX\_MESSAGE\_LENGTH** wchar\_t of error **Null**-terminated message text<br/>                                  |

 

Remarks
-------

If a scanning error occurs, and some scan data was obtained, the event data contains the partial scan data.

Requirements
------------

**Header:** pointofservicedriverinterface.h

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20MagneticStripeReaderErrorOccured%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





