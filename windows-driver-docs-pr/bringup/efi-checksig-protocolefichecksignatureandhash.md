---
title: EFI\_CHECKSIG\_PROTOCOL.EfiCheckSignatureAndHash
author: windows-driver-content
description: EFI\_CHECKSIG\_PROTOCOL.EfiCheckSignatureAndHash
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7c6d1756-a3db-4754-9edb-af6ba1ecf65b
---

# EFI\_CHECKSIG\_PROTOCOL.EfiCheckSignatureAndHash


This function verifies the signature on the catalog file in the FFU against the PK on the device. It also verifies that the hash of the table of hashes matches the hash specified in the catalog file.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_CHECKSIG_PROTOCOL.EfiCheckSignatureAndHash%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


