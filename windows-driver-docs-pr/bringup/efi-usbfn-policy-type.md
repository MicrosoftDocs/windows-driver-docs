---
title: EFI\_USBFN\_POLICY\_TYPE
description: EFI\_USBFN\_POLICY\_TYPE
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 51f615d4-a226-45d5-b5e9-fea4859640a9
---

# EFI\_USBFN\_POLICY\_TYPE


The **EFI\_USBFN\_POLICY\_TYPE** enumeration contains values used to indicate the type of endpoint.

## Syntax


``` syntax
typedef enum _EFI_USBFN_POLICY_TYPE{
  EfiUsbPolicyUndefined = 0, 
  EfiUsbPolicyMaxTransactionSize, 
  EfiUsbPolicyZeroLengthTerminationSupport, 
  EfiUsbPolicyZeroLengthTermination
} EFI_USBFN_POLICY_TYPE;
```

## Constants


<a href="" id="efiusbpolicyundefined"></a>**EfiUsbPolicyUndefined**  
Invalid policy value that must never be used across a driver boundary. If used, the callee function must never return a success status code.

<a href="" id="efiusbpolicymaxtransactionsize"></a>**EfiUsbPolicyMaxTransactionSize**  
This policy is read-only. When used with [EFI\_USBFN\_IO\_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md), the size of the maximum single transaction (delivery of service to an endpoint) supported by a controller is returned. It must be more than or equal to the maximum transfer size that can be retrieved by calling [EFI\_USBFN\_IO\_PROTOCOL.GetMaxTransferSize](efi-usbfn-io-protocolgetmaxtransfersize.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>GetEndpointPolicy</th>
<th>SetEndpointPolicy</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>BufferSize</em></p></td>
<td><p>4 bytes, sizeof(UINT32)</p></td>
<td><p>Not applicable</p></td>
</tr>
<tr class="even">
<td><p>Return status</p></td>
<td><p>EFI_STATUS</p></td>
<td><p>EFI_UNSUPPORTED</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="efiusbpolicyzerolengthterminationsupport"></a>**EfiUsbPolicyZeroLengthTerminationSupport**  
This policy is read-only. When used with [EFI\_USBFN\_IO\_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md), TRUE is returned if the USB controller hardware is capable of automatically handling zero-length packets when the transfer size is a multiple of USB maximum packet size; FALSE is returned if such a scenario is not supported by the controller hardware.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>GetEndpointPolicy</th>
<th>SetEndpointPolicy</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>BufferSize</em></p></td>
<td><p>1 byte, sizeof(BOOLEAN)</p></td>
<td><p>Not applicable</p></td>
</tr>
<tr class="even">
<td><p>Return status</p></td>
<td><p>EFI_STATUS</p></td>
<td><p>EFI_UNSUPPORTED</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="efiusbpolicyzerolengthtermination"></a>**EfiUsbPolicyZeroLengthTermination**  
When used with [EFI\_USBFN\_IO\_PROTOCOL.GetEndpointPolicy](efi-usbfn-io-protocolgetendpointpolicy.md), TRUE is returned if the USB controller hardware is configured to automatically handle zero-length packets when the transfer size is a multiple of USB maximum packet size; FALSE is returned if the controller hardware is not configured to support such a scenario.

[EFI\_USBFN\_IO\_PROTOCOL.SetEndpointPolicy](efi-usbfn-io-protocolsetendpointpolicy.md) can only accept this policy type if the USB controller hardware is capable of supporting automatic zero-length packet termination. When this value is set to TRUE, the controller must be configured to handle zero-length termination for the specified endpoint; a FALSE value would not configure the controller in such fashion.

Even if the controller hardware is capable of supporting automatic zero-length termination, it must not be the default configuration.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>GetEndpointPolicy</th>
<th>SetEndpointPolicy</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>BufferSize</em></p></td>
<td><p>1 byte, sizeof(BOOLEAN)</p></td>
<td><p>1 byte, sizeof(BOOLEAN)</p></td>
</tr>
<tr class="even">
<td><p>Return status</p></td>
<td><p>EFI_STATUS</p></td>
<td><p>EFI_STATUS</p></td>
</tr>
</tbody>
</table>

 

## Requirements


**Header:** User generated

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_POLICY_TYPE%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




