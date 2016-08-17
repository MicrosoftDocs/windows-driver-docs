---
title: IWiaMiniDrv COM Interface
MS-HAID:
- 'WIA\_arch\_db97070c-3040-490c-8b23-45265a961dae.xml'
- 'image.iwiaminidrv\_com\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a4bd0dee-fb40-42d4-a235-9dab3bc84017
description: 
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

## <a href="" id="ddk-creating-and-initializing-items-si"></a>Creating and Initializing Items


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

 

## <a href="" id="ddk-deleting-items-si"></a>Deleting Items


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

 

## <a href="" id="ddk-enumerating-device-capabilities-si"></a>Enumerating Device Capabilities


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

 

## <a href="" id="ddk-enumerating-image-formats-si"></a>Enumerating Image Formats


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

 

## <a href="" id="ddk-issuing-device-commands-si"></a>Issuing Device Commands


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

 

## <a href="" id="ddk-locking-and-unlocking-a-device-si"></a>Locking and Unlocking a Device


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

 

## <a href="" id="ddk-notifying-a-device-of-an-event-si"></a>Notifying a Device of an Event


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

 

## <a href="" id="ddk-obtaining-device-error-strings-si"></a>Obtaining Device Error Strings


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

 

## <a href="" id="ddk-reading-and-storing-item-properties-si"></a>Reading and Storing Item Properties


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

 

## <a href="" id="ddk-transferring-data-si"></a>Transferring Data


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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IWiaMiniDrv%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




