---
title: DSM\_LB\_Operations WMI Class
description: DSM\_LB\_Operations WMI Class
ms.assetid: 67f040ea-4be6-49b7-8476-abb39ad90548
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DSM\_LB\_Operations WMI Class


An MPIO driver uses the MPIO\_WMI\_METHODS WMI class to provide various services to WMI clients. MPIO publishes the MPIO\_WMI\_METHODS WMI class but expects the DSM to register the GUID and handle its implementation.

This WMI class has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following sections describe these methods and their accompanying structures:

[**DsmSetLoadBalancePolicy**](dsmsetloadbalancepolicy.md)

[**DsmSetLoadBalancePolicyALUA**](dsmsetloadbalancepolicyalua.md)

 

 





