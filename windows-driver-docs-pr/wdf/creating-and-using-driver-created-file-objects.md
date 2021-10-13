---
title: Creating and Using Driver-Created File Objects
description: Creating and Using Driver-Created File Objects
keywords:
- driver-created file object WDK UMDF
- driver-created file object WDK UMDF , creating and using
- file object to handle I/O WDK UMDF , driver-created, creating and using
- I/O requests WDK UMDF , file object, creating and using
- User-Mode Driver Framework WDK , file object to handle I/O, creating and using
- UMDF WDK , file object to handle I/O, creating and using
- user-mode drivers WDK UMDF , file object to handle I/O, creating and using
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating and Using Driver-Created File Objects


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

If your driver needs to create and send an I/O request that is independent of the application to the next driver in the stack (the default I/O target), the driver must create and close its own file objects.

### Creating a File Object

Your driver must call the [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile) method to create a file object for the driver's use. When the driver calls **IWDFDevice::CreateWdfFile**, the framework sends a create request to the next driver in the stack. The next driver in the stack could be in kernel mode or in user mode.

This create-file request processing is different in the Windows Driver Model (WDM). In WDM, a call to the [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) function causes a create IRP to go to the top of the kernel-mode stack. The following figure shows create-file request processing in UMDF versus WDM:

![create-file request handling in umdf versus wdm.](images/drvrcrtfile.gif)

By calling [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile), the driver can create a file object and then send I/O requests during device start, before the whole stack has started.

The next driver in the stack must determine if it can handle the create-file request or if it must forward the request further down the stack.

After calling [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile), a driver cannot cancel the create operation.

## Using the File Object


To send an asynchronous read request to the next driver stacked below it, your driver can use the following pattern.

1.  Call [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile) to create the file object.
2.  Call [**IWDFDevice::GetDefaultIoTarget**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-getdefaultiotarget) to retrieve the interface representing the lower level driver.
3.  Call [**IWDFDevice::CreateRequest**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest) to create an unformatted [**IWDFIoRequest**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequest) object.
4.  Call [**IWDFIoRequest::SetCompletionCallback**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-setcompletioncallback) to register a [**IRequestCallbackRequestCompletion**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-irequestcallbackrequestcompletion) interface for the [**OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion) method that the framework calls when an I/O request completes.
5.  Call [**IWDFIoTarget::FormatRequestForRead**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforread), providing a pointer to the [**IWDFDriverCreatedFile**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdrivercreatedfile) interface in the *pFile* parameter.
6.  Call [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) to send the request.

## Closing the File Object


The driver that called [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile) must later call [**IWDFDriverCreatedFile::Close**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdrivercreatedfile-close).

Typically, your driver calls [**IWDFDriverCreatedFile::Close**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdrivercreatedfile-close) either from its [**IPnpCallbackHardware::OnReleaseHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onreleasehardware) or [**IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediocleanup) callback method.

When the driver calls [**IWDFDriverCreatedFile::Close**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdrivercreatedfile-close), the framework calls the next driver's [**IFileCallbackCleanup::OnCleanupFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile) method. In this method, the next driver must cancel or complete all pending I/O requests that are associated with the file object. The framework then cancels any I/O requests created by the driver that called [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile). The framework does not cancel any I/O requests that lower drivers in the stack may have associated with the file object. It is the driver's responsibility to cancel any such requests. The file object only closes after all I/O requests associated with it have completed.

Next, the framework calls the next driver's [**IFileCallbackClose::OnCloseFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile) method. At this point, the framework guarantees that the next driver will not receive additional I/O requests for this file object.

After the framework calls [**OnCloseFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile), it destroys the [IWDFFile](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile) interface that represents the file object.

If driver-created file objects remain after the driver's device-removal methods (for example [**IPnpCallbackHardware::OnReleaseHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onreleasehardware) and [**IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediocleanup)) return, the framework generates a driver stop. For information about troubleshooting this problem, see [Determining Why UMDF Indicates Outstanding Files at Device Removal Time](determining-why-umdf-indicates-outstanding-files-at-device-removal-tim.md).

 

