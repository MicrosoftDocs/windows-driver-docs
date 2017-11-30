---
title: IDebugAdvanced2 Request method
description: The Request method performs a variety of different operations.
ms.assetid: efb3c93c-5405-418b-a063-afa8e5e9e59a
keywords: ["Request method Windows Debugging", "Request method Windows Debugging , IDebugAdvanced2 interface", "IDebugAdvanced2 interface Windows Debugging , Request method", "Request method Windows Debugging , IDebugAdvanced3 interface", "IDebugAdvanced3 interface Windows Debugging , Request method"]
topic_type:
- apiref
api_name:
- IDebugAdvanced2.Request
- IDebugAdvanced3.Request
api_location:
- dbgeng.h
api_type:
- COM
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IDebugAdvanced2::Request method


The **Request** method performs a variety of different operations.

Syntax
------

```ManagedCPlusPlus
HRESULT Request(
  [in]            ULONG  Request,
  [in, optional]  PVOID  InBuffer,
  [in]            ULONG  InBufferSize,
  [out, optional] PVOID  OutBuffer,
  [in]            ULONG  OutBufferSize,
  [out, optional] PULONG OutSize
);
```

Parameters
----------

*Request* \[in\]  
Specifies which operation to perform. **Request** can be one of the values in the following table. Details of each operation can be found by following the link in the "Request" column.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Request</th>
<th align="left">Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_SOURCE_PATH_HAS_SOURCE_SERVER</strong>](debug-request-source-path-has-source-server.md)</p></td>
<td align="left"><p>Check the source path for a source server.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DEBUG_REQUEST_TARGET_EXCEPTION_CONTEXT</strong>](debug-request-target-exception-context.md)</p></td>
<td align="left"><p>Return the [thread context](https://msdn.microsoft.com/library/windows/hardware/ff554702#thread-context) for the stored event in a user-mode minidump file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_TARGET_EXCEPTION_THREAD</strong>](debug-request-target-exception-thread.md)</p></td>
<td align="left"><p>Return the operating system thread ID for the stored event in a user-mode minidump file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DEBUG_REQUEST_TARGET_EXCEPTION_RECORD</strong>](debug-request-target-exception-record.md)</p></td>
<td align="left"><p>Return the exception record for the stored event in a user-mode minidump file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_GET_ADDITIONAL_CREATE_OPTIONS</strong>](debug-request-get-additional-create-options.md)</p></td>
<td align="left"><p>Return the default process creation options.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DEBUG_REQUEST_SET_ADDITIONAL_CREATE_OPTIONS</strong>](debug-request-set-additional-create-options.md)</p></td>
<td align="left"><p>Set the default process creation options.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_GET_WIN32_MAJOR_MINOR_VERSIONS</strong>](debug-request-get-win32-major-minor-versions.md)</p></td>
<td align="left"><p>Return the version of Windows that is currently running on the target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DEBUG_REQUEST_READ_USER_MINIDUMP_STREAM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541575)</p></td>
<td align="left"><p>Read a stream from a user-mode minidump target.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_TARGET_CAN_DETACH</strong>](debug-request-target-can-detach.md)</p></td>
<td align="left"><p>Check to see if it is possible for the debugger engine to detach from the current process (leaving the process running but no longer being debugged).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DEBUG_REQUEST_SET_LOCAL_IMPLICIT_COMMAND_LINE</strong>](debug-request-set-local-implicit-command-line.md)</p></td>
<td align="left"><p>Set the [debugger engine](https://msdn.microsoft.com/library/windows/hardware/ff551059#debugger-engine)'s implicit command line.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_GET_CAPTURED_EVENT_CODE_OFFSET</strong>](debug-request-get-captured-event-code-offset.md)</p></td>
<td align="left"><p>Return the current event's instruction pointer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>DEBUG_REQUEST_READ_CAPTURED_EVENT_CODE_STREAM</strong>](debug-request-read-captured-event-code-stream.md)</p></td>
<td align="left"><p>Return up to 64 bytes of memory at the current event's instruction pointer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DEBUG_REQUEST_EXT_TYPED_DATA_ANSI</strong>](debug-request-ext-typed-data-ansi.md)</p></td>
<td align="left"><p>Perform a variety of different operations that aid in the interpretation of typed data.</p></td>
</tr>
</tbody>
</table>

 

*InBuffer* \[in, optional\]  
Specifies the input to this method. The type and interpretation of the input depends on the *Request* parameter.

*InBufferSize* \[in\]  
Specifies the size of the input buffer *InBuffer*. If the request requires no input, *InBufferSize* should be set to zero.

*OutBuffer* \[out, optional\]  
Receives the output from this method. The type and interpretation of the output depends on the *Request* parameter. If *OutBuffer* is **NULL**, the output is not returned.

*OutBufferSize* \[in\]  
Specifies the size of the output buffer *OutBufferSize*. If the type of the output returned to *OutBuffer* has a known size, *OutBufferSize* is usually expected to be exactly that size, even if *OutBuffer* is set to **NULL**.

*OutSize* \[out, optional\]  
Receives the size of the output returned in the output buffer *OutBuffer*. If *OutSize* is **NULL**, this information is not returned.

Return value
------------

The interpretation of the return value depends on the value of the *Request* parameter. Unless otherwise stated, the following values may be returned.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>S_OK</strong></td>
<td align="left"><p>The method was successful.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>S_FALSE</strong></td>
<td align="left"><p>The method was successful. However, the output would not fit in the output buffer <em>OutBuffer</em>, so truncated output was returned.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>E_INVALIDARG</strong></td>
<td align="left"><p>The size of the input buffer <em>InBufferSize</em> or the size of the output buffer <em>OutBufferSize</em> was not the expected value.</p></td>
</tr>
</tbody>
</table>

 

This method may also return error values. See [**Return Values**](https://msdn.microsoft.com/library/windows/hardware/ff549771) for more details.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Dbgeng.h (include Dbgeng.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IDebugAdvanced2**](https://msdn.microsoft.com/library/windows/hardware/ff549803)

[**IDebugAdvanced3**](https://msdn.microsoft.com/library/windows/hardware/ff549807)

[**DEBUG\_REQUEST\_SOURCE\_PATH\_HAS\_SOURCE\_SERVER**](debug-request-source-path-has-source-server.md)

[**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_CONTEXT**](debug-request-target-exception-context.md)

[**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_THREAD**](debug-request-target-exception-thread.md)

[**DEBUG\_REQUEST\_TARGET\_EXCEPTION\_RECORD**](debug-request-target-exception-record.md)

[**DEBUG\_REQUEST\_GET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-get-additional-create-options.md)

[**DEBUG\_REQUEST\_SET\_ADDITIONAL\_CREATE\_OPTIONS**](debug-request-set-additional-create-options.md)

[**DEBUG\_REQUEST\_GET\_WIN32\_MAJOR\_MINOR\_VERSIONS**](debug-request-get-win32-major-minor-versions.md)

[**DEBUG\_REQUEST\_READ\_USER\_MINIDUMP\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff541575)

[**DEBUG\_REQUEST\_TARGET\_CAN\_DETACH**](debug-request-target-can-detach.md)

[**DEBUG\_REQUEST\_SET\_LOCAL\_IMPLICIT\_COMMAND\_LINE**](debug-request-set-local-implicit-command-line.md)

[**DEBUG\_REQUEST\_GET\_CAPTURED\_EVENT\_CODE\_OFFSET**](debug-request-get-captured-event-code-offset.md)

[**DEBUG\_REQUEST\_READ\_CAPTURED\_EVENT\_CODE\_STREAM**](debug-request-read-captured-event-code-stream.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20IDebugAdvanced2::Request%20method%20%20RELEASE:%20%2811/27/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





