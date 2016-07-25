---
title: Disk Prompting and Error Handling Functions
description: Disk Prompting and Error Handling Functions
ms.assetid: e1afeeb3-02f0-4570-9910-f948646f07bf
keywords: ["SetupAPI functions WDK , disk prompting", "SetupAPI functions WDK , error handling", "errors WDK SetupAPI", "disk prompting WDK SetupAPI", "prompting disk insertion WDK SetupAPI", "media prompting WDK SetupAPI"]
---

# Disk Prompting and Error Handling Functions


## <a href="" id="ddk-disk-prompting-and-error-handling-functions-dg"></a>


You can use the general Setup functions to prompt the user to insert new media, or to handle errors that arise when files are being copied, renamed, or deleted.

The following table lists functions that provide dialog boxes for requesting installation media and reporting errors. For detailed function descriptions, see the Microsoft Windows SDK documentation.

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
<td align="left"><p>[<strong>SetupCopyError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376989)</p></td>
<td align="left"><p>Generates a dialog box that informs the user of a copy error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDeleteError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376994)</p></td>
<td align="left"><p>Generates a dialog box that informs the user of a delete error.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupPromptForDisk</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377412)</p></td>
<td align="left"><p>Generates a dialog box that prompts the user for an installation medium or source file location.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupRenameError</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377434)</p></td>
<td align="left"><p>Generates a dialog box that informs the user of a rename error.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Disk%20Prompting%20and%20Error%20Handling%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




