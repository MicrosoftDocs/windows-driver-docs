---
title: Driver support for uvc control cache
description: Provides information about how to explicitly utilize camera control cache for a device.
ms.date: 08/16/2019
---

# Driver support for Camera UVC Control Cache

UVC controls stick on a device when frame server shuts down. If one uses an app that sets White Balance with UVC controls and then shuts down the app, then the camera's White Balance will not be reset. Other apps that open and do not change the White Balance will inherit the previous setting.

One exception is when the computer goes into S3. Depending on whether the camera device goes into D3 or D3 Cold, the UVC controls respectively may or may not stick. This behavior is because D3 Cold removes power from the camera.

Utilizing the Cache UVC Control Protocol is a way to have consistent behavior across application sessions, S3, and computer shutdowns.
  
By setting the configuration key “CacheUVCControl” to the DWORD value of 1 in the device HW registry key by way of MS OS 2.0 descriptors or the older method of custom INF file, a camera will retain UVC control values set by the user across S3 or computer reboots. The list of specific UVC control values that will be stored and reapplied is below.

## UVC Controls Affected

Below is a list of UVC Controls that would be cached and reapplied across reboot:

- KSPROPERTY_VIDEOPROCAMP_BRIGHTNESS
- KSPROPERTY_VIDEOPROCAMP_CONTRAST
- KSPROPERTY_VIDEOPROCAMP_GAIN
- KSPROPERTY_VIDEOPROCAMP_GAMMA
- KSPROPERTY_VIDEOPROCAMP_HUE(+ AUTO)
- KSPROPERTY_VIDEOPROCAMP_SATURATION
- KSPROPERTY_VIDEOPROCAMP_SHARPNESS
- KSPROPERTY_VIDEOPROCAMP_WHITEBALANCE(+ AUTO)

## INF Example

```cpp
[Device.AddReg.HW]
HKR,,"CacheUVCControl",0x00010001,1
```

## MS OS 2.0 Descriptor Example

```cpp
UCHAR Example_MSOS20DescriptorSet_CacheUVCControl[0x38] =
{
    //
    // Microsoft OS 2.0 Descriptor Set Header
    //
    0x0A, 0x00,               // wLength - 10 bytes
    0x00, 0x00,               // MSOS20_SET_HEADER_DESCRIPTOR
    0x00, 0x00, 0x0?, 0x06,   // dwWindowsVersion – 0x060?0000 for future Windows version
    0x3C, 0x00,               // wTotalLength – 60 bytes

    //
    // Microsoft OS 2.0 Registry Value Feature Descriptor
    //
    0x32, 0x00,               // wLength 0x32 (50) in bytes of this descriptor  
    0x04, 0x00,               // wDescriptorType – MSOS20_FEATURE_REG_PROPERTY  
    0x04, 0x00,               // wPropertyDataType - REG_DWORD  
    0x24, 0x00,               // wPropertyNameLength – 0x24 (36) bytes
    'C',  0x00, 'a',  0x00,   // Property Name - “CacheUVCControl”  
    'c',  0x00, 'h',  0x00,  
    'e',  0x00, 'U',  0x00,
    'V',  0x00, 'C',  0x00,  
    'C',  0x00, 'o',  0x00,  
    'n',  0x00, 't',  0x00,  
    'r',  0x00, 'o',  0x00,  
    'l',  0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00,
    0x04, 0x00,               // wPropertyDataLength – 4 bytes  
    0x01, 0x00, 0x00, 0x00,   // Enable to cache UVC controls  
}
```
