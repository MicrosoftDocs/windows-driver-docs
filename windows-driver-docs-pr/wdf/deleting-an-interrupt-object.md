---
title: Deleting an Interrupt Object
author: windows-driver-content
description: Deleting an Interrupt Object
ms.assetid: B72DA452-B22F-47CD-8C5D-E741F09F556E
---

# Deleting an Interrupt Object


\[This topic applies to UMDF 1.*x*.\]

If the driver creates an interrupt object by calling [**IWDFDevice3::CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208), the driver does not need to delete the interrupt object. The framework deletes the interrupt object automatically because the interrupt object is a child object of the framework device object.

The framework uses the following rules:

-   If the driver calls [**CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) from its [**OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734) callback method, the framework deletes the interrupt object after the driver returns from its [**OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439739) callback.

-   If the driver calls [**CreateInterrupt**](https://msdn.microsoft.com/library/windows/hardware/hh451208) from its [**OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) callback method, the framework deletes the interrupt object when the device is removed.

Optionally, the driver can call [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) to delete an interrupt object at any time. Because a driver cannot create a new interrupt object outside of [**OnDeviceAdd**](https://msdn.microsoft.com/library/windows/hardware/ff554896) or [**OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/hh439734), manual deletion of the object should not be used unless the driver must remove the object before the framework deletes it.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Deleting%20an%20Interrupt%20Object%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




