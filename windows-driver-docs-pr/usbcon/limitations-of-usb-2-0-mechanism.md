---
Description: Describes the limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism.
title: Limitations of USB 2.0 mechanism
---

# Limitations of USB 2.0 mechanism


Describes the limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism. It then provides an overview of the USB 3.0 Link Power Management (LPM) feature and how it can be used in conjunction with the Selective Suspend mechanism to reduce system power consumption. Finally, it lists the common pitfalls in LPM implementation in USB controllers, hubs, and devices.

The USB 2.0 specification defines a mechanism for conserving power that allows a device (or a hub) to enter suspended state when not in use. This mechanism is known as [Selective Suspend](http://go.microsoft.com/fwlink/p/?linkid=230962). Selective Suspend is a powerful mechanism that conserves power but has exit latency in tens of milliseconds. Selective Suspend requires the software to cancel all transfers to the device and then explicitly send the device to the suspended state. Consequently, this mechanism is practical only when the device has been idle for a long time, typically in seconds.

Selective Suspend also imposes strict power consumption limits on the device in the suspended state. Those limits are significantly less than limits that are imposed on the device when it is in the working state. If the device cannot maintain the desired wake-up functionality while restricting itself to that imposed limit, it cannot be sent to Selective Suspend.

For example, at a certain current limit, a mouse might not be able to wake up from Selective Suspend when a user moves the mouse, because there is not enough power for the optical sensors. The same mouse might be able to wake up as a result of a button press. Such a mouse cannot be sent to Selective Suspend without compromising the user experience.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Limitations%20of%20USB%202.0%20mechanism%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


