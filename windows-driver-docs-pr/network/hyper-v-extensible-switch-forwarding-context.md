---
title: Hyper-V Extensible Switch Forwarding Context Overview
description: Hyper-V Extensible Switch Forwarding Context Overview
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hyper-V Extensible Switch Forwarding Context Overview


The [**NET\_BUFFER\_LIST**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_list) structure for each packet that traverses the Hyper-V extensible switch data path contains out-of-band (OOB) data. This data specifies the source port from where the packet originated, as well as one or more destination ports for packet delivery. This OOB data is known as the *extensible switch forwarding context*.

This section includes the following topics about the extensible switch forwarding context:

[Hyper-V Extensible Switch Forwarding Context Data Types](hyper-v-extensible-switch-forwarding-context-data-types.md)

[Managing the Hyper-V Extensible Switch Forwarding Context](managing-the-hyper-v-extensible-switch-forwarding-context.md)

 

