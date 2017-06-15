---
title: WMI Class Names and Base Classes
author: windows-driver-content
description: WMI Class Names and Base Classes
MS-HAID:
- 'WMI\_f3801d44-ed43-4cb3-bcef-f8fa2ba8ff80.xml'
- 'kernel.wmi\_class\_names\_and\_base\_classes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6c3f74a3-e596-4694-8619-db38d67e030c
keywords: ["base classes WDK WMI", "names WDK WMI", "classes WDK WMI", "WMI WDK kernel , classes"]
---

# WMI Class Names and Base Classes


## <a href="" id="ddk-wmi-class-names-and-base-classes-kg"></a>


WMI class names are case-insensitive, must start with a letter, and cannot begin or end with an underscore. All remaining characters must be letters, digits, or underscores.

WMI client applications can access a driver's WMI class names and display them to users. Descriptive class names can help make classes more intuitive to use.

WMI class names must be unique within the WMI namespace. Consequently a driver's WMI class names cannot duplicate those defined by another driver.

To help prevent name collisions, a driver writer can define a driver-specific base class and derive all of the driver's WMI classes from that base class. The class name and base class name together are more likely to yield a unique name. For example, the following shows an abstract base class for a serial driver's data blocks:

```
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

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Class%20Names%20and%20Base%20Classes%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


