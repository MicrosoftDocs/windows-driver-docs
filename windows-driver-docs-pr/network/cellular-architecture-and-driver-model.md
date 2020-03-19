---
title: Cellular architecture and implementation
description: The cellular architecture for Windows 10 contains elements from both Windows 8.1 and Windows Phone 8.1.
ms.assetid: A6F23D12-BCF0-496A-B881-C1F6B35EDA4D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Cellular architecture and implementation

Cellular Architecture for Windows contains elements for provisioning the device using OEM specific settings, integration with the Windows Connection Manager and WWAN Service that is the core for integrating Modem Drivers with the rest of the OS components.

## Windows 10 architecture:

![windows 10 cellular architecture](images/CellularArchitecture.png)

## Windows 10 cellular implementation requirements

For Windows 10 for desktop editions, the following is required.

-   Implement the MBIM protocol interface in your modem hardware.
-   Implement a USB interface to the modem hardware. It could be a removable USB dongle or another interface that presents itself as a USB host controller.

## Related topics


[Mobile Broadband (MB) Design Guide](mobile-broadband--mb--design-guide.md)

 

 






