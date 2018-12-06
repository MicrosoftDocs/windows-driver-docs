---
title: Container IDs Generated from the Removable Device Capability
description: Container IDs Generated from the Removable Device Capability
ms.assetid: e09b1ee5-9ccd-428a-8af3-79f138eb07f9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Container IDs Generated from the Removable Device Capability


Starting with Windows 7, if a bus driver cannot provide a container ID for a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that it is enumerating, the Plug and Play (PnP) manager uses the removable device capability to generate a container ID for all devnodes enumerated for the physical device. The bus driver reports the removable device capability in response to an [**IRP_MN_QUERY_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request.

This section contains the following topics:

[Overview of the Removable Device Capability](overview-of-the-removable-device-capability.md)

[How Container IDs are Generated from the Removable Device Capability](how-container-ids-are-generated-from-the-removable-device-capability.md)

 

 





