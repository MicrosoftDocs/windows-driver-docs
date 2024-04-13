---
title: Object Directories
description: Object Directories
keywords: ["object directories WDK kernel", "named objects WDK kernel", "directories WDK objects", "top-level object directories WDK kernel"]
ms.date: 06/16/2017
---

# Object Directories





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

    This directory stores the MS-DOS device name of a device as a symbolic link to the corresponding device object. For more information, see [MS-DOS Device Names](introduction-to-ms-dos-device-names.md).

The system creates other top-level directories, but they are reserved for system use.

Drivers can create new object directories by calling the [**ZwCreateDirectoryObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatedirectoryobject) routine.

 

