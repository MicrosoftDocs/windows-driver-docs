---
title: Event Reporting
author: windows-driver-content
description: Event Reporting
ms.assetid: 4c3ffa7e-d0b3-483c-9f6b-3fe8ae997cf0
---

# Event Reporting


## <a href="" id="ddk-event-reporting-si"></a>


The WIA architecture enables a still image device to notify the WIA minidriver when some action on the device occurs. For example, a scanner might have a push-button on its front panel, enabling the user to initiate a scan directly from the device. The WIA minidriver must be notified of this event so it can notify the WIA service. All running applications that have registered to receive this event are notified. Furthermore, if an application has registered to be started as a result of this event prior to the event, the WIA service starts that application.

The WIA architecture supports interrupt events and polled events. For more information about these events, see [WIA Driver Event Support](wia-driver-event-support.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Event%20Reporting%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


