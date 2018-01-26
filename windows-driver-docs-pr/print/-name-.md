---
title: \ Name\
author: windows-driver-content
description: \ Name\
ms.assetid: 5259ea1a-a251-479b-88f1-711d5933868a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20%5BName%5D%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


