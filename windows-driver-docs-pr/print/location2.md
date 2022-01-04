---
title: Location (hole punch)
description: This property contains all the value entries that pertain to the location at which holes are punched in output pages.
ms.date: 07/07/2020
---

# Location (hole punch)

Schema Path:\\Printer.Finishing.HolePunch.Location

Node Type:Property

Description:This property contains all the value entries that pertain to the location at which holes are punched in output pages.

The Location property contains two child values: **CurrentValue** and **Supported**.

## CurrentValue

Schema Path:\\Printer.Finishing.HolePunch.Location:CurrentValue

Node Type:Value

Data Type:BIDI\_INT

Description:The current (default) location at which holes are punched.

The following values are allowed:

Top

Bottom

Left

Right

## Supported

Schema Path:\\Printer.Finishing.HolePunch.Location:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all the values supported for hole punch locations.
