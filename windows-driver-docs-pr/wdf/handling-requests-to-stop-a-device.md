---
title: Handling Requests to Stop a Device
description: Handling Requests to Stop a Device
keywords:
- PnP WDK KMDF , stopping devices
- Plug and Play WDK KMDF , stopping devices
- redistributing resources WDK KMDF
- resource redistribution WDK KMDF
- removing devices WDK KMDF
- device stop requests WDK KMDF
- device stop requests WKD KMDF , PnP
- temporary device stoppage WDK KMDF
- temporary device stoppage WDK KMDF , PnP
ms.date: 04/20/2017
---

# Handling Requests to Stop a Device


There are two circumstances in which, before asking a device's drivers to stop a device, the PnP manager asks the drivers if stopping the device is a good idea:

-   A user has plugged in a new device, and the PnP manager must [redistribute the system's hardware resources](#redistributing-resources) to accommodate the new device.

-   A user has indicated that he or she would like to [remove the device](#a-user-removes-or-disables-a-device).

There are several ways in which a driver can handle these situations:

-   If your driver has called [**WdfDeviceSetSpecialFileSupport**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetspecialfilesupport) because a device is supporting a special file, and if a special file is open on the device, the framework will not allow the device to be stopped.

-   To temporarily prevent all stoppages for a relatively short period of time, the driver can call [**WdfDeviceSetStaticStopRemove**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetstaticstopremove).

-   To evaluate and process each stop attempt individually, the driver can provide [*EvtDeviceQueryStop*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_stop) and [*EvtDeviceQueryRemove*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_remove) callback functions.

If the device is not supporting special files, and if stopping or removing a device is never a problem for the driver or device, the driver doesn't provide *EvtDeviceQueryStop* and *EvtDeviceQueryRemove* callback functions and never calls **WdfDeviceSetStaticStopRemove**. In this case the PnP manager always stops the device without first checking to see if the driver allows it.

### <a href="" id="redistributing-resources"></a> Redistributing Resources

Sometimes the PnP manager must redistribute the system's hardware resources. Typically, this redistribution occurs because a bus driver has reported that a new device has been plugged in, and the new device requires already-assigned resources. Devices must be stopped before resources are reassigned.

If it is necessary for your driver to sometimes prevent the PnP manager from stopping a busy device, the driver can provide an [*EvtDeviceQueryStop*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_stop) callback function. If your driver's *EvtDeviceQueryStop* callback function returns an error status value, the PnP manager will not stop the device.

If the driver determines that it is safe to stop the device, the callback function returns STATUS\_SUCCESS. If none of the device's other drivers prevent stoppage, the PnP manager temporarily stops the device.

For information about the order in which the framework calls a driver's event callback functions when the PnP manager stops a device to redistribute resources, see [The PnP Manager Redistributes System Resources](the-pnp-manager-redistributes-system-resources.md).

### <a href="" id="a-user-removes-or-disables-a-device"></a> A User Removes or Disables a Device

A user can remove or disable some devices. For example:

-   If your driver has set the **Removable** member (and not the **SurpriseRemovalOK** member) of the device's [**WDF\_DEVICE\_PNP\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_pnp_capabilities) structure, the user can run the Unplug or Eject Hardware program and then unplug or eject the device.

-   If your driver has not set the **NotDisableable** member of the device's [**WDF\_DEVICE\_STATE**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_state) structure, the user can use Device Manager to disable the device.

In such cases, the PnP manager attempts to stop the device before the user removes it.

If it is necessary for your driver to sometimes prevent removal of a busy device, the driver can provide an [*EvtDeviceQueryRemove*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_remove) callback function. If any driver's *EvtDeviceQueryRemove* callback function returns an error status value, the PnP manager will not stop the device.

If the driver determines that it is safe for the user to remove the device, the callback function returns STATUS\_SUCCESS. If none of the device's other drivers prevent removal, the PnP manager stops the device.

For information about the order in which the framework calls a driver's event callback functions when stopping a device for removal, see [A User Unplugs a Device](a-user-unplugs-a-device.md).

 

