---
title: IWiaMiniDrv COM Interface
ms.assetid: a4bd0dee-fb40-42d4-a235-9dab3bc84017
description: This topic provides detailed guidance on using the IWiaMiniDrv COM interface
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543958" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvAnalyzeItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543958)"><strong>IWiaMiniDrv::drvAnalyzeItem</strong></a></p></td>
<td><p>Inspects an item and, if necessary, creates subitems.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544986" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvInitializeWia&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544986)"><strong>IWiaMiniDrv::drvInitializeWia</strong></a></p></td>
<td><p>Initializes the WIA minidriver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544989" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvInitItemProperties&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544989)"><strong>IWiaMiniDrv::drvInitItemProperties</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543961" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvDeleteItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543961)"><strong>IWiaMiniDrv::drvDeleteItem</strong></a></p></td>
<td><p>Deletes a driver item.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543972" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvFreeDrvItemContext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543972)"><strong>IWiaMiniDrv::drvFreeDrvItemContext</strong></a></p></td>
<td><p>Frees a device-specific context.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545010" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvUnInitializeWia&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545010)"><strong>IWiaMiniDrv::drvUnInitializeWia</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543977" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetCapabilities&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543977)"><strong>IWiaMiniDrv::drvGetCapabilities</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543986" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetWiaFormatInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543986)"><strong>IWiaMiniDrv::drvGetWiaFormatInfo</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543967" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvDeviceCommand&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543967)"><strong>IWiaMiniDrv::drvDeviceCommand</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544995" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvLockWiaDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544995)"><strong>IWiaMiniDrv::drvLockWiaDevice</strong></a></p></td>
<td><p>Locks access to an imaging device.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545012" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvUnLockWiaDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545012)"><strong>IWiaMiniDrv::drvUnLockWiaDevice</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff544998" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvNotifyPnPEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544998)"><strong>IWiaMiniDrv::drvNotifyPnPEvent</strong></a></p></td>
<td><p>Indicates a WIA minidriver&#39;s response to a Plug and Play event.</p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543982" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetDeviceErrorStr&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543982)"><strong>IWiaMiniDrv::drvGetDeviceErrorStr</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545005" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvReadItemProperties&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545005)"><strong>IWiaMiniDrv::drvReadItemProperties</strong></a></p></td>
<td><p>Reads driver item properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545017" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvValidateItemProperties&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545017)"><strong>IWiaMiniDrv::drvValidateItemProperties</strong></a></p></td>
<td><p>Validates driver item properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff545020" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvWriteItemProperties&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545020)"><strong>IWiaMiniDrv::drvWriteItemProperties</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff543956" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvAcquireItemData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543956)"><strong>IWiaMiniDrv::drvAcquireItemData</strong></a></p></td>
<td><p>Transfers data from a driver item to the WIA service.</p></td>
</tr>
</tbody>
</table>

 

 

 




