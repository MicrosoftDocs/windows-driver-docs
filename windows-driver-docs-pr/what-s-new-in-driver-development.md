---
title: What's New in Driver Development for Windows 11, Version 24H2
description: This section describes new features for driver development in Windows 11, version 24H2.
ms.date: 03/04/2024
---

# <a name="top"></a>What's new in driver development for Windows 11, version 24H2

This section describes new features and updates for driver development in Windows 11, version 24H2. To target this version of Windows, you can use [WDK xx.x.xxxxx.xxxx](./download-the-wdk.md) (released April 8, 2024).

## Audio

## Bluetooth Low Energy (LE) Audio

## Camera and streaming media

## Display and graphics drivers

* A [GPU native fence synchronization object] is added as an extension to the monitored fence object, supporting the following additional features:

  * GPU wait on monitored fence value, which allows for high performance engine-to-engine synchronization without requiring CPU round trips.
  * Conditional interrupt notification only for GPU fence signals that have CPU waiters, enabling substantial power savings.
  * Fence value storage in the GPU's local memory.

* WDDM 3.2 supports the live migration of heterogenous compute devices virtualized through single root I/O virtualization partitioning. For more information, see [Live migration on GPU-P devices].

* The method that a user-mode or kernel-mode graphics driver uses to determine whether a particular WDDM feature is enabled has been updated. For more information, see [Determining WDDM feature support].

## Dynamic lighting

## File system and filter drivers

Starting in Windows 11, version 24H2, [bind links](/windows/win32/bindlink/) can be used to bind a file system namespace to a local "virtual path" through the Bind Filter (*bindflt.sys*). Minifilters can choose to veto such bind links on the system's boot partition. For more information, see [Vetoing a bind link].

## Human presence sensors

## Network drivers

* [WiFiCx Wi-Fi 7](./netcx/wificx-wi-fi-7.md) introduces support for Wi-Fi 7 features, providing faster connectivity speeds, lower latency, and improved security. WiFiCx Wi-Fi 7 enables: 
  * Multi-Link Operation (MLO) with roaming differentiation to leverage multiple simultaneous channels to the Wi-Fi access point (AP). 
  * Enhanced capabilities for WPA3-SAE authentication and Opportunistic Wireless Encryption (OWE) with GCMP-256 cipher.

* [WiFiCx WPA3 SoftAP](./netcx/wificx-wpa3-softap.md) enables devices to set up a Soft Access Point (SoftAP) using the Wi-Fi Protected Access 3 - Simultaneous Authentication of Equals (WPA3-SAE) security protocol.

* [WiFiCx QoS R1](./netcx/qos-r1.md) introduces advanced traffic management capabilities for WiFiCx devices. QoS R1 enables prioritization of Wi-Fi data packets through Mirrored Stream Classification Service (MSCS) and QoS Mapping (DSCP-to-UP Mapping).

* [UDP Receive Segment Coalescing Offload (URO)](./network/udp-rsc-offload.md) is a new hardware offload feature that enables network interface cards (NICs) to coalesce UDP receive segments. URO is available to NDIS and [NetAdapterCx](./netcx/rsc-offload.md) drivers. 

## Print devices

## Storage drivers

## USB

## Getting started

## Driver security  

## Windows debugging tools

## Related Topics

For information on what was new for drivers in past Windows releases, see the following pages:

* [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)
* [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)
* [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)
* [Driver development changes for Windows 10, version 2004](driver-changes-for-windows-10-version-2004.md)

[Back to Top](#top)
