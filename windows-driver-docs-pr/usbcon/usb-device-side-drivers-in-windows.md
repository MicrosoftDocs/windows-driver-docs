---
Description: Describes the architecture of the USB function stack.
title: USB device-side drivers in Windows
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# USB device-side drivers in Windows


Describes the architecture of the USB function stack.

## <a href="" id="stack"></a>


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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20device-side%20drivers%20in%20Windows%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


