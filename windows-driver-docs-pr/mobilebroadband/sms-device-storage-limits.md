---
title: SMS device storage limits
description: SMS device storage limits
ms.assetid: b2491562-352e-4881-99c7-98d43aeec64b
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SMS device storage limits


SMS client apps should use SMS device storage as a message queue. Total SMS storage on devices varies, but device storage is commonly limited to 30 messages.

The Mobile Broadband SMS platform is designed to maintain the ability to receive new incoming SMS messages by freeing up SMS device storage space while minimizing deletion of user data.

Devices can’t receive new SMS messages if SMS storage becomes full. Windows automatically deletes old SMS messages from device storage to ensure the ability to receive new incoming SMS data, such as important mobile network operator notifications.

We recommend the following:

-   SMS client apps should use local app storage to maintain message history instead of relying on device SMS storage.

-   SMS client apps should not delete messages on read. SMS client apps should let Windows automatically delete old messages when device storage gets full.

## <span id="related_topics"></span>Related topics


[Developing SMS apps](developing-sms-apps.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20SMS%20device%20storage%20limits%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





