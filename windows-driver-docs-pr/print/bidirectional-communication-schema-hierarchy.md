---
title: Bidirectional Communication Schema Hierarchy
description: Bidirectional Communication Schema Hierarchy
ms.assetid: b3435c17-f72b-4925-8d13-bd3e71b4947e
keywords:
- bidirectional communication schema WDK print
- bidi communication schema WDK print
- hierarchy WDK bidi communication
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bidirectional Communication Schema Hierarchy

The bidirectional communication schema contains the following hierarchy or tree of properties and values.

-   Properties are shown in plain text (for example, DeviceInfo).

-   Properties that are generated from bidi mapping files are shown in brackets (for example, \[Type\]).

-   Values are shown in italic text (for example, FriendlyName).

```cpp
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

 

 




