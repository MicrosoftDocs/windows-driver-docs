---
title: EFI_USBFN_DEVICE_INFO_ID
description: EFI_USBFN_DEVICE_INFO_ID
ms.assetid: bc0391b4-876a-4c3c-920c-a16a781a84b0
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

 

 




