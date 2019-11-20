---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) overview.
ms.assetid: de5723f8-cc32-4660-9694-63f6603e6983
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# Bluetooth Test Platform (BTP)

<<<<<<< HEAD
The **B**luetooth **T**est **P**latform (BTP) is designed for automating testing of Bluetooth hardware, drivers, and software. BTP can be used to exercise Bluetooth radios in the host (inside the PC) and peripheral radios. BTP is intended to be an extensible framework. Additional guidance can be found in the following documents:

- Adding new peripheral radios or customizing BTP hardware is covered in [supported BTP hardware](testing-BTP-supported-hardware.md).
- Customizing or adding new tests is documented in [BTP tests](testing-BTP-Tests.md).
=======
The **B**luetooth **T**est **P**latform (BTP) is designed for automating the testing of Bluetooth hardware, drivers, and software. BTP can be used to exercise Bluetooth radios in the host (inside the PC) and peripheral radios. BTP is intended to be an extensible framework. Guidance and examples of how to extend BTP hardware, software, and tests will be available soon.
>>>>>>> f7bee0b07b187b62a595a9db1b75ad23665bae58

![Test Overview - Hardware View](images/btp-hwOverview.png)

The Bluetooth Test Platform (BTP) is the software component of Microsoft's latest automated Bluetooth testing. The Traduci is a hardware platform used by BTP that supports power management and sideband control of peripheral radios plugged into it. The package consists of software tests, a firmware package, a provisioning tool, the Traduci board, and a set of peripheral radios used for testing basic functionality.

![Test Overview - Software View](images/btp-swOverview.png)