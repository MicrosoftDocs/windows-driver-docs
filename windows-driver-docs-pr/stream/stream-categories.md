---
title: Stream Categories
author: windows-driver-content
description: Stream Categories
ms.assetid: dc2af282-4976-42d8-b07b-13b2a6dfb7d5
keywords: ["video capture WDK AVStream , stream categories", "capturing video WDK AVStream , stream categories", "identifying pin primary purpose", "stream categories WDK video capture , about stream categories", "GUIDs WDK video capture"]
---

# Stream Categories


The KsProxy filter supports several types of stream categories. The tables in the following subsections describe the different types of stream categories and the data formats associated with each type of category, as well as the extended header size value that a video capture minidriver should specify per category.

A Stream class video capture minidriver provides stream category and content information in response to an [**SRB\_GET\_STREAM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568173) request. The minidriver returns information about each stream category it supports in a [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) structure.

Within the HW\_STREAM\_INFORMATION structure is a **StreamFormatsArray** member, which has an entry for each unique data format that the minidriver provides for the specified stream category. Each **StreamFormatsArray** entry contains stream format information, including image characteristics, such as color format, bit depth, cropping, and scaling information. Also included in the **StreamFormatsArray** member is the range of formats available for the specified stream category.

For each video stream category there are corresponding [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) and [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures to be used when describing the stream in the HW\_STREAM\_INFORMATION structure. The structures that correspond to stream categories are listed in the tables in the following subsections.

The stream category GUID and pin name GUID for a given video capture stream type are usually identical. These GUIDs are specified in the **Category** and **Name** members of the HW\_STREAM\_INFORMATION structure, respectively. The only case where these GUIDs do not match is when a given stream category has more than one instance on a filter. In this case, the category GUIDs should match, but each pin should be assigned a unique pin name GUID.

The following subsections contain information about each of the different video capture stream categories. The stream category GUID and pin name GUID are described, as well as the structures that should be used to support the category. Required property set support is also listed for each category. The corresponding user-mode DirectShow type information is also listed for convenience.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Categories%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


