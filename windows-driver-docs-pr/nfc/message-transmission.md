---
title: Message Transmission
description: Message transmission
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Message transmission

When the NFP technology determines that another device is proximate, as defined by the proximity technology, this should act as the trigger to transmit published messages between the devices.

Published messages should be transmitted exactly once while the devices are within proximity.

All currently published messages should be transmitted each time a device comes within proximity.

If a message is published while devices are proximate and the trigger is still active, that message should be transmitted.

Delivery of a publication to a proximate device does not mean that publication should be unpublished by the NFP provider. The publication stays active for the next proximate event until the client unpublishes it.

The NFP device driver interface does not require that the published messages be transmitted in the order they were published. The NFP device driver interface does not require that all published messages be transmitted as a single block. NFC specifically has detailed interop requirements that prevent this: transmitting multiple messages as a single block is NOT permitted. However, it is a requirement that individual published messages be received completely and without errors or they should not be handed to subscribed clients.

There is no mechanism defined in the NFP device driver interface to inform clients if any app on a receiving device was subscribed to the message. There is also no mechanism for telling clients that a message they are not subscribed to was received.

## Related topics

[Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
