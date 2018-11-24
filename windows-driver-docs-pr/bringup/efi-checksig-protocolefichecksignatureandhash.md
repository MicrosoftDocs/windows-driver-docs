---
title: EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash
description: EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash
ms.assetid: 7c6d1756-a3db-4754-9edb-af6ba1ecf65b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_CHECKSIG\_PROTOCOL.EfiCheckSignatureAndHash


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


<a href="" id="this"></a>*This*  
\[in\] A pointer to the **EFI\_CHECKSIG\_PROTOCOL** instance.

<a href="" id="pbcatalogdata"></a>*pbCatalogData*  
\[in\] A pointer to the catalog data.

<a href="" id="cbcatalogdata"></a>*cbCatalogData*  
\[in\] The size of the catalog data in bytes.

<a href="" id="pbhashtabledata"></a>*pbHashTableData*  
\[in\] A pointer to the hash table data.

<a href="" id="cbhashtabledata"></a>*cbHashTableData*  
\[in\] The size of the hash table data in bytes.

## Return Value


Returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>EFI_SUCCESS</p></td>
<td><p>The function returned successfully and the catalog signature of the hash table is valid.</p></td>
</tr>
<tr class="even">
<td><p>EFI_SECURITY_VIOLATION</p></td>
<td><p>The catalog signature or the hash table is not valid.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_INVALID_PARAMETER</p></td>
<td><p>A parameter is invalid.</p></td>
</tr>
<tr class="even">
<td><p>EFI_NO_MAPPING</p></td>
<td><p>An internal error occurred; for example, the PK is provisioned incorrectly.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


The call to this function is synchronous.

## Requirements


**Header:** User generated

 

 




