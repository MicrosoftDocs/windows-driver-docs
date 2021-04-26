---
title: Static Enumeration
description: Static Enumeration
keywords:
- static enumeration WDK KMDF
- static child lists WDK KMDF
- traversing static child lists WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static Enumeration


*Static enumeration* is a driver's ability to detect and report the existence of devices during system initialization, with a limited ability to report subsequent changes to the system's configuration.

Bus drivers can use static enumeration if the number and type of devices or functional subunits is predetermined and permanent, and does not depend on the configuration of the system on which the driver is running.

For example, a sound card's driver might act as a bus driver and create separate physical device objects (PDOs) for each of the card's capabilities, such as MIDI, audio, and joystick.

### Static Child Lists

The framework enables drivers to support static enumeration by providing static child lists. Each static child list represents a list of child devices that are connected to a parent device. The bus driver for the parent device must identify the parent's child devices, add them to the parent device's static child list, and create a PDO for each child device.

### Creating a Static Child List

Each time a driver creates a framework device object that represents a functional device object (FDO) for a device, the framework creates an empty, static child list for the device.

When the framework calls a bus driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function, the callback function must call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create an FDO for the parent device. For more information about creating an FDO, see [Creating Device Objects in a Function Driver](creating-device-objects-in-a-function-driver.md).

The driver must then enumerate the parent device's children, create PDOs for the children, and add the children to the child list.

Optionally, the driver can call [**WdfDeviceSetBusInformationForChildren**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetbusinformationforchildren) to provide the framework with information about the bus. Doing so is recommended because it makes it easier for child devices and apps to identify the bus.

To create a PDO for a detected child device, the bus driver must:

1.  Call [**WdfPdoInitAllocate**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdoinitallocate) to obtain a [**WDFDEVICE\_INIT**](./wdfdevice_init.md) structure.

2.  Initialize the WDFDEVICE\_INIT structure.

3.  Call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object that represents a PDO.

For more information about creating a PDO, see [Creating Device Objects in a Bus Driver](creating-device-objects-in-a-bus-driver.md).

After calling **WdfDeviceCreate**, the driver must call [**WdfFdoAddStaticChild**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoaddstaticchild) to add the child device to the child list.

### Modifying a Static Child List

Because drivers should only use static child lists for device configurations that are predetermined and permanent, there is little need for a driver to modify a static child list after creating it. If the driver determines that a child device has become inaccessible, the driver can call [**WdfPdoMarkMissing**](/windows-hardware/drivers/ddi/wdfpdo/nf-wdfpdo-wdfpdomarkmissing). (If a child device remains accessible but becomes unresponsive and unusable, the driver should set the **Failed** member of the [**WDF\_DEVICE\_STATE**](/windows-hardware/drivers/ddi/wdfdevice/ns-wdfdevice-_wdf_device_state) structure to **WdfTrue** and then call [**WdfDeviceSetDeviceState**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetdevicestate).)

### Traversing a Static Child List

If you need to retrieve the contents of a static child list, the driver can traverse the list by doing the following:

1.  Calling [**WdfFdoLockStaticChildListForIteration**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdolockstaticchildlistforiteration).

2.  Calling [**WdfFdoRetrieveNextStaticChild**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoretrievenextstaticchild) as many times as necessary.

3.  Calling [**WdfFdoUnlockStaticChildListFromIteration**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdounlockstaticchildlistfromiteration).

 

