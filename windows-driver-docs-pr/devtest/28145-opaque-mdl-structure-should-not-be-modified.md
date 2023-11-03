---
title: C28145 warning
description: Warning C28145 The opaque MDL structure should not be modified by a driver.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28145"
---

# C28145


warning C28145: The opaque MDL structure should not be modified by a driver

The driver code is changing a member of an MDL structure.

The **MdlFlags** field is used as a proxy for all MDL fields. No fields should be modified, with the exception of MDL\_MAPPING\_CAN\_FAIL, which is used for drivers that need to be Microsoft Windows 98 or Windows NT (SP4) compatible, and MDL\_PAGES\_LOCKED, which is used for drivers that need to be Windows 2000 compatible.

