---
title: Bug Check 0x170 CRYPTO_LIBRARY_INTERNAL_ERROR
description: The CRYPTO_LIBRARY_INTERNAL_ERROR bug check has a value of 0x00000170. It indicates that an internal error in the crypto libraries occurred.
keywords: ["Bug Check 0x170 CRYPTO_LIBRARY_INTERNAL_ERROR", "CRYPTO_LIBRARY_INTERNAL_ERROR"]
ms.date: 01/04/2019
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

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).


 ## CRYPTO\_LIBRARY\_INTERNAL\_ERROR  Parameters

|Parameter|Description|
|--- |--- |
|1| ID of failure.|
|2| Reserved.|
|3| Reserved. |
|4| Reserved. |


## Cause
-----

This bugcheck will hit if the crypto libraries detect an anomaly that should never occur but which might be the symptom of an
active attack, and the library has no safe method of signaling the error to the caller.


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)




