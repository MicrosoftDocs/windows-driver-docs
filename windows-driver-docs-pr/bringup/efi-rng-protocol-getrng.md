---
title: EFI_RNG_PROTOCOL.GetRNG
description: EFI_RNG_PROTOCOL.GetRNG
ms.assetid: 5C2E0C8F-FF3A-4F57-BC28-3BC540852CB0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_RNG\_PROTOCOL.GetRNG


Retrieves a Random Number Generation (RNG) value.

## Syntax


```cpp
typedef EFI_STATUS (EFIAPI *EFI_RNG_GET_RNG) (
    IN  struct _EFI_RNG_PROTOCOL    *This,
    IN  EFI_RNG_ALGORITHM           *RNGAlgorithm, OPTIONAL
    IN  UINTN                       RNGValueLength,
    OUT UINT8                       *RNGValue
    );
```

## Parameters


<a href="" id="this"></a>*This*  
\[in\] A pointer to the [EFI\_RNG\_PROTOCOL](efi-rng-protocol.md) instance.

<a href="" id="rngalgorithm"></a>*RNGAlgorithm*  
\[in\] A pointer to the EFI\_RNG\_ALGORITHM which identifies the RNG algorithm to use. If this parameter is NULL, the default algorithm supported by the driver will be used.

<a href="" id="rngvaluelength"></a>*RNGValueLength*  
\[in\] The length, in bytes, of the buffer returned by *RNGValue*.

<a href="" id="rngvalue"></a>*RNGValue*  
\[in\] Pointer to a buffer that will contain the RNG value. The value is allocated by this function using EFI\_BOOT\_SERVICES-&gt;AllocatePool(), and it is the caller's responsibility to free this memory by using EFI\_BOOT\_SERVICES-&gt;FreePool().

## Remarks


The minimum size of *RNGValue* is 32 bytes.

## Return value


Returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>EFI_SUCCESS</p></td>
<td><p>The function successfully returned an RNG value.</p></td>
</tr>
<tr class="even">
<td><p>EFI_INVALID_PARAMETER</p></td>
<td><p><em>RNGAlgorithm</em> is NULL when several algorithms are possible.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_UNSUPPORTED</p></td>
<td><p>The algorithm specified by <em>RNGAlgorithm</em> is not supported by this driver.</p></td>
</tr>
<tr class="even">
<td><p>EFI_DEVICE_ERROR</p></td>
<td><p>An RNG value could not be retrieved because of a hardware or firmware error.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_NOT_READY</p></td>
<td><p>There is not enough entropy data available.</p></td>
</tr>
<tr class="even">
<td><p>EFI_OUT_OF_RESOURCES</p></td>
<td><p>The driver is unable to allocate memory for the RNG value.</p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

 

 




