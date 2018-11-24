---
title: UPS Registry Entries
description: UPS Registry Entries
ms.assetid: d0d4ef8f-9df1-48a3-b0fc-cea4eb3cdf40
keywords:
- UPS minidrivers WDK , registry entries
- UPS registry entries WDK
- registry WDK UPS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UPS Registry Entries


## <span id="ddk_ups_registry_entries_kg"></span><span id="DDK_UPS_REGISTRY_ENTRIES_KG"></span>


UPS registry entries provide model-specific information about a system's UPS. A vendor-supplied UPS minidriver is responsible for supplying values for some of these registry entries, which are stored under the UPS service's tree.

The following registry key is the root of the UPS service tree:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**UPS**

The UPS registry entries are organized under the following four keys:

-   **UPS** -- Service control manager entries, and entries used by the Windows NT 4.0 UPS service

    These entries are for system use only. Vendors must not modify these entries.

-   **UPS**\\**Config** -- Information pertaining to the configuration of the UPS service.

    These entries are for system use only. Vendors must not modify these entries.

-   [UPS\\Status Registry Entries](ups-status-registry-entries.md) -- Status information.

    These entries are for vendor and system use. If vendors create and modify these entries as appropriate, **Power Options** displays them.

-   [UPS\\ServiceProviders Registry Entries](ups-serviceproviders-registry-entries.md) -- Entries for different vendor and model UPS devices.

    These entries are for vendor and system use. Vendors should create these entries while [installing UPS minidrivers](installing-ups-minidrivers.md). The system's UPS service copies UPS model-specific values to other, system-controlled registry locations after an administrator has selected the UPS model for use.

 

 




