---
title: EFI_USBFN_DEVICE_INFO_ID
description: EFI_USBFN_DEVICE_INFO_ID
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_DEVICE\_INFO\_ID


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


<a href="" id="efiusbdeviceinfounknown"></a>**EfiUsbDeviceInfoUnknown**  
Invalid ID.

<a href="" id="efiusbdeviceinfoserialnumber"></a>**EfiUsbDeviceInfoSerialNumber**  
A request for the serial number of the USB device.

<a href="" id="efiusbdeviceinfomanufacturername"></a>**EfiUsbDeviceInfoManufacturerName**  
A request for the manufacturer string.

<a href="" id="efiusbdeviceinfoproductname"></a>**EfiUsbDeviceInfoProductName**  
A request for the product name of the device.

## Requirements


**Header:** User generated

 

 




