---
title: IWiaLog COM Interface
author: windows-driver-content
description: IWiaLog COM Interface
ms.assetid: e5d42b5d-796f-42f3-9c01-4234b8765ca6
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IWiaLog COM Interface


## <a href="" id="ddk-iwialog-com-interface-si"></a>


The [**IWiaLog interface**](https://msdn.microsoft.com/library/windows/hardware/ff543935) is obsolete in Microsoft Windows XP and later and is no longer supported. Use the WIA Diagnostic Log Macros instead.

It is provided for backward compatibility only. The methods in this interface allow a minidriver to write error, trace, and warning messages to a log. The **IWiaLog** interface provides the following methods.

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
<td><p>[<strong>IWiaLog::InitializeLog</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543932)</p></td>
<td><p>Initializes the logging utility.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IWiaLog::Log</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543939)</p></td>
<td><p>Logs a message to a file or other target.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IWiaLog::hResult</strong>](https://msdn.microsoft.com/library/windows/hardware/ff543928)</p></td>
<td><p>Translates an HRESULT into a string.</p></td>
</tr>
</tbody>
</table>

 

For more information about this interface, see [IWiaLog Interface and Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff543937).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20IWiaLog%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


