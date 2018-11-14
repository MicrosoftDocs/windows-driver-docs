---
title: Bug Check 0xFE BUGCODE_USB_DRIVER
description: The BUGCODE_USB_DRIVER bug check has a value of 0x000000FE. This indicates that an error has occurred in a universal serial bus (USB) driver.
ms.assetid: 830f9d11-4b16-41a9-a804-6d689a779278
keywords: ["Bug Check 0xFE BUGCODE_USB_DRIVER", "BUGCODE_USB_DRIVER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BUGCODE_USB_DRIVER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xFE: BUGCODE\_USB\_DRIVER


The BUGCODE\_USB\_DRIVER bug check has a value of 0x000000FE. This indicates that an error has occurred in a universal serial bus (USB) driver.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BUGCODE\_USB\_DRIVER Parameters


Parameter 1 identifies the type of violation.

Parameter 1
Parameter 2
Parameter 3
Parameter 4
Cause of Error
0x1

Reserved

Reserved

Reserved

An internal error has occurred in the USB stack.

0x2

Address of the pending IRP

Address of the IRP that was passed in

Address of the USB request block (URB) that caused the error

The USB client driver has submitted a URB that is still attached to another IRP pending in the bus driver.

0x3

Reserved

Reserved

Reserved

The USB miniport driver has generated a bug check. This usually happens in response to a hardware failure.

0x4

Address of the IRP

Address of the URB

Reserved

The caller has submitted an IRP that is already pending in the USB bus driver.

0x5

Device extension pointer of the host controller

PCI vendor, product id for the controller

Pointer to endpoint data structure

A hardware failure has occurred because of a bad physical address found in a hardware data structure.

0x6

Object address

Signature that was expected

Reserved

An internal data structure (object) is corrupted.

0x7

Pointer to usbport.sys debug log

Message string

File name

Please see the provided message string for detailed information.

0x8

1

Reserved

Reserved

Reserved

2

Device object

IRP

An IRP was received by the hub driver that it does not expect or has not registered for.

3

Reserved

Reserved

Reserved

4

PDO if Parameter 3 is not NULL. Context if Parameter 3 is NULL.

Context or NULL

Fatal PDO trap

5

Reserved

Reserved

Reserved

6

Time-out code. See the following table.

Time-out code context: port data

Fatal time-out

 

If Parameter 1 has a value of 8 and Parameter 2 has a value of 6, then Parameter 3 is a time-out code. Possible values for the time-out code are given in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Time-out code</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>Non-fatal time-out</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>Failed resuming a suspended port.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>Timed out waiting for a reset, initiated by a client driver, to complete before suspending the port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>Timed out waiting for the port to complete resume before suspending it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p>Timed out waiting for the port-change state machine to be disabled prior to suspending the port.</p></td>
</tr>
<tr class="even">
<td align="left"><p>5</p></td>
<td align="left"><p>Timed out waiting for a suspend-port request to complete.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6</p></td>
<td align="left"><p>Timed out waiting for the port-change state machine to be disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>7</p></td>
<td align="left"><p>Timed out waiting for the port-change state machine to be closed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>8</p></td>
<td align="left"><p>Timed out waiting for the hub to resume from selective suspend.</p></td>
</tr>
<tr class="even">
<td align="left"><p>9</p></td>
<td align="left"><p>Timed out waiting for the hub to resume from selective suspend prior to system suspend.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>10</p></td>
<td align="left"><p>Timed out waiting for port-change state machine to become idle.</p></td>
</tr>
</tbody>
</table>

 

 

 




