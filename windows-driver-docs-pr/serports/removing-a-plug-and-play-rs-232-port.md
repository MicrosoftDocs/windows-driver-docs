---
title: Removing a Plug and Play RS-232 Port
author: windows-driver-content
description: Removing a Plug and Play RS-232 Port
ms.assetid: b439dc51-09f2-4149-a562-2e376bb504c5
keywords:
- RS-232 ports WDK serial devices
- Serenum driver WDK , Plug and Play devices
- Plug and Play serial devices WDK
- serial devices WDK , Plug and Play
- removing RS-232 ports
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Removing a Plug and Play RS-232 Port


## <a href="" id="ddk-removing-a-plug-and-play-rs-232-port-kg"></a>


The Plug and Play manager removes an RS-232 port by sending a remove request to the top of the RS-232 port stack. Serenum passes the request down the device stack, removes the filter DO in the port stack, and removes an associated PDO, if one exists. Removal of the RS-232 port also removes the serial device attached to the port.

 

 




