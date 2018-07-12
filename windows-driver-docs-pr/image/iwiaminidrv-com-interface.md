---
title: IWiaMiniDrv COM Interface
author: windows-driver-content
ms.assetid: a4bd0dee-fb40-42d4-a235-9dab3bc84017
description: This topic provides detailed guidance on using the IWiaMiniDrv COM interface
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IWiaMiniDrv COM Interface


Imaging applications make requests to the WIA service, which in turn communicates with the device minidriver through the minidriver writer-implemented [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027). Applications typically make requests for:

-   [Creating and Initializing Items](#ddk-creating-and-initializing-items-si)
-   [Deleting Items](#ddk-deleting-items-si)
-   [Enumerating Device Capabilities](#ddk-enumerating-device-capabilities-si)
-   [Enumerating Image Formats](#ddk-enumerating-image-formats-si)
-   [Issuing Device Commands](#ddk-issuing-device-commands-si)
-   [Locking and Unlocking a Device](#ddk-locking-and-unlocking-a-device-si)
-   [Notifying a Device of an Event](#ddk-notifying-a-device-of-an-event-si)
-   [Obtaining Device Error Strings](#ddk-obtaining-device-error-strings-si)
-   [Reading and Storing Item Properties](#ddk-reading-and-storing-item-properties-si)
-   [Transferring Data](#ddk-transferring-data-si)

Applications make requests to the WIA service through the WIA application programming interface (API). For more information about this interface, see the Microsoft Windows SDK documentation.

The **IWiaMiniDrv** interface provides the entry points shown in the following tables for the WIA service to control the device. A WIA minidriver must implement every **IWiaMiniDrv** method. These entry points are defined through the following **IWiaMiniDrv** methods.

## Creating and Initializing Items


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvAnalyzeItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543958)</p></td>
<td><p>Inspects an item and, if necessary, creates subitems.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaMiniDrv::drvInitializeWia</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544986)</p></td>
<td><p>Initializes the WIA minidriver.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvInitItemProperties</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544989)</p></td>
<td><p>Initializes driver item properties for each item in an application item tree.</p></td>
</tr>
</tbody>
</table>

 

## Deleting Items


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvDeleteItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543961)</p></td>
<td><p>Deletes a driver item.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaMiniDrv::drvFreeDrvItemContext</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543972)</p></td>
<td><p>Frees a device-specific context.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvUnInitializeWia</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545010)</p></td>
<td><p>Releases device resources associated with an application item tree.</p></td>
</tr>
</tbody>
</table>

 

## Enumerating Device Capabilities


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvGetCapabilities</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543977)</p></td>
<td><p>Reports the events and commands supported by a WIA minidriver.</p></td>
</tr>
</tbody>
</table>

 

## Enumerating Image Formats


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvGetWiaFormatInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543986)</p></td>
<td><p>Gets supported device formats and media types.</p></td>
</tr>
</tbody>
</table>

 

## Issuing Device Commands


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvDeviceCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543967)</p></td>
<td><p>Issues a command to an imaging device.</p></td>
</tr>
</tbody>
</table>

 

## Locking and Unlocking a Device


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvLockWiaDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544995)</p></td>
<td><p>Locks access to an imaging device.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaMiniDrv::drvUnLockWiaDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545012)</p></td>
<td><p>Unlocks access to an imaging device.</p></td>
</tr>
</tbody>
</table>

 

## Notifying a Device of an Event


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvNotifyPnPEvent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544998)</p></td>
<td><p>Indicates a WIA minidriver's response to a Plug and Play event.</p></td>
</tr>
</tbody>
</table>

 

## Obtaining Device Error Strings


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvGetDeviceErrorStr</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543982)</p></td>
<td><p>Maps a device error value to a string.</p></td>
</tr>
</tbody>
</table>

 

## Reading and Storing Item Properties


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvReadItemProperties</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545005)</p></td>
<td><p>Reads driver item properties.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaMiniDrv::drvValidateItemProperties</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545017)</p></td>
<td><p>Validates driver item properties.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvWriteItemProperties</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545020)</p></td>
<td><p>Writes driver item properties to the device (if needed).</p></td>
</tr>
</tbody>
</table>

 

## Transferring Data


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IWiaMiniDrv::drvAcquireItemData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543956)</p></td>
<td><p>Transfers data from a driver item to the WIA service.</p></td>
</tr>
</tbody>
</table>

 

 

 




