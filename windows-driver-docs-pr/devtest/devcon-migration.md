---
title: Replacing Device Console (DevCon.exe)
description: Provides guidance for replacing Device Console (DevCon.exe).
keywords:
- DevCon WDK , examples
- Device Console WDK , examples
- examples WDK DevCon
- DevCon WDK , commands
- Device Console WDK , commands
- commands WDK DevCon
ms.custom: contperf-fy22q3
ms.date: 06/19/2023
---

# Replacing Device Console (DevCon.exe)

DevCon was originally and always has been a code sample intended as an example, not a tool to be relied upon. In response to its popularity, tools have been created to replace DevCon's functionality while following best practices and adding new capabilities. Please replace DevCon usage with the solutions described below.

## Recommended Tools

### PnPUtil

PnPUtil is an inbox tool that allows the user to view information on and change the state of devices and drivers. See [PnPUtil](pnputil.md) for an in-depth usage guide.

## Table of Equivalencies

PnPUtil command support varies by Windows version. For information on minimum version support for each command, see [PnPUtil Command Syntax](pnputil-command-syntax.md).

| Devcon Command | Description | Alternative |
|---|---|---|
| classes | List all device setup classes. | pnputil /enum-classes |
| disable | Disable devices. | pnputil /disable-device |
| driverfiles | List installed driver files for devices. | pnputil /enum-drivers /files |
| drivernodes | List driver nodes of devices. | pnputil /enum-devices /drivers |
| enable | Enable devices. | pnputil /enable-device |
| find | Find devices. | pnputil /enum-devices /connected |
| findall | Find devices, including those that are not currently attached. | pnputil /enum-devices |
| hwids | List hardware IDs of devices. | pnputil /enum-devices /deviceids |
| install | Create test device and install driver. | devgen /add /bus ROOT <br> pnputil /add-driver \<*INF name*\> /install |
| listclass | List all devices in a setup class. | pnputil /enum-devices /class \<*name or GUID*\> |
| reboot | Reboot the local computer. | shutdown /r /t 0 |
| remove | Remove devices. | pnputil /remove-device |
| rescan | Scan for new hardware. | pnputil /scan-devices |
| resources | List hardware resources for devices. | pnputil /enum-devices /resources |
| restart | Restart devices. | pnputil /restart-device |
| stack | List expected driver stack for devices. | pnputil /enum-devices /stack |
| status | List running status of devices. | pnputil /enum-devices |
| update | Update a device manually. | pnputil /add-driver \<*INF name*\> /install |
| updateni | Manually update a device (non interactive). | pnputil /add-driver \<*INF name*\> /install |
| dp_add | Adds (installs) a third-party (OEM) driver package. | pnputil /add-driver \<*INF name*\> |
| dp_delete | Deletes a third-party (OEM) driver package. | pnputil /delete-driver |
| dp_enum | Lists the third-party (OEM) driver packages installed on this machine. | pnputil /enum-drivers |

## Unsupported Functionality

### Wildcard Matching

Wildcard matching is not supported in DevCon alternatives. Many of the commands listed above can change the state of the system and should not be used without specificity. As an alternative, many PnPUtil commands offer the option to perform bulk operations on devices that exactly match a hardware or compatible ID.