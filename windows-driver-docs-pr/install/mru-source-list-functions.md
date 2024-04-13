---
title: MRU Source List Functions
description: MRU Source List Functions
keywords:
- SetupAPI functions WDK , most recently used source lists
- most recently used source lists WDK SetupAPI
- MRU source lists WDK SetupAPI
- source lists WDK MRU
ms.date: 04/20/2017
---

# MRU Source List Functions





Most recently used (MRU) source lists are resident on the user's computer and contain information about source paths used in previous installations. This information can be used when prompting the user for a source path.

The *device installation application* can access a user-specific source list and, if the application has administrator privilege, the system-wide source list. The device installation application can also create a temporary source list that is discarded when the device installation application exits. By calling **SetupSetSourceList**, the device installation application identifies which source list it will use during the installation.

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
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupaddtosourcelista" data-raw-source="[&lt;strong&gt;SetupAddToSourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupaddtosourcelista)"><strong>SetupAddToSourceList</strong></a></p></td>
<td align="left"><p>Adds an entry to a source list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupcanceltemporarysourcelist" data-raw-source="[&lt;strong&gt;SetupCancelTemporarySourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupcanceltemporarysourcelist)"><strong>SetupCancelTemporarySourceList</strong></a></p></td>
<td align="left"><p>Cancels use of a temporary list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupfreesourcelista" data-raw-source="[&lt;strong&gt;SetupFreeSourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupfreesourcelista)"><strong>SetupFreeSourceList</strong></a></p></td>
<td align="left"><p>Frees resources allocated by a previous call to <a href="/windows/win32/api/setupapi/nf-setupapi-setupsetsourcelista" data-raw-source="[&lt;strong&gt;SetupSetSourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupsetsourcelista)"><strong>SetupSetSourceList</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupquerysourcelista" data-raw-source="[&lt;strong&gt;SetupQuerySourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupquerysourcelista)"><strong>SetupQuerySourceList</strong></a></p></td>
<td align="left"><p>Queries the current list of installation sources.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupremovefromsourcelista" data-raw-source="[&lt;strong&gt;SetupRemoveFromSourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupremovefromsourcelista)"><strong>SetupRemoveFromSourceList</strong></a></p></td>
<td align="left"><p>Removes an entry from an installation source list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupsetsourcelista" data-raw-source="[&lt;strong&gt;SetupSetSourceList&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupsetsourcelista)"><strong>SetupSetSourceList</strong></a></p></td>
<td align="left"><p>Sets the installation source list to the system MRU list, the user MRU list, or a temporary list.</p></td>
</tr>
</tbody>
</table>

 

