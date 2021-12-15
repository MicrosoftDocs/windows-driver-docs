---
title: Angle property
description:  Contains all of the value entries that pertain to the orientation of staples.
ms.date: 08/31/2021
---

# Angle property

Schema Path: \\Printer.Finishing.Staple.Angle

Node Type: Property

Description: This property contains all of the value entries that pertain to the orientation of staples that are applied to output pages.

The Angle property contains two child values: CurrentValue and Supported.

## CurrentValue

Schema Path: \\Printer.Finishing.Staple.Angle:CurrentValue

Node Type: Value

Data Type: BIDI_INT

Description: The current (default) orientation for staples to be applied.

The following values are allowed:

- Horizontal

- Vertical

- Slanted

- unknown

## Supported

Schema Path: \\Printer.Finishing.Staple.Angle:Supported

Node Type: Value

Data Type: BIDI_STRING

Description: A comma-separated list of all the values supported for staple Angle.
