---
title: Hardware Considerations for Biometric Drivers
description: Hardware Considerations for Biometric Drivers
ms.assetid: 07b16cfb-d3aa-4458-b6e3-acb76afe9b19
keywords:
- biometric drivers WDK , hardware considerations
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Hardware Considerations for Biometric Drivers


A biometric device that uses the WBDI framework should meet the following requirements:

-   WBDI-based drivers should follow [DEVFUND-0010 guidelines](http://go.microsoft.com/fwlink/p/?linkid=26140) for Terminal Services redirection.

    This requirement states that the device and its driver must support redirection through a Terminal Services session over the PnP Device Redirection Framework.

-   Biometric devices should have an internal buffer that is large enough to cache a full scan in full power and suspend modes.

    Larger buffer size can mean less dependency on timing during regular scan processing as well as scan processing during system resume.

-   The device should be able to enter a capture mode and make internal state transitions during a scan without extra commands from the host.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Hardware%20Considerations%20for%20Biometric%20Drivers%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




