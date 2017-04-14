---
title: Bidirectional Communication Schema Hierarchy
author: windows-driver-content
description: Bidirectional Communication Schema Hierarchy
ms.assetid: b3435c17-f72b-4925-8d13-bd3e71b4947e
keywords: ["bidirectional communication schema WDK print", "bidi communication schema WDK print", "hierarchy WDK bidi communication"]
---

# Bidirectional Communication Schema Hierarchy


The bidirectional communication schema contains the following hierarchy or tree of properties and values.

-   Properties are shown in plain text (for example, DeviceInfo).

-   Properties that are generated from bidi mapping files are shown in brackets (for example, \[Type\]).

-   Values are shown in italic text (for example, FriendlyName).

```
Printer
  DeviceInfo
 FriendlyName
 Manufacturer
 ModelName
 Location
    FirmwareVersion
    IEEE1284DeviceId
    NetworkingInfo
      HostName
      IPAddress
 Comment
  Configuration
    Memory
 Size
 PS
    HardDisk
 Installed
 Capacity
 FreeSpace
    DuplexUnit
 Installed
  Consumables
    [Name]
 Installed
      Type
      Color
      Level
      Model
  Layout
    NumberUp
      PagesPerSheet
 CurrentValue
 Supported
      Direction
 CurrentValue
 Supported
    Orientation
 CurrentValue
 Supported
    Resolution
 CurrentValue
 Supported
    InputBins
      [TrayName]
 Installed
 MediaSize
 MediaType
 MediaColor
 FeedDirection
 Capacity
 Level
  Finishing
 CollationSupported
 JogOffsetSupported
    Staple
 Installed
      Location
 CurrentValue
 Supported
      Angle
 CurrentValue
 Supported
    HolePunch
 Installed
      Pattern
 CurrentValue
 Supported
      Location
 CurrentValue
 Supported
    OutputBins
      [TrayName]
 Installed
 Capacity
 Level
Maintenance
    AlignHead
    CleanHead
Status
    Summary
 State
 StateReason
    Detailed
      Event###
 Name
        Component
 Group
 Name
 Severity
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Bidirectional%20Communication%20Schema%20Hierarchy%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


