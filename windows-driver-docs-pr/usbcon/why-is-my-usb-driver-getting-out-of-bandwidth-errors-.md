---
Description: Why is my USB driver getting out of bandwidth errors?
MS-HAID:
- 'usb-io\_cc4c3579-ca5f-47cf-bdac-6a88b05ec7be.xml'
- 'buses.why\_is\_my\_usb\_driver\_getting\_out\_of\_bandwidth\_errors\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: Why is my USB driver getting out of bandwidth errors?
---

# Why is my USB driver getting out of bandwidth errors?


Competition for bandwidth on the USB bus comes from multiple sources, both hardware and software, so it is difficult to predict exactly how much bandwidth will be available for a USB client driver. The USB host controller requires a certain amount of bandwidth for its operations, but the amount required depends on whether the controller is high speed or not, so it will vary from system to system. USB hubs that operate at high speed must sometimes translate transactions between high-speed upstream ports and low-speed devices downstream, and this translation process consumes bandwidth. But whether bandwidth is required for transaction translation depends on the kind of devices that are connected and the topology of the device tree.

The most serious strain on bandwidth resource usually comes from USB client drivers that monopolize bandwidth. The system allocates bandwidth on a first-come-first-serve basis. If the first USB driver loaded requests all of the available bandwidth, a USB driver that loads at a later time will not obtain any bandwidth at all for its device. When this occurs, the system cannot configure the device and fails to enumerate it. Since it is usually not apparent why the enumeration failed, this can lead to a bad user experience.

Occasionally, a client driver will exhaust the available bandwidth with a high-speed interrupt transfer. But the most common case, by far, is that of a client driver that allocates too much bandwidth for an isochronous transfer, then fails to release the bandwidth in a timely fashion. The system reserves allocated bandwidth until the driver that requested it closes its endpoint (by opening another endpoint), or the device for which the bandwidth was allocated is removed. The system does not allocate guaranteed bandwidth for bulk transfers, so bulk transfers are never the cause of enumeration failures. However, the performance of bulk transfer devices depends on how much bandwidth is allocated for devices that do periodic (isochronous and interrupt) transfers.

The USB 2.0 specification requires an isochronous device to have zero-bandwidth endpoints on its default interface setting. This ensures that no bandwidth is reserved for the device until a function driver opens a non-default interface, which, in turn, helps prevent enumeration failures caused by excessive bandwidth requests during device configuration. However, it does not prevent a client driver from allocating too much bandwidth after configuring its device, thereby preventing other devices from functioning properly.

The key to proper bandwidth management is that every USB device in the system that does isochronous transfers must offer multiple alternative (Alt) settings for each interface that contains isochronous endpoints, and client drivers must make judicious use of these Alt settings. Client drivers should begin by requesting the interface setting with the highest bandwidth. If the request fails, the client driver should request interface settings with smaller and smaller bandwidths until a request succeeds.

For instance, suppose a webcam device has the following interfaces:

Interface 0 (Default interface setting: No endpoints with nonzero isochronous bandwidth in the default setting)

Isochronous Endpoint 1: maximum packet size = 0 bytes

Isochronous Endpoint 2: maximum packet size = 0 bytes

Interface 0 Alt setting 1

Isochronous Endpoint 1: maximum packet size = 256 bytes

Isochronous Endpoint 2: maximum packet size = 256 bytes

Interface 0 Alt setting 2

Isochronous Endpoint 1: maximum packet size = 512 bytes

Isochronous Endpoint 2: maximum packet size = 512 bytes

The driver for the webcam configures the webcam to use the default interface setting when it initializes. The default setting has no isochronous bandwidth, so using the default setting during initialization avoids the danger that the webcam might fail to enumerate, because of a failed request for isochronous bandwidth.

When the client driver is ready to do an isochronous transfer, it should attempt to use Alt setting 2, because Alt setting 2 has the largest packet size. If the request fails, the driver can make a second attempt, using Alt setting 1. Since Alt setting 1 requires less bandwidth, this request might succeed, even though the first request failed. Multiple Alt settings allow the driver to make several attempts, before giving up.

After the webcam becomes idle, it can return the allocated bandwidth to the free bandwidth pool by selecting the default setting once again.

Starting with Windows Vista, users can see how much bandwidth a USB controller has allocated by checking the controller's properties in the Device Manager. Select the controller's properties then look under the Advanced tab. This reading does not indicate how much bandwidth USB hubs have allocated for transaction translation.

The Device Manager feature that reports the bandwidth usage of a USB controller does not work properly in Windows XP.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Why%20is%20my%20USB%20driver%20getting%20out%20of%20bandwidth%20errors?%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



