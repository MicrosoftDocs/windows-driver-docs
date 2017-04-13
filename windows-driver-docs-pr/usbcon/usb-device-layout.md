---
Description: A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts.
MS-HAID: buses.usb\_device\_layout
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB device layout
---

# USB device layout


A Universal Serial Bus (USB) device defines its capabilities and features through configurations, interfaces, alternate settings, and endpoints. This topic provides a high-level overview of those concepts.

A *USB configuration* defines the capabilities and features of a device, mainly its power capabilities and interfaces. The device can have multiple configurations, but only one is active at a time. The active configuration isn't chosen by the USB driver stack, but might be initiated by an application, a driver, the device driver. The device driver selects an active configuration.

A configuration can have one or more *USB interfaces* that define the functionality of the device. Typically, there is a one-to-one correlation between a function and an interface. However, certain devices expose multiple interfaces related to one function. In that case, the device can have an interface association descriptor (IAD). An IAD groups together interfaces that belong to a particular function.

Each interface contains one or more *endpoints*, which are used to transfer data to and from the device. In addition, the interface contains *alternate settings* that define the bandwidth requirements of the function associated with the interface. To sum up, a group of endpoints form an interface, and a set of interfaces constitutes a configuration in the device.

So what does it mean to select an active configuration? During device initialization, the device driver for USB device must select a configuration, one or more or interfaces within that configuration, and an alternate setting for each interface. Most USB devices don't provide multiple interfaces or multiple alternate settings. For example, the OSR USB FX2 Learning Kit device has one interface with one alternate setting and three endpoints. For more information about the learning kit, see [OSR Online](http://www.osronline.com/).

**Single interface device**

This diagram shows the configuration of a device with a single interface:

![usb device layout for single interface device](images/device-layout-single.png)

In this example, the diagram shows Endpoint 0, called the *default endpoint*. All USB devices must have a default endpoint that is used for control transfers (see [USB Control Transfer](usb-control-transfer.md)). Configuration 0 has one interface: Interface 0 with one alternate setting. Alternate Setting 0 uses all three endpoints in the interface.

**Multiple-interfaces device**

For multifunction devices, the device has multiple interfaces. To use a particular function or an interface, the client driver selects the interface and an associated alternate setting. Consider a multi-function USB device such as a webcam. The device has two functions, video-capture (camera) and audio input (microphone). The device defines an endpoint in a video interface that streams video. The device has another endpoint in a separate interface that takes audio input through the microphone. The configuration of the device includes both of these interfaces.

This diagram shows the configuration of the webcam device:

![device layout for multiple interface device](images/device-descriptors-multi.png)

In this example, the diagram shows the default endpoint. Configuration 0 has two interfaces: Interface 0 and Interface 1. Interface 0 has three alternate settings. Only one of the alternate settings is active at any given time. Notice that Alternate Setting 0 doesn't use an endpoint, whereas Alternate Settings 1 and 2 use Endpoint 1. Typically, a video camera uses an *isochronous endpoint* for streaming. For that type of endpoint, when the endpoint is in use, bandwidth is reserved on the bus. When the camera is not streaming video, the client driver can select Alternate Setting 0 to conserve bandwidth. When the webcam is streaming video, the client driver can switch to either Alternate Setting 1 or Alternate Setting 2, which provides increasing levels of quality and consumes increasing bus bandwidth. Interface 1 has two alternate settings. Similar to Interface 0, Alternate Setting 0 doesn't use an endpoint. Alternate Setting 1 is defined to use Endpoint 1.

Endpoints can't be shared between two interfaces within a configuration. The device uses the endpoint address to determine the target endpoint for a data transfer or endpoint operation, such as pipe reset. All those operations are initiated by the host.

Before you start using the device, get information about the device layout. [USBView](https://msdn.microsoft.com/library/windows/hardware/86CB0BEE-0C2E-426E-866A-CECF07837457.aspx) is an application that enables you to browse all USB controllers and the USB devices that are connected to them. For each connected device, you can view the device, configuration, interface, and endpoint descriptors to get an idea about the capability of the device.

Next, see [Standard USB descriptors](standard-usb-descriptors.md).

## Related topics


[Concepts for all USB developers](usb-concepts-for-all-developers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20device%20layout%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




