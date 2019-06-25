---
title: Receive Operations
description: Receive Operations
ms.assetid: 9ec2ba38-36dd-42d2-b0a8-0abe4d1bb847
keywords:
- receive operations WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receive Operations




 

When performing a post-association operation, initiated through a call to [*Dot11ExtIhvPerformPostAssociate*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_perform_post_associate), the operating system calls the [*Dot11ExtIhvReceivePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_receive_packet) function to forward packets to the HV Extensions DLL received through the wireless LAN (WLAN) adapter. For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

In order to receive packets, the IHV Extensions DLL must call [**Dot11ExtSetEtherTypeHandling**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) to register a list of one or more IEEE EtherTypes. When a packet is received with an EtherType that matches an entry in this list, the operating system calls the [*Dot11ExtIhvReceivePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_receive_packet) function and passes the packet buffer through the function's *pvInBuffer* parameter.

**Note**  The IHV Extensions DLL must call [**Dot11ExtSetEtherTypeHandling**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11ext_set_ethertype_handling) before the DLL completes a pre-association operation. For more information about this operation, see [Pre-Association Operations](pre-association-operations.md).

 

When [*Dot11ExtIhvReceivePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_receive_packet) is called, the *pvInBuffer* parameter points to a buffer allocated by the operating system that contains the entire 802.11 packet, including media access control (MAC) header, LLC encapsulation (if necessary), and payload data.

The IHV Extensions DLL can send a response to the received packet from within the call to [*Dot11ExtIhvReceivePacket*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wlanihv/nc-wlanihv-dot11extihv_receive_packet). In this situation, the DLL must follow the guidelines described in [Send Operations](send-operations.md).

 

 





