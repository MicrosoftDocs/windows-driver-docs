---
title: Device Console (DevCon.exe) examples
description: Provides examples for Device Console (DevCon.exe) commands.
keywords:
- DevCon WDK , examples
- Device Console WDK , examples
- examples WDK DevCon
- DevCon WDK , commands
- Device Console WDK , commands
- commands WDK DevCon
- Example 44 Forcibly update the HAL
- HAL update example
ms.custom: contperf-fy22q3 
ms.date: 01/26/2022
---

# Replacing Device Console (DevCon.exe)

DevCon was originally and always has been a code sample intended as an example, not a tool to be relied upon. In response to its popularity, tools have been created to replace DevCon's functionality while following best practices and adding new capabilities. Please replace DevCon usage with the solutions described below.

## Recommended Tools

### PnPUtil

PnPUtil is an inbox tool that allows the user to view information on and change the state of devices and drivers. See [PnPUtil](pnputil.md) for an in-depth usage guide.

### DevGen

DevGen is a tool included in the WDK from SV2 onward. It is used to create software and root enumerated devices for driver development purposes.

## Table of Equivalencies

<table>
<colgroup>
<col width="20%" />
<col width="40%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th align="center">Devcon Command</th>
<th align="center">Description</th>
<th align="center">Alternative</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>classes</p></td>
<td align="left"><p>List all device setup classes.</p></td>
<td align="left"><p>pnputil /enum-classes</p></td>
</tr>
<tr class="even">
<td align="left"><p>disable</p></td>
<td align="left"><p>Disable devices.</p></td>
<td align="left"><p>pnputil /disable-device</p></td>
</tr>
<tr class="odd">
<td align="left"><p>driverfiles</p></td>
<td align="left"><p>List installed driver files for devices.</p></td>
<td align="left"><p>pnputil /enum-driver /files</p></td>
</tr>
<tr class="even">
<td align="left"><p>drivernodes</p></td>
<td align="left"><p>List driver nodes of devices.</p></td>
<td align="left"><p>pnputil /enum-devices /drivers</p></td>
</tr>
<tr class="odd">
<td align="left"><p>enable</p></td>
<td align="left"><p>Enable devices.</p></td>
<td align="left"><p>pnputil /enable-device</p></td>
</tr>
<tr class="even">
<td align="left"><p>find</p></td>
<td align="left"><p>Find devices.</p></td>
<td align="left"><p>pnputil /enum-devices</p></td>
</tr>
<tr class="odd">
<td align="left"><p>findall</p></td>
<td align="left"><p>Find devices, including those that are not currently attached.</p></td>
<td align="left"><p>pnputil /enum-devices</p></td>
</tr>
<tr class="even">
<td align="left"><p>hwids</p></td>
<td align="left"><p>List hardware IDs of devices.</p></td>
<td align="left"><p>pnputil /enum-devices /deviceids</p></td>
</tr>
<tr class="odd">
<td align="left"><p>install</p></td>
<td align="left"><p>Create test device and install driver.</p></td>
<td align="left"><p>devgen /add</p><p>pnputil /add-driver /install</p></td>
</tr>
<tr class="even">
<td align="left"><p>listclass</p></td>
<td align="left"><p>List all devices in a setup class.</p></td>
<td align="left"><p>pnputil /enum-devices /class &lt;name or GUID&gt;</p></td>
</tr>
<tr class="odd">
<td align="left"><p>reboot</p></td>
<td align="left"><p>Reboot the local computer.</p></td>
<td align="left"><p>shutdown /r /t 0</p></td>
</tr>
<tr class="even">
<td align="left"><p>remove</p></td>
<td align="left"><p>Remove devices.</p></td>
<td align="left"><p>pnputil /remove-device</p></td>
</tr>
<tr class="odd">
<td align="left"><p>rescan</p></td>
<td align="left"><p>Scan for new hardware.</p></td>
<td align="left"><p>pnputil /scan-devices</p></td>
</tr>
<tr class="even">
<td align="left"><p>resources</p></td>
<td align="left"><p>List hardware resources for devices.</p></td>
<td align="left"><p>pnputil /enum-devices /resources</p></td>
</tr>
<tr class="odd">
<td align="left"><p>restart</p></td>
<td align="left"><p>Restart devices.</p></td>
<td align="left"><p>pnputil /restart-device</p></td>
</tr>
<tr class="even">
<td align="left"><p>sethwid</p></td>
<td align="left"><p>Modify Hardware IDs of listed root-enumerated devices.</p></td>
<td align="left"><p>devgen /add /hardwareid &lt;hardware ID&gt;</p><p>note: this command creates a new test device with the specified ID</p></td>
</tr>
<tr class="odd">
<td align="left"><p>stack</p></td>
<td align="left"><p>List expected driver stack for devices.</p></td>
<td align="left"><p>pnputil /enum-devices /stack</p></td>
</tr>
<tr class="even">
<td align="left"><p>status</p></td>
<td align="left"><p>List running status of devices.</p></td>
<td align="left"><p>pnputil /enum-devices</p></td>
</tr>
<tr class="odd">
<td align="left"><p>update</p></td>
<td align="left"><p>Update a device manually.</p></td>
<td align="left"><p>pnputil /add-driver /install</p></td>
</tr>
<tr class="even">
<td align="left"><p>updateni</p></td>
<td align="left"><p>Manually update a device (non interactive).</p></td>
<td align="left"><p>pnputil /add-driver /install</p></td>
</tr>
<tr class="odd">
<td align="left"><p>dp_add</p></td>
<td align="left"><p>Adds (installs) a third-party (OEM) driver package.</p></td>
<td align="left"><p>pnputil /add-driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>dp_delete</p></td>
<td align="left"><p>Deletes a third-party (OEM) driver package.</p></td>
<td align="left"><p>pnputil /delete-driver</p></td>
</tr>
<tr class="odd">
<td align="left"><p>dp_enum</p></td>
<td align="left"><p>Lists the third-party (OEM) driver packages installed on this machine.</p></td>
<td align="left"><p>pnputil /enum-drivers</p></td>
</tr>
</tbody>
</table>