---
title: Guidelines for MB Miniport Driver IP Address Notifications
description: Guidelines for MB Miniport Driver IP Address Notifications
ms.date: 04/20/2017
ms.custom: UpdateFrequency3
---

# Guidelines for MB Miniport Driver IP Address Notifications


MB miniport drivers that specify *EnableDhcp* equal to zero in their INF files can use the [IP Helper](ip-helper.md) and associated [functions](./ip-helper.md) in kernel mode to create, change, and delete the IP address:

To use the IP Helper functions in kernel mode, miniport drivers must include the Netioapi.h header file, and link against Netio.lib.

When miniport drivers specify *EnableDhcp* equal to zero they are required to perform the following operations to notify the MB Service about any of the following events:

-   Set IP address for the MB interface

-   Set default gateway address

-   Update DNS addresses

IP addresses and default gateways that are set by using the IP Helper API persist network connect or disconnect events, or both. Therefore, if the new IP address or default gateway, or both, values are different than the values currently set, the miniport driver should first clear the previous values before setting new values on a network connection event.

**Note**  Miniport drivers can find the **LUID** and **Index** of the MB interface from the **NetLuid** or **IfIndex** members of [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure that is passed to the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

 

### Resetting the IP Address and Gateway Address

Certain changes to the TCP/IP stack, such as the loading of a mandatory filter driver, can remove the IP and gateway addresses set by the IP helper functions. Miniport drivers must reset the IP and gateway addresses if changes to the TCP/IP stack remove the settings.

Miniport drivers should use following procedure to be notified when the addresses are removed, and must be reset again.

1.  During **driver initialization**, miniport drivers should specify a callback function to register for IP interface change notifications using [**NotifyIpInterfaceChange**](/previous-versions/windows/hardware/drivers/ff568805(v=vs.85)). Windows will call the function whenever an IP interface is added, deleted or changed.

2.  During **adapter initialization**, miniport drivers should save in miniport driver's local adapter context the **LUID** value from the [**NDIS\_MINIPORT\_INIT\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_init_parameters) structure that is passed to the miniport driver's [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function. The value contains the *NetLuid* which identifies adapter's interface, which is used in the notification callback.

3.  In the **notification callback**, Windows passes the following parameters to the notification function registered with [**NotifyIpInterfaceChange**](/previous-versions/windows/hardware/drivers/ff568805(v=vs.85)):

    -   A pointer to a [**MIB\_IPINTERFACE\_ROW**](/previous-versions/windows/hardware/drivers/ff559254(v=vs.85)) structure, which contains the *NetLuid* of the miniport adapter's interface.
    -   The type of notification, which can be **MibAddInstance**, **MibDeleteInstance** or **MibParameterNotification**.

    Miniport drivers should reset the IP and gateway addresses when the adapter is in a connected state, and the notification type is **MibAddInstance**, and the *NetLuid* in [**MIB\_IPINTERFACE\_ROW**](/previous-versions/windows/hardware/drivers/ff559254(v=vs.85)) corresponds to one of the miniport driver's adapters, which was saved during adapter initialization.

    Miniport drivers should then follow the Setting the IP Address for the MB Interface and Setting Default Gateway Address procedures to reset the respective addresses.

4.  During **driver unload**, miniport drivers should unregister the notification callback function using the [**CancelMibChangeNotify2**](/previous-versions/windows/hardware/drivers/ff544864(v=vs.85)) IP helper function.

### Setting the IP Address for the MB Interface

To set an IPv4 address, use the following procedure. You can use similar IP Helper functionality to set an IPv6 address.

1.  Use the [**GetUnicastIpAddressTable**](/previous-versions/windows/hardware/drivers/ff552594(v=vs.85)) IP Helper function to find all the IP address entries in the system.

2.  For each entry whose **InterfaceLuid** value matches the **InterfaceLuid** of the MB interface:
    1.  Find the IP address entry that matches the IP address used in previous connection. First time connections will not have a previous IP address.
    2.  If the new IP address is different than the previous IP address, delete the IP address entry for previous connection IP addresses by using the [**DeleteUnicastIpAddressEntry**](/previous-versions/windows/hardware/drivers/ff546370(v=vs.85)) IP Helper function.
    3.  If the new IP address is the same as the previous IP address, verify that the desired entry already exists.

3.  If the miniport driver did not find the desired IP address entry in the previous loop, it should add a new entry.
    1.  Use the [**InitializeUnicastIpAddressEntry**](/previous-versions/windows/hardware/drivers/ff554886(v=vs.85)) IP Helper function to initialize a [**MIB\_UNICASTIPADDRESS\_ROW**](/previous-versions/windows/hardware/drivers/ff559308(v=vs.85)) structure and set the following members of the structure:
        1.  Set the **InterfaceLuid** or **InterfaceIndex** members, as appropriate.
        2.  Set the **OnlinePrefixLength** member. This is the number of bits that have a value of one in the subnet mask. For example, if the subnet mask is 255.255.255.0, **OnlinePrefixLength** should be 24.
        3.  Set the **Address** member.
        4.  Set the **PrefixOrigin** member to **IpPrefixOriginManual**.

    2.  Pass the initialized MIB\_UNICASTADDRESS\_ROW structure to the [**CreateUnicastIpAddressEntry**](/previous-versions/windows/hardware/drivers/ff546227(v=vs.85)) IP Helper function to create the IP address entry.

### Setting Default Gateway Address

To set an IPv4 gateway address, use the following procedure. You can use similar IP Helper functionality to set an IPv6 gateway address.

1.  Use [**GetIpForwardTable2**](/previous-versions/windows/hardware/drivers/ff552536(v=vs.85)) IP Helper function to obtain all the routing entries in the system.

2.  For each entry whose **InterfaceLuid** value matches the **InterfaceLuid** value of the MB interface and **DestinationPrefix** is "0.0.0.0/0", call the [**DeleteIpForwardEntry2**](/previous-versions/windows/hardware/drivers/ff546365(v=vs.85)) IP Helper function to delete the route if **NextHop** is not equal to the new gateway address. Otherwise, the routing entry is already in the system.

3.  If the miniport driver did not find the desired routing entry in the previous loop, it should add a new entry by using the [**InitializeIpForwardEntry**](/previous-versions/windows/hardware/drivers/ff554882(v=vs.85)) IP Helper function to initialize a [**MIB\_IPFORWARD\_ROW2**](/previous-versions/windows/hardware/drivers/ff559245(v=vs.85)) structure. Initialize the following members of the structure:

    **InterfaceLuid** or **InterfaceIndex** .

    Set **DestinationPrefix** to 0.0.0.0/0 for default gateway. (Prefix = 0.0.0.0 and PrefixLength = 0)

    Set **NextHop** to the IP address of the default gateway.

    Other members are set to default values during initialization. Miniport drivers should use default values for those members.

4.  Pass the [**MIB\_IPFORWARD\_ROW2**](/previous-versions/windows/hardware/drivers/ff559245(v=vs.85)) structure to the [**CreateIpForwardEntry2**](/previous-versions/windows/hardware/drivers/ff546209(v=vs.85)) IP Helper function to set a new default gateway address.

### To Set DNS Addresses

-   Set the **NameServer** registry key as described in [MB DNS Updates](mb-dns-updates.md) to notify Windows about updated DNS addresses.

 

