---
title: Message Transmission
description: Message Transmission
ms.assetid: 96C5CE38-25EE-425A-A7C5-05990CBE2C3E
---

# Message Transmission


When the NFP technology determines that another device is proximate, as defined by the proximity technology, this should act as the trigger to transmit published messages between the devices.

Published messages should be transmitted exactly once while the devices are within proximity.

All currently published messages should be transmitted each time a device comes within proximity.

If a message is published while devices are proximate and the trigger is still active, that message should be transmitted.

Delivery of a publication to a proximate device does not mean that publication should be unpublished by the NFP provider. The publication stays active for the next proximate event until the client unpublishes it.

The NFP device driver interface does not require that the published messages be transmitted in the order they were published. The NFP device driver interface does not require that all published messages be transmitted as a single block. NFC specifically has detailed interop requirements that prevent this: transmitting multiple messages as a single block is NOT permitted. However, it is a requirement that individual published messages be received completely and without errors or they should not be handed to subscribed clients.

There is no mechanism defined in the NFP device driver interface to inform clients if any app on a receiving device was subscribed to the message. There is also no mechanism for telling clients that a message they are not subscribed to was received.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Message%20Transmission%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




