---
title: Orientation
description: Current page orientation and a list of page orientations supported by the device.
ms.date: 08/31/2021
ms.localizationpriority: medium
---

# Orientation

Schema Path: \\Printer.Layout.Orientation

Node Type: Property

Description: The property associated with page orientation. The value entries that are children of this property are the current page orientation and a list of page orientations supported by the device.

The Orientation property contains two child values: **CurrentValue** and **Supported**.

## CurrentValue

Schema Path: \\Printer.Layout.Orientation:CurrentValue

Node Type: Value

Data Type: BIDI_STRING

Description: The current (default) orientation in which pages will be printed.

Must be one of the following values.

- Portrait

- Landscape

- ReversePortrait

- ReverseLandscape

## Supported

Schema Path: \\Printer.Layout.Orientation:Supported

Node Type: Value

Data Type: BIDI_STRING

Description: A comma-separated list of all values supported for Orientation.
