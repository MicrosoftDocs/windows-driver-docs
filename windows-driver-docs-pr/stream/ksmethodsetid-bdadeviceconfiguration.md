---
title: KSMETHODSETID_BdaDeviceConfiguration
description: KSMETHODSETID_BdaDeviceConfiguration is the BDA device configuration method set.
ms.date: 10/12/2021
ms.localizationpriority: medium
---

# KSMETHODSETID_BdaDeviceConfiguration

**KSMETHODSETID_BdaDeviceConfiguration** is the BDA device configuration method set. It is used to configure a filter for a filter graph.

The following methods are available:

[**KSMETHOD_BDA_CREATE_PIN_FACTORY**](ksmethod-bda-create-pin-factory.md)  
Triggers a call that creates a pin factory for the filter.

[**KSMETHOD_BDA_DELETE_PIN_FACTORY**](ksmethod-bda-delete-pin-factory.md)  
Triggers a call that deletes a pin factory for the filter.

[**KSMETHOD_BDA_CREATE_TOPOLOGY**](ksmethod-bda-create-topology.md)  
Creates a topology structure in Ring 3 that reflects the known connections in the filter.

## Comments

This method set is implemented on filters.

If a BDA minidriver does not define it's own handlers for the methods in this method set, then the BDA support library will add default handlers when the BDA minidriver calls the **BdaInitFilter** function.

## See also

[**BdaInitFilter**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdainitfilter)
