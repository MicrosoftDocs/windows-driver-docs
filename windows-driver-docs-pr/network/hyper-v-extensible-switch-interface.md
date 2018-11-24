---
title: Hyper-V Extensible Switch Interface
description: Hyper-V Extensible Switch Interface
ms.assetid: 268AEA25-39D6-4494-B778-49C0B209E62E
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Interface


**Note**  This page assumes that you are familiar with the information and diagrams in [Overview of the Hyper-V Extensible Switch](overview-of-the-hyper-v-extensible-switch.md) and [Hybrid Forwarding](hybrid-forwarding.md).

 

A Hyper-V extensible switch is a virtual Ethernet switch that runs in the management operating system of the Hyper-V parent partition. Each instance of the extensible switch routes packets between the physical network interface in the host and the virtual network interfaces that are configured for the Hyper-V child partitions. These virtual network interfaces include Hyper-V external, internal, and private network interfaces.

Starting with NDIS 6.30 in Windows Server 2012, the extensible switch module supports an interface that allows NDIS filter drivers (known as *extensible switch extensions*) to bind within the extensible switch driver stack. This allows extensions to monitor, modify, and forward packets to extensible switch ports. This also allows extensions to inspect and inject packets in the virtual network interfaces that are used by the various Hyper-V partitions.

Extensions can be configured with switch and port policies to apply to packets that are routed through the extensible switch data path. This allows the driver to allow or deny a packet from being sent or received over a port.

In the extensible switch interface, the filter drivers are known as *extensible switch extensions* and the driver stack is known as the *extensible switch driver stack*.

The extensible switch interface supports the following types of extensions:

<a href="" id="capturing-extension"></a>Capturing Extension  
An extension that captures and monitors packet traffic. This type of extension cannot modify packets or packet destinations through the extensible switch. However, capturing extensions can originate packet traffic, such as packets that contain traffic statistics that the extension sends to a host application.

For more information, see [Capturing Extensions](capturing-extensions.md).

<a href="" id="filtering-extension"></a>Filtering Extension  
An extension that captures and monitors packet traffic. This type of extension can also inspect and reject packet delivery based on custom port or switch policy settings.

For more information, see [Filtering Extensions](filtering-extensions.md).

<a href="" id="forwarding-extension"></a>Forwarding Extension  
An extension that has the same capabilities as a filtering extension. This type of extension can determine the extensible switch destination ports that a packet is delivered to, as well as inject packet traffic to any extensible switch port. This type of extension also inspects and rejects packet delivery based on standard port policy settings.

For more information, see [Forwarding Extensions](forwarding-extensions.md).

**Note**  In NDIS 6.40 (Windows Server 2012 R2) and later, forwarding extensions must support [Hybrid Forwarding](hybrid-forwarding.md).

 

**Note**  If a forwarding extension is not installed and enabled in the extensible switch, the switch determines a packet's destination ports as well as filters packets based on standard port settings.

 

For more information about the extensible switch interface, see [Hyper-V Extensible Switch](hyper-v-extensible-switch.md).

 

 





