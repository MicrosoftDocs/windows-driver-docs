---
title: PwrTest Log File
description: PwrTest Log File
ms.assetid: f4782b27-25e0-4ec3-bf0b-82a614815f90
---

# PwrTest Log File


PwrTest supports multiple simultaneous logging outputs in different formats: .log (plaintext), .xml (format varies per scenario), .wtl (WTTLog), and .etl (ETW trace). By default, PwrTest generates log files named pwrtestlog.\*. You can use the **/ln:***name* option to change the log names. These files will be generated in the current directory by default. You can use the **/lf:***folder* option to change the output location.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PwrTest%20Log%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





