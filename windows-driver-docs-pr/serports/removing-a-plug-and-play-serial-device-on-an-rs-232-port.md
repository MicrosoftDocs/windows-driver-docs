---
title: Removing a Plug and Play Serial Device on an RS-232 Port
description: Removing a Plug and Play Serial Device on an RS-232 Port
ms.assetid: a9019445-3013-49b2-94fd-1ab8a85c3d7a
keywords:
- RS-232 ports WDK serial devices
- Serenum driver WDK , Plug and Play devices
- Plug and Play serial devices WDK
- serial devices WDK , Plug and Play
- removing Plug and Play devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Removing a Plug and Play Serial Device on an RS-232 Port





The Plug and Play manager removes a serial device by sending a remove request to the top of a serial device stack. After Serenum receives a remove request for the serial device, it removes the device's PDO and completes the request. Serenum does not pass the request to the RS-232 port stack because the RS-232 port is the parent device for the serial device that is removed.

 

 




