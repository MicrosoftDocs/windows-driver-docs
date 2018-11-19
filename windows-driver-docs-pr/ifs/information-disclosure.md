---
title: Information Disclosure
description: Information Disclosure
ms.assetid: e5794acb-44f7-4775-854b-69884f60658a
keywords:
- threat models WDK file systems , information disclosure
- security threat models WDK file systems , information disclosure
- information disclosure WDK file systems
- I/O WDK file systems
- buffers WDK file systems
- disclosure WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Information Disclosure


## <span id="ddk_information_disclosure_if"></span><span id="DDK_INFORMATION_DISCLOSURE_IF"></span>


For a driver, information disclosure typically relates to exposing information to an application through poor buffer handling. For example, a driver with a buffered I/O request normally indicates the amount of data being returned by setting the **Information** member of the *IOStatus* block structure. The I/O manager then uses that information to copy the results back into the application's buffer.

If the driver indicates more data is being returned, the I/O manager will copy additional data from the *SystemBuffer*. However, if the driver did not fill in the balance of the *SystemBuffer*, then whatever was in that memory will be returned back to the application, potentially exposing sensitive data to the application. Witness the problem with network drivers where extra information might be sent to other systems because the data buffers used were not cleared. For example, an ICMP ping response might include extra information. This problem of exposing data inadvertently is very real and happens in a wide variety of systems.

For a file system or file system filter driver, there is the added risk of disclosing file information to users who should not be allowed to access the data. This can be done in many different ways:

-   A filter driver that uses [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) to open the file, and then provides access to the data through its intermediate handle. The **ZwCreateFile** function will, by default, open the file and bypassing security checks because the request is coming from kernel mode. So, access using this handle may disclose information that would not normally be available to an application.

    If the filter driver wants to enforce access checks to ensure it is not exposing data that should not be exposed, then the filter driver should specify OBJ\_FORCE\_ACCESS\_CHECK in the *ObjectAttributes* parameter of the [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) function.

-   A filter driver that opens a handle in kernel mode (bypassing access checks) but does not specify OBJ\_KERNEL\_HANDLE. So the handle created is placed in the current process's handle table. This handle, with full access to the data, is then visible in user mode. A rogue application can be watching for such handles and try to use them to access the data.

-   A file system or file system filter driver that posts an IRP\_MJ\_CREATE request, and then processes it in the context of a system worker thread. When the IRP is processed by the system worker thread, the create operation will normally be completed using the privileges of the system thread. So, access using these system privileges can disclose information that would not normally be available to the application.

-   A file system or file system filter driver that performs file object-based I/O without confirming that the calling process should be allowed access to the given data.

Because of their unique role in managing and protecting information, file systems and file system filter drivers must be particularly vigilant in ensuring their protection of information.

 

 




