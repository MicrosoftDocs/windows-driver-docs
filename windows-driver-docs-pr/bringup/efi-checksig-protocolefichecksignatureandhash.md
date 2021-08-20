---
title: EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash
description: Provides information about EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash

This function verifies the signature on the catalog file in the FFU against the PK on the device. It also verifies that the hash of the table of hashes matches the hash specified in the catalog file.

## Syntax

```cpp
typedef EFI_STATUS
(EFIAPI * EFI_CHECK_SIG_AND_HASH) (
  IN EFI_CHECKSIG_PROTOCOL *This,
  IN UINT8 *pbCatalogData,
  IN UINT32 cbCatalogData,
  IN UINT8 *pbHashTableData,
  IN UINT32 cbHashTableData
);
```

## Parameters

*This*  
[in] A pointer to the **EFI_CHECKSIG_PROTOCOL** instance.

*pbCatalogData*  
[in] A pointer to the catalog data.

*cbCatalogData*  
[in] The size of the catalog data in bytes.

*pbHashTableData*  
[in] A pointer to the hash table data.

*cbHashTableData*  
[in] The size of the hash table data in bytes.

## Return Value

Returns one of the following status codes.

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully and the catalog signature of the hash table is valid. |
| EFI_SECURITY_VIOLATION | The catalog signature or the hash table is not valid. |
| EFI_INVALID_PARAMETER | A parameter is invalid. |
| EFI_NO_MAPPING | An internal error occurred; for example, the PK is provisioned incorrectly. |

## Remarks

The call to this function is synchronous.

## Requirements

**Header:** User generated
