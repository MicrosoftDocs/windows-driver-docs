---
title: MagneticStripeReaderDataReceived
description: MagneticStripeReaderDataReceived
ms.assetid: '5074669c-3914-4d15-983b-d979c7f88b21'
---

# MagneticStripeReaderDataReceived


This event is raised after a successful magnetic stripe reader (MSR) scan event.

Syntax
------

``` syntax
typedef struct _MSR_DATA_RECEIVED {
    MsrCardType CardType;
    unsigned char Track1EncryptedDataLength;
    unsigned char Track2EncryptedDataLength;
    unsigned char Track3EncryptedDataLength;
    unsigned char Track4EncryptedDataLength;
    unsigned char Track1EncryptedData[MSR_TRACK_SIZE];
    unsigned char Track2EncryptedData[MSR_TRACK_SIZE];
    unsigned char Track3EncryptedData[MSR_TRACK_SIZE];
    unsigned char Track4EncryptedData[MSR_TRACK_SIZE];
    unsigned char Track1MaskedDataLength;
    unsigned char Track2MaskedDataLength;
    unsigned char Track3MaskedDataLength;
    unsigned char Track4MaskedDataLength;
    unsigned char Track1MaskedData[MSR_TRACK_SIZE];
    unsigned char Track2MaskedData[MSR_TRACK_SIZE];
    unsigned char Track3MaskedData[MSR_TRACK_SIZE];
    unsigned char Track4MaskedData[MSR_TRACK_SIZE];
    unsigned char Track1DiscretionaryDataLength;
    unsigned char Track2DiscretionaryDataLength;
    unsigned char Track1DiscretionaryData[MSR_TRACK_SIZE];
    unsigned char Track2DiscretionaryData[MSR_TRACK_SIZE];
    unsigned char CardAuthenicationDataLength; // Length of data after encryption, may include padding.
    unsigned char CardAuthenticationDataAbsoluteLength; // Length of data before encryption, may be needed to strip padding on decryption.
    unsigned char CardAuthenicationData[MSR_CARD_AUTHENTICATION_DATA_SIZE];
    unsigned char AdditionalSecurityInformationLength;
    unsigned char AdditionalSecurityInformation[MSR_ADDITIONAL_SECURITY_INFORMATION_SIZE];
} MSR_DATA_RECEIVED, *PMSR_DATA_RECEIVED;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value                                                                   | Description                                                                                                                                      |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x00000008                                                          | **EventType = PosEventType:: MagneticStripeReaderDataReceived**                                                                       |
| UINT32                                                              | **DataLength** = sizeof(**PosEventDataHeader**) + sizeof(**MSR\_DATA\_RECEIVED**)                                                     |
| 32-bit MsrCardType                                                  | [MsrCardType](https://msdn.microsoft.com/library/windows/hardware/dn772167)                                                                                                        |
| unsigned char                                                       | **Track1EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](https://msdn.microsoft.com/library/windows/hardware/dn772169) is **MsrDataEncryption\_None**. |
| unsigned char                                                       | **Track2EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](https://msdn.microsoft.com/library/windows/hardware/dn772169) is **MsrDataEncryption\_None**. |
| unsigned char                                                       | **Track3EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](https://msdn.microsoft.com/library/windows/hardware/dn772169) is **MsrDataEncryption\_None**. |
| unsigned char                                                       | **Track4EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](https://msdn.microsoft.com/library/windows/hardware/dn772169) is **MsrDataEncryption\_None**. |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track1EncryptedDataLength** bytes of encrypted track 1 data                                                                         |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track2EncryptedDataLength** bytes of encrypted track 2 data                                                                         |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track3EncryptedDataLength** bytes of encrypted track 3 data                                                                         |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track4EncryptedDataLength** bytes of encrypted track 4 data                                                                         |
| unsigned char                                                       | **Track1MaskedDataLength**                                                                                                            |
| unsigned char                                                       | **Track2MaskedDataLength**                                                                                                            |
| unsigned char                                                       | **Track3MaskedDataLength**                                                                                                            |
| unsigned char                                                       | **Track4MaskedDataLength**                                                                                                            |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track1MaskedDataLength** bytes of masked track 1 data                                                                               |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track2MaskedDataLength** bytes of masked track 2 data                                                                               |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track3MaskedDataLength** bytes of masked track 3 data                                                                               |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track4MaskedDataLength** bytes of masked track 4 data                                                                               |
| unsigned char                                                       | **Track1DiscretionaryDataLength** – Will always be zero (0) if **MagneticStripeReaderIsDecodeDataEnabled** is false.                |
| unsigned char                                                       | **Track2DiscretionaryDataLength**– Will always be zero (0) if **MagneticStripeReaderIsDecodeDataEnabled** is false.                 |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track1DiscretionaryDataLength** bytes of discretionary track 1 data                                                                 |
| unsigned char \[MSR\_TRACK\_SIZE\]                                  | **Track2DiscretionaryDataLength** bytes of discretionary track 2 data                                                                 |
| unsigned char                                                       | **CardAuthenicationDataLength** - length of the encrypted data in bytes, including padding                                            |
| unsigned char                                                       | **CardAuthenticationDataAbsoluteLength** - length of the unencrypted data in bytes (you may need to strip padding during decryption)  |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_DATA\_SIZE\] | **CardAuthenticationDataAbsoluteLength** bytes of card authentication data                                                            |
| unsigned char                                                       | **AdditionalSecurityInformationLength**                                                                                               |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_SIZE\]       | **AdditionalSecurityInformationLength** bytes of additional security information                                                      |



Requirements
------------

**Header:** pointofservicedriverinterface.h





[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20MagneticStripeReaderDataReceived%20%20RELEASE:%20%282/18/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





