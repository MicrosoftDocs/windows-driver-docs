---
title: WDI NDIS idle detection
description: This following diagram shows a simple state diagram of NDIS idle detection, which is used to drive USB selective suspend.
ms.date: 03/02/2023
---

# WDI NDIS idle detection


This following diagram shows a simple state diagram of NDIS idle detection, which is used to drive USB selective suspend.

![wdi ndis idle detection for usb selective suspend.](images/wdi-idle-detection-selective-suspend.png)

If the WDI device/driver supports USB selective suspend, NDIS detects its idle state to send the device into low power state (D2).

 

 





