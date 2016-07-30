---
title: MRU Source List Functions
description: MRU Source List Functions
ms.assetid: 62c6b144-5883-45cf-a114-7b82453f275f
keywords: ["SetupAPI functions WDK , most recently used source lists", "most recently used source lists WDK SetupAPI", "MRU source lists WDK SetupAPI", "source lists WDK MRU"]
---

# MRU Source List Functions


## <a href="" id="ddk-mru-source-list-functions-dg"></a>


Most recently used (MRU) source lists are resident on the user's computer and contain information about source paths used in previous installations. This information can be used when prompting the user for a source path.

The [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) can access a user-specific source list and, if the application has administrator privilege, the system-wide source list. The device installation application can also create a temporary source list that is discarded when the device installation application exits. By calling **SetupSetSourceList**, the device installation application identifies which source list it will use during the installation.

The following table lists the functions that can be used to manipulate source lists. For detailed function descriptions, see the Microsoft Windows SDK documentation.

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
<td align="left"><p>[<strong>SetupAddToSourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376981)</p></td>
<td align="left"><p>Adds an entry to a source list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupCancelTemporarySourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376983)</p></td>
<td align="left"><p>Cancels use of a temporary list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupFreeSourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377241)</p></td>
<td align="left"><p>Frees resources allocated by a previous call to [<strong>SetupSetSourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377441).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQuerySourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377419)</p></td>
<td align="left"><p>Queries the current list of installation sources.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupRemoveFromSourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377431)</p></td>
<td align="left"><p>Removes an entry from an installation source list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupSetSourceList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377441)</p></td>
<td align="left"><p>Sets the installation source list to the system MRU list, the user MRU list, or a temporary list.</p></td>
</tr>
</tbody>
</table>

 

 

 





