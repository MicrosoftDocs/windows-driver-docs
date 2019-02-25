---
title: Example WDM Device Stack
description: Example WDM Device Stack
ms.assetid: 1128e098-9ef4-4bc3-aa09-74df3142fb11
keywords: ["device stacks WDK kernel , examples", "joystick WDK device stacks", "functional device objects WDK kernel", "FDO WDK kernel", "physical device objects WDK kernel", "PDOs WDK kernel", "filter DOs WDK kernel", "USB hub device stacks WDK kernel", "USB host controller device stacks WDK kernel", "PCI bus device stacks WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Example WDM Device Stack





This section describes the device objects created by a possible set of drivers for USB hardware to illustrate WDM device objects and how they are layered.

The following figure shows the device objects that are created by the sample drivers described in [WDM Driver Layers: An Example](wdm-driver-layers---an-example.md).

![diagram illustrating sample wdm device object layers for a usb joystick](images/joydobj.png)

Starting at the bottom of this figure, the device objects in the sample device stacks include:

1.  A PDO and an FDO for the PCI bus.

    The root bus driver enumerates the internal system bus (the root bus) and creates a PDO for each device it finds. One of these PDOs is for the PCI bus. (The PDO and FDO for the root bus are not shown in the figure.)

    The PnP manager identifies the PCI driver as the function driver for the PCI bus, loads the driver (if it is not already loaded), and passes the PDO to the PCI driver. In its [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, the PCI driver creates an FDO for the PCI bus ([**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)) and attaches the FDO to the device stack ([**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)) for the PCI bus. The PCI driver creates and attaches this FDO as part of its responsibilities as the function driver for the PCI bus.

    There are no filter drivers for the PCI bus in this example.

2.  A PDO and an FDO for the USB host controller.

    The PnP manager directs the PCI driver to start its device ([**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)) and then queries the PCI driver for its children ([**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) with relation type of **BusRelations**). In response, the PCI driver enumerates the devices on its bus. In this example, the PCI driver finds a USB host controller and creates a PDO for that device. The wide arrow in the figure indicates that the USB host controller is a "child" of the PCI bus. The PCI driver creates PDOs for its child devices as part of its responsibilities as the bus driver for the PCI bus.

    The PnP manager identifies the USB host controller miniclass/class driver pair as the function driver for the USB host controller and loads the driver pair. The PnP manager calls the driver pair at the appropriate time to create and attach an FDO for the USB host controller.

    There are no filter drivers for the USB host controller in this example.

3.  A PDO and an FDO for the USB hub.

    The USB host controller enumerates its bus, locates the USB hub in the sole port, and creates a PDO for the hub. The USB hub driver creates and attaches an FDO for the hub.

    There are no filter drivers for the USB hub in this example.

4.  A PDO, an FDO, and two filter DOs for the joystick device.

    The USB hub driver enumerates its bus, locates a HID device (the joystick), and creates a PDO for the joystick.

    In this example, a lower-level filter driver has been set up in the registry for joystick devices, so the PnP manager loads the filter driver. The filter driver determines that it is relevant to the device and creates and attaches a filter DO to the device stack.

    The PnP manager determines that the function driver for the joystick device is the HID class/miniclass driver pair and loads those drivers. The driver pair consists of a miniclass driver linked to a class driver DLL; together they act as one function driver for the device. The class/miniclass driver pair creates one device object, the FDO, and attaches it to the device stack.

    An upper-level filter driver creates and attaches a filter DO to the device stack, in a manner similar to the lower-level filter.

Note that the PDO created by the parent bus driver is always at the bottom of the device stack for a particular device. When drivers handle PnP or power IRPs, they must pass each IRP all the way down the device stack to the PDO and its associated bus driver.

The following figure shows the same device stacks as the previous figure, but emphasizes which device objects are created and managed by which drivers.

![diagram illustrating sample device object layers from the driver perspective](images/joydobj2.png)

A bus driver spans more than one device stack. A bus driver creates the FDO for its bus adapter/controller and creates a PDO for each of its child devices.

 

 




