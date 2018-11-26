---
title: Opening and Initializing a Serial Device
description: Opening and Initializing a Serial Device
ms.assetid: 08266561-4738-4313-b53b-d60081e875c7
keywords:
- Serial driver WDK , device opening
- Serial driver WDK , device initializing
- serial devices WDK , opening
- serial devices WDK , initializing
- initializing serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening and Initializing a Serial Device





When Serial is used as a function driver, the following considerations apply to opening and initializing a serial device:

-   Serial supports only one open at a time on a serial device.

-   A device is in an undefined state when it is opened. A client should initialize a device to a known state before using the device. A user-mode client must use the communications functions that are supported by the Windows Base Services in the Microsoft Windows SDK. A kernel-mode client can use the [IOCTL\_SERIAL\_SET\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547466) and the [IOCTL\_SERIAL\_INTERNAL\_Xxx](https://msdn.microsoft.com/library/windows/hardware/ff547480) requests.

-   All clients must open a serial device when needed, and close the device immediately after they are through with the port.

-   Serenum must open an RS-232 port to enumerate the port. Clients that hold an RS-232 port open indefinitely should not use Serenum.

 

 




