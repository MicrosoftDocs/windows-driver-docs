---
title: Pattern Property
description: Contains all the value entries that pertain to the patterns in which holes can be punched in output pages.
ms.date: 09/08/2021
---

# Pattern property

Schema Path: \\Printer.Finishing.HolePunch.Pattern

Node Type: Property

Description: This property contains all the value entries that pertain to the patterns in which holes can be punched in output pages.

The Pattern property contains two child values: **CurrentValue** and **Supported**.

## CurrentValue

Schema Path: \\Printer.Finishing.HolePunch.Pattern:CurrentValue

Node Type: Value

Data Type: BIDI_STRING

Description: The current (default) hole punch pattern to be applied to output pages.

The following values are allowed:

- TwoHoleUSTop

- ThreeHoleUS

- TwoHoleDIN

- FourHoleDIN

- TwentyTwoHoleUS

- NineteenHoleUS

- TwoHoleMetric

- Swedish4Hole

- TwoHoleUSSide

- FiveHoleUS

- SevenHoleUS

- Mixed7H4S

- Norweg6Hole

- Metric26Hole

- Metric30Hole

- unknown

## Supported

Schema Path: \\Printer.Finishing.HolePunch.Pattern:Supported

Node Type: Value

Data Type: BIDI_STRING

Description: A comma-separated list of all values supported for hole punch Pattern.
