---
title: RDF_CARD_EJECT callback function
description: RDF_CARD_EJECT callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
- card eject
ms.date: 09/09/2022
---

# RDF\_CARD\_EJECT callback function

The RDF\_CARD\_EJECT callback function ejects an inserted smart card from the reader.

## Syntax

``` c++
NTSTATUS (*ReaderFunction[RDF_CARD_EJECT])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

- *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device. On input, **SmartcardExtension-\>MajorIoControlCode** contains [**IOCTL\_SMARTCARD\_EJECT**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_eject).

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
</tbody>
</table>

## Remarks

It is optional for smart card reader drivers to implement this callback function.

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

[**IOCTL\_SMARTCARD\_EJECT**](https://msdn.microsoft.com/library/ff548901\(v=vs.85\))

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)
