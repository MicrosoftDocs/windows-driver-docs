---
title: Obtaining Collection Information
description: Obtaining Collection Information
ms.assetid: 0568993b-ff50-48ac-a875-95ab643d6c28
keywords:
- collections WDK HID , informatin gathering
- HID collections WDK , information gathering
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining Collection Information





This section addresses obtaining information that user-mode applications and kernel-mode drivers use to operate a [HID collection](hid-collections.md).

After an application or driver has connected to a HID collection, it can obtain the following information:

-   [Collection's capabilities](collection-capability.md).

-   [Button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md), which describe the capabilities of buttons and values supported by the collection.

-   Link collection array, which describes the internal organization of its [link collections](link-collections.md).

This information includes the [HID usage](hid-usages.md) of the collection and all the controls supported by the collection. If an application or driver does not use these controls, it should immediately close its connection to the collection.

After obtaining this information, an application or driver has the information it requires to access control data in HID reports.

 

 




