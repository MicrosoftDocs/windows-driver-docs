---
title: Framework File Objects
description: Framework File Objects
ms.assetid: 93ec5dd7-8ef0-4cea-9253-ea5d7869d4b8
keywords:
- I/O requests WDK KMDF , file objects
- file objects WDK KMDF
- request processing WDK KMDF , file objects
- framework objects WDK KMDF , file objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework File Objects





When an application or a driver attempts to access a device, typically by creating or opening a file, the operating system sends a file creation request to the driver stack. When the application or driver has finished using the device, the system sends file cleanup and close requests to the driver stack. The [request types](https://msdn.microsoft.com/library/windows/hardware/ff552503) of these three requests are **WdfRequestTypeCreate**, **WdfRequestTypeCleanup**, and **WdfRequestTypeClose**, respectively.

Typically, unless your driver has called [**WdfDeviceInitSetExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff546097), the driver must perform file-specific or other access-specific operations when it receives file creation, cleanup, and close requests, because multiple files can be open simultaneously or multiple applications can access the device simultaneously. The driver must therefore keep track of the I/O requests that are associated with each file or application.

The framework defines *framework file objects*, which represent an application or driver's means for accessing a device, such as a file, directory, volume, mail slot, named pipe, or the entire device. A file name can be associated with a file object, but the meaning of a file name is driver-specific. For more information about file names, see [Controlling Device Namespace Access](https://msdn.microsoft.com/library/windows/hardware/ff542068).

If your driver must handle file operations, it must call [**WdfDeviceInitSetFileObjectConfig**](https://msdn.microsoft.com/library/windows/hardware/ff546107) from within its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. The **WdfDeviceInitSetFileObjectConfig** method receives a [**WDF\_FILEOBJECT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551319) structure as input. The driver uses this structure to register its [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868), [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700), and [*EvtFileClose*](https://msdn.microsoft.com/library/windows/hardware/ff541702) callback functions and, optionally, to indicate whether the framework should create a framework file object each time that the driver receives a file creation request.

Most drivers that handle file operations store file-specific information in the framework file object's [context space](framework-object-context-space.md). If your driver handles file operations but does not need to store information in a file object's context space, the framework does not have to create framework file objects for the driver.

### Creating or Opening a File

When the framework receives a file creation request for your function driver, it:

1.  Creates a framework file object that represents the file, unless the driver previously indicated that it does not need to use framework file objects.

2.  Calls your driver's [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function, if the driver has registered the callback function.

The [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function typically [obtains information](#obtaining-file-information) about the file, such as its name and file object flags. The driver typically stores this information in the context space of the framework file object.

Instead of providing an [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function, the driver can call [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920) to set an I/O queue to receive all file creation requests (**WdfRequestTypeCreate** request type). The driver will subsequently receive file creation requests in the queue's [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) request handler. (An I/O queue cannot receive file creation requests if the **DefaultQueue** member of the queue's [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure is set to **TRUE**.)

If your driver does not provide an [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function and does not set up an I/O queue to handle **WdfRequestTypeCreate**-typed I/O requests, the framework:

-   Completes all file creation requests for the driver with a status value of STATUS\_SUCCESS, if your driver is a function driver.

-   Forwards all file creation requests to the next-lower driver, if your driver is a filter driver.

(To see how you can change this behavior, see the **AutoForwardCleanupClose** member of the [**WDF\_FILEOBJECT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551319) structure.)

**Note**   If your function driver does not provide any [device interfaces](using-device-interfaces.md) that applications can use to access the driver's devices, the driver must provide an [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function that completes all file creation requests with a status value for which NT\_SUCCESS(*status*) equals **FALSE**. Otherwise, a malicious application might attempt to access a device by using the name of the device's physical device object (PDO). (All PDOs have [names](controlling-device-access-in-kmdf-drivers.md#naming-device-objects-only-when-necessary).)

 

If a driver [forwards](forwarding-i-o-requests.md) a creation request to an I/O target, the driver must not subsequently [complete](completing-i-o-requests.md) the request with a failure status value unless the driver receives a failure status value from the I/O target. Otherwise, the lower drivers will not be notified that the creation request failed and might attempt to operate as if the file is open.

If a driver forwards a creation request to an I/O target, the driver cannot set the [**WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET**](https://msdn.microsoft.com/library/windows/hardware/ff552493) flag if the framework has created a framework file object for the creation request. Therefore, the driver cannot set the WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET flag for a creation request unless it also sets the [**WdfFileObjectNotRequired**](https://msdn.microsoft.com/library/windows/hardware/ff551315) flag.

Note that if a driver completes a creation request with an error status, the framework deletes the framework file object but does not call the driver's [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700) or [*EvtFileClose*](https://msdn.microsoft.com/library/windows/hardware/ff541702) callback functions. Therefore, if the driver allocates extra object-specific memory outside of the file object's context space it must provide an [*EvtCleanupCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540840) or [*EvtDestroyCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540841) callback function that deletes the allocated memory.

For Windows Vista and later, file creation requests can be [canceled](canceling-i-o-requests.md). Earlier versions of the Windows operating system do not support canceling file creation requests.

The system always creates a Windows Driver Model (WDM) file object for each creation request that comes from a user application. If a driver sends a creation request, it might not create a WDM file object for the request. Typically, the framework does not create a framework file object if a WDM file object is not present. However, if your driver has called [**WdfDeviceInitSetExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff546097) and if the driver has set [**WdfFileObjectWdfCannotUseFsContexts**](https://msdn.microsoft.com/library/windows/hardware/ff551315) in the **FileObjectClass** member of the [**WDF\_FILEOBJECT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551319) structure, the framework will create a framework file object even if a WDM file object does not exist.

### <a href="" id="obtaining-file-information"></a> Obtaining File Information

The driver's [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function can call one or more of the following object methods to obtain information about an application or driver's access to a device:

<a href="" id="---------wdffileobjectgetfilename--------"></a>[**WdfFileObjectGetFileName**](https://msdn.microsoft.com/library/windows/hardware/ff547310)  
Returns the file name that is contained in a framework file object.

<a href="" id="---------wdffileobjectgetflags--------"></a>[**WdfFileObjectGetFlags**](https://msdn.microsoft.com/library/windows/hardware/ff547316)  
Returns the flags that are contained within a framework file object.

<a href="" id="---------wdffileobjectwdmgetfileobject--------"></a>[**WdfFileObjectWdmGetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff547324)  
Returns the WDM file object that is associated with a framework file object.

<a href="" id="---------wdfrequestgetparameters--------"></a>[**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969)  
Retrieves the parameters that are associated with a framework request object. If the [request type](https://msdn.microsoft.com/library/windows/hardware/ff552503) is **WdfRequestTypeCreate**, the **Parameters.Create** member of the [**WDF\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff552472) structure contains information about the file creation request.

Typically, the driver stores file information in the framework file object's context space. When your driver obtains an I/O request from one if its I/O queues, the driver can call [**WdfRequestGetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff549963) to obtain a handle to the framework file object that is associated with the request. The driver can then retrieve the file information that it stored in the framework file object's context space.

Your driver can search an I/O queue for requests that are associated with a particular file by calling [**WdfIoQueueRetrieveRequestByFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff548470).

If your driver has a pointer to a WDM [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure, the driver can call [**WdfDeviceGetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff546007) to obtain a handle to the framework file object that is associated with the WDM device object.

### Closing a File

When an application or another driver closes a file, the framework receives a cleanup request and a close request for your driver. The framework:

1.  Calls your driver's [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700) and [*EvtFileClose*](https://msdn.microsoft.com/library/windows/hardware/ff541702) callback functions, if the driver has registered these callback functions.

2.  Deletes the framework file object that represents the file.

The driver's [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700) and [*EvtFileClose*](https://msdn.microsoft.com/library/windows/hardware/ff541702) callback functions receive a handle to the framework file object. The driver can call [**WdfFileObjectGetDevice**](https://msdn.microsoft.com/library/windows/hardware/ff547302) to determine which framework device object is associated with the framework file object.

 

 





