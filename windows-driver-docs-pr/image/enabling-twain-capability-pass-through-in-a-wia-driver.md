---
title: Enabling TWAIN Capability Pass-Through in a WIA Driver
author: windows-driver-content
description: Enabling TWAIN Capability Pass-Through in a WIA Driver
ms.assetid: b2108109-9e41-481d-bc25-67327420faf9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enabling TWAIN Capability Pass-Through in a WIA Driver


## <a href="" id="ddk-enabling-twain-capability-pass-through-in-a-wia-driver-si"></a>


To enable support for TWAIN capability pass-through, add the **WiaItemTypeTwainCapabilityPassThrough** flag to the [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585) property on the root item. This flag is defined in header file *wiatwcmp.h*.

The following example is taken from the *wiascanr* sample (which is included in the Driver Development Kit \[DDK\]) and demonstrates the use of the **WiaItemTypeTwainCapabilityPassThrough** flag).

```
// Initialize WIA_IPA_ITEM_FLAGS
  m_pszRootItemDefaults[PropIndex] = WIA_IPA_ITEM_FLAGS_STR;
  m_piRootItemDefaults[PropIndex] = WIA_IPA_ITEM_FLAGS;
// Next assignment adds the WiaItemTypeTwainCapabilityPassThrough flag.
  m_pvRootItemDefaults[PropIndex].lVal = 
     WiaItemTypeRoot|WiaItemTypeFolder | 
     WiaItemTypeDevice| WiaItemTypeTwainCapabilityPassThrough;
  m_pvRootItemDefaults[PropIndex].vt = VT_I4;
  m_psRootItemDefaults[PropIndex].ulKind = PRSPEC_PROPID;
  m_psRootItemDefaults[PropIndex].propid = 
     m_piRootItemDefaults[PropIndex];
  m_wpiRootItemDefaults[PropIndex].lAccessFlags = 
     WIA_PROP_READ | WIA_PROP_FLAG;
  m_wpiRootItemDefaults[PropIndex].vt = 
     m_pvRootItemDefaults [PropIndex].vt;
  m_wpiRootItemDefaults[PropIndex].ValidVal.Flag.Nom = 
     m_pvRootItemDefaults [PropIndex].lVal;
  m_wpiRootItemDefaults[PropIndex].ValidVal.Flag.ValidBits = 
     WiaItemTypeRoot | WiaItemTypeFolder|WiaItemTypeDevice;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Enabling%20TWAIN%20Capability%20Pass-Through%20in%20a%20WIA%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


