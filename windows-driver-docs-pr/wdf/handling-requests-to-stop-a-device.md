---
title: Handling Requests to Stop a Device
description: Handling Requests to Stop a Device
ms.assetid: 4c8f37b3-7961-4c78-a88b-3eec58155e66
keywords: ["PnP WDK KMDF , stopping devices", "Plug and Play WDK KMDF , stopping devices", "redistributing resources WDK KMDF", "resource redistribution WDK KMDF", "removing devices WDK KMDF", "device stop requests WDK KMDF", "device stop requests WKD KMDF , PnP", "temporary device stoppage WDK KMDF", "temporary device stoppage WDK KMDF , PnP"]
---

# Handling Requests to Stop a Device


There are two circumstances in which, before asking a device's drivers to stop a device, the PnP manager asks the drivers if stopping the device is a good idea:

-   A user has plugged in a new device, and the PnP manager must [redistribute the system's hardware resources](#redistributing-resources) to accommodate the new device.

-   A user has indicated that he or she would like to [remove the device](#a-user-removes-or-disables-a-device).

There are several ways in which a driver can handle these situations:

-   If your driver has called [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) because a device is supporting a special file, and if a special file is open on the device, the framework will not allow the device to be stopped.

-   To temporarily prevent all stoppages for a relatively short period of time, the driver can call [**WdfDeviceSetStaticStopRemove**](https://msdn.microsoft.com/library/windows/hardware/ff546915).

-   To evaluate and process each stop attempt individually, the driver can provide [*EvtDeviceQueryStop*](https://msdn.microsoft.com/library/windows/hardware/ff540885) and [*EvtDeviceQueryRemove*](https://msdn.microsoft.com/library/windows/hardware/ff540883) callback functions.

If the device is not supporting special files, and if stopping or removing a device is never a problem for the driver or device, the driver doesn't provide *EvtDeviceQueryStop* and *EvtDeviceQueryRemove* callback functions and never calls **WdfDeviceSetStaticStopRemove**. In this case the PnP manager always stops the device without first checking to see if the driver allows it.

### <a href="" id="redistributing-resources"></a> Redistributing Resources

Sometimes the PnP manager must redistribute the system's hardware resources. Typically, this redistribution occurs because a bus driver has reported that a new device has been plugged in, and the new device requires already-assigned resources. Devices must be stopped before resources are reassigned.

If it is necessary for your driver to sometimes prevent the PnP manager from stopping a busy device, the driver can provide an [*EvtDeviceQueryStop*](https://msdn.microsoft.com/library/windows/hardware/ff540885) callback function. If your driver's *EvtDeviceQueryStop* callback function returns an error status value, the PnP manager will not stop the device.

If the driver determines that it is safe to stop the device, the callback function returns STATUS\_SUCCESS. If none of the device's other drivers prevent stoppage, the PnP manager temporarily stops the device.

For information about the order in which the framework calls a driver's event callback functions when the PnP manager stops a device to redistribute resources, see [The PnP Manager Redistributes System Resources](the-pnp-manager-redistributes-system-resources.md).

### <a href="" id="a-user-removes-or-disables-a-device"></a> A User Removes or Disables a Device

A user can remove or disable some devices. For example:

-   If your driver has set the **Removable** member (and not the **SurpriseRemovalOK** member) of the device's [**WDF\_DEVICE\_PNP\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551257) structure, the user can run the Unplug or Eject Hardware program and then unplug or eject the device.

-   If your driver has not set the **NotDisableable** member of the device's [**WDF\_DEVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff551284) structure, the user can use Device Manager to disable the device.

In such cases, the PnP manager attempts to stop the device before the user removes it.

If it is necessary for your driver to sometimes prevent removal of a busy device, the driver can provide an [*EvtDeviceQueryRemove*](https://msdn.microsoft.com/library/windows/hardware/ff540883) callback function. If any driver's *EvtDeviceQueryRemove* callback function returns an error status value, the PnP manager will not stop the device.

If the driver determines that it is safe for the user to remove the device, the callback function returns STATUS\_SUCCESS. If none of the device's other drivers prevent removal, the PnP manager stops the device.

For information about the order in which the framework calls a driver's event callback functions when stopping a device for removal, see [A User Unplugs a Device](a-user-unplugs-a-device.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20Requests%20to%20Stop%20a%20Device%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




