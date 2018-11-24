---
title: What's new in NFC device drivers
description: This topic summarizes the new features and improvements for NFC device drivers in Windows 10.
ms.assetid: 07E0E7F4-9D2B-423F-925C-D6923D8D9A4A
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# What's new for NFC device drivers in Windows 10


This topic summarizes the new features and improvements for NFC device drivers in Windows 10.

* The NFC device driver model has converged for both desktop and mobile devices to create a universal NFC device driver model. Hardware partners can now build a single driver that can run on all Windows device platforms.

* The NFC class extension (CX) implements the Windows-defined device driver interfaces to interact with the NFC controller, Secure Elements, and Remote RF endpoints.

* An in-box NFC radio manager has been added to take care of managing Airplane Mode for NFC. Do not package IHV-supplied NFC radio managers with NFC drivers (as was done in earlier versions of Windows). Installing an IHV-supplied NFC radio manager alongside the Windows 10 NFC radio manager will cause conflicts between those software components.

 
## Related topics
 [NFC device driver interface (DDI) reference](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
 
