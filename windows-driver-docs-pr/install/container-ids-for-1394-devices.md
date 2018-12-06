---
title: Container IDs for 1394 Devices
description: Container IDs for 1394 Devices
ms.assetid: 667df2c6-bbbd-41da-b626-da493e316016
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container IDs for 1394 Devices


The 1394 bus specification does not specify an internal hardware mechanism to indicate whether a device function is or is not removable from the 1394 host controller. The 1394 bus driver that is included with Windows marks every device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) as removable from the parent host controller.

If a single 1394 device exposes multiple device functions, each devnode that the bus driver enumerates is marked as removable. However, the 1394 bus driver that is included with Windows recognizes that each devnode originated from a single device and assigns the same container ID to each devnode. Therefore, each 1394 device receives a single device container object and is displayed as a single device in the Devices and Printers user interface (UI).

 

 





