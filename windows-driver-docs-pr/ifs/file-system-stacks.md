---
title: File System Stacks
description: File System Stacks
ms.assetid: 67839ffb-fe38-42c2-8f33-89d01d796d8a
keywords:
- filter drivers WDK file system , file system stacks
- file system filter drivers WDK , file system stacks
- file system stacks WDK
- volumes WDK file system , device objects
- VDOs WDK file system
- control device objects WDK file system
- CDOs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Stacks


## <span id="ddk_file_system_stacks_if"></span><span id="DDK_FILE_SYSTEM_STACKS_IF"></span>


File system drivers create two different types of device objects: control device objects (CDO) and volume device objects (VDO). A *file system stack* consists of one of these device object, together with any filter device objects for file system filter drivers that are attached to it. The file system's device object always forms the bottom of the stack.

### <span id="ddk_file_system_control_device_objects_if"></span><span id="DDK_FILE_SYSTEM_CONTROL_DEVICE_OBJECTS_IF"></span>File System Control Device Objects

File system control device objects represent entire file systems, rather than individual volumes, and are stored in the global file system queue. A file system creates one or more named control device objects in its **DriverEntry** routine. For example, FastFat creates two CDOs: one for fixed media and one for removable media. CDFS creates only one CDO, because it has only removable media.

File system control device objects are required to be named. This is because file system filter drivers, as well as many kernel-mode support routines, rely on this difference between volume device objects and control device objects as a way of telling them apart.

### <span id="ddk_file_system_volume_device_objects_if"></span><span id="DDK_FILE_SYSTEM_VOLUME_DEVICE_OBJECTS_IF"></span>File System Volume Device Objects

File system volume device objects represent volumes mounted by file systems. A file system creates a volume device object when it mounts a volume, usually in response to a volume mount request. Unlike a control device object, a volume device object is always associated with a specific logical or physical storage device.

**Note**   Unlike control device objects, volume device objects must never be named, because naming a volume device object would create a security hole.

 

 

 




