---
title: Subscribing for messages
description: Subscribing for messages
ms.assetid: CF0D5CE0-A0E0-47D4-88E6-FBE186F78626
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Subscribing for messages


Clients can subscribe to messages by type. When messages are received, the NFP provider will only issue messages to clients that have a subscription for that exact type. The receiving client will have no knowledge of where or when the message was published unless such info is placed within the message by the publisher. There are no means within the model to determine what other clients also received the message.

Subscriptions have the same lifetime model as published messages.

When a client unsubscribes for a message it should no longer be issued messages that match the unsubscribed subscription type.

## Subscribed Message Arrival


When the NFP provider receives a message, it will deliver it to any subscribed clients. Messages are delivered to clients only when the subscription type matches the published message.

There is no ordering or priority defined in the model. It is acceptable for the provider to issue subscribed messages in parallel, but this is not required.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

