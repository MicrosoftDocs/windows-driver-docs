---
title: WindowsInfo XML Example
description: WindowsInfo XML Example
ms.assetid: 5933512e-d2bf-437f-abd8-dc3486e07be0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WindowsInfo XML Example

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The following XML document uses the [WindowsInfo XML schema](windowsinfo-xml-schema.md) to specify the display actions for the service that is specified within a metadata package:

``` syntax
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<WindowsInfo xmlns="http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/"
             xmlns:v2="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/WindowsInfov2">
  <ShowDeviceInDisconnectedState>false</ShowDeviceInDisconnectedState>
</WindowsInfo>
```

 

 





