---
title: WIA Diagnostic Log Macros
author: windows-driver-content
description: WIA Diagnostic Log Macros
MS-HAID:
- 'WIA\_arch\_43228ef6-1d22-4092-9c25-58db78ed25f6.xml'
- 'image.wia\_diagnostic\_log\_macros'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b544045-e9d7-422b-825c-f1a5531e0e11
---

# WIA Diagnostic Log Macros


## <a href="" id="ddk-wia-diagnostic-log-macros-si"></a>


For error handling on Windows Vista and later operating systems, see [WIA Driver Error Recovery for Windows Vista](wia-driver-error-recovery-for-windows-vista.md).

The [Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff540599) enable minidrivers to log trace, error, and warning messages to the *Wiaservc.log* diagnostic log file.

For more information about error handling on Windows Vista and later operating systems, see [WIA Driver Error Recovery for Windows Vista](wia-driver-error-recovery-for-windows-vista.md).

The first three macros can be used to write a logging statement with a specified type of error, trace, or warning, respectively. The fourth macro can be used to translate an HRESULT into a descriptive string.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>WIAS_LERROR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549580)</p></td>
<td><p>Writes a log statement of type ERROR to the <em>Wiaservc.log</em> diagnostic log file..</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WIAS_LHRESULT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549589)</p></td>
<td><p>Translates an HRESULT value into a string and writes the string to the <em>Wiaservc.log</em> diagnostic log file.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>WIAS_LTRACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549600)</p></td>
<td><p>Writes a log statement of type TRACE to the <em>Wiaservc.log</em> diagnostic log file..</p></td>
</tr>
<tr class="even">
<td><p>[<strong>WIAS_LWARNING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549610)</p></td>
<td><p>Writes a log statement of type WARNING to the <em>Wiaservc.log</em> diagnostic log file..</p></td>
</tr>
<tr class="odd">
<td><p><strong>WIAS_ERROR</strong></p></td>
<td><p>This macro is available in Windows Vista and later operating systems.</p>
<p>Writes a log statement of type ERROR to the <em>Wiatrace.log</em> diagnostic log file.</p></td>
</tr>
<tr class="even">
<td><p><strong>WIAS_TRACE</strong></p></td>
<td><p>This macro is available in Windows Vista and later operating systems.</p>
<p>Writes a log statement of type TRACE to the <em>Wiatrace.log</em> diagnostic log file.</p></td>
</tr>
</tbody>
</table>

 

For more information about these macros, see [IWiaLog Interface and Diagnostic Log Macros](https://msdn.microsoft.com/library/windows/hardware/ff543937).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Diagnostic%20Log%20Macros%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


