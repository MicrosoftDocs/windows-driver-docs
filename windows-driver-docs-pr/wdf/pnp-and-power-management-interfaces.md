---
title: PnP and Power Management Interfaces
description: PnP and Power Management Interfaces
ms.assetid: b80228f7-50be-4551-870b-2d7e2b5db239
keywords:
- Plug and Play WDK UMDF , power management interfaces
- PnP WDK UMDF , power management interfaces
- power management WDK UMDF , interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PnP and Power Management Interfaces


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

When a new device arrives in the system, the framework calls the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method to notify the UMDF driver of the arrival and passes the [**IWDFDriver**](https://msdn.microsoft.com/library/windows/hardware/ff558893) and [**IWDFDeviceInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff556965) interfaces in the call. The driver calls the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to create a framework device object for the device.

When drivers create a framework device object, they can register the following interfaces so that the framework notifies the driver—by calling the methods associated with the interfaces—when Plug and Play (PnP) and power management (PM) events occur.

[**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762)

[**IPnpCallbackSelfManagedIo**](https://msdn.microsoft.com/library/windows/hardware/ff556776)

[**IPnpCallbackHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556764)

[**IPowerPolicyCallbackWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff556815)

[**IPowerPolicyCallbackWakeFromSx**](https://msdn.microsoft.com/library/windows/hardware/ff556825)

 

 





