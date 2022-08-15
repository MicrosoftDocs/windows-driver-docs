---
title: EFI_USBFN_DEVICE_INFO_ID
description: The EFI_USBFN_DEVICE_INFO_ID enumeration is used to identify a specific string in a request to the driver.
ms.date: 08/20/2021
---

# EFI_USBFN_DEVICE_INFO_ID

This enumeration is used to identify a specific string in a request to the driver.

## Syntax

```cpp
typedef enum _EFI_USBFN_DEVICE_INFO_ID   
{
    EfiUsbDeviceInfoUnknown = 0,
    EfiUsbDeviceInfoSerialNumber,
    EfiUsbDeviceInfoManufacturerName,
    EfiUsbDeviceInfoProductName
} EFI_USBFN_DEVICE_INFO_ID;
```

## Constants

**EfiUsbDeviceInfoUnknown**  
Invalid ID.

**EfiUsbDeviceInfoSerialNumber**  
A request for the serial number of the USB device.

**EfiUsbDeviceInfoManufacturerName**  
A request for the manufacturer string.

**EfiUsbDeviceInfoProductName**  
A request for the product name of the device.

## Requirements

**Header:** User generated
