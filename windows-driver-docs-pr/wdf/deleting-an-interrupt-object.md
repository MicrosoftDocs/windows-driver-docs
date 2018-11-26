---
title: Deleting an Interrupt Object
description: Deleting an Interrupt Object
ms.assetid: B72DA452-B22F-47CD-8C5D-E741F09F556E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting an Interrupt Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

If the driver creates an interrupt object by calling [**IWDFDevice3::CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208), the driver does not need to delete the interrupt object. The framework deletes the interrupt object automatically because the interrupt object is a child object of the framework device object.

The framework uses the following rules:

-   If the driver calls [**CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) from its [**OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) callback method, the framework deletes the interrupt object after the driver returns from its [**OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439739) callback.

-   If the driver calls [**CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) from its [**OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback method, the framework deletes the interrupt object when the device is removed.

Optionally, the driver can call [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) to delete an interrupt object at any time. Because a driver cannot create a new interrupt object outside of [**OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) or [**OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734), manual deletion of the object should not be used unless the driver must remove the object before the framework deletes it.

 

 





