---
title: NFP power management
description: NFP power management
ms.assetid: A47F4B01-A912-410A-8CF8-656D2C125148
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFP power management


NFP devices operate in one of three power modes. These modes are *active*, *idle*, *standby*, and *power-removed*. The NFP device can enter a low-power mode when publications or subscriptions to the device are disabled. The NFP driver will transition the device to one of the power modes in response to an enable or disable notification from Windows.

The NFP driver will receive an [**IOCTL\_NFP\_ENABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853316) or an [**IOCTL\_NFP\_DISABLE**](https://msdn.microsoft.com/library/windows/hardware/jj853315) control code to enable or disable subscriptions, publications, and presence events. These control codes will also trigger a power mode change for the device. The [Near-field proximity (NFP) power management for connected standby platforms](https://msdn.microsoft.com/library/windows/hardware/mt614845) topic provides detailed description of power mode changes for NFP devices.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

