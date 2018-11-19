---
title: EFI_USBFN_IO_PROTOCOL.GetVendorIdProductId
description: EFI_USBFN_IO_PROTOCOL.GetVendorIdProductId
ms.assetid: 78dbc589-3ffd-4ee2-9d80-4570b3b20b2f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_IO\_PROTOCOL.GetVendorIdProductId


The **GetVendorIdProductId** function returns the vendor-id and product-id of the device.

## Syntax


```cpp
typedef
EFI_STATUS
(EFIAPI * EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID) (
  IN EFI_USBFN_IO_PROTOCOL      *This,
  OUT UINT16                    *Vid,
  OUT UINT16                    *Pid
  );
```

## Parameters


<a href="" id="this"></a>*This*  
A pointer to the EFI\_USBFN\_IO\_PROTOCOL instance.

<a href="" id="vid"></a>*Vid*  
Returned vendor-id of the device. Vendor IDs (VIDs) are 16-bit numbers owned by the vendor company and are assigned and maintained by the USB-IF.

<a href="" id="pid"></a>*Pid*  
Returned product-id of the device. Product IDs (PIDs) are 16-bit numbers assigned by each vendor as they see fit.

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
<td><p>The function returned successfully</p></td>
</tr>
<tr class="even">
<td><p><strong>EFI_INVALID_PARAMETER</strong></p></td>
<td><p>A parameter is invalid</p></td>
</tr>
<tr class="odd">
<td><p><strong>EFI_NOT_FOUND</strong></p></td>
<td><p>Unable to return VID or PID.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


## Requirements


**Header:** User generated

 

 




