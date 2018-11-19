---
title: Processing Tape Device Control Requests
description: Processing Tape Device Control Requests
ms.assetid: de6edfc6-9b4b-4866-8fdb-1047b43163de
keywords:
- tape drivers WDK storage , mapping status values
- storage tape drivers WDK , mapping status values
- TAPE_STATUS_SEND_SRB_AND_CALLBACK
- TAPE_STATUS_CHECK_TEST_UNIT_READY
- TAPE_STATUS_CALLBACK
- TAPE_STATUS_REQUIRES_CLEANING
- TAPE_STATUS
- mapping TAPE_STATUS values
- status values WDK tape
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Tape Device Control Requests


## <span id="ddk_processing_tape_device_control_requests_kg"></span><span id="DDK_PROCESSING_TAPE_DEVICE_CONTROL_REQUESTS_KG"></span>


All tape miniclass drivers must report status using the values listed in the [**TAPE\_STATUS**](https://msdn.microsoft.com/library/windows/hardware/ff567975) enumerator. However, when the tape class driver completes an I/O control request, it reports status using the equivalent NT Status Values. The following table provides a mapping between TAPE\_STATUS values and their equivalent NT status values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">NT Status Value</th>
<th align="left">Tape Status Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STATUS_INSUFFICIENT_RESOURCES</p></td>
<td align="left"><p>TAPE_STATUS_INSUFFICIENT_RESOURCES</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_NOT_IMPLEMENTED</p></td>
<td align="left"><p>TAPE_STATUS_NOT_IMPLEMENTED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_INVALID_DEVICE_REQUEST</p></td>
<td align="left"><p>TAPE_STATUS_INVALID_DEVICE_REQUEST</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_INVALID_PARAMETER</p></td>
<td align="left"><p>TAPE_STATUS_INVALID_PARAMETER</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_VERIFY_REQUIRED</p></td>
<td align="left"><p>TAPE_STATUS_MEDIA_CHANGED</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_BUS_RESET</p></td>
<td align="left"><p>TAPE_STATUS_BUS_RESET</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_SETMARK_DETECTED</p></td>
<td align="left"><p>TAPE_STATUS_SETMARK_DETECTED</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_FILEMARK_DETECTED</p></td>
<td align="left"><p>TAPE_STATUS_FILEMARK_DETECTED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_BEGINNING_OF_MEDIA</p></td>
<td align="left"><p>TAPE_STATUS_BEGINNING_OF_MEDIA</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_END_OF_MEDIA</p></td>
<td align="left"><p>TAPE_STATUS_END_OF_MEDIA</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_BUFFER_OVERFLOW</p></td>
<td align="left"><p>TAPE_STATUS_BUFFER_OVERFLOW</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_NO_DATA_DETECTED</p></td>
<td align="left"><p>TAPE_STATUS_NO_DATA_DETECTED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_EOM_OVERFLOW</p></td>
<td align="left"><p>TAPE_STATUS_EOM_OVERFLOW</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_NO_MEDIA</p></td>
<td align="left"><p>TAPE_STATUS_NO_MEDIA</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_IO_DEVICE_ERROR</p></td>
<td align="left"><p>TAPE_STATUS_IO_DEVICE_ERROR</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_UNRECOGNIZED_MEDIA</p></td>
<td align="left"><p>TAPE_STATUS_UNRECOGNIZED_MEDIA</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_NOT_READY</p></td>
<td align="left"><p>TAPE_STATUS_DEVICE_NOT_READY</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_MEDIA_WRITE_PROTECTED</p></td>
<td align="left"><p>TAPE_STATUS_MEDIA_WRITE_PROTECTED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_DATA_ERROR</p></td>
<td align="left"><p>TAPE_STATUS_DEVICE_DATA_ERROR</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_NO_SUCH_DEVICE</p></td>
<td align="left"><p>TAPE_STATUS_NO_SUCH_DEVICE</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_INVALID_BLOCK_LENGTH</p></td>
<td align="left"><p>TAPE_STATUS_INVALID_BLOCK_LENGTH</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_IO_TIMEOUT</p></td>
<td align="left"><p>TAPE_STATUS_IO_TIMEOUT</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_NOT_CONNECTED</p></td>
<td align="left"><p>TAPE_STATUS_DEVICE_NOT_CONNECTED</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_DATA_OVERRUN</p></td>
<td align="left"><p>TAPE_STATUS_DATA_OVERRUN</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_DEVICE_BUSY</p></td>
<td align="left"><p>TAPE_STATUS_DEVICE_BUSY</p></td>
</tr>
<tr class="even">
<td align="left"><p>STATUS_DEVICE_REQUIRES_CLEANING</p></td>
<td align="left"><p>TAPE_STATUS_REQUIRES_CLEANING</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STATUS_CLEANER_CARTRIDGE_INSTALLED</p></td>
<td align="left"><p>TAPE_STATUS_CLEANER_CARTRIDGE_INSTALLED</p></td>
</tr>
</tbody>
</table>

 

Whenever the class driver must call a miniclass routine more than once to complete a request, the miniclass driver uses the return status to indicate whether the request is complete or whether the routine should be called again. The tape class driver maintains a zero-based count of the number of times that it has called the miniclass routine for a given request and passes that count to the routine as the *CallNumber* parameter.

A miniclass routine returns one of the following status values to indicate that the class driver should call the routine again:

-   TAPE\_STATUS\_SEND\_SRB\_AND\_CALLBACK

    This return value directs the tape class driver to send the SRB to the device. A tape miniclass routine usually returns this status after filling in the SRB passed by the tape class driver. If the operation is successful, the class driver increments *CallNumber* and calls the miniclass routine again. If the SRB fails, the class driver calls the miniclass routine again depending on the value of *RetryFlags*.

-   TAPE\_STATUS\_CHECK\_TEST\_UNIT\_READY

    This return value directs the tape class driver to create an SRB for the test unit ready command and to send the SRB to the device.

-   TAPE\_STATUS\_CALLBACK

    This return value directs the tape class driver to increment *CallNumber* without sending an SRB to the device. This streamlines case statements that support several devices. For example, suppose that most of the tape devices supported by a particular miniclass driver require three SRBs to process a certain request. One device, however, requires only the first and third SRBs. For the unique device the tape miniclass driver can return TAPE\_STATUS\_CALLBACK to skip the second SRB, allowing the driver to use the same code to process the request for all the devices it supports.

-   TAPE\_STATUS\_REQUIRES\_CLEANING

    If a tape device supports cleaning notification in sense data rather than as an error, a tape miniclass driver's TapeMiniGetStatus routine returns this status to indicate to the tape class driver that the drive needs cleaning.

When the miniclass routine finishes processing a request--either successfully or with an error after retries are exhausted--it returns to the tape class driver with a TAPE\_STATUS\_*XXX* that indicates the success or failure of the request.

 

 




