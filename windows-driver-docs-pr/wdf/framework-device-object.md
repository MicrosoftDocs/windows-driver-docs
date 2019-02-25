---
title: Framework Device Object
description: Framework Device Object
ms.assetid: 6be47eac-d6e4-43d1-bf2d-d49dcb2273c0
keywords:
- UMDF objects WDK , device objects
- framework objects WDK UMDF , device objects
- device objects WDK UMDF
- IWDFDevice
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Device Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework device object is exposed to drivers by the [IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917) interface. The framework device object is the framework representation of the device on the system. Each device object has a parent driver object.

When a new device arrives in the system, the framework calls the [**IDriverEntry::OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) method to notify the driver of the arrival and passes the [IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893) and [IWDFDeviceInitialize](https://msdn.microsoft.com/library/windows/hardware/ff556965) interfaces in the call. The driver can call methods of the IWDFDeviceInitialize interface to initialize the new device. For example, the driver calls the [**IWDFDeviceInitialize::RetrieveDevicePropertyStore**](https://msdn.microsoft.com/library/windows/hardware/ff556982) method to query for the device information that is provided as part of device installation. The driver can then call the [**IWDFDriver::CreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff558899) method to configure and create the device object.

When drivers create a framework device object, they can register their [IPnpCallback](https://msdn.microsoft.com/library/windows/hardware/ff556762), [IPnpCallbackSelfManagedIo](https://msdn.microsoft.com/library/windows/hardware/ff556776), [IPnpCallbackHardware](https://msdn.microsoft.com/library/windows/hardware/ff556764), [IFileCallbackCleanup](https://msdn.microsoft.com/library/windows/hardware/ff554902), and [IFileCallbackClose](https://msdn.microsoft.com/library/windows/hardware/ff554907) interfaces. The framework then notifies the driver when file cleanup and close and Plug and Play (PnP) and power management (PM) events occur. For more information about supporting PnP and PM, see [PnP and Power Management in UMDF-based Drivers](pnp-and-power-management-in-umdf-drivers.md).

 

 





