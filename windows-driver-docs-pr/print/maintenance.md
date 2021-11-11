---
title: Maintenance
description: Contains information about the maintenance of the print device.
ms.date: 08/31/2021
ms.localizationpriority: medium
---

# Maintenance

Schema Path: \\Printer.Maintenance

Node Type: Property

The Maintenance property contains information about the maintenance of the print device.

The Maintenance property contains two child values: **AlignHead** and **CleanHead**.

## AlignHead

Schema Path: \\Printer.Maintenance.AlignHead

Node Type: Value

Data Type: BIDI_BOOL

Description: This value represents a command to perform a head alignment procedure on the device. This value is a write-only value. An attempt to read this value should be rejected. If the value is set to 1, the device should perform the command.

## CleanHead

Schema Path: \\Printer.Maintenance.CleanHead

Node Type: Value

Data Type: BIDI_BOOL

Description: This value represents a command to perform a head cleaning procedure on the device. This value is a write-only value. An attempt to read this value should be rejected. If the value is set to 1, the device should perform the command.
