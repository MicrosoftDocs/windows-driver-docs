---
title: Summary of Framework Objects
description: Summary of Framework Objects
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 799284a5-91c0-47b0-8f20-75a5f8e2284d
keywords: ["framework objects WDK KMDF listed", "framework objects WDK KMDF summary"]
---

# Summary of Framework Objects


The following table lists all of the framework objects and provides some basic information about each object. The mode column indicates whether the object can be used in KMDF and UMDF drivers, or KMDF only.

For a list of callbacks and methods and which frameworks are applicable, see [Summary of WDF Callbacks and Methods](https://msdn.microsoft.com/library/windows/hardware/dn265591).

<table style="width:100%;">
<colgroup>
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
<col width="14%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Handle</th>
<th align="left">Purpose</th>
<th align="left">Default parent</th>
<th align="left">Can driver override default parent?</th>
<th align="left">Mode</th>
<th align="left">Reference</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Child-list object</p></td>
<td align="left"><p>WDFCHILDLIST</p></td>
<td align="left"><p>Represents a list of child devices that are connected to a parent device.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF Child-List Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265624)</td>
</tr>
<tr class="even">
<td align="left"><p>Collection object</p></td>
<td align="left"><p>WDFCOLLECTION</p></td>
<td align="left"><p>Represents an object collection.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Collection Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265626)</td>
</tr>
<tr class="odd">
<td align="left"><p>Common buffer object</p></td>
<td align="left"><p>WDFCOMMONBUFFER</p></td>
<td align="left"><p>Represents a common buffer.</p></td>
<td align="left"><p>DMA enabler object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF Common Buffer Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265627)</td>
</tr>
<tr class="even">
<td align="left"><p>Device object</p></td>
<td align="left"><p>WDFDEVICE</p></td>
<td align="left"><p>Represents a device.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Device Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265631)</td>
</tr>
<tr class="odd">
<td align="left"><p>DMA enabler object</p></td>
<td align="left"><p>WDFDMAENABLER</p></td>
<td align="left"><p>Enables a driver to use the framework's DMA capabilities.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM</td>
<td align="left">[WDF DMA Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265634)</td>
</tr>
<tr class="even">
<td align="left"><p>DMA transaction object</p></td>
<td align="left"><p>WDFDMATRANSACTION</p></td>
<td align="left"><p>Represents a DMA transaction.</p></td>
<td align="left"><p>DMA enabler object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF DMA Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265634)</td>
</tr>
<tr class="odd">
<td align="left"><p>DPC object</p></td>
<td align="left"><p>WDFDPC</p></td>
<td align="left"><p>Represents a deferred procedure call.</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM</td>
<td align="left">[WDF DPC Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265635)</td>
</tr>
<tr class="even">
<td align="left"><p>Driver object</p></td>
<td align="left"><p>WDFDRIVER</p></td>
<td align="left"><p>Represents a driver.</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Driver Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265636)</td>
</tr>
<tr class="odd">
<td align="left"><p>File object</p></td>
<td align="left"><p>WDFFILEOBJECT</p></td>
<td align="left"><p>Represents a file.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF File Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265638)</td>
</tr>
<tr class="even">
<td align="left"><p>General object</p></td>
<td align="left"><p>WDFOBJECT</p></td>
<td align="left"><p>Represents a general object.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF General Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265639)</td>
</tr>
<tr class="odd">
<td align="left"><p>Interrupt object</p></td>
<td align="left"><p>WDFINTERRUPT</p></td>
<td align="left"><p>Represents a hardware interrupt resource.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Interrupt Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265640)</td>
</tr>
<tr class="even">
<td align="left"><p>I/O target object</p></td>
<td align="left"><p>WDFIOTARGET</p></td>
<td align="left"><p>Represents a driver to which another driver sends I/O requests.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF I/O Target Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265644)</td>
</tr>
<tr class="odd">
<td align="left"><p>Lookaside-list object</p></td>
<td align="left"><p>WDFLOOKASIDE</p></td>
<td align="left"><p>Represents a lookaside list.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM</td>
<td align="left">[WDF Memory Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265645)</td>
</tr>
<tr class="even">
<td align="left"><p>Memory object</p></td>
<td align="left"><p>WDFMEMORY</p></td>
<td align="left"><p>Represents a memory buffer.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Memory Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265645)</td>
</tr>
<tr class="odd">
<td align="left"><p>Queue object</p></td>
<td align="left"><p>WDFQUEUE</p></td>
<td align="left"><p>Represents an I/O queue that receives I/O requests.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Queue Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265647)</td>
</tr>
<tr class="even">
<td align="left"><p>Registry key object</p></td>
<td align="left"><p>WDFKEY</p></td>
<td align="left"><p>Represents a registry key.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Registry Key Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265663)</td>
</tr>
<tr class="odd">
<td align="left"><p>Request object</p></td>
<td align="left"><p>WDFREQUEST</p></td>
<td align="left"><p>Represents an I/O request.</p></td>
<td align="left"><p>None, if created by framework. Driver object, if created by driver.</p></td>
<td align="left"><p>Yes, if created by driver.</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Request Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265664)</td>
</tr>
<tr class="even">
<td align="left"><p>Resource list object</p></td>
<td align="left"><p>WDFCMRESLIST</p></td>
<td align="left"><p>Represents a resource list.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Resource Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265665)</td>
</tr>
<tr class="odd">
<td align="left"><p>Resource range list object</p></td>
<td align="left"><p>WDFIORESLIST</p></td>
<td align="left"><p>Represents a logical configuration.</p></td>
<td align="left"><p>Resource requirements list object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF Resource Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265665)</td>
</tr>
<tr class="even">
<td align="left"><p>Resource requirements list object</p></td>
<td align="left"><p>WDFIORESREQLIST</p></td>
<td align="left"><p>Represents a resource requirements list.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF Resource Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265665)</td>
</tr>
<tr class="odd">
<td align="left"><p>Spin-lock object</p></td>
<td align="left"><p>WDFSPINLOCK</p></td>
<td align="left"><p>Represents a spin lock.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Synchronization Methods](https://msdn.microsoft.com/library/windows/hardware/dn265669)</td>
</tr>
<tr class="even">
<td align="left"><p>String object</p></td>
<td align="left"><p>WDFSTRING</p></td>
<td align="left"><p>Repesents a Unicode string.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF String Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265667)</td>
</tr>
<tr class="odd">
<td align="left"><p>Timer object</p></td>
<td align="left"><p>WDFTIMER</p></td>
<td align="left"><p>Represents a timer.</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Timer Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265670)</td>
</tr>
<tr class="even">
<td align="left"><p>USB device object</p></td>
<td align="left"><p>WDFUSBDEVICE</p></td>
<td align="left"><p>Represents a device connected to a USB.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF USB Reference](https://msdn.microsoft.com/library/windows/hardware/dn265671)</td>
</tr>
<tr class="odd">
<td align="left"><p>USB interface object</p></td>
<td align="left"><p>WDFUSBINTERFACE</p></td>
<td align="left"><p>Represents a USB device interface.</p></td>
<td align="left"><p>USB device object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF USB Reference](https://msdn.microsoft.com/library/windows/hardware/dn265671)</td>
</tr>
<tr class="even">
<td align="left"><p>USB pipe object</p></td>
<td align="left"><p>WDFUSBPIPE</p></td>
<td align="left"><p>Represents a USB device pipe.</p></td>
<td align="left"><p>USB interface object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF USB Reference](https://msdn.microsoft.com/library/windows/hardware/dn265671)</td>
</tr>
<tr class="odd">
<td align="left"><p>Wait-lock object</p></td>
<td align="left"><p>WDFWAITLOCK</p></td>
<td align="left"><p>Represents a wait lock.</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Synchronization Methods](https://msdn.microsoft.com/library/windows/hardware/dn265669)</td>
</tr>
<tr class="even">
<td align="left"><p>WMI instance object</p></td>
<td align="left"><p>WDFWMIINSTANCE</p></td>
<td align="left"><p>Represents an instance of a WMI data block.</p></td>
<td align="left"><p>WMI provider object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF WMI Reference](https://msdn.microsoft.com/library/windows/hardware/dn265672)</td>
</tr>
<tr class="odd">
<td align="left"><p>WMI provider object</p></td>
<td align="left"><p>WDFWMIPROVIDER</p></td>
<td align="left"><p>Represents a WMI data block.</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left">KM</td>
<td align="left">[WDF WMI Reference](https://msdn.microsoft.com/library/windows/hardware/dn265672)</td>
</tr>
<tr class="even">
<td align="left"><p>Work-item object</p></td>
<td align="left"><p>WDFWORKITEM</p></td>
<td align="left"><p>Represents a work item.</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>Yes</p></td>
<td align="left">KM/UM</td>
<td align="left">[WDF Work-Item Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265673)</td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Summary%20of%20Framework%20Objects%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




