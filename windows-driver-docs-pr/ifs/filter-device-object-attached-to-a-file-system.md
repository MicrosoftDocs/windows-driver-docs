---
title: Filter Device Object Attached to a File System
description: Filter Device Object Attached to a File System
keywords:
- filter device objects WDK file system
- device object I/O requests WDK file system
- filter drivers WDK file system , device object I/O requests
- file system filter drivers WDK , device object I/O requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Device Object Attached to a File System


## <span id="ddk_a_filter_device_object_attached_to_a_file_system_if"></span><span id="DDK_A_FILTER_DEVICE_OBJECT_ATTACHED_TO_A_FILE_SYSTEM_IF"></span>


To filter an entire file system, a file system filter driver creates a filter device object and attaches it above a file system driver's CDO in the global file system queue.

### <span id="types_of_i_o_requests_that_are_sent_to_a_file_system"></span><span id="TYPES_OF_I_O_REQUESTS_THAT_ARE_SENT_TO_A_FILE_SYSTEM"></span>Types of I/O Requests That Are Sent to a File System

A filter device object that is attached above a file system can generally expect to receive the following types of I/O requests:

[**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](./irp-mj-file-system-control.md)

[**IRP\_MJ\_SHUTDOWN**](./irp-mj-shutdown.md)

If the file system supports opening handles to its control device object, filters can expect to see the following types of I/O requests as well:

[**IRP\_MJ\_CLEANUP**](./irp-mj-cleanup.md)

[**IRP\_MJ\_CLOSE**](./irp-mj-close.md)

[**IRP\_MJ\_CREATE**](./irp-mj-create.md)

File system filter device objects attached to file systems are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack by default.

 

