---
title: Creating a SCO Client Connection to a Remote Device
description: Creating a SCO Client Connection to a Remote Device
keywords:
- Synchronous Connection-Oriented WDK Bluetooth
- SCO profile drivers WDK Bluetooth
- initiating SCO connections
ms.date: 01/10/2024
---

# Creating a SCO Client Connection to a Remote Device

A SCO client profile driver is a profile driver that requests Synchronous Connection-Oriented (SCO) connection to a remote device. If the device accepts the connection, the SCO client profile driver is notified of any changes to the connection. For example, a SCO client profile driver can request a connection to a remote headset, and after the headset accepts the connection request, the Bluetooth driver stack can notify the profile driver when the headset is turned off or removed.

Because SCO connections are point-to-point connections between two Bluetooth devices, a SCO client profile driver needs only the Bluetooth address of the remote device to connect to.

To initiate a SCO connection to a remote device, profile drivers should [build and send](building-and-sending-a-brb.md) a **[_BRB_SCO_OPEN_CHANNEL](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_open_channel)** request.

If the remote device accepts the profile driver's SCO connection request, the profile driver can then perform additional BRB commands across the newly connected channel by using **[IOCTL_INTERNAL_BTH_SUBMIT_BRB](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_internal_bth_submit_brb)** to submit a Bluetooth Request Block (BRB) to the Bluetooth driver stack, including:

- **[_BRB_SCO_GET_CHANNEL_INFO](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_get_channel_info)**
- **[_BRB_SCO_GET_SYSTEM_INFO](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_get_system_info)**
- **[_BRB_SCO_TRANSFER](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_transfer)**

> [!NOTE]
> Profile drivers should [build and send](building-and-sending-a-brb.md) a **BRB_SCO_GET_SYSTEM_INFO** request during initialization to determine if the underlying hardware supports SCO and, if so, what the global SCO settings are.

When the profile driver no longer requires the SCO connection to the remote device, it should [build and send](building-and-sending-a-brb.md) a **[_BRB_SCO_CLOSE_CHANNEL](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_brb_sco_close_channel)** request.
