---
title: MagneticStripeReaderDataReceived
description: The MagneticStripeReaderDataReceived event is raised after a successful magnetic stripe reader (MSR) scan event.
ms.date: 03/17/2023
---

# MagneticStripeReaderDataReceived

This event is raised after a successful magnetic stripe reader (MSR) scan event.

## Syntax

```cpp
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

| Memory value | Description |
|---|---|
| 0x00000008 | **EventType = PosEventType:: MagneticStripeReaderDataReceived** |
| UINT32 | **DataLength** = sizeof(**PosEventDataHeader**) + sizeof(**MSR\_DATA\_RECEIVED**) |
| 32-bit MsrCardType | [MsrCardType](/windows-hardware/drivers/ddi/pointofservicedriverinterface/ne-pointofservicedriverinterface-_msrcardtype) |
| unsigned char | **Track1EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](/windows-hardware/drivers/ddi/pointofservicedriverinterface/ne-pointofservicedriverinterface-_msrdataencryption) is **MsrDataEncryption\_None**. |
| unsigned char | **Track2EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](/windows-hardware/drivers/ddi/pointofservicedriverinterface/ne-pointofservicedriverinterface-_msrdataencryption) is **MsrDataEncryption\_None**. |
| unsigned char | **Track3EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](/windows-hardware/drivers/ddi/pointofservicedriverinterface/ne-pointofservicedriverinterface-_msrdataencryption) is **MsrDataEncryption\_None**. |
| unsigned char | **Track4EncryptedDataLength** - Will always be zero (0) if [MsrDataEncryption](/windows-hardware/drivers/ddi/pointofservicedriverinterface/ne-pointofservicedriverinterface-_msrdataencryption) is **MsrDataEncryption\_None**. |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track1EncryptedDataLength** bytes of encrypted track 1 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track2EncryptedDataLength** bytes of encrypted track 2 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track3EncryptedDataLength** bytes of encrypted track 3 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track4EncryptedDataLength** bytes of encrypted track 4 data |
| unsigned char | **Track1MaskedDataLength** |
| unsigned char | **Track2MaskedDataLength** |
| unsigned char | **Track3MaskedDataLength** |
| unsigned char | **Track4MaskedDataLength** |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track1MaskedDataLength** bytes of masked track 1 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track2MaskedDataLength** bytes of masked track 2 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track3MaskedDataLength** bytes of masked track 3 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track4MaskedDataLength** bytes of masked track 4 data |
| unsigned char | **Track1DiscretionaryDataLength** – Will always be zero (0) if **MagneticStripeReaderIsDecodeDataEnabled** is false. |
| unsigned char | **Track2DiscretionaryDataLength**– Will always be zero (0) if **MagneticStripeReaderIsDecodeDataEnabled** is false. |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track1DiscretionaryDataLength** bytes of discretionary track 1 data |
| unsigned char \[MSR\_TRACK\_SIZE\] | **Track2DiscretionaryDataLength** bytes of discretionary track 2 data |
| unsigned char | **CardAuthenicationDataLength** - length of the encrypted data in bytes, including padding |
| unsigned char | **CardAuthenticationDataAbsoluteLength** - length of the unencrypted data in bytes (you may need to strip padding during decryption) |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_DATA\_SIZE\] | **CardAuthenticationDataAbsoluteLength** bytes of card authentication data |
| unsigned char | **AdditionalSecurityInformationLength** |
| unsigned char\[MSR\_ADDITIONAL\_SECURITY\_INFORMATION\_SIZE\] | **AdditionalSecurityInformationLength** bytes of additional security information |

## Requirements

**Header:** pointofservicedriverinterface.h
