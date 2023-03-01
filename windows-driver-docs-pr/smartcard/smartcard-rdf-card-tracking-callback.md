---
title: RDF_CARD_TRACKING callback function
description: RDF_CARD_TRACKING callback function
keywords:
- vendor-supplied drivers RDF callback functions
- WDK smart card
ms.date: 09/09/2022
ms.topic: reference
---

# RDF\_CARD\_TRACKING callback function

The RDF\_CARD\_TRACKING callback function installs an event handler to track every time a card is inserted in or removed from a card reader.

## Syntax

``` c++
NTSTATUS (*ReaderFunction[RDF_CARD_TRACKING])(
   PSMARTCARD_EXTENSION SmartcardExtension
);
```

## Parameters

  - *SmartcardExtension*  
    A pointer to the smart card extension, [**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension), of the device.
    
    **SmartcardExtension-\>OsData-\>NotificationIrp** contains the IRP that receives notification of the insertion or removal event.

## Return value

This function returnsone of the following NTSTATUS values:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_PENDING</strong></td>
<td><p>Smart card tracking has started.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_INVALID_DEVICE_STATE</strong></td>
<td><p>The device cannot accept the request.</p></td>
</tr>
<tr class="odd">
<td><strong>STATUS_SUCCESS</strong></td>
<td><p>Smart card status matches the requested tracking call.</p></td>
</tr>
<tr class="even">
<td><strong>STATUS_DEVICE_BUSY</strong></td>
<td><p>A smart card tracking event is pending.</p></td>
</tr>
</tbody>
</table>

## Remarks

It is mandatory for smart card reader drivers to implement this callback function.

Upon receiving an [**IOCTL\_SMARTCARD\_IS\_PRESENT**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_is_present) request, the driver library determines if the smart card is already present. If the smart card is present, the driver library completes the request with a status of STATUS\_SUCCESS. If there is no smart card present, the driver library calls the reader driver's smart card tracking callback function, and the reader driver starts looking for the smart card. After initiating smart card tracking, the driver library marks the request as having a status of STATUS\_PENDING.

The driver library completes the request.

**WDM Device Drivers**

The corresponding WDM driver library adds a pointer to the request in **SmartcardExtension-\>OsData-\>NotificationIrp**. The reader driver must complete the request as soon as it detects that a smart card has been inserted or removed. The reader driver completes the request by calling [**IoCompleteRequest**](https://msdn.microsoft.com/library/ff548343\(v=vs.85\)), after which, the reader driver must set the **NotificationIrp** member of **SmartcardExtension -\> OsData** back to **NULL** to inform the driver library that the reader driver can accept further smart card tracking requests.

Because this call can have an indefinite duration and the caller can terminate the request before it is complete, it is important to mark this IRP as cancelable.

```cpp
    MyDriverCardSupervision(
    SmartcardExtension, 
    OtherParameters)
    //
    //    This function is called whenever the card status changes
    //    For example, the card has been inserted or the card has been removed
    //
    {
        if (SmartcardExtension->OsData->NotificationOverlappedData != NULL){
    
            SmartcardCompleteCardTracking(SmartcardExtension);
        }
        //
        // Do additional tasks
        //
    }
```

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

[**IoCompleteRequest**](https://msdn.microsoft.com/library/ff548343\(v=vs.85\))

[**IOCTL\_SMARTCARD\_IS\_PRESENT**](/windows-hardware/drivers/ddi/winsmcrd/ni-winsmcrd-ioctl_smartcard_is_present)

[**SMARTCARD\_EXTENSION**](/windows-hardware/drivers/ddi/smclib/ns-smclib-_smartcard_extension)
