---
title: Compatible ID
description: A compatible ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.assetid: 3d20b43a-9e2b-4a8d-9a1a-eb9217233405
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Compatible ID


A compatible ID is a vendor-defined identification string that Windows uses to match a device to an INF file. A device can have associated with it a list of compatible IDs. The compatible IDs should be listed in order of decreasing suitability. If Windows cannot locate an INF file that matches one of a device's hardware IDs, it uses compatible IDs to locate an INF file. Compatible IDs have the same format as [hardware IDs](hardware-ids.md). However, compatible IDs are typically more generic than hardware IDs.

## <a href="" id="ddk-compatible-ids-dg"></a>


If a vendor ships an INF file that specifies a compatible ID for a [*driver node*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-node), the vendor should make sure that their INF file can support all the hardware that matches the compatible ID.

To obtain a list of compatible IDs for a device, call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) with the *DeviceProperty* parameter set to **DevicePropertyCompatibleID**. The list of compatible IDs that this routine retrieves is a REG_MULTI_SZ value. The maximum number of characters in a compatible ID list, including a NULL terminator after each compatible ID and a final NULL terminator, is REGSTR_VAL_MAX_HCID_LEN. The maximum possible number of IDs in a list of compatible IDs is 64.

 

 





