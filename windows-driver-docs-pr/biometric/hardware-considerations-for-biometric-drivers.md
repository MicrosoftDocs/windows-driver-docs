---
title: Hardware Considerations for Biometric Drivers
description: Hardware Considerations for Biometric Drivers
ms.assetid: 07b16cfb-d3aa-4458-b6e3-acb76afe9b19
keywords:
- biometric drivers WDK , hardware considerations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Considerations for Biometric Drivers


A biometric device that uses the WBDI framework should meet the following requirements:

-   WBDI-based drivers should follow [DEVFUND-0010 guidelines](http://go.microsoft.com/fwlink/p/?linkid=26140) for Terminal Services redirection.

    This requirement states that the device and its driver must support redirection through a Terminal Services session over the PnP Device Redirection Framework.

-   Biometric devices should have an internal buffer that is large enough to cache a full scan in full power and suspend modes.

    Larger buffer size can mean less dependency on timing during regular scan processing as well as scan processing during system resume.

-   The device should be able to enter a capture mode and make internal state transitions during a scan without extra commands from the host.

 

 





