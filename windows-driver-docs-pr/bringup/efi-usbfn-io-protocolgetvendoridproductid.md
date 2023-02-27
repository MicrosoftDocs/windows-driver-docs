---
title: EFI_USBFN_IO_PROTOCOL.GetVendorIdProductId
description: The *GetVendorIdProductId* function returns the vendor-id and product-id of the device.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_USBFN_IO_PROTOCOL.GetVendorIdProductId

The *GetVendorIdProductId* function returns the vendor-id and product-id of the device.

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

*This*  
A pointer to the EFI_USBFN_IO_PROTOCOL instance.

>*Vid*  
Returned vendor-id of the device. Vendor IDs (VIDs) are 16-bit numbers owned by the vendor company and are assigned and maintained by the USB-IF.

*Pid*  
Returned product-id of the device. Product IDs (PIDs) are 16-bit numbers assigned by each vendor as they see fit.

## Return values

The function returns the following values:

| Return code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully |
| EFI_INVALID_PARAMETER | A parameter is invalid |
| EFI_NOT_FOUND | Unable to return VID or PID. |

## Remarks

## Requirements

**Header:** User generated
