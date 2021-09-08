---
title: Name property
description: This property is an vendor-mapped Consumable name.
ms.date: 09/08/2021
ms.localizationpriority: medium
---

# Name property

Schema Path: \\Printer.Consumables.\[Name\]

Node Type: Property

Description: This property is an vendor-mapped Consumable name. The name corresponds to the vendor-specific unique ID for this consumable. This ID enables the possibility for multiple Consumables with the same Type and Color combination. The \[Name\] property is always required and the name cannot contain any spaces.

This property contains the following child values:

- Type

- Color

- Installed

- Level

- Model

## Type

Schema Path: \\Printer.Consumables.\[Name\].Type

Node Type: Value

Description: This value represents the type of the referenced consumable.

The following predefined types are available:

- Ink

- Toner

- Developer

- FuserOil

- Wax

- WasteToner

- WasteInk

- WasteWax

Vendors can add values that are specific to their printing processes or printing devices.

## Color

Schema Path: \\Printer.Consumables.\[Name\].Color

Node Type: BIDI_STRING

Description: This value represents the color of the referenced consumable. This data value is optional, because some types of consumable do not actually have a color associated with them.

The following color types are predefined:

- Black

- Blue

- Color

- Cyan

- Gray

- Green

- Magenta

- PhotoBlack

- PhotoColor

- PhotoCyan

- PhotoMagenta

- PhotoYellow

- Red

- White

- Yellow

Each vendor can add any values specific to their printing process and devices.

## Installed

Schema Path:\\Printer.Consumables.\[Name\].Installed

Node Type:Value

Data Type: BIDI_BOOL

Description: This value indicates whether the consumable item that Type and Color describe is installed on the device.

## Level

Schema Path: \\Printer.Consumables.\[Name\].Level

Node Type: Value

Data Type: BIDI_INT

Description: This value represents the current level of the referenced consumable. The unit for this value is percentage points. A full level would have a value of 100, and an empty level would have a value of 0. If the level is not measurable, a value of -1 (unknown) should be returned.

## Model

Schema Path: \\Printer.Consumables.\[Name\].Model

Node Type: Value

Data Type: BIDI_STRING

Description: An optional value that represents the vendor Model indicator for the referenced consumable. This value enables a client to distinguish exactly what version of a particular Type and Color combination Consumable is installed in the device.
