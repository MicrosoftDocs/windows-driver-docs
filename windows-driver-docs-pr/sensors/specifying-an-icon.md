---
title: Specifying a sensor icon
description: Specifying a sensor icon
ms.assetid: fe4a204f-befb-45d4-ad95-03b9e788e375
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying a sensor icon


Sensor drivers can specify one of a set of platform-defined icons, or a custom icon, to represent the device in Control Panel. To specify a particular icon, create a DeviceIcon entry in your driver's INX (or INF) file, with the following format:

```c
DeviceIcon,,,,"<full path to DLL>,-<resource id>"
```

For example, to specify the light sensor icon, you would add the following section:

```c

[DriverPropertiesSection]
DeviceIcon,,,,"%SystemRoot%\system32\sensorscpl.dll,-1008"
```

To specify a custom icon, replace the DLL path with the path of the DLL that contains your icon and replace the resource ID with the appropriate value.

If your INX file does not already contain a driver properties section, you must add the `AddProperty` directive to the `_Install.NT` section. For example, a Time Sensor sample could include the following section:

```c

[TimeSensor_Install.NT]
CopyFiles       = UMDriverCopy
AddProperty     = DriverPropertiesSection
```

For more information about device properties in INF files, see [**INF AddProperty Directive**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addproperty-directive).

## Related topics
[**Sensor Icon Constants**](sensor-icon-constants.md)



