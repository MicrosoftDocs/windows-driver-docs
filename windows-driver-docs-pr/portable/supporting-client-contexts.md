---
Description: Supporting Client Contexts
title: Supporting Client Contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Client Contexts


A Windows Portable Devices (WPD) driver provides the communication channel between applications and the physical device. There can be multiple WPD applications running at any time. The driver needs to handle requests from different clients on the computer and identify the clients based on the queued requests. In other words, the driver needs an efficient and easy way to store client data on a per connection basis, and retrieve the data upon request.

The User-Mode Driver Frameork (UMDF) supports this capability by using a context area: a generic mechanism in which a driver saves client data. A WPD driver should allocate a data structure or object to hold the client data, assign the data structure to the context area for the framework object, and retrieve the context at a later time.

The appropriate per connection WDF framework object to use is the WDF file object.

## <span id="Assigning_the_Context"></span><span id="assigning_the_context"></span><span id="ASSIGNING_THE_CONTEXT"></span>Assigning the Context


The driver assigns the context when the client computer opens a connection to it.

When a WPD application calls the **IPortableDevice::Open** or the **IPortableDeviceService::Open** method, the WPD API creates a handle to the driver by using the Win32 **CreateFile** method. On the driver side, the User-Mode Driver Frameork (UMDF) initializes an **IWDFFile** object and forwards it, along with the Creation request, to the driver's **IQueueCallbackCreate::OnCreateFile** method. The **IWDFFile** object in this case represents a Win32 **HANDLE** that is used for subsequent communication from this client to the driver.

You can find an example of a **CreateFile** callback implementation in the WpdWudfSampleDriver's **CQueue::OnCreateFile** method. A driver-specific ContextMap COM object is used to store client data (application name, version, in-progress enumeration, and resource contexts, and so on). Be aware that the use of COM objects as context data is not required by UMDF; UMDF sees the context data as a **PVOID**. If you are using a COM object to store context data, your driver must maintain the reference count for that COM object, and ensure that its resources are freed in the appropriate cleanup methods.

To save context data, the driver initializes a new ContextMap object, and calls the **IWDFObject::AssignContext** method for the **IWDFFile** object that is handed in by UMDF. The parameters for this method are pointers to an **IObjectCleanup** object and the newly created ContextMap. The **IObjectCleanup** object contains the context cleanup code; the newly created map contains the data being stored. The driver calls the **IObjectCleanup::OnCleanup** method when the file object is destroyed during CloseHandle.

In addition, only one context can be assigned to the file object (or any UMDF framework object). Subsequent calls to the **AssignContext** method fail if a context has already been assigned. To add or remove client-specific data dynamically, a driver can implement a mapping object to manage the data and assign a pointer to that object as the context of the file object. For an example, refer to the WpdWudfSampleDriver's ContextMap object.

## <span id="Retrieving_and_Saving_Context_Data"></span><span id="retrieving_and_saving_context_data"></span><span id="RETRIEVING_AND_SAVING_CONTEXT_DATA"></span>Retrieving and Saving Context Data


To access the client data during requests, a WPD driver retrieves the context from the given **IWDFFile** object.

The retrieval sequence is accomplished by completing the following steps:

1.  The driver calls the **IWDFIoRequest::GetFileObject** method to obtain the **IWDFFile** object.
2.  The driver calls the **IWDFObject::RetrieveContext** method on the **IWDFFile** object to access the context area. In the sample driver, the context area is the pointer to the ContextMap object that was created in **CQueue::OnCreateFile** when the application called **IPortableDevice::Open**.
3.  The driver adds data to, or removes data from, the ContextMap object directly when it processes the WPD commands. Each time an application connects by calling **IPortableDevice::Open**, it will have its own **IWDFFile** and ContextMap objects.

Refer to the code from WpdWudfSampleDriver for examples of how to retrieve context maps and add client information. The following table describes where you can find the code in the WpdWudfSampleDriver.

| Example                                                                                                                  | Location in sample driver           |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| Retrieving the context map from the file object for the WDF request.                                                     | **CQueue::OnDeviceIoControl**       |
| Adding client information to the context map when processing the WPD\_COMMAND\_COMMON\_SAVE\_CLIENT\_INFORMATION command | **WpdBaseDriver::OnSaveClientInfo** |

 

## <span id="Releasing_the_Context"></span><span id="releasing_the_context"></span><span id="RELEASING_THE_CONTEXT"></span>Releasing the Context


When the client application calls the **IPortableDevice::Close** method, the WPD API in turn calls **CloseHandle** on the Win32 handle that is associated with the open connection. Before UMDF destroys the **IWDFFile** object in response to the **CloseHandle**, it calls the file object's **IObjectCleanup::OnCleanup** method that the driver passed into **AssignContext** during **OnCreateFile**.

An example implementation of the **IQueueCleanup** callback is the WpdWudfSampleDriver driver's **CQueue::OnCleanup** method. This method retrieves the ContextMap that is stored in the IWDFObject object (in this case, the instance of IWDFFile from **OnCreateFile**) and frees the allocated memory, including the objects that the ContextMap holds. To avoid memory leaks, make sure that the objects are properly cleaned up, and (if applicable) decrement the reference count.

## <span id="related_topics"></span>Related topics


****
[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





