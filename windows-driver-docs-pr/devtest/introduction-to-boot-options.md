---
title: Introduction to Boot Options
description: The concept and content of boot options are very similar on all computers that run Microsoft Windows operating systems.
ms.assetid: e8e835c4-75de-4ce1-965f-d9b822e15044
keywords: ["boot options WDK , about boot options", "storing boot options", "boot loaders WDK"]
---

# Introduction to Boot Options


The concept and content of boot options are very similar on all computers that run Microsoft Windows operating systems. However, prior to Windows Vista, computers with different processor firmware store boot options differently and require different tools to view and edit the options on each system.

## <span id="ddk_introduction_to_boot_options_tools"></span><span id="DDK_INTRODUCTION_TO_BOOT_OPTIONS_TOOLS"></span>


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Version of Windows</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="______Windows_7__Windows_Server_2008__Windows_Vista"></span><span id="______windows_7__windows_server_2008__windows_vista"></span><span id="______WINDOWS_7__WINDOWS_SERVER_2008__WINDOWS_VISTA"></span>Windows 10, Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, Windows Vista</p></td>
<td align="left"><p>Windows Vista, and later versions of Windows, store boot option in a firmware-independent storage and configuration system. Windows Vista also introduces a new Boot Manager and system-specific boot loaders. For more information, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).</p></td>
</tr>
</tbody>
</table>

 

This section includes:

[Boot Options in a Boot.ini File](boot-options-in-a-boot-ini-file.md) (Windows XP, Windows Server 2003)

[Boot Options in EFI NVRAM](boot-options-in-efi-nvram.md) (Windows XP, Windows Server 2003)

[Overview of Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md) (Windows 8, Windows Server 2012, Windows 7, Windows Server 2008)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Introduction%20to%20Boot%20Options%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




