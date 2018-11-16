---
title: NFC design guide
description: Windows exposes a rich set of experiences using NFC technology including the following platforms
ms.assetid: 26BFE25A-AC46-4634-8330-990DB447E55A
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Near field communications (NFC) design guide


Windows exposes a rich set of experiences using NFC technology including the following platforms:

-   Proximity Platform – Provides a platform to initiate peer-to-peer sharing of content between devices via NFC, focusing on Windows devices, as well as other NFC-compliant mobile devices as well as reading/write content to/from NFC forum compliant tags.

-   Wallet Platform – Provides the secure storage and transactional capabilities to power on-device payment scenarios, as well as brick-and-mortar payments and other NFC transactions.

To enable NFC support, Microsoft relies on IHVs to provide device drivers that implement the Device Driver Interface (DDI) defined in these topics.

Use the User-Mode Driver Framework (UMDF) 2.0 to write NFC drivers for Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.

## Related topics
 [Getting Started with UMDF](https://msdn.microsoft.com/library/windows/hardware/dn384105)  
 [NFC device driver interface (DDI) reference](https://msdn.microsoft.com/library/windows/hardware/mt715815)    


----------
