---
title: RDF_ATR_PARSE callback function
description: RDF_ATR_PARSE callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
ms.topic: reference
---

# RDF\_ATR\_PARSE callback function

The RDF\_ATR\_PARSE parse function parses an answer-to-reset (ATR) for the smart card driver library when the driver library is unable to recognize or parse the smart card driver library.

## Syntax

``` c++
NTSTATUS (*ReaderFunction[RDF_ATR_PARSE])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

- *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device. On input, the structure pointed to by *SmartcardExtension* should have the **MajorIoControlCode** member set to [**IOCTL\_SMARTCARD\_SET\_PROTOCOL**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_set_protocol).

## Return value

This function returns an NTSTATUS value, or the appropriate error value.

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

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)
