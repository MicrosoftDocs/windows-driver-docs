---
title: Cabinet File Function
description: Cabinet File Function
ms.assetid: 0f72c833-6bcb-4b11-aa7e-dc5cc678836f
keywords: ["SetupAPI functions WDK , cabinet files", ".cab files", "CAB files"]
---

# Cabinet File Function


## <a href="" id="ddk-cabinet-file-function-dg"></a>


A cabinet (CAB) file is a single file, usually with a .*cab* extension, that contains several compressed files as a file library. CAB files are used to organize the installation files that will be copied to the user's system. A compressed file can be spread over several CAB files.

The following function is used with CAB files. For a detailed function description, see the Microsoft Windows SDK documentation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>SetupIterateCabinet</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377404)</p></td>
<td align="left"><p>Sends a notification to a callback function for each file that is stored in a CAB file.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Cabinet%20File%20Function%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




