---
title: WMI Class Names and Base Classes
description: WMI Class Names and Base Classes
ms.assetid: 6c3f74a3-e596-4694-8619-db38d67e030c
keywords: ["base classes WDK WMI", "names WDK WMI", "classes WDK WMI", "WMI WDK kernel , classes"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Class Names and Base Classes





WMI class names are case-insensitive, must start with a letter, and cannot begin or end with an underscore. All remaining characters must be letters, digits, or underscores.

WMI client applications can access a driver's WMI class names and display them to users. Descriptive class names can help make classes more intuitive to use.

WMI class names must be unique within the WMI namespace. Consequently a driver's WMI class names cannot duplicate those defined by another driver.

To help prevent name collisions, a driver writer can define a driver-specific base class and derive all of the driver's WMI classes from that base class. The class name and base class name together are more likely to yield a unique name. For example, the following shows an abstract base class for a serial driver's data blocks:

```cpp
// Serial driver&#39;s base class for data blocks
[abstract]
class MSSerial {
}
 
// Example class definition for a data block
[
    //Class qualifiers 
]
class MSSerial_StandardSerialInformation : MSSerial 
{
    //Data items
}
```

Device-specific custom data blocks should include the manufacturer, model, and type of driver or device in the base class name. For example:

```cpp
[abstract]
class Adaptec1542 {
}
 
class Adaptec1542_Bandwidth : Adaptec1542 {
    //Data items
}
 
class Adaptec1542_Speed : Adaptec1542 {
    //Data items
}
```

WMI allows only one abstract base class in a given class hierarchy. Classes that define event blocks must derive from **WmiEvent**, which is an abstract base class, so the **abstract** qualifier cannot be used in a driver-defined base class for event blocks. Instead, derive a nonabstract base class from **WmiEvent**, then derive individual event classes from that base class. For example:

```cpp
//Serial driver&#39;s base class for event blocks
class MSSerialEvent : WmiEvent 
{
}
 
//Example class definition for an event block
[
    //Class qualifiers 
]
class MSSerial_SendEvent : MSSerialEvent 
{
    //Data items
}
```

For more information about defining base classes in MOF format, see the Microsoft Windows SDK.

 

 




