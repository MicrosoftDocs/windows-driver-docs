---
title: RDF_CARD_POWER callback function
description: RDF_CARD_POWER callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
---

# RDF\_CARD\_POWER callback function

The RDF\_CARD\_POWER callback function resets or turns off an inserted smart card.

## Syntax

``` c++
NTSTATUS (*ReaderFunction[RDF_CARD_POWER])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

- *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device. For more information about the members of this structure, see Remarks.

## Return value

This function returns one of the following NTSTATUS values:

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
<td><p>The function was successfully executed.</p></td>
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
<td><p>The user buffer is not large enough to hold the answer-to-reset (ATR).</p></td>
</tr>
</tbody>
</table>

## Remarks

It is mandatory for smart card reader drivers to implement this callback function.

On input, the structure pointed to by **SmartcardExtension** should have the following member values:

  - **MajorIoControlCode**  
    Should have a value of [**IOCTL\_SMARTCARD\_POWER**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_power).

  - **IoRequest.ReplyBufferLength**  
    Should contain the length of the buffer.

  - **MinorIoControlCode**  
    Should have one of the following minor codes:
    
      - SCARD\_COLD\_RESET  
        Performs a cold reset of the smart card.
    
      - SCARD\_WARM\_RESET  
        Performs a warm reset of the smart card.
    
      - SCARD\_POWER\_DOWN  
        Turns off smart card power.

On output, the structure pointed to by **SmartcardExtension** should have the following values:

  - **IoRequest.ReplyBuffer**  
    Receives the ATR that is returned by the smart card. In addition, you must transfer the ATR to *SmartcardExtension-\>CardCapabilities.ATR.Buffer* so that the library can parse the ATR.

  - **IoRequest.Information**  
    Receives the length of the ATR.

  - **CardCapabilities.ATR.Length**  
    Contains the length of the ATR.

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
