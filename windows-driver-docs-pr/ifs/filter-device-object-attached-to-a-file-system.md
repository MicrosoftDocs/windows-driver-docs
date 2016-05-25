---
title: Filter Device Object Attached to a File System
author: windows-driver-content
description: Filter Device Object Attached to a File System
ms.assetid: 5fb0ec43-a639-4b2a-8057-3313e9dee457
keywords: ["filter device objects WDK file system", "device object I/O requests WDK file system", "filter drivers WDK file system , device object I/O requests", "file system filter drivers WDK , device object I/O requests"]
---

# Filter Device Object Attached to a File System


## <span id="ddk_a_filter_device_object_attached_to_a_file_system_if"></span><span id="DDK_A_FILTER_DEVICE_OBJECT_ATTACHED_TO_A_FILE_SYSTEM_IF"></span>


To filter an entire file system, a file system filter driver creates a filter device object and attaches it above a file system driver's CDO in the global file system queue.

### <span id="types_of_i_o_requests_that_are_sent_to_a_file_system"></span><span id="TYPES_OF_I_O_REQUESTS_THAT_ARE_SENT_TO_A_FILE_SYSTEM"></span>Types of I/O Requests That Are Sent to a File System

A filter device object that is attached above a file system can generally expect to receive the following types of I/O requests:

[**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548649)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670)

[**IRP\_MJ\_SHUTDOWN**](https://msdn.microsoft.com/library/windows/hardware/ff549423)

If the file system supports opening handles to its control device object, filters can expect to see the following types of I/O requests as well:

[**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff548608)

[**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff548621)

[**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630)

File system filter device objects attached to file systems are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack by default.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Filter%20Device%20Object%20Attached%20to%20a%20File%20System%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


