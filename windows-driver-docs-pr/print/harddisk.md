---
title: HardDisk
description: The value entries for a hard disk installed in the device.
ms.date: 08/31/2021
ms.localizationpriority: medium
---

# HardDisk

Schema Path: \\Printer.Configuration.HardDisk

Node Type: Property

Description: The value entries for a hard disk installed in the device.

The HardDisk property contains three child values: Installed, Capacity, and FreeSpace.

## Installed

Schema Path: \\Printer.Configuration.HardDisk:Installed

Node Type: Value

Data Type: BIDI_BOOL

Description: Indicates whether a hard disk is installed on the device. If **TRUE**, a hard disk is installed; if **FALSE**, a hard disk is not installed.

## Capacity

Schema Path: \\Printer.Configuration.HardDisk:Capacity

Node Type: Value

Data Type: BIDI_INT

Description: The capacity, in megabytes (MB), of the installed hard disk.

## FreeSpace

Schema Path: \\Printer.Configuration.HardDisk:FreeSpace

Node Type: Value

Data Type: BIDI_INT

Description: The currently available free space, in megabytes (MB), of the installed hard disk.
