---
title: Enabling TWAIN Capability Pass-Through in a WIA Driver
description: Enabling TWAIN Capability Pass-Through in a WIA Driver
ms.assetid: b2108109-9e41-481d-bc25-67327420faf9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling TWAIN Capability Pass-Through in a WIA Driver





To enable support for TWAIN capability pass-through, add the **WiaItemTypeTwainCapabilityPassThrough** flag to the [**WIA\_IPA\_ITEM\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff551585) property on the root item. This flag is defined in header file *wiatwcmp.h*.

The following example is taken from the *wiascanr* sample (which is included in the Driver Development Kit \[DDK\]) and demonstrates the use of the **WiaItemTypeTwainCapabilityPassThrough** flag).

```cpp
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

 

 




