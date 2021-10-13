---
title: IWiaMiniDrv COM Interface
description: This topic provides detailed guidance on using the IWiaMiniDrv COM interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IWiaMiniDrv COM Interface

Imaging applications make requests to the WIA service, which in turn communicates with the device minidriver through the minidriver writer-implemented [IWiaMiniDrv interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv). Applications typically make requests for:

- [Creating and Initializing Items](#creating-and-initializing-items)
- [Deleting Items](#deleting-items)
- [Enumerating Device Capabilities](#enumerating-device-capabilities)
- [Enumerating Image Formats](#enumerating-image-formats)
- [Issuing Device Commands](#issuing-device-commands)
- [Locking and Unlocking a Device](#locking-and-unlocking-a-device)
- [Notifying a Device of an Event](#notifying-a-device-of-an-event)
- [Obtaining Device Error Strings](#obtaining-device-error-strings)
- [Reading and Storing Item Properties](#reading-and-storing-item-properties)
- [Transferring Data](#transferring-data)

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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvanalyzeitem" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvAnalyzeItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvanalyzeitem)"><strong>IWiaMiniDrv::drvAnalyzeItem</strong></a></p></td>
<td><p>Inspects an item and, if necessary, creates subitems.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvInitializeWia&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia)"><strong>IWiaMiniDrv::drvInitializeWia</strong></a></p></td>
<td><p>Initializes the WIA minidriver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinititemproperties" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvInitItemProperties&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinititemproperties)"><strong>IWiaMiniDrv::drvInitItemProperties</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdeleteitem" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvDeleteItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdeleteitem)"><strong>IWiaMiniDrv::drvDeleteItem</strong></a></p></td>
<td><p>Deletes a driver item.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvfreedrvitemcontext" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvFreeDrvItemContext&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvfreedrvitemcontext)"><strong>IWiaMiniDrv::drvFreeDrvItemContext</strong></a></p></td>
<td><p>Frees a device-specific context.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvuninitializewia" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvUnInitializeWia&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvuninitializewia)"><strong>IWiaMiniDrv::drvUnInitializeWia</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetCapabilities&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities)"><strong>IWiaMiniDrv::drvGetCapabilities</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetWiaFormatInfo&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo)"><strong>IWiaMiniDrv::drvGetWiaFormatInfo</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdevicecommand" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvDeviceCommand&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdevicecommand)"><strong>IWiaMiniDrv::drvDeviceCommand</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvlockwiadevice" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvLockWiaDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvlockwiadevice)"><strong>IWiaMiniDrv::drvLockWiaDevice</strong></a></p></td>
<td><p>Locks access to an imaging device.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvunlockwiadevice" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvUnLockWiaDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvunlockwiadevice)"><strong>IWiaMiniDrv::drvUnLockWiaDevice</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvNotifyPnPEvent&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent)"><strong>IWiaMiniDrv::drvNotifyPnPEvent</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetdeviceerrorstr" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvGetDeviceErrorStr&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetdeviceerrorstr)"><strong>IWiaMiniDrv::drvGetDeviceErrorStr</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvreaditemproperties" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvReadItemProperties&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvreaditemproperties)"><strong>IWiaMiniDrv::drvReadItemProperties</strong></a></p></td>
<td><p>Reads driver item properties.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvValidateItemProperties&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties)"><strong>IWiaMiniDrv::drvValidateItemProperties</strong></a></p></td>
<td><p>Validates driver item properties.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvWriteItemProperties&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties)"><strong>IWiaMiniDrv::drvWriteItemProperties</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata" data-raw-source="[&lt;strong&gt;IWiaMiniDrv::drvAcquireItemData&lt;/strong&gt;](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata)"><strong>IWiaMiniDrv::drvAcquireItemData</strong></a></p></td>
<td><p>Transfers data from a driver item to the WIA service.</p></td>
</tr>
</tbody>
</table>
