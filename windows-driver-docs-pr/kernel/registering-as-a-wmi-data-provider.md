---
title: Registering as a WMI Data Provider
description: Registering as a WMI Data Provider
keywords: ["WMI WDK kernel , registering with WMI", "registering WMI data providers", "data providers WDK WMI", "driver registrations WDK WMI", "event blocks WDK WMI", "blocks WDK WMI"]
ms.date: 06/16/2017
---

# Registering as a WMI Data Provider





A driver that supports WMI must register as a WMI data provider to make its data and event blocks available to WMI clients. A driver typically registers with WMI when starting its device, after the device has been initialized to the point that the driver can handle WMI IRPs. During the registration process, the driver passes WMI a pointer to its device object and information about the data and event blocks it supports.

A driver registers with WMI in two phases:

1.  The driver calls [**IoWMIRegistrationControl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iowmiregistrationcontrol) with the action WMIREG\_ACTION\_REGISTER and a pointer to the device object passed to the driver's [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine.

2.  The driver handles the [**IRP\_MN\_REGINFO**](./irp-mn-reginfo.md) or [**IRP\_MN\_REGINFO\_EX**](./irp-mn-reginfo-ex.md) request that WMI sends in response to the driver's **IoWMIRegistrationControl** call. The **Parameters.WMI.DataPath** member of the IRP is set to WMIREGISTER and **Parameters.WMI.ProviderId** is set to the driver's device object pointer. The driver supplies WMI with registration information about its data and event blocks, either by using the WMI Library as described in [Using the WMI Library to Register Blocks](using-the-wmi-library-to-register-blocks.md), or by handling the **IRP\_MN\_REGINFO** or **IRP\_MN\_REGINFO\_EX** requests as described in [Handling IRP\_MN\_REGINFO and IRP\_MN\_REGINFO\_EX to Register Blocks](handling-irp-mn-reginfo-and-irp-mn-reginfo-ex-to-register-blocks.md).

 

