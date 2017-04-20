---
title: Specifying a sensor icon
author: windows-driver-content
description: Specifying a sensor icon
ms.assetid: fe4a204f-befb-45d4-ad95-03b9e788e375
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying a sensor icon


Sensor drivers can specify one of a set of platform-defined icons, or a custom icon, to represent the device in Control Panel. To specify a particular icon, create a DeviceIcon entry in your driver's INX (or INF) file, with the following format:

```
DeviceIcon,,,,"<full path to DLL>,-<resource id>"
```

For example, to specify the light sensor icon, you would add the following section:

```
 
[DriverPropertiesSection]
DeviceIcon,,,,"%SystemRoot%\system32\sensorscpl.dll,-1008" 
 
```

To specify a custom icon, replace the DLL path with the path of the DLL that contains your icon and replace the resource ID with the appropriate value.

If your INX file does not already contain a driver properties section, you must add the `AddProperty` directive to the `_Install.NT` section. For example, a Time Sensor sample could include the following section:

```
 
[TimeSensor_Install.NT]
CopyFiles       = UMDriverCopy
AddProperty     = DriverPropertiesSection 
```

For more information about device properties in INF files, see [**INF AddProperty Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546318).

## Related topics
[**Sensor Icon Constants**](https://msdn.microsoft.com/library/windows/hardware/ff545838)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Specifying%20a%20sensor%20icon%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


