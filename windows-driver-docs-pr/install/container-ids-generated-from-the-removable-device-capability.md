---
title: Container IDs Generated from the Removable Device Capability
description: Container IDs Generated from the Removable Device Capability
ms.date: 04/20/2017
---

# Container IDs Generated from the Removable Device Capability


Starting with Windows 7, if a bus driver cannot provide a container ID for a device node (*devnode*) that it is enumerating, the Plug and Play (PnP) manager uses the removable device capability to generate a container ID for all devnodes enumerated for the physical device. The bus driver reports the removable device capability in response to an [**IRP_MN_QUERY_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md) request.

This section contains the following topics:

[Overview of the Removable Device Capability](overview-of-the-removable-device-capability.md)

[How Container IDs are Generated from the Removable Device Capability](how-container-ids-are-generated-from-the-removable-device-capability.md)

 

