---
Description: Describes the limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism.
title: Limitations of USB 2.0 mechanism
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Limitations of USB 2.0 mechanism


Describes the limitations of the Universal Serial Bus (USB) 2.0 Selective Suspend mechanism. It then provides an overview of the USB 3.0 Link Power Management (LPM) feature and how it can be used in conjunction with the Selective Suspend mechanism to reduce system power consumption. Finally, it lists the common pitfalls in LPM implementation in USB controllers, hubs, and devices.

The USB 2.0 specification defines a mechanism for conserving power that allows a device (or a hub) to enter suspended state when not in use. This mechanism is known as [Selective Suspend](http://go.microsoft.com/fwlink/p/?linkid=230962). Selective Suspend is a powerful mechanism that conserves power but has exit latency in tens of milliseconds. Selective Suspend requires the software to cancel all transfers to the device and then explicitly send the device to the suspended state. Consequently, this mechanism is practical only when the device has been idle for a long time, typically in seconds.

Selective Suspend also imposes strict power consumption limits on the device in the suspended state. Those limits are significantly less than limits that are imposed on the device when it is in the working state. If the device cannot maintain the desired wake-up functionality while restricting itself to that imposed limit, it cannot be sent to Selective Suspend.

For example, at a certain current limit, a mouse might not be able to wake up from Selective Suspend when a user moves the mouse, because there is not enough power for the optical sensors. The same mouse might be able to wake up as a result of a button press. Such a mouse cannot be sent to Selective Suspend without compromising the user experience.

 

 




