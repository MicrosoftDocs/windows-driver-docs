---
title: EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy
description: EFI_USBFN_IO_PROTOCOL.GetEndpointPolicy
ms.assetid: 143ee448-2c29-46f4-b62c-6429a4a1d890
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.GetEndpointPolicy


The **GetEndpointPolicy** function retrieves the configuration policy for the specified non-control endpoint.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_GET_ENDPOINT_POLICY) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN EFI_USBFN_POLICY_TYPE        PolicyType,
  IN OUT UINTN                    BufferSize,
  IN OUT VOID                     *Buffer
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="endpointindex"></a>*EndpointIndex*  
Indicates the non-control endpoint for which the policy needs to be set.

<a href="" id="direction"></a>*Direction*  
The direction of the endpoint. For more information, see [EFI\_USBFN\_ENDPOINT\_DIRECTION](efi-usbfn-endpoint-direction.md).

<a href="" id="policytype"></a>*PolicyType*  
The policy type the user is trying to retrieve for the specified non-control endpoint. For more information, see [EFI\_USBFN\_POLICY\_TYPE](efi-usbfn-policy-type.md).

<a href="" id="buffersize"></a>*BufferSize*  
On input, the size of *Buffer* in bytes. On output, the amount of data returned by *Buffer* in bytes.

<a href="" id="buffer"></a>*Buffer*  
A pointer to a buffer to return the requested endpoint policy value. For more information about the size requirements of the policy types, see [EFI\_USBFN\_POLICY\_TYPE](efi-usbfn-policy-type.md).

## Return values


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
<td><p><strong>EFI_SUCCESS</strong></p></td>
<td><p>The function returned successfully.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_INVALID_PARAMETER</strong></p></td>
<td><p>A parameter is invalid.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_DEVICE_ERROR</strong></p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_UNSUPPORTED</strong></p></td>
<td><p>Changing this policy value is not supported.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_BUFFER_TOO_SMALL</strong></p></td>
<td><p>The supplied buffer is not large enough to hold the requested policy value.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


There are no associated calling restrictions for this function. This function is available starting in revision 0x00010001 of the **EFI\_USBFN\_IO\_PROTOCOL**.

## Requirements


**Header:** User generated

 

 




