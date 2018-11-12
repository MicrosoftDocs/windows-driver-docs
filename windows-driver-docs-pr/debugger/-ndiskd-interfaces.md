---
title: ndiskd.interfaces
description: The ndiskd.interfaces extension displays information about a network interface.
ms.assetid: AC458FDF-CCB6-4A65-8C9C-38C436062017
keywords: ["ndiskd.interfaces Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.interfaces
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.interfaces


The **!ndiskd.interfaces** extension displays information about a network interface. If you run this extension with no parameters, !ndiskd will display a list of all network interfaces.

For more information about network interfaces, see [NDIS Network Interfaces](https://msdn.microsoft.com/windows/hardware/drivers/network/ndis-network-interfaces2).

```console
!ndiskd.interfaces [-handle <x>] [-luid <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of a network interface.

<span id="_______-luid______"></span><span id="_______-LUID______"></span> *-luid*   
[NetLuid](https://msdn.microsoft.com/windows/hardware/drivers/network/net-luid-value) (Net Locally Unique Identifier) of a network interface.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run the **!ndiskd.interfaces** extension with no parameters to see a list of all network interfaces on the system. In this example, look for the Intel(R) 82579LM Gigabit Network Connection interface. Its handle is ffffdf80139f8a20.

```console
1: kd> !ndiskd.interfaces
    Interface                                                                   
    ffffdf801494fa20 - Microsoft Kernel Debug Network Adapter-WFP Native MAC Layer LightWeight Filter-0000
    ffffdf801494c010 - Microsoft Kernel Debug Network Adapter-QoS Packet Scheduler-0000
    ffffdf801494ba20 - Microsoft Kernel Debug Network Adapter-WFP 802.3 MAC Layer LightWeight Filter-0000
    ffffdf80139b3a20 - Microsoft Kernel Debug Network Adapter
    ffffdf80139f8a20 - Intel(R) 82579LM Gigabit Network Connection
    ffffdf80139baa20 - WAN Miniport (IP)
    ffffdf80139a4a20 - WAN Miniport (IPv6)
    ffffdf80131d0010 - WAN Miniport (Network Monitor)
    ffffdf80131cda20 - WAN Miniport (PPPOE)
    ffffdf80139b6a20 - Software Loopback Interface 1
    ffffdf80139b0a20 - Microsoft ISATAP Adapter
    ffffdf80139ada20 - WAN Miniport (SSTP)
    ffffdf80131cf010 - WAN Miniport (IKEv2)
    ffffdf80139fea20 - WAN Miniport (L2TP)
    ffffdf80139a7a20 - WAN Miniport (PPTP)
    ffffdf80139aaa20 - Microsoft ISATAP Adapter #2
    ffffdf80139fba20 - Teredo Tunneling Pseudo-Interface
```

By clicking on the handle for an interface or by entering the **!ndiskd.interfaces -handle** command, you can see the details about that interface, including its Identifier information and its current state. In this example, you can see that the Intel(R) 82579LM Gigabit Network Connection is an Ethernet connection (its ifAlias) and is in a MediaConnectUnknown state for its connection (as it has been reserved for use by the Windows kernel debugger).

```console
1: kd> !ndiskd.interfaces ffffdf80139f8a20


INTERFACE

    Ethernet

    Ndis handle        ffffdf80139f8a20
    IfProvider         ffffdf80131ca8d0 - The NDIS interface provider
    Provider context   ffffdf80139f8a20

    ifType             IF_TYPE_ETHERNET_CSMACD
    Media type         802.3
    Physical medium    802.3
    Access type        BROADCAST
    Direction type     SEND_AND_RECEIVE
    Connection type    DEDICATED

    ifConnectorPresent No

    Network            ffffdf80139b8900 - [Unnamed network]
    Compartment        ffffdf80139b9940 - Compartment #1


IDENTIFIERS

    ifAlias            Ethernet
    ifDescr            Intel(R) 82579LM Gigabit Network Connection
    ifName (NET_LUID)  06:8001
    ifPhysAddress      18-03-73-c1-e8-72

    ifIndex            0n14
    ifGuid             cbddfde1-5570-4c65-9d47-52d63abce00c


STATE

    Connected          MediaConnectUnknown
    ifOperStatus       NOT_PRESENT

    Link speed         0 [Speed is not applicable]
    ifMtu              0
    Duplex             UnknownDuplex

    Refer to RFC 2863 for definitions of many of these terms
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[NDIS Network Interfaces](https://msdn.microsoft.com/windows/hardware/drivers/network/ndis-network-interfaces2)

[NET\_LUID Value](https://msdn.microsoft.com/windows/hardware/drivers/network/net-luid-value)

 

 






