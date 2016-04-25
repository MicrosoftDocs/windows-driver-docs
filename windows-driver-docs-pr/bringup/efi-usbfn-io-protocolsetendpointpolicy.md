---
title: EFI\_USBFN\_IO\_PROTOCOL.SetEndpointPolicy
description: EFI\_USBFN\_IO\_PROTOCOL.SetEndpointPolicy
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d7ab0529-1925-47b5-9706-2e6288a6a5cf
---

# EFI\_USBFN\_IO\_PROTOCOL.SetEndpointPolicy


The **SetEndpointPolicy** function sets the configuration policy for the specified non-control endpoint.

## Syntax


``` syntax
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_SET_ENDPOINT_POLICY) (
  IN EFI_USBFN_IO_PROTOCOL        *This,
  IN UINT8                        EndpointIndex,
  IN EFI_USBFN_ENDPOINT_DIRECTION Direction,
  IN EFI_USBFN_POLICY_TYPE        PolicyType,
  IN UINTN                        BufferSize,
  IN VOID                         *Buffer
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
The policy type the user is trying to set for the specified non-control endpoint. For more information, see [EFI\_USBFN\_POLICY\_TYPE](efi-usbfn-policy-type.md).

<a href="" id="buffersize"></a>*BufferSize*  
The size of *Buffer* in bytes.

<a href="" id="buffer"></a>*Buffer*  
A pointer to the buffer that contains the new endpoint policy value. For more information about the size requirements of the policy types, see [EFI\_USBFN\_POLICY\_TYPE](efi-usbfn-policy-type.md).

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
</tbody>
</table>

 

## Remarks


This function can be called only before [EFI\_USBFN\_IO\_PROTOCOL.StartController](efi-usbfn-io-protocolstartcontroller.md) or after [EFI\_USBFN\_IO\_PROTOCOL.StopController](efi-usbfn-io-protocolstopcontroller.md) has been called. This function is available starting in revision 0x00010001 of the **EFI\_USBFN\_IO\_PROTOCOL**.

## Requirements


**Header:** User generated

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_IO_PROTOCOL.SetEndpointPolicy%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


