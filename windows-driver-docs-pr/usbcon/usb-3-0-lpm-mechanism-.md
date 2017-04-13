---
Description: This topic describes the USB 3.0 LPM mechanism.There is an addendum to the official USB 2.0 Specification (USB2\_LinkPowerMangement\_ECN), which defines LPM for newer USB 2.0 hardware.
MS-HAID: buses.usb\_3\_0\_lpm\_mechanism\_
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB 3.0 LPM mechanism
---

# USB 3.0 LPM mechanism


This topic describes the USB 3.0 LPM mechanism.

There is an addendum to the official [USB 2.0 Specification](http://go.microsoft.com/fwlink/p/?linkid=230961) (USB2\_LinkPowerMangement\_ECN), which defines LPM for newer USB 2.0 hardware. This topic does not cover that USB 2.0 LPM mechanism. The purpose of this topic is to describe USB 3.0 LPM states, specifically U1 and U2.

USB 3.0 devices also support Selective Suspend. To overcome the limitations of Selective Suspend, the official USB 3.0 specification defines finer-grained power management states. Before describing those states and how they can be used to improve power management, let’s first understand the concept of a link.

## What is a link


A USB connection exists between two USB ports:

-   The downstream port (DS port) of a host or a hub.
-   The upstream port (US port) of an attached device or hub.

A *link* is a pair of DS and US ports; the ports are known as link partners. Each port has two layers. The physical layer transmits or receives sequences of bytes or other control signals. The logical layer manages the physical layer and ensures smooth flow of information between the link partners. The logical layer is also responsible for any buffering that might be required for the information flow.

## U states


As per the USB 2.0 specification, a link enters a low power state (consuming less power than the working state) only when the downstream device enters the suspended state through the Selective Suspend mechanism. The USB 3.0 specification decouples link power states from device power states. The specification defines the LPM feature (see Section C.1 in the specification) that refers to power management of physical and logical layers of a pair of ports that constitute a link. The specification defines four link power states known as U states, from U0 to U3. An active link is in state U0.

After remaining idle for a certain period of time, link partners progressively enter U1 (standby with fast exit) and then U2 (standby with slower exit). After they are idle for sufficient time, software initiates the transition to U3 by sending a command to the DS port link partner.

The steps that are required by software, to send the link to U3, are identical to the steps required for USB 2.0 Selective suspend. The device must enter the suspended state when the link enters U3. As a result, the device is subject to similar restrictions as with USB 2.0 Selective Suspend. To overcome those limitations, the USB 3.0 specification defines U1 and U2 states.

## <a href="" id="advantages-of-u1-and-u2-"></a>Advantages of U1 and U2


U1 and U2 states are designed to complement Selective Suspend, which can lead to significant power savings. After the software configures the link partners for U1 or U2 transition, the hardware enters the states autonomously without any software intervention. The exit times from U1 and U2 are really fast (from microseconds to a few milliseconds) and have less of an impact on the performance of the devices. This allows for much better power management where links can enter and exit these states even when the device is in use.

For example, a device with isochronous endpoints can put the link to U1 or U2 between service intervals. To save some power, when the device is idle, it can send its upstream link to those states even before Selective Suspend gets invoked. There are no restrictions on how much power the device can draw when the link is in U1 or U2. A device could remain fully powered when the link is in U1 or U2. Therefore, unlike Selective Suspend, a device can send its link to U1 or U2 without losing any capabilities.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%203.0%20LPM%20mechanism%20%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



