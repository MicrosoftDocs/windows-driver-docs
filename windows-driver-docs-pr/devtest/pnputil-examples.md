---
title: PnPUtil Command Examples for Windows Driver Management
description: "Learn how to use PnPUtil commands to add, delete, enable, disable, and manage Windows drivers and devices with practical examples."
ms.date: 11/05/2025
ms.topic: how-to
no-loc: ["enable-device", "remove-device", "restart-device", "scan-devices"]
---

# PnPUtil examples

This article provides practical PnPUtil command examples for managing Windows drivers and devices. Each example includes the exact syntax and expected output to help you immediately apply these commands.

**In this article, you'll learn how to:**
- Add and install driver packages
- Enable and disable devices
- Enumerate drivers and devices on your system
- Troubleshoot driver issues

## Prerequisites

Administrator rights are required for most PnPUtil commands.

## /add-driver

Add driver package

```console
pnputil /add-driver x:\driver.inf
```

Add multiple driver packages

```console
pnputil /add-driver c:\oem\*.inf
```

Add and install driver package on an existing device

```console
pnputil /add-driver device.inf /install
```

## /delete-driver

Delete driver package

```console
pnputil /delete-driver oem0.inf
```

Force delete driver package

```console
pnputil /delete-driver oem1.inf /force
```

## /disable-device

Disable the device specified by device instance ID

```console
pnputil /disable-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"
```

Disable all devices with a specific hardware or compatible ID

```console
pnputil /disable-device /deviceid "USB\Class_03"
```

Disable all devices of a specific class on a specific bus

```console
pnputil /disable-device /class "USB" /bus "PCI"
```

## /enable-device

Enable device specified by device instance ID

```console
pnputil /enable-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"
```

Enable all devices with specific hardware/compatible ID

```console
pnputil /enable-device /deviceid "USB\Class_03"
```

Enable all devices of a specific class on a specific bus

```console
pnputil /enable-device /class "USB" /bus "PCI"
```

## /enum-classes

Enumerate all device setup classes on the system

```console
pnputil /enum-classes
```

Enumerate information for a specific device setup class

```console
pnputil /enum-classes /class "Display"
```

## /enum-devices

Enumerate devices on the system. An enabled device appears with status **Started**; a disabled device appears as **Disabled**.

```console
pnputil /enum-devices
```

Enumerate only connected devices on the system

```console
pnputil /enum-devices /connected
```

Enumerate device with specific instance ID

```console
pnputil /enum-devices /instanceid "ROOT\SYSTEM\0000"
```

Enumerate all devices with specific class

```console
pnputil /enum-devices /class "Display"
```

Enumerate all devices with specific problem code

```console
pnputil /enum-devices /problem 28
```

Enumerate all devices with problems and display hardware/compatible IDs

```console
pnputil /enum-devices /problem /deviceids
```

Enumerate all devices with specific hardware/compatible ID

```console
pnputil /enum-devices /deviceid "USB\Class_03"
```

Enumerate all devices with specific bus

```console
pnputil /enum-devices /bus "PCI"
```

## /enum-drivers

Enumerate OEM driver packages

```console
pnputil /enum-drivers
```

Enumerate all OEM driver packages of a specific class

```console
pnputil /enum-drivers /class "System"
```

Enumerate all OEM driver packages and display driver files

```console
pnputil /enum-drivers /files
```

## /enum-interfaces

Enumerate only enabled interfaces on the system

```console
pnputil /enum-interfaces /enabled
```

Enumerate all interfaces with specific interface class GUID

```console
pnputil /enum-interfaces /class "{884b96c3-56ef-11d1-bc8c-00a0c91405dd}"
```

## /export-driver

Export driver package

```console
pnputil /export-driver oem6.inf .
```

Export all driver packages

```console
pnputil /export-driver * c:\backup
```

## /remove-device

Remove device specified by device instance ID

```console
pnputil /remove-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"
```

Remove all devices with specific hardware/compatible ID

```console
pnputil /remove-device /deviceid "USB\Class_03"
```

Remove all devices of a specific class on a specific bus

```console
pnputil /remove-device /class "USB" /bus "PCI"
```

## /restart-device

Restart device specified by device instance ID

```console
pnputil /restart-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"
```

Restart all devices with specific hardware/compatible ID

```console
pnputil /restart-device /deviceid "USB\Class_03"
```

Restart all devices of a specific class on a specific bus

```console
pnputil /restart-device /class "USB" /bus "PCI"
```

## /scan-devices

Scan the system for any device hardware changes. Use this command after connecting new hardware to force Windows to detect it.

```console
pnputil /scan-devices
```

After scanning, use /enum-devices /connected to verify your new device was detected.

## /enum-devicetree

Enumerate device tree

```console
pnputil /enum-devicetree
```

Enumerate device tree with "ROOT\SYSTEM\0000" as root

```console
pnputil /enum-devicetree "ROOT\SYSTEM\0000"
```

Enumerate device tree with "ROOT\SYSTEM\0000" as root and display driver information

```console
pnputil /enum-devicetree ROOT\SYSTEM\0000 /drivers
```

Enumerate tree of connected devices and display device interfaces

```console
pnputil /enum-devicetree /connected /interfaces
```

Enumerate tree and display device stack information, interfaces, drivers and services

```console
pnputil /enum-devicetree /stack /interfaces /drivers /services
```

## /enum-containers

Enumerate all device containers on the system

```console
pnputil /enum-containers
```

Enumerate specific device container

```console
pnputil /enum-containers /containerid "{00000000-0000-0000-ffff-ffffffffffff}"
```

Enumerate all connected device containers and associated devices

```console
pnputil /enum-containers /connected /devices
```


Enumerate all disconnected device containers, associated devices and output to a file in XML format

```console
pnputil /enum-containers /disconnected /devices /format xml /output-file disconnecteddevices.xml
```

## Troubleshooting

- Verify you're running the command prompt as Administrator.
- Check the PnPUtil Command Syntax for correct parameter format.
- Use `/enum-devices /problem` to identify device issues.

## Related content

[PnPUtil](pnputil.md)

[PnPUtil Command Syntax](pnputil-command-syntax.md)
