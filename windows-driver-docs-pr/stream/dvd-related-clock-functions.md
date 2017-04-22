---
title: DVD Related Clock Functions
author: windows-driver-content
description: DVD Related Clock Functions
ms.assetid: 495f25dc-cd79-4f7f-acbc-b8b271269fb3
keywords:
- DVD decoder minidrivers WDK , master clock
- decoder minidrivers WDK DVD , master clock
- master clocks WDK DVD decoder
- clocks WDK DVD decoder
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Related Clock Functions


## <a href="" id="ddk-dvd-related-clock-functions-ksg"></a>


All clock handles should be stored with the appropriate individual streams. They should not be stored globally or in a static variable. For more information, see [KS Clocks](ks-clocks.md).

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
<td><p>[<strong>SRB_OPEN_MASTER_CLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568190)</p></td>
<td><p>Indicates to the DVD decoder minidriver that the specified stream is being opened as a master clock, and provides a master clock handle to be used on all calls into the DVD decoder minidriver master clock routine for access to that clock.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SRB_CLOSE_MASTER_CLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568163)</p></td>
<td><p>Indicates the specified master clock handle is no longer active.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>SRB_INDICATE_MASTER_CLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568179)</p></td>
<td><p>Indicates the handle to be used when calling for time stamps and is provided to all streams.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Related%20Clock%20Functions%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


