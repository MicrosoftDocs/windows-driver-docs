---
title: Using GPUView
description: Using GPUView
ms.assetid: 55f589fd-e3ea-4fd2-9e8d-c225c2c3dbb5
---

# Using GPUView


GPUView (*GPUView.exe*) is a development tool for determining the performance of the graphics processing unit (GPU) and CPU. It looks at performance with regard to direct memory access (DMA) buffer processing and all other video processing on the video hardware. GPUView is useful for developing display drivers that comply with the Windows Vista display driver model. GPUView is introduced with the release of the Windows 7 operating system.

GPUView and other files that are associated with it are included with the Windows Performance Toolkit (WPT) as an installable option of the WPT MSI. GPUView binaries are available for x86-based, x64-based, and IA64-based architectures. For example, *Wpt\_x86.msi* is for an x86 platform. The WPT MSI includes the files that are described in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Files</th>
<th align="left">Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>EULA.rtf</em></p></td>
<td align="left"><p>Legal agreement</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>GPUView.chm</em></p></td>
<td align="left"><p>GPUView help file</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Readme.txt</em></p></td>
<td align="left"><p>Any additional information that is not included in the help file</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>GPUView.exe</em></p></td>
<td align="left"><p>Program for viewing ETL files with video data</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>AEplugin.dll</em>, <em>DWMPlugin.dll</em>, <em>MFPlugin.dll</em>, <em>NTPlugin.dll</em>, <em>DxPlugin.dll</em>, and <em>DxgkPlugin.dll</em></p></td>
<td align="left"><p>Plugins to interpret events</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>CoreTPlugin.dll</em></p></td>
<td align="left"><p>Plugin for Statistical Options dialog</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Log.cmd</em></p></td>
<td align="left"><p>Script to turn on and off the appropriate information for logging</p></td>
</tr>
<tr class="even">
<td align="left"><p><em>SymbolSearchPath.txt</em></p></td>
<td align="left"><p>A text file that sets the symbol path to resolve stackwalk and other events</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20GPUView%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




