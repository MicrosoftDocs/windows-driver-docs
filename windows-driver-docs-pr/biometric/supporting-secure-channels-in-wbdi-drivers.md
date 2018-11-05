---
title: Supporting Secure Channels in WBDI Drivers
description: Supporting Secure Channels in WBDI Drivers
ms.assetid: 1b4532f4-18ee-4c65-9373-2ca635d2f40d
keywords:
- biometric drivers WDK , secure channels
- secure channels WDK biometric
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Secure Channels in WBDI Drivers


To support a secure channel between the host and the device in a WBDI driver, you must encapsulate the security-related functionality in the driver. The driver then manages the secure channel. When the driver passes sample data to the Windows Biometric Service (WBS), the data must be unencrypted. A vendor-supplied engine plug-in within the WBS can set up a secure channel to a web service if necessary.

Security considerations should be transparent to WBF applications.

 

 





