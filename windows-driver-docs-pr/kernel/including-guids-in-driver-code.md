---
title: Including GUIDs in Driver Code
author: windows-driver-content
description: Including GUIDs in Driver Code
MS-HAID:
- 'Other\_ef1d42c7-4e37-4443-8529-c0c63331cc60.xml'
- 'kernel.including\_guids\_in\_driver\_code'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9235f9e6-9c40-4c4b-a98b-99e6b46a11ce
keywords: ["globally unique identifiers WDK kernel", "GUIDs WDK kernel", "identifiers WDK GUIDs"]
---

# Including GUIDs in Driver Code


## <a href="" id="ddk-including-guids-in-driver-code-kg"></a>


To use GUIDs in a kernel-mode driver, you must do two things:

1.  Include the Initguid.h header file that redefines the **DEFINE\_GUID** macro.

    The Initguid.h header file redefines the **DEFINE\_GUID** macro to instantiate GUIDs (versus just declaring an EXTERN reference). Include this header file in the driver source file where the GUIDs should be instantiated. (User-mode applications include Objbase.h before including header files containing GUID definitions.)

2.  Include the header file(s) that define the GUIDs.

    After the statement to include Initguid.h, you include the header files containing the GUID definitions. A driver might include more than one header file that contains GUID definitions, including system-supplied header files and third-party header files.

The following code excerpt shows the sequence of statements for including GUIDs:

```
:
// include system headers here such as wdm.h
 
#include <initguid.h>
 
// include system and driver-specific header files here that contain
// GUID definitions

...
 
```

Put the above statements in one module of the driver; typically the main module. When the above statements are present, the driver refers to a GUID using its symbolic name.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Including%20GUIDs%20in%20Driver%20Code%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


