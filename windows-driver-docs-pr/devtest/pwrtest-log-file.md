---
title: PwrTest Log File
description: PwrTest Log File
ms.assetid: f4782b27-25e0-4ec3-bf0b-82a614815f90
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PwrTest Log File


PwrTest supports multiple simultaneous logging outputs in different formats: .log (plaintext), .xml (format varies per scenario), .wtl (WTTLog), and .etl (ETW trace). By default, PwrTest generates log files named pwrtestlog.\*. You can use the **/ln:**<em>name</em> option to change the log names. These files will be generated in the current directory by default. You can use the **/lf:**<em>folder</em> option to change the output location.

The WTTLog file format is common to all Microsoft Windows Driver Kit (WDK) tools that use the WTTLog interface. PwrTest will not generate a .wtl (WTTLog) log file if you run PwrTest on a computer that does not have WTTLog installed.

The PwrTest .xml log file (pwrtestlog.xml) provides information about the specific scenario that is run. All PwrTest .xml log files have the following root element and header:

```XML
<PwrTestLog date="today&#39;s date" time="beginning time" filename = "logfile path">
  <SystemInformation>
    <ComputerName></ComputerName>
    <OSBuildNumber></OSBuildNumber>
    <SystemManufacturer></SystemManufacturer>
    <SystemProductName></SystemProductName>
    <BIOSVersion></BIOSVersion>
    <BIOSReleaseDate></BIOSReleaseDate>
    <ProcessorCount></ProcessorCount>
    <ProcessorPackageCount></ProcessorPackageCount>
  </SystemInformation>

  ... 
  scenario tags and data
  ...

</PwrTestLog>
```

## <span id="related_topics"></span>Related topics


[PwrTest Syntax](pwrtest-syntax.md)

 

 






