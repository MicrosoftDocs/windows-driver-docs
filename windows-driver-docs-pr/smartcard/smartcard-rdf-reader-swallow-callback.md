---
title: RDF_READER_SWALLOW callback function
description: RDF_READER_SWALLOW callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
ms.topic: reference
---

#  RDF\_READER\_SWALLOW callback function

The RDF\_READER\_SWALLOW callback function performs a mechanical swallow, which is what happens when the smart card is fully inserted into the smart card reader.

## Syntax

``` c++
NTSTATUS (*ReaderFunction[RDF_READER_SWALLOW])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

 - *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device. On input, **SmartcardExtension-\>MajorIoControlCode** contains [**IOCTL\_SMARTCARD\_SWALLOW**](https://msdn.microsoft.com/library/ff548910\(v=vs.85\)).

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

[**IOCTL\_SMARTCARD\_SWALLOW**](https://msdn.microsoft.com/library/ff548910\(v=vs.85\))

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)

