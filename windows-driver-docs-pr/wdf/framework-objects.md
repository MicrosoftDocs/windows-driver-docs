---
title: Framework Objects
description: Framework Objects
ms.assetid: bd9ec812-205d-4f9a-b85b-4e3a2f7556bd
keywords: ["UMDF objects WDK listed", "framework objects WDK UMDF listed"]
---

# Framework Objects


\[This topic applies to UMDF 1.*x*.\]

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
<td align="left"><p>[Driver object](framework-driver-object.md)</p></td>
<td align="left"><p>[IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893)</p></td>
<td align="left"><p>Represents a driver</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Device object](framework-device-object.md)</p></td>
<td align="left"><p>[IWDFDevice](https://msdn.microsoft.com/library/windows/hardware/ff556917)</p></td>
<td align="left"><p>Represents a device</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[File object](framework-file-object.md)</p></td>
<td align="left"><p>[IWDFFile](https://msdn.microsoft.com/library/windows/hardware/ff558912)</p></td>
<td align="left"><p>Represents a file</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p></p>
No, if created by framework;
Yes, if created by driver</td>
</tr>
<tr class="even">
<td align="left"><p>[Interrupt object](framework-interrupt-object.md)</p></td>
<td align="left">[IWDFInterrupt](https://msdn.microsoft.com/library/windows/hardware/hh451283)</td>
<td align="left"><p>Represents an interrupt</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Queue object](framework-i-o-queue-object.md)</p></td>
<td align="left"><p>[IWDFIoQueue](https://msdn.microsoft.com/library/windows/hardware/ff558943)</p></td>
<td align="left"><p>Represents an I/O queue that receives I/O requests</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Request object](framework-i-o-request-object.md)</p></td>
<td align="left"><p>[IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985)</p></td>
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
<td align="left"><p>[Target object](framework-i-o-target-object.md)</p></td>
<td align="left"><p>[IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170)</p></td>
<td align="left"><p>Represents a driver that another driver sends requests to</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p></p>
No, for the default target;
Yes, for all other targets</td>
</tr>
<tr class="even">
<td align="left"><p>USB device object</p></td>
<td align="left"><p>[IWDFUsbTargetDevice](https://msdn.microsoft.com/library/windows/hardware/ff560362)</p></td>
<td align="left"><p>Represents a device that is connected to USB</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes (see target object)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>USB pipe object</p></td>
<td align="left"><p>[IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391)</p></td>
<td align="left"><p>Represents a USB device pipe</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes (see target object)</p></td>
</tr>
<tr class="even">
<td align="left"><p>USB interface object</p></td>
<td align="left"><p>[IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312)</p></td>
<td align="left"><p>Represents a USB device interface</p></td>
<td align="left"><p>Device object</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes (see target object)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[Base object](framework-base-object.md)</p></td>
<td align="left"><p>[IWDFObject](https://msdn.microsoft.com/library/windows/hardware/ff560200)</p></td>
<td align="left"><p>Represents a general base object</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes, if created by driver</p></td>
</tr>
<tr class="even">
<td align="left"><p>[Memory object](framework-memory-object.md)</p></td>
<td align="left"><p>[IWDFMemory](https://msdn.microsoft.com/library/windows/hardware/ff559249)</p></td>
<td align="left"><p>Represents a memory object</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p></p>
No, if created by framework;
Yes, if created by driver</td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20Objects%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




