---
Description: Describes the architecture of the USB function stack.
title: USB device-side drivers in Windows
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB device-side drivers in Windows


Describes the architecture of the USB function stack.




On a USB device, the USB function stack refers to a group of drivers that are enumerated by the Plug and Play Manager, when ACPI creates a USB device physical device object (PDO).

In a single configuration device, a USB device can define one or more interfaces. For example, the Media Transfer Protocol (MTP) for transferring files to and from the device. A composite USB device can support multiple interfaces in a single configuration. The USB function stack creates PDOs for each interface and PnP Manager loads the class driver that creates the function device object (FDO) for that interface.

The USB function stack is conceptualized in this image:

![usb function stack](images/usb-fn.png)

**Applications and Services**

-   All user-mode requests are sent to the Microsoft-provided kernel-mode class driver GenericUSBFn.sys. You can create a user-mode service that communicates with GenericUSBFn.sys by sending [these I/O control codes (IOCTLs)](https://msdn.microsoft.com/library/windows/hardware/mt188014), and the driver handles kernel-mode communication with the USB function drivers.

**USB function class driver**

A USB function class driver implements the functionality of a specific interface (or group of interfaces) on the USB device. MTP and IpOverUsb are examples of system-supplied class drivers. The class driver may be implemented purely as a kernel-mode driver, or it may be a user-mode service paired with the system-supplied class driver GenericUSBFn.sys.

A function class driver sends requests to the controller by using [USB function class driver to UFX programming interfaces](https://msdn.microsoft.com/library/windows/hardware/mt188008).

**USB function class extension (UFX)**

The USB function class extension (UFX) is a system-supplied extension to [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff551869) (KMDF). USB is a standard bus and has some required functionality and capabilities. UFX is responsible for implementing USB function logic that is common to all USB function controllers and handling and/or dispatching requests from USB function class drivers. In particular, UFX handles the process of enumerating the device and processing standard control transfers. To perform some of these operations, UFX needs to know about the capabilities of the bus. Those capabilities are reported to UFX when the class-extension interface is established.

UFX exposes standard IOCTLs that the upper layers (USB function class driver and user mode services) can use to send requests to the controller. Additionally, UFX notify upper layers about the standard requests received from the host.

**USB function client driver**

UFX provides an abstracted interface that works consistently across different controllers. However, controllers have different capabilities, with limitations such as the number of endpoints, the types of endpoints, low power, remote wake-up. For example, certain controllers support DMA, while others do not. Some controllers implement streams in the hardware while other controllers expect the driver to handle streams. For these reasons, only common functionality is handled in UFX. Transfers, power management, stream support, and other features which vary from controller to controller are handled by the client driver.

The USB function client driver is responsible for implementing controller-specific operations. These include implementing endpoint data transfers, USB device state changes (reset, suspend, resume), attach/detach detection, port/charger detection. The client driver is also responsible for handling power management, and PnP events.

The function client driver is written as [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff551869) (KMDF) driver by using [USB function class driver to UFX programming interfaces](https://msdn.microsoft.com/library/windows/hardware/mt188008).

Microsoft provides in-box function client drivers (UfxChipidea.sys, Ufxsynopsys.sys) for ChipIdea and Synopsys controllers.

**USB lower filter driver**

A USB lower filter driver supports detection of chargers if the function controller uses the in-box Synopsys and ChipIdea drivers. The filter driver manages USB charging starting from USB port detection. t must publish a GUID for each charger type it supports, and a list of that charger’s properties. If a specific charger is configurable, the lower USB filter driver defines a list of supported PropertyIDs and their corresponding value types that can be sent to it, to configure the charger. The driver also notifies the battery stack when it can begin charging and the maximum amount of current the device can draw. For client drivers other than Synopsys and ChipIdea drivers, charging logic can be implemented in the client driver.

A function class driver sends request to UFX by using [Programming interfaces for supporting proprietary chargers](https://msdn.microsoft.com/library/windows/hardware/mt188012).

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



