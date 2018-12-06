---
title: Review of the Older Alignment Method
description: Review of the Older Alignment Method
ms.assetid: 4efc380f-6303-42e1-8651-c9d64498942a
keywords:
- drawing extended surface alignment WDK DirectDraw
- DirectDraw extended surface alignment WDK Windows 2000 display
- surfaces WDK DirectDraw , extended alignment
- extended surface alignment WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Review of the Older Alignment Method


## <span id="ddk_review_of_the_older_alignment_method_gg"></span><span id="DDK_REVIEW_OF_THE_OLDER_ALIGNMENT_METHOD_GG"></span>


Versions of DirectDraw before DirectX 5.0 allowed the driver to express pitch alignment requirements for linear heaps. For the purposes of this discussion, use of these alignment requirements by DirectDraw can be seen in three steps:

1.  Create the surface and fill in an aligned **lPitch** member based on the driver's global alignment requirements (as returned in the [**VIDEOMEMORYINFO**](https://msdn.microsoft.com/library/windows/hardware/ff570172) structure) and the surface's **ddsCaps** member. This pitch is increased until it is a multiple of the appropriate alignment requirement.

2.  Call the driver's [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) callback, if defined. The driver can modify the **lPitch** value, but this change will be ignored by Microsoft Windows 2000 and later.

3.  If the driver call is not handled, or if it requests allocation, allocate display memory for the surface from one of the driver's heaps. The width of the allocated surface is taken to be the aligned pitch determined in step 1, unless modified by the driver in step 2.

If a driver implemented the [*DdCreateSurface*](https://msdn.microsoft.com/library/windows/hardware/ff549263) callback, it could be assured that any incoming surface would have its **lPitch** member set to an aligned value. For backward-compatibility, this behavior still exists. Step three maintains exactly the same behavior, unless the driver has exposed a **GetHeapAlignment** entry point (see the [**DD\_GETHEAPALIGNMENTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff551572) structure). If, and only if, this entry point is defined, the previously calculated **lPitch** alignment is discarded, and all surface alignment conforms to the requirements reported using GUID\_GetHeapAlignment. Drivers can keep their [**VIDEOMEMORYINFO**](https://msdn.microsoft.com/library/windows/hardware/ff570172) structure alignment requirements as they are, and expect the same alignment behavior when run on older DirectDraw runtimes. This alignment behavior has been completely replaced for DirectX 5.0 and later versions of the DirectDraw runtime. It should be noted that exposing **GetHeapAlignment** turns off this legacy alignment procedure for all heaps, not just those for which GUID\_GetHeapAlignment reports alignment requirements.

 

 





