---
title: EFI\_USBFN\_ENDPOINT\_DIRECTION
author: windows-driver-content
description: EFI\_USBFN\_ENDPOINT\_DIRECTION
ms.assetid: 910f7ab5-b4c0-4385-9306-37d863d19bf7
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# EFI\_USBFN\_ENDPOINT\_DIRECTION


The **EFI\_USBFN\_ENDPOINT\_DIRECTION** enumeration is used to identify direction of an USB transfer.

## Syntax


``` syntax
typedef enum _EFI_USBFN_ENDPOINT_DIRECTION 
{
    EfiUsbEndpointDirectionHostOut  = 0,
    EfiUsbEndpointDirectionHostIn,
    EfiUsbEndpointDirectionDeviceTx = EfiUsbEndpointDirectionHostIn,
    EfiUsbEndpointDirectionDeviceRx = EfiUsbEndpointDirectionHostOut
} EFI_USBFN_ENDPOINT_DIRECTION;
```

## Constants


<a href="" id="efiusbendpointdirectionhostout"></a>**EfiUsbEndpointDirectionHostOut**  
Indicates USB OUT transfer. D irection is from host to device

<a href="" id="efiusbendpointdirectionhostin"></a>**EfiUsbEndpointDirectionHostIn**  
Indicates USB IN transfer. Direction is from device to host.

<a href="" id="efiusbendpointdirectiondevicetx"></a>**EfiUsbEndpointDirectionDeviceTx**  
Indicates USB IN transfer. Direction is from device to host.

<a href="" id="efiusbendpointdirectiondevicerx"></a>**EfiUsbEndpointDirectionDeviceRx**  
Indicates USB OUT transfer. Direction is from host to device

## Requirements


**Header:** User generated

 

 


--------------------


