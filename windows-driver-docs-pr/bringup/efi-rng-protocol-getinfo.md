---
title: EFI\_RNG\_PROTOCOL.GetInfo
description: EFI\_RNG\_PROTOCOL.GetInfo
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 11E9927B-8BC6-4B01-A12D-C75B636E3988
---

# EFI\_RNG\_PROTOCOL.GetInfo


Returns information about the RNG algorithms supported by a driver that implements EFI\_RNG\_PROTOCOL.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_RNG_PROTOCOL.GetInfo%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


