---
title: Compiling a Driver's MOF File
description: Compiling a Driver's MOF File
ms.assetid: 0a4ab163-3e2c-48e9-9659-756d35ad445f
keywords: ["WMI WDK kernel , publishing schema", "publishing WMI schema WDK", "schema publishing WDK WMI", "MOF files WDK WMI", "compiling MOF files"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Compiling a Driver's MOF File





To compile a MOF file that defines WMI data and event blocks, use the MOF compiler, called Mofcomp, that is included with the Microsoft Windows operating systems. Use the following syntax:

```cpp
 mofcomp -WMI -B:filename.bmf filename.mof
```

The following items appear in the preceding syntax:

<a href="" id="-wmi"></a>**-WMI**  
Validates all classes in *filename.mof* for use with WMI. If any class definition is invalid, Mofcomp deletes the output file *filename.bmf*. If **-WMI** is omitted, you should run [Wmimofck](using-wmimofck-exe.md) on *filename.bmf* to validate the classes. A driver must either use the WMI switch or run Wmimofck to validate the MOF. Failure to do so can result in the MOF file not loading correctly into the WMI schema.

<a href="" id="-b-filename-bmf"></a>**-B:**<em>filename.bmf</em>  
Requests that the compiler create a platform-independent binary version of the MOF file in *filename.bmf* without making any modifications to the CIMOM object repository.

<a href="" id="filename-mof"></a>*filename.mof*  
Specifies the name of the input MOF file.

To learn more about how to use Mofcomp, open a Command Prompt window and type **mofcomp /?**.

For more information about Mofcomp, see [MofComp](http://go.microsoft.com/fwlink/p/?linkid=51316) and other topics in the Windows SDK.

To include the compiled MOF file as a resource in the driver's binary image, add the following line to the driver's resource script (RC) file:

**MofResource MOFDATA** *filename.bmf*

A driver specifies its MOF resource name in response to a registration request (an [**IRP\_MN\_REGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551731) or [**IRP\_MN\_REGINFO\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff551734) request with **Parameters.WMI.DataPath** set to WMIREGISTER):

-   If the driver is using the WMI library routines to handle WMI IRPs, it specifies the MOF resource name in its [*DpWmiQueryReginfo*](https://msdn.microsoft.com/library/windows/hardware/ff544097) routine.

-   If the driver is handling WMI IRPs directly, it specifies the MOF resource name in the [**WMIREGINFO**](https://msdn.microsoft.com/library/windows/hardware/ff565832) structure that the driver passes to WMI.

For more information about handling **IRP\_MN\_REGINFO** and **IRP\_MN\_REGINFO\_EX** requests, see [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

For more information about handling WMI IRPs using WMI iibrary routines, see [Handling WMI Requests](handling-wmi-requests.md).

For more information about defining and including resources in executable files, see the Microsoft Windows SDK.

 

 




