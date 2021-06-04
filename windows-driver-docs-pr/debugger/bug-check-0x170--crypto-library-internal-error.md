---
title: Bug Check 0x170 CRYPTO_LIBRARY_INTERNAL_ERROR
description: The CRYPTO_LIBRARY_INTERNAL_ERROR bug check has a value of 0x00000170. It indicates that an internal error in the crypto libraries occurred.
keywords: ["Bug Check 0x170 CRYPTO_LIBRARY_INTERNAL_ERROR", "CRYPTO_LIBRARY_INTERNAL_ERROR"]
ms.date: 01/10/2019
topic_type:
- apiref
api_name:
- CRYPTO_LIBRARY_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x170: CRYPTO\_LIBRARY\_INTERNAL\_ERROR 

The CRYPTO\_LIBRARY\_INTERNAL\_ERROR  bug check has a value of 0x00000170. It indicates that an internal error in the crypto libraries occurred.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).



 ## CRYPTO\_LIBRARY\_INTERNAL\_ERROR  Parameters

|Parameter|Description|
|--- |--- |
|1| ID of failure.|
|2| Reserved.|
|3| Reserved. |
|4| Reserved. |


## ## Cause

This bugcheck indicates the cryptographic library hit an anomaly which should never occur, and the library has no safe method of signaling the error to the caller.  This might be the symptom of an active attack.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

[Cryptography API: Next Generation](/windows/desktop/SecCNG/cng-portal)