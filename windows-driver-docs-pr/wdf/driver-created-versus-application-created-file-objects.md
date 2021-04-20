---
title: Driver-Created Versus Application-Created File Objects
description: Driver-Created Versus Application-Created File Objects
keywords:
- file object to handle I/O WDK UMDF , driver-created
- file object to handle I/O WDK UMDF , application-created
- I/O requests WDK UMDF , file object, driver-created versus application-created
- User-Mode Driver Framework WDK , file object to handle I/O, driver-created versus application-created
- UMDF WDK , file object to handle I/O, driver-created versus application-created
- user-mode drivers WDK UMDF , file object to handle I/O, driver-created versus application-created
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver-Created Versus Application-Created File Objects


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

When an application opens a handle to a device, the framework calls your driver's [**IQueueCallbackCreate::OnCreateFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackcreate-oncreatefile) method and supplies a pointer to the [**IWDFFile**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdffile) interface for the file object that is associated with the device. Any I/O requests that the application sends to the opened handle are associated with the created file object. When such requests arrive, the framework calls the appropriate method from one of the driver-supplied [UMDF Queue Object Interfaces](/windows-hardware/drivers/ddi/wudfddi/). The driver can then call [**IWDFIoRequest::GetFileObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-getfileobject) to determine the file object associated with the request. The driver can call [**AssignContext**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-assigncontext) on the file object to associate context that is specific to the I/O session.

The following table shows calls the application makes and the resulting notifications that the driver receives.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Application initiates</th>
<th align="left">Driver receives</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>A call to the Microsoft Win32 <a href="/windows/win32/api/fileapi/nf-fileapi-createfilea" data-raw-source="[&lt;strong&gt;CreateFile&lt;/strong&gt;](/windows/win32/api/fileapi/nf-fileapi-createfilea)"><strong>CreateFile</strong></a> function.</p></td>
<td align="left"><p>A call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackcreate-oncreatefile" data-raw-source="[&lt;strong&gt;IQueueCallbackCreate::OnCreateFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackcreate-oncreatefile)"><strong>IQueueCallbackCreate::OnCreateFile</strong></a> method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A call to the Win32 <strong>ReadFileEx</strong>, <strong>WriteFileEx</strong>, or <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a> function.</p></td>
<td align="left"><p>A call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackread-onread" data-raw-source="[&lt;strong&gt;IQueueCallbackRead::OnRead&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackread-onread)"><strong>IQueueCallbackRead::OnRead</strong></a>, <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackwrite-onwrite" data-raw-source="[&lt;strong&gt;IQueueCallbackWrite::OnWrite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackwrite-onwrite)"><strong>IQueueCallbackWrite::OnWrite</strong></a>, or <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol" data-raw-source="[&lt;strong&gt;IQueueCallbackDeviceIoControl::OnDeviceIoControl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol)"><strong>IQueueCallbackDeviceIoControl::OnDeviceIoControl</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A call to the Win32 <strong>CloseHandle</strong> function for the last open handle to the file object.</p></td>
<td align="left"><p>A call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile" data-raw-source="[&lt;strong&gt;IFileCallbackCleanup::OnCleanupFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile)"><strong>IFileCallbackCleanup::OnCleanupFile</strong></a> method.</p>
<p>The driver cancels or completes all I/O requests that are associated with the file object.</p>
<p>After the driver returns from the cleanup notification, UMDF cancels any pending I/O requests.</p>
<p>After cleanup completes and UMDF cancels pending I/O requests, the driver receives a call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile" data-raw-source="[&lt;strong&gt;IFileCallbackClose::OnCloseFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile)"><strong>IFileCallbackClose::OnCloseFile</strong></a> method.</p></td>
</tr>
</tbody>
</table>

 

A system component may issue a create request on behalf of a Universal Windows app. If the driver needs to determine the process ID of the app that issued the create request, it can call the [**IWDFFile3::GetInitiatorProcessId**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdffile3-getinitiatorprocessid) method.

## Driver-created file objects


If your driver needs to create and send an I/O request independent of the application to the next driver in the stack (the default I/O target), the driver must call [**IWDFDevice::CreateWdfFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile) to retrieve a pointer to a [**IWDFDriverCreatedFile**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdrivercreatedfile) interface. In this case, the next driver receives the same notifications that your driver receives when the application generates the request.

The following table shows calls your driver makes and the resulting notifications to the next driver in the stack.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver initiates</th>
<th align="left">Next driver in the stack receives</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>A call to the <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile" data-raw-source="[&lt;strong&gt;IWDFDevice::CreateWdfFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createwdffile)"><strong>IWDFDevice::CreateWdfFile</strong></a> method.</p>
<p>The file object that UMDF creates represents an I/O session between the device and the next device in the stack.</p></td>
<td align="left"><p>A call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackcreate-oncreatefile" data-raw-source="[&lt;strong&gt;IQueueCallbackCreate::OnCreateFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackcreate-oncreatefile)"><strong>IQueueCallbackCreate::OnCreateFile</strong></a> method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A call to the <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest" data-raw-source="[&lt;strong&gt;IWDFDevice::CreateRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createrequest)"><strong>IWDFDevice::CreateRequest</strong></a> method.</p>
<p>A call to format the request (for example, a call to the <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforioctl" data-raw-source="[&lt;strong&gt;IWDFIoTarget::FormatRequestForIoctl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforioctl)"><strong>IWDFIoTarget::FormatRequestForIoctl</strong></a> method).</p>
<p>A call to the <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send" data-raw-source="[&lt;strong&gt;IWDFIoRequest::Send&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send)"><strong>IWDFIoRequest::Send</strong></a> method.</p></td>
<td align="left"><p>A call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackread-onread" data-raw-source="[&lt;strong&gt;IQueueCallbackRead::OnRead&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackread-onread)"><strong>IQueueCallbackRead::OnRead</strong></a>, <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackwrite-onwrite" data-raw-source="[&lt;strong&gt;IQueueCallbackWrite::OnWrite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackwrite-onwrite)"><strong>IQueueCallbackWrite::OnWrite</strong></a>, or <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol" data-raw-source="[&lt;strong&gt;IQueueCallbackDeviceIoControl::OnDeviceIoControl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol)"><strong>IQueueCallbackDeviceIoControl::OnDeviceIoControl</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A call to the <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdrivercreatedfile-close" data-raw-source="[&lt;strong&gt;IWDFDriverCreatedFile::Close&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdrivercreatedfile-close)"><strong>IWDFDriverCreatedFile::Close</strong></a> method.</p></td>
<td align="left"><p>A call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile" data-raw-source="[&lt;strong&gt;IFileCallbackCleanup::OnCleanupFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile)"><strong>IFileCallbackCleanup::OnCleanupFile</strong></a> method.</p>
<p>The driver cancels or completes all I/O requests that are associated with the file object.</p>
<p>After the driver returns from the cleanup notification, UMDF cancels any pending I/O requests.</p>
<p>After cleanup completes and UMDF cancels pending I/O requests, the driver receives a call to its <a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile" data-raw-source="[&lt;strong&gt;IFileCallbackClose::OnCloseFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackclose-onclosefile)"><strong>IFileCallbackClose::OnCloseFile</strong></a> method.</p></td>
</tr>
</tbody>
</table>

 

For the next device in the stack, no difference exists between the file object that is created by an application and the file object that is created by a higher-layer device.

