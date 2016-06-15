---
title: UPS Registry Entries
description: UPS Registry Entries
ms.assetid: d0d4ef8f-9df1-48a3-b0fc-cea4eb3cdf40
keywords: ["UPS minidrivers WDK , registry entries", "UPS registry entries WDK", "registry WDK UPS"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[battery\battery]:%20UPS%20Registry%20Entries%20%20RELEASE:%20%286/7/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


