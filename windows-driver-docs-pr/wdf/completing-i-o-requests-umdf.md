---
title: Completing I/O Requests in UMDF
description: Completing I/O Requests in UMDF
keywords:
- I/O requests WDK UMDF , completing
- request processing WDK UMDF , completing requests
- completing I/O requests WDK UMDF
ms.date: 04/20/2017
---

# Completing I/O Requests in UMDF


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

Every I/O request must eventually be completed by a UMDF driver. To complete a request, the driver must call either the [**IWDFIoRequest::Complete**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-complete) or [**IWDFIoRequest::CompleteWithInformation**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-completewithinformation) method. When the driver completes the request, it indicates one of the following scenarios:

-   The requested I/O operation finished successfully.

-   The requested I/O operation started but failed before it finished.

-   The requested I/O operation is not supported or is not valid at the time it was received and therefore cannot communicate with the device.

-   The requested I/O operation was [canceled](canceling-i-o-requests.md).

The driver calls the [**IWDFIoRequest::CompleteWithInformation**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-completewithinformation) method to pass additional information about the request operation. For example, for a read operation, the driver should provide the number of bytes read.

To complete an I/O request, the driver must pass the appropriate completion status to the *CompletionStatus* parameter in the call to [**IWDFIoRequest::Complete**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-complete) or [**IWDFIoRequest::CompleteWithInformation**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-completewithinformation). The driver uses an HRESULT code to communicate the status of the completed request.

The [UMDF driver host process](umdf-driver-host-process.md) converts the HRESULT code to an NTSTATUS code before it passes the completed request to the reflector (Wudfrd.sys). The reflector passes the NTSTATUS code to the operating system. The operating system converts the NTSTATUS code to a Microsoft Win32 error code before it presents the result to the calling application.

To ensure that your driver's error codes can be converted correctly, you should create error codes by either of the following techniques:

-   Use an error code from Winerror.h and apply the HRESULT\_FROM\_WIN32 macro.

-   Use an error code from Ntstatus.h and apply the HRESULT\_FROM\_NT macro.

For more information about these macros, see the Microsoft Windows SDK documentation.

The following example code shows how to complete a request with a suitable error code:

```cpp
VOID
STDMETHODCALLTYPE
CMyQueue::OnWrite(
    __in IWDFIoQueue *pWdfQueue,
    __in IWDFIoRequest *pWdfRequest,
    __in SIZE_T BytesToWrite
    )
{
            -------------------- 
    if( BytesToWrite > MAX_WRITE_LENGTH ) {
        pWdfRequest->CompleteWithInformation(HRESULT_FROM_WIN32(ERROR_MORE_DATA), 0);
        return;
    }
            ---------------------
}
```

When a driver completes a request successfully, it returns S\_OK, which is an HRESULT value. Because S\_OK is equivalent to NO\_ERROR in Winerror.h and STATUS\_SUCCESS in Ntstatus.h, the conversion macros are not needed.

If [Driver Verifier](../devtest/driver-verifier.md) is enabled for the reflector, it identifies an invalid status code and causes a system bugcheck.

**Note**   Driver Verifier for Windows XP incorrectly causes a system bugcheck for Win32 error codes whose values exceed decimal 1024 (1024L). If your driver runs on Windows XP, please be aware of this issue if you enable Driver Verifier for the reflector.

 

If the driver previously sent a request to a lower-level driver, the driver requires notification when the lower-level driver completes the request. To register for notification, the driver calls the [**IWDFIoRequest::SetCompletionCallback**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-setcompletioncallback) method to register the interface for the method that the framework calls when the lower-level driver completes the request. The driver implements the [**IRequestCallbackRequestCompletion::OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion) callback function to perform the operations required to complete the request.

A driver does not complete an I/O request that it has created by calling [**IWDFDevice::CreateRequest**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest). Instead, the driver must call [**IWDFObject::DeleteWdfObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-deletewdfobject) to delete the request object, typically after an I/O target has completed the request.

For example, a driver might receive a read or write request for an amount of data that is larger than the driver's I/O targets can handle at one time. The driver must divide the data into several smaller requests and send these smaller requests to one or more I/O targets. Techniques for handling this situation include:

-   Calling [**IWDFDevice::CreateRequest**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest) to create a single additional request object that represents a smaller request.

    The driver can send this request synchronously to an I/O target. The smaller request's [**IRequestCallbackRequestCompletion::OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion) callback function can call [**IWDFIoRequest2::Reuse**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest2-reuse) so that the driver can reuse the request and send it to the I/O target again. After the I/O target completes the last of the smaller requests, the **OnCompletion** callback function can call [**IWDFObject::DeleteWdfObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-deletewdfobject) to delete the driver-created request object and the driver can call [**IWDFIoRequest::Complete**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-complete) to complete the original request.

-   Calling [**IWDFDevice::CreateRequest**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest) to create several additional request objects that represent the smaller requests.

    The driver's I/O targets can process these multiple smaller requests asynchronously. The driver can register a [**OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion) callback function for each of the smaller requests. Each time that the **OnCompletion** callback function is called, it can call [**IWDFObject::DeleteWdfObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-deletewdfobject) to delete a driver-created request object. After the I/O target completes all of the smaller requests, the driver can call [**IWDFIoRequest::Complete**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-complete) to complete the original request.

### Obtaining Completion Information

To obtain information about an I/O request that another driver has completed, a UMDF-based driver can:

-   Use the [**IWDFRequestCompletionParams**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfrequestcompletionparams) interface to obtain an I/O request's completion status and other information.

-   Use the [**IWDFIoRequestCompletionParams**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfiorequestcompletionparams) interface to obtain an I/O request's memory buffers.

-   Use the [**IWDFUsbRequestCompletionParams**](/windows-hardware/drivers/ddi/wudfusb/nn-wudfusb-iwdfusbrequestcompletionparams) interface to obtain memory buffers and other information related to a request that was sent to a USB target pipe object.

In addition, a UMDF-based driver can use the [**IWDFIoRequest2::GetStatus**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest2-getstatus) method to obtain an I/O request's current status, either before or after the request has been completed.

 

