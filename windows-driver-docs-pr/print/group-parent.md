---
title: Group Parent
author: windows-driver-content
description: Group Parent
ms.assetid: b4c40c15-df16-4af0-81c8-9e70d26ba598
keywords: ["group parents WDK print", "Common Property Sheet User Interface WDK print , group parents", "CPSUI WDK print , group parents", "property sheet pages WDK print , group parents", "grouping property sheet pages"]
---

# Group Parent


## <a href="" id="ddk-group-parent-gg"></a>


Property sheet pages can be grouped together by assigning them to a single *group parent*. You can create a group parent by calling CPSUI's [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207) function with a [**CPSFUNC\_INSERT\_PSUIPAGE**](https://msdn.microsoft.com/library/windows/hardware/ff546414) function code, and specifying PSUIPAGEINSERT\_GROUP\_PARENT as the **Type** member for an [**INSERTPSUIPAGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff551634) structure.

When a new group parent is created, a handle is returned. The handle can then be used as the *hComPropSheet* parameter to [**ComPropSheet**](https://msdn.microsoft.com/library/windows/hardware/ff546207), when adding or deleting property sheet pages.

Additionally, a group parent handle is received as the **hComPropSheet** member of the [**PROPSHEETUI\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff561767) structure that is received by an application's [**PFNPROPSHEETUI**](https://msdn.microsoft.com/library/windows/hardware/ff559812)-typed callback function. If you don't create new group parents, all property sheet pages should be assigned to this one.

You can create additional group parents under each group parent that is created. The property sheet itself is considered to be the top-level group parent. If you do not explicitly create additional group parents, all added property sheet pages are assigned to the top-level parent.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Group%20Parent%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


