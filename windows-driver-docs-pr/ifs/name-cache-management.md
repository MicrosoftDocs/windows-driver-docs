---
title: Name Cache Management
description: Name Cache Management
ms.assetid: 3e1b1419-320e-44e0-a6c2-823517cf07c7
keywords:
- RDBSS WDK file systems , name cache
- Redirected Drive Buffering Subsystem WDK file systems , name cache
- NAME_CACHE structure
- names WDK RDBSS
- cache WDK RDBSS
- file not found messages WDK RDBSS
- name cache WDK RDBSS
- NAME_CACHE_CONTROL structure
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Name Cache Management


## <span id="ddk_name_cache_management_if"></span><span id="DDK_NAME_CACHE_MANAGEMENT_IF"></span>


The NAME\_CACHE structure caches the name strings of recent operations performed at the server so the client can suppress redundant requests. For example, if an open request has recently failed with a "file not found" message and the client application tries the open request again with an upper-case string, and the network mini-redirector does not support case-sensitive names, RDBSS can fail the request immediately without hitting the server.

In general, the algorithm is to put a time window and operation count limit on the NAME\_CACHE entry. The time window is usually two seconds. So if the NAME\_CACHE entry is greater than two seconds, the match will fail and the request will go to the server. If the request fails again at the server, the NAME\_CACHE entry is updated with another two-second window. If the request operation count doesn't match, then one or more requests have been sent to the server, which could make this NAME\_CACHE entry invalid. So again, this operation will be sent to the server.

A NAME\_CACHE structure has a public portion exposed to the network mini-redirector, MRX\_NAME\_CACHE, and a private section for use solely by RDBSS. The mini-redirector portion has a context field, NTSTATUS, for the result of a prior server operation on this name entry and a context extension pointer for some additional mini-redirector specific storage that can be co-allocated with the NAME\_CACHE structure. For more information, see [**RxNameCacheInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554586).

For Windows networking, the SMB operation count is an example of a mini-redirector-specific state, which could be saved in the context field of MRX\_NAME\_CACHE. When [**RxNameCacheCheckEntry**](https://msdn.microsoft.com/library/windows/hardware/ff554558) is called, it will perform an equality check between the context field and a supplied parameter as part of finding a match in the name cache. When a NAME\_CACHE entry is created or updated, it is the network mini-redirector's job to supply an appropriate value for this field and the lifetime, in seconds, for the NAME\_CACHE entry.

The private RDBSS portion of the NAME\_CACHE structure contains the name as a Unicode string, a hash value of the name to speed lookups, an expiration time of the entry, and a flag that indicates whether the server supports case-sensitive names.

The NAME\_CACHE\_CONTROL structure manages a given name cache. It has a free list, an active list, and a lock to synchronize updates. The NAME\_CACHE\_CONTROL structure also has fields to store the current number of NAME\_CACHE entries allocated, a value for the maximum number of entries to be allocated, the size of any additional network-mini-redirector storage used for each NAME\_CACHE entry, and values for statistics (the number of times the cache was updated, checked, a valid match was returned, and when the network-mini-redirector saved a network operation). The **MaximumEntries** field limits the number of NAME\_CACHE entries created in case a poorly behaved program were to generate a large number of open requests with bad file names that consume large quantities of memory.

Currently there are name caches maintained by RDBSS for OBJECT\_NAME\_NOT\_FOUND. For this name cache, a two-second window is maintained, which is invalidated if any operation is sent to the server. This could happen when the client application has a file (sample1) open that an application on the server could use to signal the creation of a different file (sample2) on the server. When the client reads the first file (sample1) and learns that the second file (sample2) has been created on the server, then a hit in the name cache that matches the second file (sample2) cannot return an error. This optimization only handles the case of successive file open operations on the same file that does not yet exist. This scenario happens using Microsoft Word.

The RDBSS name cache management routines include the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554552" data-raw-source="[&lt;strong&gt;RxNameCacheActivateEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554552)"><strong>RxNameCacheActivateEntry</strong></a></p></td>
<td align="left"><p>This routine takes a name cache entry and updates the expiration time and the network mini-redirector context. It then puts the entry on the active list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554558" data-raw-source="[&lt;strong&gt;RxNameCacheCheckEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554558)"><strong>RxNameCacheCheckEntry</strong></a></p></td>
<td align="left"><p>This routine checks a NAME_CACHE entry for validity.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554565" data-raw-source="[&lt;strong&gt;RxNameCacheCreateEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554565)"><strong>RxNameCacheCreateEntry</strong></a></p></td>
<td align="left"><p>This routine allocates and initializes a NAME_CACHE structure with the given name string. It is expected that the caller will then initialize any additional network mini-redirector elements of the name cache context and then put the entry on the name cache active list.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554569" data-raw-source="[&lt;strong&gt;RxNameCacheExpireEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554569)"><strong>RxNameCacheExpireEntry</strong></a></p></td>
<td align="left"><p>This routine puts a NAME_CACHE entry on the free list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554570" data-raw-source="[&lt;strong&gt;RxNameCacheExpireEntryWithShortName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554570)"><strong>RxNameCacheExpireEntryWithShortName</strong></a></p></td>
<td align="left"><p>This routine expires all of the NAME_CACHE entries whose name prefix matches the given short file name.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554573" data-raw-source="[&lt;strong&gt;RxNameCacheFetchEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554573)"><strong>RxNameCacheFetchEntry</strong></a></p></td>
<td align="left"><p>This routine looks for a match with a specified name string for a NAME_CACHE entry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554575" data-raw-source="[&lt;strong&gt;RxNameCacheFinalize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554575)"><strong>RxNameCacheFinalize</strong></a></p></td>
<td align="left"><p>This routine releases the storage for all of the NAME_CACHE entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554579" data-raw-source="[&lt;strong&gt;RxNameCacheFreeEntry&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554579)"><strong>RxNameCacheFreeEntry</strong></a></p></td>
<td align="left"><p>This routine releases the storage for a NAME_CACHE entry and decrements the count of NAME_CACHE cache entries associated with a NAME_CACHE_CONTROL structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554586" data-raw-source="[&lt;strong&gt;RxNameCacheInitialize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554586)"><strong>RxNameCacheInitialize</strong></a></p></td>
<td align="left"><p>This routine initializes a name cache (a NAME_CACHE_CONTROL structure).</p></td>
</tr>
</tbody>
</table>

 

 

 




