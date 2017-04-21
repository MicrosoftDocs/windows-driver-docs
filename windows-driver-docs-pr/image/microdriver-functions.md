---
title: Microdriver Functions
author: windows-driver-content
description: Microdriver Functions
ms.assetid: 491b954a-8ffa-4899-8c7d-0aee409f4742
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Microdriver Functions


## <a href="" id="ddk-microdriver-functions-si"></a>


The WIA Flatbed Driver responds to requests from the WIA service by calling the WIA microdriver functions. These functions must be implemented by every vendor-supplied microdriver and consist of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>MicroEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545248)</p></td>
<td><p>Responds to commands sent by the WIA Flatbed Driver.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Scan</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547322)</p></td>
<td><p>Reads data from the device and returns the data to the WIA Flatbed Driver.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>SetPixelWindow</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548129)</p></td>
<td><p>Sets the area to be scanned.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Microdriver%20Functions%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


