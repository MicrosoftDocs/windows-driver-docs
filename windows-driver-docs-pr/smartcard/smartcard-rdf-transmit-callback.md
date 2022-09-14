---
title: RDF_TRANSMIT callback function
description: RDF_TRANSMIT callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
---

# RDF\_TRANSMIT callback function

The RDF\_TRANSMIT callback function performs data transmissions.

## Syntax

``` c++
NTSTATUS  (*ReaderFunction[RDF_TRANSMIT])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

- *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device.

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
<td><p>Transmission successful.</p></td>
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
<td><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td><p>The protocol, defined by <strong>dwProtocol</strong>, is invalid.</p></td>
</tr>
</tbody>
</table>

## Remarks

Smart card reader drivers must implement this callback function.

On input, the caller must pass the following values to the function:

  - **SmartcardExtension-\>MajorIoControlCode**  
    Contains [**IOCTL\_SMARTCARD\_TRANSMIT**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_transmit).

  - **SmartcardExtension-\>IoRequest.RequestBuffer**  
    A pointer to an SCARD\_IO\_REQUEST structure followed by data to transmit to the card.

  - **SmartcardExtension-\>IoRequest.RequestBufferLength**  
    The number of bytes to transmit to the card.

  - **SmartcardExtension-\>IoRequest.ReplyBufferLength**  
    The size, in bytes, of the reply buffer.

The request returns the following values:

  - **SmartcardExtension-\>IoRequest.ReplyBuffer**  
    A pointer to the buffer that receives the SCARD\_IO\_REQUEST structure, plus the result of the card.

  - **SmartcardExtension-\>IoRequest.Information**  
    Receives the actual number of bytes returned by the smart card, plus the size of the SCARD\_IO\_REQUEST structure. For a definition of the SCARD\_IO\_REQUEST structure, see IOCTL\_SMARTCARD\_TRANSMIT.

When this function is called, **SmartcardExtension-\>IoRequest.RequestBuffer** points to an SCARD\_IO\_REQUEST structure followed by the data to transmit.

``` c++
typedef struct _SCARD_IO_REQUEST{
  DWORD  dwProtocol;   // Protocol identifier
  DWORD  cbPciLength;  // Protocol Control Information Length
} SCARD_IO_REQUEST, *PSCARD_IO_REQUEST, *LPSCARD_IO_REQUEST;
```

The **dwProtocol** member must contain the protocol identifier that is returned by a call to IOCTL\_SMARTCARD\_SET\_PROTOCOL.

The **cbPciLength** member contains the size, in bytes, of the SCARD\_IO\_REQUEST structure. The size of this structure is usually 8 bytes.

The SCARD\_IO\_REQUEST structure is followed by (protocol) data to transmit to the card. Depending on the protocol to use for the transmission, the library offers several support functions. For more information about these support functions, see SmartcardT0Request (WDM) and SmartcardT1Request (WDM).

*RequestBuffer* and *ReplyBuffer* point to the same system buffer. If you use the library function *SmartcardxxRequest* and *SmartcardxxReply*, you will not overwrite the input buffer. If you do not use these functions, make a copy of the *RequestBuffer* before you start transmissions.

You must copy the SCARD\_IO\_REQUEST structure to the *ReplyBuffer* parameter, followed by the data received from the card. Again, if you use the *SmartcardxxRequest* and *SmartcardxxReply* functions, the library will copy the structure for you.

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

[**IOCTL\_SMARTCARD\_TRANSMIT**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_transmit)

[**SmartcardT0Request (WDM)**](https://msdn.microsoft.com/library/ff548965\(v=vs.85\))

[**SmartcardT1Request (WDM)**](https://msdn.microsoft.com/library/ff548969\(v=vs.85\))

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)

