---
title: Driver-Created Versus Application-Created File Objects
description: Driver-Created Versus Application-Created File Objects
ms.assetid: f81ae0ed-a29c-476e-9b16-ff554eef1de9
keywords: ["file object to handle I/O WDK UMDF , driver-created", "file object to handle I/O WDK UMDF , application-created", "I/O requests WDK UMDF , file object, driver-created versus application-created", "User-Mode Driver Framework WDK , file object to handle I/O, driver-created versus application-created", "UMDF WDK , file object to handle I/O, driver-created versus application-created", "user-mode drivers WDK UMDF , file object to handle I/O, driver-created versus application-created"]
---

# Driver-Created Versus Application-Created File Objects


\[This topic applies to UMDF 1.*x*.\]

When an application opens a handle to a device, the framework calls your driver's [**IQueueCallbackCreate::OnCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff556841) method and supplies a pointer to the [**IWDFFile**](https://msdn.microsoft.com/library/windows/hardware/ff558912) interface for the file object that is associated with the device. Any I/O requests that the application sends to the opened handle are associated with the created file object. When such requests arrive, the framework calls the appropriate method from one of the driver-supplied [UMDF Queue Object Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff561301). The driver can then call [**IWDFIoRequest::GetFileObject**](https://msdn.microsoft.com/library/windows/hardware/ff559099) to determine the file object associated with the request. The driver can call [**AssignContext**](https://msdn.microsoft.com/library/windows/hardware/ff560208) on the file object to associate context that is is specific to the I/O session.

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
<td align="left"><p>A call to the Microsoft Win32 [<strong>CreateFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.</p></td>
<td align="left"><p>A call to its [<strong>IQueueCallbackCreate::OnCreateFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556841) method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A call to the Win32 <strong>ReadFileEx</strong>, <strong>WriteFileEx</strong>, or [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216) function.</p></td>
<td align="left"><p>A call to its [<strong>IQueueCallbackRead::OnRead</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556875), [<strong>IQueueCallbackWrite::OnWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556885), or [<strong>IQueueCallbackDeviceIoControl::OnDeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556854) method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A call to the Win32 <strong>CloseHandle</strong> function for the last open handle to the file object.</p></td>
<td align="left"><p>A call to its [<strong>IFileCallbackCleanup::OnCleanupFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554905) method.</p>
<p>The driver cancels or completes all I/O requests that are associated with the file object.</p>
<p>After the driver returns from the cleanup notification, UMDF cancels any pending I/O requests.</p>
<p>After cleanup completes and UMDF cancels pending I/O requests, the driver receives a call to its [<strong>IFileCallbackClose::OnCloseFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554910) method.</p></td>
</tr>
</tbody>
</table>

 

A system component may issue a create request on behalf of a Universal Windows app. If the driver needs to determine the process ID of the app that issued the create request, it can call the [**IWDFFile3::GetInitiatorProcessId**](https://msdn.microsoft.com/library/windows/hardware/hh451279) method.

## Driver-created file objects


If your driver needs to create and send an I/O request independent of the application to the next driver in the stack (the default I/O target), the driver must call [**IWDFDevice::CreateWdfFile**](https://msdn.microsoft.com/library/windows/hardware/ff558828) to retrieve a pointer to a [**IWDFDriverCreatedFile**](https://msdn.microsoft.com/library/windows/hardware/ff558895) interface. In this case, the next driver receives the same notifications that your driver receives when the application generates the request.

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
<td align="left"><p>A call to the [<strong>IWDFDevice::CreateWdfFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558828) method.</p>
<p>The file object that UMDF creates represents an I/O session between the device and the next device in the stack.</p></td>
<td align="left"><p>A call to its [<strong>IQueueCallbackCreate::OnCreateFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556841) method.</p></td>
</tr>
<tr class="even">
<td align="left"><p>A call to the [<strong>IWDFDevice::CreateRequest</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557021) method.</p>
<p>A call to format the request (for example, a call to the [<strong>IWDFIoTarget::FormatRequestForIoctl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559230) method).</p>
<p>A call to the [<strong>IWDFIoRequest::Send</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559149) method.</p></td>
<td align="left"><p>A call to its [<strong>IQueueCallbackRead::OnRead</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556875), [<strong>IQueueCallbackWrite::OnWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556885), or [<strong>IQueueCallbackDeviceIoControl::OnDeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556854) method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A call to the [<strong>IWDFDriverCreatedFile::Close</strong>](https://msdn.microsoft.com/library/windows/hardware/ff558897) method.</p></td>
<td align="left"><p>A call to its [<strong>IFileCallbackCleanup::OnCleanupFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554905) method.</p>
<p>The driver cancels or completes all I/O requests that are associated with the file object.</p>
<p>After the driver returns from the cleanup notification, UMDF cancels any pending I/O requests.</p>
<p>After cleanup completes and UMDF cancels pending I/O requests, the driver receives a call to its [<strong>IFileCallbackClose::OnCloseFile</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554910) method.</p></td>
</tr>
</tbody>
</table>

 

For the next device in the stack, no difference exists between the file object that is created by an application and the file object that is created by a higher-layer device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Driver-Created%20Versus%20Application-Created%20File%20Objects%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




