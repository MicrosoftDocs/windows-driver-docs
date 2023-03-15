---
title: Hardware Considerations for Biometric Drivers
description: Hardware Considerations for Biometric Drivers
keywords:
- biometric drivers WDK , hardware considerations
ms.date: 03/03/2023
---

# Hardware Considerations for Biometric Drivers


A biometric device that uses the WBDI framework should meet the following requirements:

-   WBDI-based drivers should follow [DEVFUND-0010 guidelines](/windows-hardware/test/hlk/) for Terminal Services redirection.

    This requirement states that the device and its driver must support redirection through a Terminal Services session over the PnP Device Redirection Framework.

-   Biometric devices should have an internal buffer that is large enough to cache a full scan in full power and suspend modes.

    Larger buffer size can mean less dependency on timing during regular scan processing as well as scan processing during system resume.

-   The device should be able to enter a capture mode and make internal state transitions during a scan without extra commands from the host.

 

