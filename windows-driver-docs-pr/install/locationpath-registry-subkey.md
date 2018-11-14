---
title: LocationPath Registry Subkey
description: LocationPath Registry Subkey
ms.assetid: 3b6f3501-5969-453c-a04b-5559761c3222
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# LocationPath Registry Subkey


Beginning with Windows 7, the **LocationPath** registry subkey specifies the location path for a removable device capability override of a single device identified through either the [HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md) registry subkey. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The **LocationPath** registry subkey applies the removable device capability value to only the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that exists at the specified location path. This lets the removable device capability override be applied to a single instance of a device installed in the system. Other devices with the same **HardwareID** or **CompatibleID** at other location paths are not affected by such a removable device capability override.

By convention, the location path string takes the form *ServiceName(BusSpecificLocation)*. For example, PCI devices use PCI (*XXYY*), where *XX* is the device number and *YY* is the function number. The string is unique to the device in relation to its bus. The Plug and Play (PnP) manager assembles the location path for each node in the devnode tree. Each devnode in the tree concatenates its service name string to the end of the location path string that its parent devnode supplied. Therefore, the position of any devnode in the tree can be uniquely identified through the location path.

The following table defines the format and requirements of the **LocationPath** registry subkey.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry subkey name</th>
<th align="left">Required/optional</th>
<th align="left">Format requirements</th>
<th align="left">Parent subkey</th>
<th align="left">Child subkeys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Valid &quot;<em>LocationPath</em>&quot; value</p></td>
<td align="left"><p>Optional (* or a valid location path must be present to indicate the scope of the removable device capability override)</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p><a href="locationpaths-registry-subkey.md" data-raw-source="[LocationPaths](locationpaths-registry-subkey.md)">LocationPaths</a> or <a href="childlocationpaths-registry-subkey.md" data-raw-source="[ChildLocationPaths](childlocationpaths-registry-subkey.md)">ChildLocationPaths</a></p></td>
<td align="left"><p>None</p></td>
</tr>
</tbody>
</table>

 

Either the **LocationPath** or [\*](--registry-subkey.md) registry subkeys must be present to indicate the scope of the removable device capability override.

The **LocationPath** subkey must contain a **Removable** DWORD value that specifies whether the device is removable or not. The following table defines the valid **Removable** values.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Removable value</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>The devnode should be regarded as not removable</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>The devnode should be regarded as removable</p></td>
</tr>
</tbody>
</table>

 

The location path string for a given devnode can be displayed through Device Manager through the following steps:

1.  Open Device Manager and locate the devnode on which the registry override is to be applied. To do this, you may be required to change the view to **Devices by connection**.

2.  Right-click the devnode, click **Properties** and then click the **Details** tab.

3.  In the **Property** drop-down list, find the **LocationPaths** property. This property contains the location path string for this devnode and is the value that should be used for the **LocationPath** registry subkey.

**Note**  It is possible that the devnode does not have a **LocationPaths** value. This is because the driver for this devnode or one of its parents does not implement the [GUID_PNP_LOCATION_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/ff546564) interface. In this case, you must check the parent devnode for a **LocationPaths** property.

 

The **LocationPaths** registry subkey is intended to be used for overriding the removable device capability of devices that are hardwired to a fixed bus location. This typically occurs in portable computers, and includes the following devices:

-   Wireless network adapters

-   Bluetooth adapters

-   Keyboards or pointing devices

These devices exist on different internal buses at fixed locations that the user cannot change. The **LocationPaths** override lets you specify that only the device at the given bus location is affected by the removable device capability override. This prevents the override from affecting devices at other bus locations that may share the same [HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md) subkey value as the override target. This is common when devices specify only a **CompatibleID** subkey value to match an inbox driver.

When you use a [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkey to override the removable device capability of child devnodes, it is often useful to target only child devnodes at specific locations, regardless of what kind of devices they are.

For example, a laptop may have an internal USB hub with both internal and external ports. If this USB hub is misreporting its internal ports as being external, any device that is internally hardwired to these ports is incorrectly recognized as being removable. Similarly, if all ports are misreported as being internal, any externally connected device is treated as if it is a nondetachable part of the laptop.

To discover the location paths value for a device that is connected to an external USB port, you can plug any device into the port and observe its location paths property. Any other USB devices that are plugged into the same port should receive the same location paths value, because the parent bus and how it internally identifies a port never changes.

 

 





