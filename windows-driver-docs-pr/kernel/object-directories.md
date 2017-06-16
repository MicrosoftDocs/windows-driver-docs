---
title: Object Directories
author: windows-driver-content
description: Object Directories
ms.assetid: b0e0d077-6736-4a54-b1eb-a30962442942
keywords: ["object directories WDK kernel", "named objects WDK kernel", "directories WDK objects", "top-level object directories WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Object Directories


## <a href="" id="ddk-object-directories-kg"></a>


An *object directory* is a named object that is used solely to contain other named objects. For example, the **\\Device** object directory contains the named device objects created by drivers.

Do not confuse object directories with file system directories. Object directories exist only within the object manager, and do not correspond to any directory on disk. (File system directories are, in fact, represented as file objects.)

The following is a list of the top-level object directories that contain objects drivers might create or use:

-   **\\Callbacks**

    The system creates standard callback objects in this directory. For more information, see [Using a System-Defined Callback Object](using-a-system-defined-callback-object.md).

-   **\\Device**

    Drivers create named device objects in this directory. For more information, see [Named Device Objects](named-device-objects.md).

-   **\\KernelObjects**

    The system creates standard event objects in this directory. For more information, see [Standard Event Objects](standard-event-objects.md).

-   **\\DosDevices**

    This directory stores the MS-DOS device name of a device as a symbolic link to the corresponding device object. For more information, see [MS-DOS Device Names](ms-dos-device-names.md).

The system creates other top-level directories, but they are reserved for system use.

Drivers can create new object directories by calling the [**ZwCreateDirectoryObject**](https://msdn.microsoft.com/library/windows/hardware/ff566421) routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Object%20Directories%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


