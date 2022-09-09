---
title: RDF_SET_PROTOCOL callback function
description: RDF_SET_PROTOCOL callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
---

# RDF\_SET\_PROTOCOL callback function

The RDF\_SET\_PROTOCOL callback function selects a transmission protocol for the inserted smart card.

## Syntax

``` c++
NTSTATUS (*ReaderFunction[RDF_SET_PROTOCOL])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

- *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device. For a description of the members of this structure, see Remarks.

## Return value

This function returns an NTSTATUS value. Possible values include the following:

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
<td><p>A protocol was successfully selected.</p></td>
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
<td><p>The user buffer is not large enough to hold a ULONG value.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_INVALID_DEVICE_STATE</strong></td>
<td><p>The reader is not in the correct state to select a protocol. That is, a smart card is inserted, but not reset.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td><p>The mask contains an unknown protocol.</p></td>
</tr>
</tbody>
</table>

## Remarks

Smart card reader drivers must implement this callback function.

On input, the caller must pass the following values to the function:

  - **SmartcardExtension-\>MajorIoControlCode**  
    Contains [**IOCTL\_SMARTCARD\_SET\_PROTOCOL**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_set_protocol).

  - **SmartcardExtension-\>MinorIoControlCode**  
    Contains a bitwise OR of one or more protocols than the caller accepts. The driver must select a protocol that the inserted smart card supports. We recommend that the T = 1 protocol is given precedence over the T = 0 protocol.

    <table>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>SCARD_PROTOCOL_RAW</p></td>
    <td><p>Selects the raw protocol.</p></td>
    </tr>
    <tr class="even">
    <td><p>SCARD_PROTOCOL_T0</p></td>
    <td><p>Selects the ISO T = 0 protocol.</p></td>
    </tr>
    <tr class="odd">
    <td><p>SCARD_PROTOCOL_T1</p></td>
    <td><p>Selects the ISO T = 1 protocol.</p></td>
    </tr>
    </tbody>
    </table>

  - **SmartcardExtension-\>IoRequest.ReplyBufferLength**  
    Contains the length of the reply buffer.

  - **SmartcardExtension-\>CardCapabilities.PtsData**  
    Contains the required parameters to perform the PTS request. For more information, see [**PTS\_DATA**](https://msdn.microsoft.com/library/ff548916\(v=vs.85\)).

The request returns the following values:

  - **SmartcardExtension-\>IoRequest.ReplyBuffer**  
    Contains the selected protocol.

  - **SmartcardExtension-\>IoRequest.Information**  
    Set to **sizeof**(ULONG).

The caller can supply a mask of acceptable protocols. The driver's set protocol callback routine selects one of the protocols in the mask and returns the selected protocol in **SmartcardExtension-\>IoRequest.ReplyBuffer**.

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

[**IOCTL\_SMARTCARD\_SET\_PROTOCOL**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_set_protocol)

[**PTS\_DATA**](https://msdn.microsoft.com/library/ff548916\(v=vs.85\))

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)
 