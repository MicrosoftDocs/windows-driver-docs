---
title: Example WDM Device Stack
description: Example WDM Device Stack
keywords: ["device stacks WDK kernel , examples", "joystick WDK device stacks", "functional device objects WDK kernel", "FDO WDK kernel", "physical device objects WDK kernel", "PDOs WDK kernel", "filter DOs WDK kernel", "USB hub device stacks WDK kernel", "USB host controller device stacks WDK kernel", "PCI bus device stacks WDK kernel"]
ms.date: 10/10/2025
ms.topic: concept-article
---

# Example WDM Device Stack

This section describes the device objects that a set of drivers might create for USB hardware. It illustrates WDM device objects and how they layer.

The following figure shows the device objects that the sample drivers create. For more information, see [WDM Driver Layers: An Example](wdm-driver-layers---an-example.md).

![diagram illustrating sample wdm device object layers for a usb joystick.](images/joydobj.png)

Starting at the bottom of this figure, the device objects in the sample device stacks include:

1. A PDO and an FDO for the PCI bus.

   The root bus driver enumerates the internal system bus (the root bus) and creates a PDO for each device it finds. One of these PDOs is for the PCI bus. (The figure doesn't show the PDO and FDO for the root bus.)

   The PnP manager identifies the PCI driver as the function driver for the PCI bus, loads the driver (if it's not already loaded), and passes the PDO to the PCI driver. In its [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, the PCI driver creates an FDO for the PCI bus ([**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice)) and attaches the FDO to the device stack ([**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)) for the PCI bus. The PCI driver creates and attaches this FDO as part of its responsibilities as the function driver for the PCI bus.

   This example doesn't include filter drivers for the PCI bus.

1. A PDO and an FDO for the USB host controller.

   The PnP manager directs the PCI driver to start its device ([**IRP_MN_START_DEVICE**](./irp-mn-start-device.md)) and then queries the PCI driver for its children ([**IRP_MN_QUERY_DEVICE_RELATIONS**](./irp-mn-query-device-relations.md) with relation type of **BusRelations**). In response, the PCI driver enumerates the devices on its bus. In this example, the PCI driver finds a USB host controller and creates a PDO for that device. The wide arrow in the figure indicates that the USB host controller is a "child" of the PCI bus. The PCI driver creates PDOs for its child devices as part of its responsibilities as the bus driver for the PCI bus.

   The PnP manager identifies the USB host controller miniclass/class driver pair as the function driver for the USB host controller and loads the driver pair. The PnP manager calls the driver pair at the appropriate time to create and attach an FDO for the USB host controller.

   This example doesn't include filter drivers for the USB host controller.

1. A PDO and an FDO for the USB hub.

   The USB host controller enumerates its bus, locates the USB hub in the sole port, and creates a PDO for the hub. The USB hub driver creates and attaches an FDO for the hub.

   This example doesn't include filter drivers for the USB hub.

1. A PDO, an FDO, and two filter DOs for the joystick device.

   The USB hub driver enumerates its bus, locates a HID device (the joystick), and creates a PDO for the joystick.

   In this example, a lower-level filter driver is set up in the registry for joystick devices, so the PnP manager loads the filter driver. The filter driver determines that it's relevant to the device and creates and attaches a filter DO to the device stack.

   The PnP manager determines that the function driver for the joystick device is the HID class/miniclass driver pair and loads those drivers. The driver pair consists of a miniclass driver linked to a class driver DLL. Together they act as one function driver for the device. The class/miniclass driver pair creates one device object, the FDO, and attaches it to the device stack.

   An upper-level filter driver creates and attaches a filter DO to the device stack, in a manner similar to the lower-level filter.

The parent bus driver always creates the PDO at the bottom of the device stack for a particular device. When drivers handle PnP or power IRPs, they must pass each IRP all the way down the device stack to the PDO and its associated bus driver.

The following figure shows the same device stacks as the previous figure, but emphasizes which device objects each driver creates and manages.

![diagram illustrating sample device object layers from the driver perspective.](images/joydobj2.png)

A bus driver spans more than one device stack. A bus driver creates the FDO for its bus adapter or controller and creates a PDO for each of its child devices.
