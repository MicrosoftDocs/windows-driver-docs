---
title: RDF_IOCTL_VENDOR callback function
description: RDF_IOCTL_VENDOR callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
---

# RDF\_IOCTL\_VENDOR callback function

The RDF\_IOCTL\_VENDOR callback function performs vendor-specific IOCTL operations.

## Syntax

```cpp
NTSTATUS (*ReaderFunction[RDF_IOCTL_VENDOR])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

- *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device. For more information about the members of this structure, see Remarks.

## Return value

This function returns an NTSTATUS value. Because this function executes a vendor-defined IOCTL call, the value returned depends upon the function that is performed. The possible NTSTATUS values are:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_SUCCESS</strong></td>
<td><p>Function successfully executed.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_NO_MEDIA</strong></td>
<td><p>No smart card is inserted in the reader.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_IO_TIMEOUT</strong></td>
<td><p>The request timed out.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_BUFFER_TOO_SMALL</strong></td>
<td><p>The user's reply buffer is too small.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td><p>The request is not valid for the IOCTL.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_PENDING</strong></td>
<td><p>The operation is pending.</p></td>
</tr>
</tbody>
</table>

## Remarks

It is optional for smart card reader drivers to implement this callback function.

On input, the caller must pass the following values to the function:

  - **SmartcardExtension-\>MajorIoControlCode**  
    Contains a vendor-specific IOCTL code. Refer to the macro SCARD\_CTL\_CODE in *Winsmcrd.h* for information about how to define a vendor-specific IOCTL code. Note that the code must be between 2048 and 4095.

  - **SmartcardExtension-\>IoRequest.RequestBuffer**  
    A pointer to the user's input buffer.

  - **SmartcardExtension-\>IoRequest.RequestBufferLength**  
    The size, in bytes, of the user's input buffer.

  - **SmartcardExtension-\>IoRequest.ReplyBuffer**  
    A pointer to the user's output buffer.

  - **SmartcardExtension-\>IoRequest.ReplyBufferLength**  
    The size, in bytes, of the user's output buffer.

  - **SmartcardExtension-\>IoRequest.Information**  
    The value supplied by the request. Must be set to the number of bytes returned.

As with all other IOCTLs, a user-mode application dispatches a vendor-defined IOCTL to a smart card reader device by calling the [**DeviceIoControl**](https://msdn.microsoft.com/library/aa363216\(v=vs.85\)) function. When the IOCTL is vendor-defined, however, the application must first open the reader device for "overlapped" (that is, asynchronous) access. The application must also define an OVERLAPPED structure and pass it to the system in the last argument of **DeviceIoControl** (The OVERLAPPED structure is also described in the Windows SDK documentation.). When the operating system calls the driver's I/O control dispatch routine, it passes a DIOCPARAMETERS structure to the driver. The **lpoOverlapped** member of the DIOCPARAMETERS structure contains a pointer to the OVERLAPPED structure.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Smclib.h (include Smclib.h)</td>
</tr>
</tbody>
</table>

## See also

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)
