---
title: Using mbidgenerator.exe to generate hardware IDs
description: Using mbidgenerator.exe to generate hardware IDs
ms.date: 04/20/2017
---

# Using mbidgenerator.exe to generate hardware IDs

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

To generate hardware ID values for your service metadata package, you can use the MBIDGenerator.exe command-line tool, which is part of the SDK in Windows 8.1 and Windows 10.

**Note**  
In Windows 8 MBIDGenerator.exe was included in the WDK.

 

## Input


MBIDGenerator.exe accepts the following parameters:

``` syntax
MBIDGenerator.exe [/Test] <input file> [<output file>]
```

**Note**  
The *Test* parameter provides non-hashed output and should not be used for generating hardware IDs for submission to the Windows Dev Center Dashboard.

 

## Output


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

 

 





