---
title: Framework Objects
description: Framework Objects
ms.assetid: bd9ec812-205d-4f9a-b85b-4e3a2f7556bd
keywords:
- UMDF objects WDK , listed
- framework objects WDK UMDF , listed
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Objects


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The following table provides basic information about each framework object, links to the object's interface, and links to more information about the core framework objects.

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Objectname</th>
<th align="left">ObjectInterface</th>
<th align="left">Purpose</th>
<th align="left">Defaultparent</th>
<th align="left">Can driver overridedefaultparent?</th>
<th align="left">Can driver own?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="framework-driver-object.md" data-raw-source="[Driver object](framework-driver-object.md)">Driver object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff558893" data-raw-source="[IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893)">IWDFDriver</a></p></td>
<td align="left"><p>Represents a driver</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="framework-device-object.md" data-raw-source="[Device object](framework-device-object.md)">Device object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff556917" data-raw-source="[IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917)">IWDFDevice</a></p></td>
<td align="left"><p>Represents a device</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="framework-file-object.md" data-raw-source="[File object](framework-file-object.md)">File object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff558912" data-raw-source="[IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912)">IWDFFile</a></p></td>
<td align="left"><p>Represents a file</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p></p>
No, if created by framework;
Yes, if created by driver</td>
</tr>
<tr class="even">
<td align="left"><p><a href="framework-interrupt-object.md" data-raw-source="[Interrupt object](framework-interrupt-object.md)">Interrupt object</a></p></td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/hh451283" data-raw-source="[IWDFInterrupt](https://msdn.microsoft.com/library/windows/hardware/hh451283)">IWDFInterrupt</a></td>
<td align="left"><p>Represents an interrupt</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="framework-i-o-queue-object.md" data-raw-source="[Queue object](framework-i-o-queue-object.md)">Queue object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff558943" data-raw-source="[IWDFIoQueue](https://msdn.microsoft.com/library/windows/hardware/ff558943)">IWDFIoQueue</a></p></td>
<td align="left"><p>Represents an I/O queue that receives I/O requests</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="framework-i-o-request-object.md" data-raw-source="[Request object](framework-i-o-request-object.md)">Request object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff558985" data-raw-source="[IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985)">IWDFIoRequest</a></p></td>
<td align="left"><p>Represents an I/O request</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p></p>
No, if created by framework;
Yes, if created by driver</td>
<td align="left"><p></p>
No, if created by framework (for example, redirected requests);
Yes, if created by driver</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="framework-i-o-target-object.md" data-raw-source="[Target object](framework-i-o-target-object.md)">Target object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559170" data-raw-source="[IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170)">IWDFIoTarget</a></p></td>
<td align="left"><p>Represents a driver that another driver sends requests to</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p></p>
No, for the default target;
Yes, for all other targets</td>
</tr>
<tr class="even">
<td align="left"><p>USB device object</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560362" data-raw-source="[IWDFUsbTargetDevice](https://msdn.microsoft.com/library/windows/hardware/ff560362)">IWDFUsbTargetDevice</a></p></td>
<td align="left"><p>Represents a device that is connected to USB</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes (see target object)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>USB pipe object</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560391" data-raw-source="[IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391)">IWDFUsbTargetPipe</a></p></td>
<td align="left"><p>Represents a USB device pipe</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes (see target object)</p></td>
</tr>
<tr class="even">
<td align="left"><p>USB interface object</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560312" data-raw-source="[IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312)">IWDFUsbInterface</a></p></td>
<td align="left"><p>Represents a USB device interface</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes (see target object)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="framework-base-object.md" data-raw-source="[Base object](framework-base-object.md)">Base object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff560200" data-raw-source="[IWDFObject](https://msdn.microsoft.com/library/windows/hardware/ff560200)">IWDFObject</a></p></td>
<td align="left"><p>Represents a general base object</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes, if created by driver</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="framework-memory-object.md" data-raw-source="[Memory object](framework-memory-object.md)">Memory object</a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff559249" data-raw-source="[IWDFMemory](https://msdn.microsoft.com/library/windows/hardware/ff559249)">IWDFMemory</a></p></td>
<td align="left"><p>Represents a memory object</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p></p>
No, if created by framework;
Yes, if created by driver</td>
</tr>
</tbody>
</table>

 

 

 





