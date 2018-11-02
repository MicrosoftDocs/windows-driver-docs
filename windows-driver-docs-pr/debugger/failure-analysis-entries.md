---
title: Failure Analysis Entries
description: A DebugFailureAnalysis object has a collection of failure analysis entries.
ms.assetid: 759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Failure Analysis Entries


A [**DebugFailureAnalysis**](https://msdn.microsoft.com/library/windows/hardware/jj983405) object has a collection of failure analysis entries. For more information, see [Failure Analysis Entries, Tags, and Data Types](writing-an-analysis-extension-to-extend--analyze.md#failure-analysis-entries-tags-and-data-types).

A *failure analysis entry* (also called an *FA entry*) is one of the following:

-   An [**FA\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/jj991808) structure
-   An [**FA\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/jj991808) structure followed by a data block

The **DataSize** member of the [**FA\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/jj991808) structure holds the size, in bytes, of the data block. If there is no data block, **DataSize** is equal to 0. The **Tag** member of an **FA\_ENTRY** structure identifies the kind of information that is stored in the FA entry. For example, the tag **DEBUG\_FLR\_BUGCHECK\_CODE** indicates that the data block of the **FA\_ENTRY** holds a bug check code.

In some cases, there is no need for a data block; all the information is conveyed by the tag. For example, an [**FA\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/jj991808) with tag **DEBUG\_FLR\_KERNEL\_VERIFIER\_ENABLED** has no data block.

Each tag is associated with one of the data types in the [**FA\_ENTRY\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/jj991809) enumeration. For example, the tag **DEBUG\_FLR\_BUGCHECK\_CODE** is associated with the data type **DEBUG\_FA\_ENTRY\_ULONG**. To determine the data type of a tag, call the [**GetType**](https://msdn.microsoft.com/library/windows/hardware/jj991813) method of the [IDebugFAEntryTags](https://msdn.microsoft.com/library/windows/hardware/jj983404) interface.

To get or set the data block of an FA entry, use the [**IDebugFailureAnalysis2**](https://msdn.microsoft.com/library/windows/hardware/jj983405) interface.

## <span id="related_topics"></span>Related topics


[Writing an Analysis Extension Plug-in to Extend !analyze](writing-an-analysis-extension-to-extend--analyze.md)

[**FA\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/jj991808)

 

 






