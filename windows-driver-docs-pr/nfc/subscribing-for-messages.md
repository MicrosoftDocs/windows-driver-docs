---
title: Subscribing for messages
author: windows-driver-content
description: Subscribing for messages
ms.assetid: CF0D5CE0-A0E0-47D4-88E6-FBE186F78626
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# Subscribing for messages


Clients can subscribe to messages by type. When messages are received, the NFP provider will only issue messages to clients that have a subscription for that exact type. The receiving client will have no knowledge of where or when the message was published unless such info is placed within the message by the publisher. There are no means within the model to determine what other clients also received the message.

Subscriptions have the same lifetime model as published messages.

When a client unsubscribes for a message it should no longer be issued messages that match the unsubscribed subscription type.

## Subscribed Message Arrival


When the NFP provider receives a message, it will deliver it to any subscribed clients. Messages are delivered to clients only when the subscription type matches the published message.

There is no ordering or priority defined in the model. It is acceptable for the provider to issue subscribed messages in parallel, but this is not required.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Subscribing%20for%20messages%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




