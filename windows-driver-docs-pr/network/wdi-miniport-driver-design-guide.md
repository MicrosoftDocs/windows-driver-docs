---
title: WDI Miniport Driver Design Guide
description: WLAN Device Driver Interface (WDI) is the new WLAN Universal Windows driver model for both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile.
ms.assetid: E1666D5E-1932-4378-B4F6-61F28716183E
keywords:
- wi-fi drivers, wi-fi drivers Windows 10, wireless drivers, wireless drivers windows 10, wlan drivers, wlan drivers windows 10, wlan driver interface, WDI drivers, WDI network drivers, WDI Windows 10
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI Miniport Driver Design Guide


WLAN Device Driver Interface (WDI) is the new Universal Windows driver model for Wi-Fi drivers, for both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile. The WLAN device manufacturer writes a WDI miniport driver to work with the Windows 10 OS implementation. WDI enables device manufacturers to write less code than the previous Native WLAN driver model. All new WLAN features introduced in Windows 10 require WDI-based drivers.

Vendor-supplied native WLAN drivers continue to work in Windows 10, but functionality is limited to the version of Windows for which they were developed.

The WDI requirements and interface specification are documented in this design guide. The key goals for the new model are:

-   Improve the quality and reliability of Windows WLAN drivers.
-   Reduce the complexity of the current driver model, which in turn reduces the complexity of the IHV driver and reduces the overall cost of IHV driver development.

The focus of this documentation is to specify the flow and behavior of Wi-Fi operations between Windows and the IHV driver component. It does not cover software interface signature (for example, the device driver interface model) and details about how the IHV component is loaded in Windows.

## Design principles


The following principles guided the overall model and design of this protocol.

1.  Minimize the chattiness of the traffic between the host component and the IHV component/device. This is particularly important for implementations on buses such as SDIO, which is inherently chatty.
2.  Wi-Fi functionality (especially functionality that must be performed with low latency) is expected to be handled by the device.
3.  All regulatory related functionality resides in the IHV component and is controlled by the IHV.
4.  The Windows experience is controlled by the host component and the Windows operating system.
5.  Windows has the ability to resurrect hung devices. It has enough state to reprogram the IHV component and recover within 10 seconds.
6.  Operations that require lot of system memory or fast processors and are not vendor specific are handled by the host.

## Definitions


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Device</p></td>
<td align="left"><p>The entire piece of hardware that connects to the bus. A device can have multiple radios in it (notably Wi-Fi and Bluetooth).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Wi-Fi adapter</p></td>
<td align="left"><p>The specific part of the device that implements Wi-Fi functionality as described in this specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Port</p></td>
<td align="left"><p>An object that represents a MAC and PHY state for a particular connection.</p></td>
</tr>
<tr class="even">
<td align="left"><p>IHV component</p></td>
<td align="left"><p>The IHV-developed software component that represents the Wi-Fi Adapter/Device to the host.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Host</p></td>
<td align="left"><p>The host-side Microsoft/operating system software that interacts with the IHV component using the interfaces described in this specification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Upper Edge Driver (UE)</p></td>
<td align="left"><p>UE refers to the WdiWiFi driver, called WDI in this documentation. The UE and the Lower Edge (LE) IHV driver combine into a complete NDIS miniport driver. The UE implements the core Wi-Fi logic.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Lower Edge Driver (LE)</p></td>
<td align="left"><p>LE refers to the IHV driver at the lower edge. The LE and UE combine into a complete NDIS miniport driver. The LE implements bus and hardware specific functions.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Functional Level Reset (FLR)</p></td>
<td align="left"><p>Functional Level Reset, as in the PCIe specification. This term refers to the reset of a function, versus a reset of the complete device which may have a composite function. The reset of such scope does not impair the other functions on the same device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platform Level Reset (PLR)</p></td>
<td align="left"><p>Platform Level Reset. This reset method impacts all functions on a device. It is very popular to build multiple functions on a device to reduce the cost and footprint. For example, Bluetooth is typically built with Wi-Fi on a chip. However, such a reset method resets all function units on the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Reset Recovery (RR)</p></td>
<td align="left"><p>RR refers to the event sequence of Reset and Recovery.</p>
<p>For FLR, this includes:</p>
<ul>
<li>The request to NDIS, which forwards the request to the bus to reset the Wi-Fi function.</li>
<li>Recovery of firmware context by the driver.</li>
<li>Reconnection to the access point if it was connected before the reset.</li>
</ul>
<p>For PLR, this includes:</p>
<ul>
<li>The request to NDIS, which forwards the request to the bus. The bus interacts with PnP to surprise-remove the device.</li>
<li>Re-enumeration of the device.</li>
<li>Re-establishing the device stack.</li>
<li>Wi-Fi is restarted and reconnects.</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>WDI commands</p></td>
<td align="left"><p>The UE sends WDI OIDs and calls LE callbacks. All of these are called WDI commands.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MAC Address Randomization</p></td>
<td align="left"><p>In order to improve the privacy of Windows 10 users, configured Wi-Fi MAC addresses are used in some circumstances, such as before connecting to a particular Wi-Fi network or when initiating scans in specific conditions. This only applies to the station port. The system ensures that randomization is used appropriately, so important connectivity scenarios are not broken. The system manages changes of addresses by issuing <a href="https://msdn.microsoft.com/library/windows/hardware/dn925952" data-raw-source="[OID_WDI_TASK_DOT11_RESET](https://msdn.microsoft.com/library/windows/hardware/dn925952)">OID_WDI_TASK_DOT11_RESET</a> commands prior to issuing a scan or connect command. The reset command parameters include an optional MAC address argument. If the argument is present, the MAC address is reset to the specified value. If it is absent, the MAC address is left to the current value. When configuring randomized MAC addresses, the operating system uses the &quot;locally administered&quot; format defined for IEEE802 addresses.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ECSA</p></td>
<td align="left"><p>Extended Channel Switch Announcement.</p></td>
</tr>
</tbody>
</table>

 

## Related topics


[WDI Miniport Driver Reference](https://msdn.microsoft.com/library/windows/hardware/dn926075)

 

 






