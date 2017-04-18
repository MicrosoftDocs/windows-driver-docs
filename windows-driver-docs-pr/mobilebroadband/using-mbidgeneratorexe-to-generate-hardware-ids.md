---
title: Using mbidgenerator.exe to generate hardware IDs
description: Using mbidgenerator.exe to generate hardware IDs
ms.assetid: 2f2286e2-9300-4ef8-8e13-0851b60cd8eb
---

# Using mbidgenerator.exe to generate hardware IDs


To generate hardware ID values for your service metadata package, you can use the MBIDGenerator.exe command-line tool, which is part of the SDK in Windows 8.1 and Windows 10.

**Note**  
In Windows 8 MBIDGenerator.exe was included in the WDK.

 

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


MBIDGenerator.exe accepts the following parameters:

``` syntax
MBIDGenerator.exe [/Test] <input file> [<output file>]
```

**Note**  
The *Test* parameter provides non-hashed output and should not be used for generating hardware IDs for submission to the Windows Dev Center Dashboard.

 

## <span id="Output"></span><span id="output"></span><span id="OUTPUT"></span>Output


The output from the MBIDGenerator.exe is through a standard command-line output display. Optionally, you can specify a path and file name for the output file. Errors are always reported back to the command prompt.

The output values appear in the following way:

``` syntax
<HardwareIDList>
  <HardwareID>MBAE:0:hashednumber1</HardwareID>
  <HardwareID>MBAE:0:hashednumber2</HardwareID>
  <HardwareID>MBAE:0:hashednumber3</HardwareID>
</HardwareIDList>
```

You can take the output from MBIDGenerator.exe and insert it into the [PackageInfo XML schema](packageinfo-xml-schema.md) of your service metadata package.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Using%20mbidgenerator.exe%20to%20generate%20hardware%20IDs%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




