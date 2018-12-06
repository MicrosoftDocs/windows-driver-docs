---
title: \ Name\
description: \ Name\
ms.assetid: 5259ea1a-a251-479b-88f1-711d5933868a
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# \[Name\]


Schema Path:\\Printer.Consumables.\[Name\]

Node Type:Property

Description:This property is an vendor-mapped Consumable name. The name corresponds to the vendor-specific unique ID for this consumable. This ID enables the possibility for multiple Consumables with the same Type and Color combination. The \[Name\] property is always required and the name cannot contain any spaces.

This property contains the following child values:

Type

Color

Installed

Level

Modal

### <span id="type"></span><span id="TYPE"></span> Type

Schema Path:\\Printer.Consumables.\[Name\].Type

Node Type:Value

Description:This value represents the type of the referenced consumable.

The following predefined types are available:

Ink

Toner

Developer

FuserOil

Wax

WasteToner

WasteInk

WasteWax

Vendors can add values that are specific to their printing processes or printing devices.

### <span id="color"></span><span id="COLOR"></span> Color

Schema Path:\\Printer.Consumables.\[Name\].Color

Node Type:BIDI\_STRING

Description:This value represents the color of the referenced consumable. This data value is optional, because some types of consumable do not actually have a color associated with them.

The following color types are predefined.

Black

Blue

Color

Cyan

Gray

Green

Magenta

PhotoBlack

PhotoColor

PhotoCyan

PhotoMagenta

PhotoYellow

Red

White

Yellow

Each vendor can add any values specific to their printing process and devices.

### <span id="installed"></span><span id="INSTALLED"></span> Installed

Schema Path:\\Printer.Consumables.\[Name\].Installed

Node Type:Value

Data Type:BIDI\_BOOL

Description:This value indicates whether the consumable item that Type and Color describe is installed on the device.

### <span id="level"></span><span id="LEVEL"></span> Level

Schema Path:\\Printer.Consumables.\[Name\].Level

Node Type:Value

Data Type:BIDI\_INT

Description: This value represents the current level of the referenced consumable. The unit for this value is percentage points. A full level would have a value of 100, and an empty level would have a value of 0. If the level is not measurable, a value of -1 (unknown) should be returned.

### <span id="model"></span><span id="MODEL"></span> Model

Schema Path:\\Printer.Consumables.\[Name\].Model

Node Type:Value

Data Type: BIDI\_STRING

Description:An optional value that represents the vendor Model indicator for the referenced consumable. This value enables a client to distinguish exactly what version of a particular Type and Color combination Consumable is installed in the device.

 

 




