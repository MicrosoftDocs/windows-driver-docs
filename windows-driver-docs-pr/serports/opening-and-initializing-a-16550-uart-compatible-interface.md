---
title: Opening and Initializing a 16550 UART-Compatible Interface
description: Opening and Initializing a 16550 UART-Compatible Interface
ms.assetid: 341cc1cb-bbcf-4514-8f5d-8970e49923c2
keywords:
- Serial driver WDK , 16550 UART-compatible interfaces
- universal asynchronous receiver-transmitters WDK serial devices
- UART WDK serial devices
- 16550 UART-compatible interfaces WDK serial devices
- initializing 16550 UART-compatible interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening and Initializing a 16550 UART-Compatible Interface





When Serial is used as a lower-level device filter driver, the following considerations apply to opening and initializing the filter device:

-   Serial supports only one open at a time on the filter device.

-   The filter device is in an undefined state when it is open.

    A client should initialize the filter device to a known state before using it. A user-mode client can use the [IOCTL\_SERIAL\_SET\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547466) requests. Note, however, that a Win32-compliant application must use the communication functions that are supported by the Windows Base Services in the Microsoft Windows SDK. A kernel-mode client can use the IOCTL\_SERIAL\_Xxx and the [IOCTL\_SERIAL\_INTERNAL\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547480) requests.

 

 




