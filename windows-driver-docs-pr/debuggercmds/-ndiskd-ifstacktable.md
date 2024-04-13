---
title: "!ndiskd.ifstacktable"
description: "The !ndiskd.ifstacktable extension displays the network interface stack table (ifStackTable)."
keywords: ["!ndiskd.ifstacktable Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.ifstacktable
api_type:
- NA
---

# !ndiskd.ifstacktable


The **!ndiskd.ifstacktable** extension displays the network interface stack table (ifStackTable).

For more information about the interface stack table, see [Maintaining a Network Interface Stack](../network/maintaining-a-network-interface-stack.md).

```console
!ndiskd.ifstacktable 
```

## Parameters


This extension has no parameters.

## DLL

Ndiskd.dll

## Examples

Run the **!ndiskd.ifstacktable** command to see the ifStackTable.

```console
3: kd> !ndiskd.ifstacktable


INTERFACE STACK TABLE

    Lower interface    Lower IfIndex       Higher IfIndex     Higher interface  
    ffffdf80139b3a20   6                   15                 ffffdf801494fa20
    ffffdf801494fa20   15                  16                 ffffdf801494c010
    ffffdf801494c010   16                  17                 ffffdf801494ba20
```

NDIS maintains the stack table for NDIS miniport adapters, NDIS 5.x filter intermediate drivers, and NDIS filter modules, whereas [NDIS MUX Intermediate Drivers](../network/ndis-mux-intermediate-drivers.md) drivers are required to specify the internal interface relationship between the virtual miniport interface and the protocol lower interface. Therefore, the ifStackTable could be useful for seeing the interface stack relationships in a system with more complicated MUX drivers installed.

Since there are no NDIS MUX Intermediate drivers installed on this example system, the ifStackTable only shows the stack relationships that NDIS has provided. In the following example, clicking on the handle for the Lower interface of the third row (handle ffffdf801494c010, Lower IfIndex 16) shows the interface for the QoS Packet Scheduler.

```console
3: kd> !ndiskd.interface ffffdf801494c010


INTERFACE

    [Zero-length string]

    Ndis handle        ffffdf801494c010 
    IfProvider         ffffdf80131ca8d0 - The NDIS interface provider
    NDIS filter        ffffdf801494dc70 - Microsoft Kernel Debug Network Adapter-QoS Packet Scheduler-0000

    ifType             IF_TYPE_ETHERNET_CSMACD
    Media type         802.3
    Physical medium    NdisPhysicalMediumOther
    Access type        BROADCAST
    Direction type     SEND_AND_RECEIVE
    Connection type    DEDICATED

    ifConnectorPresent No

    Network            ffffdf80139b8900 - [Unnamed network]
    Compartment        ffffdf80139b9940 - Compartment #1


IDENTIFIERS

    ifAlias            [Zero-length string]
    ifDescr            Microsoft Kernel Debug Network Adapter-QoS Packet Scheduler-0000
    ifName (NET_LUID)  06:01
    ifPhysAddress      18-03-73-c1-e8-72

    ifIndex            0n16
    ifGuid             fc2a0ae1-b103-11e6-b724-806e6f6e6963


STATE

    Connected          Connected
    ifOperStatus       DORMANT
    ifOperStatusFlags  DORMANT_PAUSED

    Link speed         1000000000 (1 Gbps)
    ifMtu              0n1500
    Duplex             FullDuplex

    Refer to RFC 2863 for definitions of many of these terms
```

Continuing the same example, clicking the handle for the Higher interface of the third row (handle ffffdf801494ba20, Higher IfIndex 17) shows the interface for the WFP 802.3 MAC Layer LightWeight Filter.

```console
3: kd> !ndiskd.interface ffffdf801494ba20


INTERFACE

    [Zero-length string]

    Ndis handle        ffffdf801494ba20    [type it]
    IfProvider         ffffdf80131ca8d0 - The NDIS interface provider
    NDIS filter        ffffdf801494c670 - Microsoft Kernel Debug Network Adapter-WFP 802.3 MAC Layer LightWeight Filter-0000

    ifType             IF_TYPE_ETHERNET_CSMACD
    Media type         802.3
    Physical medium    NdisPhysicalMediumOther
    Access type        BROADCAST
    Direction type     SEND_AND_RECEIVE
    Connection type    DEDICATED

    ifConnectorPresent No

    Network            ffffdf80139b8900 - [Unnamed network]
    Compartment        ffffdf80139b9940 - Compartment #1


IDENTIFIERS

    ifAlias            [Zero-length string]
    ifDescr            Microsoft Kernel Debug Network Adapter-WFP 802.3 MAC Layer LightWeight Filter-0000
    ifName (NET_LUID)  06:02
    ifPhysAddress      18-03-73-c1-e8-72

    ifIndex            0n17
    ifGuid             fc2a0ae0-b103-11e6-b724-806e6f6e6963


STATE

    Connected          Connected
    ifOperStatus       DORMANT
    ifOperStatusFlags  DORMANT_PAUSED

    Link speed         1000000000 (1 Gbps)
    ifMtu              0n1500
    Duplex             FullDuplex

    Refer to RFC 2863 for definitions of many of these terms
```

This shows that the WFP 802.3 MAC Layer LightWeight Filter sits above the QoS Packet Scheudler filter in the network interface stack. You can confirm this by running the [**!ndiskd.netreport**](-ndiskd-netreport.md) extension, which shows you the network stack visually.

## See also


[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Maintaining a Network Interface Stack](../network/maintaining-a-network-interface-stack.md)

[NDIS MUX Intermediate Drivers](../network/ndis-mux-intermediate-drivers.md)

[**!ndiskd.netreport**](-ndiskd-netreport.md)

 


