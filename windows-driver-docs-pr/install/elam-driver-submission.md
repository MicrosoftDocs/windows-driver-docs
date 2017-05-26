---
title: ELAM Prerequisites
description: Early Launch Antimalware (ELAM) drivers can be submitted using the listed steps to ensure validation and adherence to documented requirements
ms.assetid:
ms.author: windowsdriverdev
ms.date: 04/27/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---
# ELAM driver submission Process

The following steps can be used to submit an Early Launch Antimalware (ELAM) driver:

1. Ensure your driver adheres to the documented requirements for ELAM drivers.  Be sure to update the INF to include the **[SignatureAttributes]** section for the ELAM driver you are submitting. See [ELAM driver requirements](https://msdn.microsoft.com/windows/hardware/drivers/install/elam-driver-requirements) and [INF SignatureAttributes Section](https://msdn.microsoft.com/windows/hardware/drivers/install/inf-signatureattributes-section) for more information.

2. Validate your driver using the Hardware Logo Kit (HLK) and Hardware Certification Kit (HCK). If your driver will be used in Windows 8 as well as Windows 10, you need to run both versions of the kit. Include the results with your submission. See [HLK tools technical reference](https://msdn.microsoft.com/library/windows/hardware/dn939924) for more information. For information about required HCK tests, see [ELAM Prerequisites](https://docs.microsoft.com/windows-hardware/drivers/install/elam-prerequisites)

3. Follow the kernel mode driver signing policy as stated in the [Driver signing policy](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/kernel-mode-code-signing-policy--windows-vista-and-later-) topic.

4. Submit the driver package for evaluation at the [Windows Hardware Dev Center](https://developer.microsoft.com/en-us/windows)
