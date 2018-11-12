---
title: System-Provided DCB Components
description: System-Provided DCB Components
ms.assetid: 64C9ADEF-5512-41E4-AE7B-DFEF1B94FC5F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# System-Provided DCB Components


This section describes the various components that are part of the NDIS Quality of Service (QoS) architecture for IEEE 802.1 Data Center Bridging (DCB). These components are shown in the following diagram.

![device installation components](images/dcb.png)

The unshaded boxes in the diagram represent modules that the Windows operating system provides. In particular, the operating system provides the following modules that support DCB:

<a href="" id="network-qos-policy-wmi-provider"></a>Network QoS Policy WMI Provider  
This module provides an interface for Windows Management Instrumentation (WMI) clients to query and set QoS-based network policies within the operating system’s network stack. These policies allow specific types of network traffic to be assigned to DCB traffic classes for transmit, or *egress*, management and prioritized delivery.

A network policy defines a set of conditions and actions. An egress packet that matches a condition, such as a TCP or UDP port number, is assigned the action related to the condition. Starting with NDIS 6.30, policy actions specify an 802.1p priority level to which a DCB traffic class has been assigned.

Network QoS policies are a superset of NDIS QoS classifications. A policy defined by using the Network Policy WMI Provider may be automatically migrated to NDIS QoS as long as the policy conditions and actions match the restrictions of an NDIS QoS classification element. For more information about these elements, see [NDIS QoS Traffic Classifications](ndis-qos-traffic-classifications.md).

This WMI provider saves the network policies within a separate store in the system registry.

<a href="" id="dcb-wmi-provider"></a>DCB WMI Provider  
This component provides an interface for WMI clients to query and set NDIS QoS parameters on the underlying miniport driver. Through WMI-based PowerShell cmdlets and WMI methods, clients can configure DCB functionality, such as Priority-based Flow Control (PFC) and Enhanced Transmission Selection (ETS), on the miniport driver that supports DCB.

<a href="" id="dcb"></a>DCB  
The DCB component (Msdcb.sys) configures the DCB-capable miniport driver with DCB parameter settings. The DCB component obtains these settings from the following sources:

-   Persistent settings from the DCB policy store in the system registry.

-   Dynamic settings from the DCB WMI user-mode provider. These settings are delivered over a private I/O control (IOCTL) interface between the DCB WMI provider and the DCB module.

The DCB component also relays QOS classification settings from the QIM component to miniport drivers that support NDIS QoS.

<a href="" id="qos-inspection-module--qim-"></a>QoS Inspection Module (QIM)  
The QIM component is part of the packet inspection layer in the core TCP/IP network stack (Tcpip.sys). Starting with Windows Server 2012, this component performs QoS-based packet classification for traffic prioritization.

The QIM component exposes a private Network Programming Interface (NPI). When the DCB component sets QoS parameters on the underlying miniport driver, it relays those settings to the QIM component over this NPI interface. This allows DCB to create QoS policies in QIM that are based on DCB application priority settings. For more information about the NPI interface, see [Network Programming Interface](network-programming-interface.md).

The QIM component also processes networking QoS policies from the policy store in the registry. If those policies are compatible with NDIS QoS classification elements, the QIM component migrates the policies and issues them to the DCB component over the NPI interface.

**Note**  The policies that are created by the QIM component go into the active store and do not persist through a system restart.

 

**Note**  Starting with Windows Server 2012, the DCB and DCB WMI provider components are not installed by default. These components are installed and enabled through the installation of the Microsoft DCB server feature. This feature is installed by using the Add Roles and Features wizard of the Server Manager.

 

 

 





