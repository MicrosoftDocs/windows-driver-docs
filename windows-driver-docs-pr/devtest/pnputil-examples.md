---
title: PnPUtil Examples
description: PnPUtil Examples
ms.date: 11/09/2022
---

# PnPUtil Examples

This topic provides examples on how to use the PnPUtil tool.

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

## /export-driver

Export driver package

```console
pnputil /export-driver oem6.inf .
```

Export all driver packages

```console
pnputil /export-driver * c:\backup
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

## /disable-device

Disable device specified by device instance ID

```console
pnputil /disable-device "USB\VID_045E&PID_00DB\6&870CE29&0&1"
```

Disable all devices with specific hardware/compatible ID

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

## /scan-devices

Scan the system for any device hardware changes

```console
pnputil /scan-devices
```

## /enum-devices

Enumerate only connected devices on the system

```console
pnputil /enum-devices /connected
```

Enumerate device with specific instance ID

```console
pnputil /enum-devices /instanceid "ACPI\PNP0A08\1"
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

## /enum-interfaces

Enumerate only enabled interfaces on the system

```console
pnputil /enum-interfaces /enabled
```

Enumerate all interfaces with specific interface class GUID

```console
pnputil /enum-interfaces /class "{884b96c3-56ef-11d1-bc8c-00a0c91405dd}"
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
