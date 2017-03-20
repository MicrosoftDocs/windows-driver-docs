---
title: Extended Heap Restrictions
description: Extended Heap Restrictions
ms.assetid: 4f907768-670a-4ce5-b2d7-7af27baf80da
keywords: ["drawing extended surface capabilities WDK DirectDraw , heaps", "DirectDraw extended surface capabilities WDK Windows 2000 display , heaps", "extended surface capabilities WDK DirectDraw , heaps", "heaps WDK DirectDraw"]
---

# Extended Heap Restrictions


## <span id="ddk_extended_heap_restrictions_gg"></span><span id="DDK_EXTENDED_HEAP_RESTRICTIONS_GG"></span>


The [**DD\_MORESURFACECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff551659) structure is of variable size. It always has a **ddsCapsMore** member, but it may have zero or more **ddsExtendedHeapRestrictions** entries. If the driver responds to the GUID\_DDMoreSurfaceCaps query, it should return a DD\_MORESURFACECAPS structure that contains as many **ddsExtendedHeapRestrictions** entries as it returned display memory heaps in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure (DirectDraw guarantees that the GUID\_DDMoreSurfaceCaps query is made after the driver reports DD\_HALINFO.)

The driver should also fill in an appropriate **dwSize** value in the DD\_MORESURFACECAPS structure. The value of **dwSize** is calculated in this way:

```
DDMORESURFACECAPS.dwSize = 
          (DWORD) (sizeof(DDMORESURFACECAPS) 
        + (((signed int)DDHALINFO.vmiData.dwNumHeaps) - 1) 
        * sizeof(DDSCAPSEX)*2 );
```

Note that subtracting 1 from the value of **dwNumHeaps** is necessary to account for the fact that the [**DD\_MORESURFACECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff551659) structure has a **ddsExtendedHeapRestrictions** member that is a one-element array. Only those array elements after the first (that is, from **ddsExtendedHeapRestrictions\[**1**\]** on) should be counted in calculating the total size of the DD\_MORESURFACECAPS structure.

The **ddsCapsEx** and **ddsCapsExAlt** members are exactly analogous to the **ddsCaps** and **ddsCapsAlt** members of the array of [**VIDEOMEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff570171) structures returned in the **pvmList** member of the [**VIDEOMEMORYINFO**](https://msdn.microsoft.com/library/windows/hardware/ff570172) structure, which is contained as a member of the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure. Any bit set in **ddsCapsEx** means that surface with that bit set must not be placed in that heap. Any bit set in the **ddsCapsExAlt** member means that the surface cannot be placed in that heap. When allocating surfaces, DirectDraw first passes through all heaps, and if it finds any heap for which no capability bits in the **ddsCaps** member of the VIDEOMEMORY structure match with the DDSCAPS bits of the surface, it allocates the surface in that heap. If this pass finds no such heaps, then DirectDraw makes the same pass but checks the **ddsCapsEx** field. If this pass fails to find any heaps, then the surface cannot be created in any heap.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Extended%20Heap%20Restrictions%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




