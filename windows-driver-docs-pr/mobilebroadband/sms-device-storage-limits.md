---
title: SMS device storage limits
description: SMS device storage limits
ms.assetid: b2491562-352e-4881-99c7-98d43aeec64b
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 






