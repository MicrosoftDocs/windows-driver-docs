---
title: Resolutions
description: Contains all the value entries that pertain to the print resolutions that are supported by the device.
ms.date: 09/02/2021
ms.localizationpriority: medium
---

# Resolutions

Schema Path: \\Printer.Layout.Resolutions

Node Type: Property

Description: This property contains all the value entries that pertain to the print resolutions that are supported by the device. All resolutions are in dots per inch (dpi).

The Resolutions property contains two child values: **CurrentValue** and **Supported**.

## CurrentValue

Schema Path: \\Printer.Layout.Resolutions:CurrentValue

Node Type: Value

Data Type: BIDI_INT

Description: The current (default) value of the device print resolution, in dots per inch (dpi).

## Supported

Schema Path: \\Printer.Layout.Resolutions:Supported

Node Type: Value

Data Type: BIDI_STRING

Description: A comma-separated list of all the values supported for Resolutions, in dots per inch (dpi).
