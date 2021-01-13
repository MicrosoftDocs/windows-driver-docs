---
title: Send Operations
description: Send Operations
keywords:
- send operations WDK Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Send Operations




 

When performing a post-association operation, initiated through a call to [*Dot11ExtIhvPerformPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_post_associate), the IHV Extensions DLL can send packets through the wireless LAN (WLAN) adapter. For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

Typically, the DLL sends security packets to an access point (AP) for data port authentication by using the algorithm enabled through [**Dot11ExtSetAuthAlgorithm**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_set_auth_algorithm). The IHV Extensions DLL calls **Dot11ExtSetAuthAlgorithm** during the pre-association operation. For more information about this operation, see [Pre-Association Operations](pre-association-operations.md).

**Note**  For Windows Vista, the IHV Extensions DLL supports only infrastructure basic service set (BSS) networks.

 

When sending packets, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL must allocate the memory for a complete 802.11 data packet, including 802.11 media access control (MAC) header, LLC encapsulation (if necessary), and payload data.

    The following table describes which fields and subfields within the 802.11 MAC header are set by the IHV Extensions DLL or WLAN adapter.

    <table>
    <colgroup>
    <col width="25%" />
    <col width="25%" />
    <col width="25%" />
    <col width="25%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Field name</th>
    <th align="left">Subfield name</th>
    <th align="left">Set by IHV Extension DLL</th>
    <th align="left">Set by WLAN adapter</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Protocol Version</p></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Type</p></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Subtype</p></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>To DS</p></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>From DS</p></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>More Fragments</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Retry</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Pwr Mgt</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>More Data</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Protected Frame</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Frame Control</p></td>
    <td align="left"><p>Order</p></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Duration/ID</p></td>
    <td align="left"></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Address 1</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Address 2</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Address 3</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    <td align="left"></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Sequence Control</p></td>
    <td align="left"><p>Fragment Number</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Sequence Control</p></td>
    <td align="left"><p>Sequence Number</p></td>
    <td align="left"></td>
    <td align="left"><p>X</p></td>
    </tr>
    </tbody>
    </table>

     

-   The IHV Extensions DLL calls the [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet) function to send the packet through the wireless LAN (WLAN) adapter. The DLL passes a unique handle value, which identifies the packet, to the function's *hSendCompletion* parameter. Typically, the DLL passes the address of the allocated buffer that contains the packet to the *hSendCompletion* parameter.
    **Note**  Only unicast packets can be sent through calls to the [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet) function.

     

-   When the WLAN adapter has sent the packet, the operating system calls the [*Dot11ExtIhvSendPacketCompletion*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_send_packet_completion) function. The operating system passes the packet's handle value to the *hSendCompletion* parameter of the function. This handle value will be the same value used by the IHV Extensions DLL in its call to [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet).

    When [*Dot11ExtIhvSendPacketCompletion*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_send_packet_completion) is called, the IHV Extensions DLL must release the memory it allocated for the packet.

    **Note**  The IHV Extensions DLL must not free the resources allocated for a packet sent through [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet) until the corresponding call to [*Dot11ExtIhvSendPacketCompletion*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_send_packet_completion) is made.

     

 

 
