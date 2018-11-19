---
title: Access Memory Through a Permanent Memory Window
description: Access PCMCIA Attribute Memory Through a Permanent Memory Window
ms.assetid: 866851b9-8e39-4480-9f22-dc2a2eb80ce0
keywords:
- attribute memory WDK PCMCIA bus , permanent-assigned memory window
- permanent memory window WDK PCMCIA bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access PCMCIA Attribute Memory Through a Permanent Memory Window





This section describes how a PC Card or CardBus card driver can use a permanent-assigned memory window to access attribute memory.

A driver should use this method to support PCMCIA devices that implement device registers in attribute memory. In such cases, a driver's ISR typically needs fast direct access to the device registers while running at IRQL DIRQL.

Drivers can use this method while running at IRQL DIRQL.

Setup and the Plug and Play manager support the [**INF DDInstall.LogConfigOverride section**](https://msdn.microsoft.com/library/windows/hardware/ff547339), which can force the Plug and Play manager to use the resources specified in a **PcCardConfig** entry. The **LogConfigOverride** section specifies a log config section that contains a **PcCardConfig** entry. Fields in the **PcCardConfig** entry specify the required memory resource, and that the memory resource is used for attribute memory.

 

 





