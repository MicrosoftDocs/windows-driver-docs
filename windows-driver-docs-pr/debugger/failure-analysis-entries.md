---
title: Failure Analysis Entries
description: A DebugFailureAnalysis object has a collection of failure analysis entries.
ms.assetid: 759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Failure%20Analysis%20Entries%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





