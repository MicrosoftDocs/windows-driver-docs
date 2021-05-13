---
title: Bug Check 0xF0 STORAGE_MINIPORT_ERROR
description: The STORAGE_MINIPORT_ERROR bug check has a value of 0x00000F0. It indicates that a storage Miniport driver failed to complete a SRB request.
keywords: ["Bug Check 0xF0 STORAGE_MINIPORT_ERROR", "STORAGE_MINIPORT_ERROR"]
ms.date: 01/24/2019
topic_type:
- apiref
api_name:
- STORAGE_MINIPORT_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF0: STORAGE\_MINIPORT\_ERROR

The STORAGE\_MINIPORT\_ERROR bug check has a value of 0x00000F0. It indicates that a storage Miniport driver failed to complete a SRB request.


> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## STORAGE\_MINIPORT\_ERROR Parameters

|Parameter|Description|
|-------- |---------- |
|1| Error Code. See Values below.|
|2| See Values below.|
|3| See Values below.|
|4| See Values below.|

**Values**

```text
1: Miniport failed to complete a SRB request even after successful reset operation.
    2 - Driver name unicode string address
    3 - SRB address
    4 - Storport unit device object

2: Miniport failed to complete a SRB request even after successful abort operation for the SRB.
    2 - Driver name unicode string address
    3 - Abort SRB address
    4 - SRB that was being aborted

3: Miniport failed to complete a request within a given timeout.
    2 - Driver name unicode string address
    3 - SRB address
    4 - Timeout of the request

4: Miniport failed to complete a request for a crypto operation. This can occur if it is trying to enable an encryption key on an ICE (Inline Crypto Engine) enabled UFS host. 
    2 - Driver name unicode string address
    3 - The STOR_CRYPTO_OPERATION_TYPE for this failure, typically StorCryptoOperationInsertKey
    4 - Reserved    
```


## ## Cause

A bug in the storage Miniport driver kept a SRB request from completing. See the error code values listed above for the specific type of failure.


## Resolution
-----

The [!analyze](-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause. 

The driver name returned in parameter 2 should point to the offending driver.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

[Storport's Interface with Storport Miniport Drivers](../storage/storport-s-interface-with-storport-miniport-drivers.md)