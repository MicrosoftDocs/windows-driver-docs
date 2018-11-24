---
title: Stream Categories
description: Stream Categories
ms.assetid: dc2af282-4976-42d8-b07b-13b2a6dfb7d5
keywords:
- video capture WDK AVStream , stream categories
- capturing video WDK AVStream , stream categories
- identifying pin primary purpose
- stream categories WDK video capture , about stream categories
- GUIDs WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Categories


The KsProxy filter supports several types of stream categories. The tables in the following subsections describe the different types of stream categories and the data formats associated with each type of category, as well as the extended header size value that a video capture minidriver should specify per category.

A Stream class video capture minidriver provides stream category and content information in response to an [**SRB\_GET\_STREAM\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568173) request. The minidriver returns information about each stream category it supports in a [**HW\_STREAM\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559692) structure.

Within the HW\_STREAM\_INFORMATION structure is a **StreamFormatsArray** member, which has an entry for each unique data format that the minidriver provides for the specified stream category. Each **StreamFormatsArray** entry contains stream format information, including image characteristics, such as color format, bit depth, cropping, and scaling information. Also included in the **StreamFormatsArray** member is the range of formats available for the specified stream category.

For each video stream category there are corresponding [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) and [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures to be used when describing the stream in the HW\_STREAM\_INFORMATION structure. The structures that correspond to stream categories are listed in the tables in the following subsections.

The stream category GUID and pin name GUID for a given video capture stream type are usually identical. These GUIDs are specified in the **Category** and **Name** members of the HW\_STREAM\_INFORMATION structure, respectively. The only case where these GUIDs do not match is when a given stream category has more than one instance on a filter. In this case, the category GUIDs should match, but each pin should be assigned a unique pin name GUID.

The following subsections contain information about each of the different video capture stream categories. The stream category GUID and pin name GUID are described, as well as the structures that should be used to support the category. Required property set support is also listed for each category. The corresponding user-mode DirectShow type information is also listed for convenience.

 

 




