---
title: Location (staple)
description: This property contains all the value entries that pertain to the location of staples on output pages.
ms.date: 07/07/2020
---

# Location (staple)

Schema Path:\\Printer.Finishing.Staple.Location

Node Type:Property

Description:This property contains all the value entries that pertain to the location of staples on output pages.

The Location property contains two child values: **CurrentValue** and **Supported**.

## CurrentValue

Schema Path:\\Printer.Finishing.Staple.Location:CurrentValue

Node Type:Value

Data Type:BIDI\_STRING

Description:The current (default) location at which staples are applied.

The following values are allowed:

StapleTopLeft

StapleBottomLeft

StapleTopRight

StapleBottomRight

StapleDualLeft

StapleDualRight

StapleDualTop

StapleDualBottom

SaddleStitch

Other

Unknown

## Supported

Schema Path:\\Printer.Finishing.Staple.Location:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all the values supported for staple Location.
