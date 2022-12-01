---
title: DevGen Examples
description: DevGen examples.
ms.date: 12/01/2022
---

# DevGen Examples

This page provides examples on how to use the DevGen tool.

## /add

Create a software device

```console
devgen /add
```

Create a software device with a custom instance ID

```console
devgen /add /instanceid "TESTDEVICE"
```

Create a software device with specific hardware and compatible IDs

```console
devgen /add /hardwareid "USB\VID_1234&PID_ABCD" /compatibleid "USB\DevClass_FF&SubClass_FF"
```

Create a software device under a parent and unplug after user prompt

```console
devgen /add /parent "ACPI\PNP0A03\0" /wait /unplug
```

Create a software device and remove it after 5 seconds

```console
devgen /add /wait 5000
```

Create a root enumerated device

```console
devgen /add /bus ROOT
```

Create a root enumerated device with a custom instance ID

```console
devgen /add /bus ROOT /instanceid 1
```

Create a root enumerated device and remove after user prompt

```console
devgen /add /bus ROOT /wait
```

## /remove

Remove a device

```console
devgen /remove "SWD\DEVGEN\0000"
```

Remove a device and any children

```console
devgen /remove "SWD\DEVGEN\0000" /subtree
```