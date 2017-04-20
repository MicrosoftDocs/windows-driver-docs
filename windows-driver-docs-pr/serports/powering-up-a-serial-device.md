---
title: Powering Up a Serial Device
author: windows-driver-content
description: Powering Up a Serial Device
ms.assetid: 83f86da6-0acb-4cad-8856-e826c98c2182
keywords:
- Serial driver WDK , device power
- powering up serial devices WDK
- turning on serial devices WDK
- serial devices WDK , powering up
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Powering Up a Serial Device


## <a href="" id="ddk-powering-up-a-serial-device-kg"></a>


A serial device must be turned on (in the device power state **PowerDeviceD0**) for Serial to communicate with the device hardware. If the device is not turned on, Serial will attempt to turn on the device before the driver completes a request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Powering%20Up%20a%20Serial%20Device%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


