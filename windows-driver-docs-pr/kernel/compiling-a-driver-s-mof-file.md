---
title: Compiling a Driver's MOF File
author: windows-driver-content
description: Compiling a Driver's MOF File
ms.assetid: 0a4ab163-3e2c-48e9-9659-756d35ad445f
keywords: ["WMI WDK kernel , publishing schema", "publishing WMI schema WDK", "schema publishing WDK WMI", "MOF files WDK WMI", "compiling MOF files"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Compiling a Driver's MOF File


## <a href="" id="ddk-compiling-a-driver-s-mof-file-kg"></a>


To compile a MOF file that defines WMI data and event blocks, use the MOF compiler, called Mofcomp, that is included with the Microsoft Windows operating systems. Use the following syntax:

```
 mofcomp -WMI -B:filename.bmf filename.mof
```

The following items appear in the preceding syntax:

<a href="" id="-wmi"></a>**-WMI**  
Validates all classes in *filename.mof* for use with WMI. If any class definition is invalid, Mofcomp deletes the output file *filename.bmf*. If **-WMI** is omitted, you should run [Wmimofck](using-wmimofck-exe.md) on *filename.bmf* to validate the classes. A driver must either use the WMI switch or run Wmimofck to validate the MOF. Failure to do so can result in the MOF file not loading correctly into the WMI schema.

<a href="" id="-b-filename-bmf"></a>**-B:***filename.bmf*  
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Compiling%20a%20Driver's%20MOF%20File%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


