---
title: eHS_UNLOAD_REASON enumeration
description: The eHS_UNLOAD_REASON enumeration indicates the reason for the plugin to get unloaded.
ms.assetid: 1e658dd3-f66d-4803-ad3c-84bfa1890a86
keywords: 
- eHS_UNLOAD_REASON enumeration Network Drivers Starting with Windows Vista
ms.date: 07/31/2017
ms.localizationpriority: medium
---

# eHS\_UNLOAD\_REASON enumeration

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]


The **eHS\_UNLOAD\_REASON** enumeration indicates the reason for the plugin to get unloaded.

Syntax
------

```ManagedCPlusPlus
typedef enum _eHS_UNLOAD_REASON { 
  HS_UNLOAD_REASON_NONE,
  HS_UNLOAD_REASON_PLUGN_INIT_FAILED,
  HS_UNLOAD_REASON_NO_NETWORKS_SUPPORTED,
  HS_UNLOAD_REASON_NO_PROVIDE_NAME_ID,
  HS_UNLOAD_REASON_ZERO_SIM_COUNT,
  HS_UNLOAD_REASON_DISPLAY_FLAG_BUT_NO_DISPLAY_STRING_ID,
  HS_UNLOAD_REASON_CUSTOM_REALM_FLAG_BUT_NO_REALM_STRING,
  HS_UNLOAD_REASON_DUPLICATE_PLUGIN_LOADED,
  HS_UNLOAD_REASON_RELOAD_REQUESTED_BY_PLUGIN,
  HS_UNLOAD_REASON_EXCEPTION_DURING_PLUGIN_CALL,
  HS_UNLOAD_REASON_EXCEPTION_IN_PLUGIN_HOST,
  HS_UNLOAD_REASON_ASYNC_INITIALIZATION_FAILED,
  HS_UNLOAD_REASON_UNSUPPORTED_AUTH_CAPABILITY_REQUESTED,
  HS_UNLOAD_REASON_FAILED_TO_LOAD_PROVIDER_NAME_STRING,
  HS_UNLOAD_REASON_FAILED_TO_LOAD_ADVANCED_PAGE_STRING,
  HS_UNLOAD_REASON_FAILED_TO_LOAD_NETWORK_NAME_STRING,
  HS_UNLOAD_REASON_FAILED_TO_CONFIGURE_HIDDEN_NETWORK,
  HS_UNLOAD_REASON_HIDDEN_NETWORK_ALREADY_CONFIGURED,
  HS_UNLOAD_REASON_FAILED_TO_QUERY_SIMS,
  HS_UNLOAD_REASON_PLUGIN_REQUIRED_SIM_NOT_PRESENT,
  HS_UNLOAD_REASON_SIM_CONFIG_CHANGED,
  HS_UNLOAD_REASON_WIFI_SWITCHED_OFF_IN_OS,
  HS_UNLOAD_REASON_MAX
} eHS_UNLOAD_REASON;
```

Constants
---------

<a href="" id="hs-unload-reason-none"></a>**HS\_UNLOAD\_REASON\_NONE**  
No specific reason for the unload operation.

<a href="" id="hs-unload-reason-plugn-init-failed"></a>**HS\_UNLOAD\_REASON\_PLUGN\_INIT\_FAILED**  
The plugin is being unloaded because it failed to initialize successfully.

<a href="" id="hs-unload-reason-no-networks-supported"></a>**HS\_UNLOAD\_REASON\_NO\_NETWORKS\_SUPPORTED**  
The plugin is being unloaded because the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure did not indicate a valid value for **dwNumNetworksSupported**.

<a href="" id="hs-unload-reason-no-provide-name-id"></a>**HS\_UNLOAD\_REASON\_NO\_PROVIDE\_NAME\_ID**  
The plugin is being unloaded because the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure did not specify a string ID for **dwProviderNameStringID**.

<a href="" id="hs-unload-reason-zero-sim-count"></a>**HS\_UNLOAD\_REASON\_ZERO\_SIM\_COUNT**  
The plugin is being unloaded because there are no SIM cards present.

<a href="" id="hs-unload-reason-display-flag-but-no-display-string-id"></a>**HS\_UNLOAD\_REASON\_DISPLAY\_FLAG\_BUT\_NO\_DISPLAY\_STRING\_ID**  
The plugin is being unloaded because the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure requires HTTP or EAP SIM-based authentication but did not specify a value for **dwSupportedSIMCount.**

<a href="" id="hs-unload-reason-custom-realm-flag-but-no-realm-string"></a>**HS\_UNLOAD\_REASON\_CUSTOM\_REALM\_FLAG\_BUT\_NO\_REALM\_STRING**  
The plugin is being unloaded because the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure specified the **HS\_FLAG\_CAPABILITY\_NETWORK\_CUSTOM\_REALM** capability but did not provide a valid string for **szRealm**.

<a href="" id="hs-unload-reason-duplicate-plugin-loaded"></a>**HS\_UNLOAD\_REASON\_DUPLICATE\_PLUGIN\_LOADED**  
The plugin is being unloaded because another plugin is using the same DLL.

<a href="" id="hs-unload-reason-reload-requested-by-plugin"></a>**HS\_UNLOAD\_REASON\_RELOAD\_REQUESTED\_BY\_PLUGIN**  
The plugin is being unloaded because the plugin requested to be unloaded and reloaded by specifying the **HS\_UPDATE\_RESULT\_ACTION\_RELOAD** action with the [**eHS\_UPDATE\_RESULT**](ehs-update-result.md) enumeration.

<a href="" id="hs-unload-reason-exception-during-plugin-call"></a>**HS\_UNLOAD\_REASON\_EXCEPTION\_DURING\_PLUGIN\_CALL**  
The plugin is being unloaded because the host process encountered an exception while in a call to the plugin.

<a href="" id="hs-unload-reason-exception-in-plugin-host"></a>**HS\_UNLOAD\_REASON\_EXCEPTION\_IN\_PLUGIN\_HOST**  
The plugin is being unloaded because the hotspot host encountered an exception.

<a href="" id="hs-unload-reason-async-initialization-failed"></a>**HS\_UNLOAD\_REASON\_ASYNC\_INITIALIZATION\_FAILED**  
The plugin is being unloaded because the hotspot service failed to register for notifications from the plugin.

<a href="" id="hs-unload-reason-unsupported-auth-capability-requested"></a>**HS\_UNLOAD\_REASON\_UNSUPPORTED\_AUTH\_CAPABILITY\_REQUESTED**  
The plugin is being unloaded because none of the authentication capabilities requested by the plugin are available.

<a href="" id="hs-unload-reason-failed-to-load-provider-name-string"></a>**HS\_UNLOAD\_REASON\_FAILED\_TO\_LOAD\_PROVIDER\_NAME\_STRING**  
The plugin is being unloaded because the hotspot service could not map the **dwProviderNameStringID** string ID provided in the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure to a valid string.

<a href="" id="hs-unload-reason-failed-to-load-advanced-page-string"></a>**HS\_UNLOAD\_REASON\_FAILED\_TO\_LOAD\_ADVANCED\_PAGE\_STRING**  
The plugin is being unloaded because the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure specified an (optional) **dwAdvancedPageStringID** string ID but it did not map to a valid string.

<a href="" id="hs-unload-reason-failed-to-load-network-name-string"></a>**HS\_UNLOAD\_REASON\_FAILED\_TO\_LOAD\_NETWORK\_NAME\_STRING**  
The plugin is being unloaded because the plugin's [**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md) structure specified an (optional) **dwGenericNetworkNameStringID** string ID, but it did not map to a valid string.

<a href="" id="hs-unload-reason-failed-to-configure-hidden-network"></a>**HS\_UNLOAD\_REASON\_FAILED\_TO\_CONFIGURE\_HIDDEN\_NETWORK**  
The plugin is being unloaded because the plugin specified a hidden network (via the **HS\_FLAG\_CAPABILITY\_NETWORK\_TYPE\_HIDDEN** capability), but the hotspot service was unable to configure the hidden network.

<a href="" id="hs-unload-reason-hidden-network-already-configured"></a>**HS\_UNLOAD\_REASON\_HIDDEN\_NETWORK\_ALREADY\_CONFIGURED**  
The plugin is being unloaded because the plugin specified a hidden network via the **HS\_FLAG\_CAPABILITY\_NETWORK\_TYPE\_HIDDEN** capability but another plugin has already claimed the hidden network slot.

<a href="" id="hs-unload-reason-failed-to-query-sims"></a>**HS\_UNLOAD\_REASON\_FAILED\_TO\_QUERY\_SIMS**  
The plugin is being unloaded because the call to [**HS\_PLUGIN\_QUERY\_SUPPORTED\_SIMS**](hs-plugin-query-supported-sims.md) failed.

<a href="" id="hs-unload-reason-plugin-required-sim-not-present"></a>**HS\_UNLOAD\_REASON\_PLUGIN\_REQUIRED\_SIM\_NOT\_PRESENT**  
The plugin is being unloaded because the SIMs required by the plugin are not present in the device.

<a href="" id="hs-unload-reason-sim-config-changed"></a>**HS\_UNLOAD\_REASON\_SIM\_CONFIG\_CHANGED**  
The plugin is being unloaded because the SIM configuration changed, which requires the plugins to be unloaded and reloaded.

<a href="" id="hs-unload-reason-wifi-switched-off-in-os"></a>**HS\_UNLOAD\_REASON\_WIFI\_SWITCHED\_OFF\_IN\_OS**  
The plugin is being unloaded because Wi-Fi functionality was switched off in the OS.

<a href="" id="hs-unload-reason-max"></a>**HS\_UNLOAD\_REASON\_MAX**  
Indicates an out-of-range value.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Hotspotoffloadplugin.h (include Hotspotoffloadplugin.h)</td>
</tr>
</tbody>
</table>

## See also


[**HS\_PLUGIN\_PROFILE**](hs-plugin-profile.md)

[**eHS\_UPDATE\_RESULT**](ehs-update-result.md)

[**HS\_PLUGIN\_QUERY\_SUPPORTED\_SIMS**](hs-plugin-query-supported-sims.md)

 

 




