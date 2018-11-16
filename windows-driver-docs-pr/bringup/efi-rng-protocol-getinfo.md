---
title: EFI_RNG_PROTOCOL.GetInfo
description: EFI_RNG_PROTOCOL.GetInfo
ms.assetid: 11E9927B-8BC6-4B01-A12D-C75B636E3988
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_RNG\_PROTOCOL.GetInfo


Returns information about the RNG algorithms supported by a driver that implements EFI\_RNG\_PROTOCOL.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI *EFI_RNG_GET_INFO) (
    IN  struct _EFI_RNG_PROTOCOL    *This,
    IN  OUT UINTN                   *RNGAlgorithmListSize,
    OUT EFI_RNG_ALGORITHM           *RNGAlgorithmList
    );
```

## Parameters


<a href="" id="this"></a>*This*  
\[in\] A pointer to the [EFI\_RNG\_PROTOCOL](efi-rng-protocol.md) instance.

<a href="" id="rngalgorithmlistsize"></a>*RNGAlgorithmListSize*  
\[in, out\] The number of algorithms in *RNGAlgorithmList*.

<a href="" id="rngalgorithmlist"></a>*RNGAlgorithmList*  
\[out\] A pointer to a list of [EFI\_RNG\_ALGORITHM](efi-display-power-state.md) values that represent RNG algorithms. Each algorithm is `sizeof(EFI_GUID)` bytes long.

## Remarks


A driver that implements EFI\_RNG\_PROTOCOL can support one or more RNG algorithms.

The value returned by the *RNGAlgorithmList* parameter must not change across multiple calls to the same driver. The first algorithm in the list is the default algorithm for the driver.

The list of algorithms is allocated by this function using EFI\_BOOT\_SERVICES-&gt;AllocatePool(), and it is the caller's responsibility to free this list by using EFI\_BOOT\_SERVICES-&gt;FreePool().

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
<td><p>The function successfully retrieved the list of RNG algorithms.</p></td>
</tr>
<tr class="even">
<td><p>EFI_UNSUPPORTED</p></td>
<td><p>The service is not supported by this driver.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_DEVICE_ERROR</p></td>
<td><p>The list of RNG algorithms could not be retrieved because of a hardware or firmware error.</p></td>
</tr>
<tr class="even">
<td><p>EFI_OUT_OF_RESOURCES</p></td>
<td><p>The driver is unable to allocate memory for the <em>RNGAlgorithmList</em> parameter.</p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

 

 




