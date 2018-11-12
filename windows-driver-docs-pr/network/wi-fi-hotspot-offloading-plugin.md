---
title: Wi-Fi Hotspot Offloading Plugin
description: Wi-Fi Hotspot Offloading Plugin
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wi-Fi Hotspot Offloading Plugin

[!include[Wi-Fi Hotspot Offloading deprecation](wi-fi-hotspot-offloading-deprecation.md)]

To enable Wi-Fi offloading, create and install a hotspot plugin. This topic discusses a few of the issues to consider when developing a hotspot plugin. It also provides a general description of the plugin APIs to be implemented as part of the plugin package.

## Planning the plugin

Before starting plugin development, make sure to address the following issues:

### Supported authentication methods

Identify the authentication methods required by the networks that the plugin will support. The hotspot offload framework supports three classes of networks:

* Networks that use WISPr 1.0, or some variant, to authenticate the user and/or device over HTTP. These networks are represented by the following capability:
  * **HS_FLAG_CAPABILITY_NETWORK_AUTH_HTTP**
* Networks that use EAP-SIM/AKA/AKA' to authenticate the device. These networks are represented by the following capabilities:
  * **HS_FLAG_CAPABILITY_NETWORK_AUTH_EAP_SIM**
  * **HS_FLAG_CAPABILITY_NETWORK_AUTH_EAP_AKA**
  * **HS_FLAG_CAPABILITY_NETWORK_AUTH_EAP_AKA_PRIME**

  For EAP-based networks, the plugin can also specify a custom realm by using the **HS_FLAG_CAPABILITY_NETWORK_CUSTOM_REALM** capability.

* Networks that do not require any authentication or networks for which the plugin has an independent authentication mechanism that does not require any device credentials. These networks are represented by the following capability:
  * **HS_FLAG_CAPABILITY_NETWORK_AUTH_NO_SIM**

### Hidden networks

Hidden networks must be prespecified at initialization time because the network is not visible in the scan results. Due to the power and privacy implications of hidden networks, the framework supports at most one hidden network globally. Therefore, if another plugin has also requested connectivity to a hidden network, the request of the second plugin will be denied. If the plugin requires a hidden network to be configured, it must specify the **HS_FLAG_CAPABILITY_NETWORK_TYPE_HIDDEN** capability for that network.

For all other networks, the plugin should specify the **HS_FLAG_CAPABILITY_NETWORK_TYPE_VISIBLE** capability.

### User interface display strings

Custom UI display strings, used by the plugin to communicate with the user, must be stored in a string table (in an .rc file). The plugin must pass the string IDs to the hotspot offload service to enable it to load the appropriate strings. Currently, the following display strings are supported:

* Provider name (up to **HS_CONST_MAX_PROVIDER_NAME_LENGTH** length)
* Network name (up to **HS_CONST_MAX_NETWORK_DISPLAY_NAME_LENGTH** length)
* Message on the Advanced page (up to **HS_CONST_MAX_ADVANCED_PAGE_STRING_LENGTH** length)
* Any additional strings passed to the user using the HSHostSendUserMessage function (up to **MAX\_PATH** length). For more information, see [HS_HOST_SEND_USER_MESSAGE](https://msdn.microsoft.com/library/windows/hardware/dn789353).

**Note:** For more information about Wi-Fi Hotspot Offloading capabilities and constants, see [Wi-Fi Hotspot Offloading Constants](https://msdn.microsoft.com/library/windows/hardware/mt800328).

## Implementing the plugin

The plugin is implemented as a DLL. The functions [HSPluginGetVersion](https://msdn.microsoft.com/library/windows/hardware/dn789345) and [HSPluginInitPlugin](https://msdn.microsoft.com/library/windows/hardware/dn789346) must be exposed either by specifying them in the .def file of the plugin DLL, or by adding the “__declspec(dllexport)” keyword to them in the function implementation.

## Initialization

The plugin APIs are invoked in the following order at initialization:

### HsPluginGetVersion

The plugin should return its version information, to verify that the plugin version matches the host device version. The current version is stored in the constant **HS_CONST_HOST_CURRENT_API_VERSION**.

### HSPluginInitPlugin

This is the main initialization function. It provides the following information to the plugin:

* A context handle for the plugin to use whenever it calls any of the hotspot plugin host (**HS_HOST_\*\\***) functions
* The version number currently used by the host (**dwVerNumUsed**)
* Information about the device (**pDeviceIdentity**)
* The OS capabilities available to the plugin, specified as a HS_FLAG_CAPABILITY_NETWORK_** type (**dwHostCapabilities**)
* Handlers for the functions used by the plugin to call back to the host (**pHotspotHostHandlers**)

The plugin returns the following information to the hotspot plugin host:

* A pointer to the structure that contains the list of plugin APIs (**pHotspotPluginAPIs**). For more information, see [HOTSPOT_PLUGIN_APIS](https://msdn.microsoft.com/library/windows/hardware/dn789344).
* A pointer to the structure that contains the plugin profile (**pPluginProfile**). For more information, see [HS_PLUGIN_PROFILE](https://msdn.microsoft.com/library/windows/hardware/dn789365). 

The profile includes all of the capabilities required by the plugin. This is represented by a single value that results from combining the applicable capability flag values (HS_FLAG_CAPABILITY_NETWORK_\*) by using a bitwise OR operation. If the plugin specifies the HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_HTTP capability or the HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_EAP\_\* capabilities, the **dwSupportedSIMCount** member of the **HS_PLUGIN_PROFILE** structure must be set to the number of supported SIMs. The plugin must also specify the total number of networks that it supports by setting the **dwNumNetworksSupported** member of its **HS_PLUGIN_PROFILE** structure.

### HsPluginQueryHiddenNetwork [Optional]

If the plugin specifies the **HS_FLAG_CAPABILITY_NETWORK_TYPE_HIDDEN** capability and the device can support a hidden network, this function is called by the hotspot plugin host to obtain the hidden network information from the plugin. For more information, see [HS_PLUGIN_QUERY_HIDDEN_NETWORK](https://msdn.microsoft.com/library/windows/hardware/dn789367).

### HsPluginQuerySupportedSIMs [Optional]

The hotspot plugin host calls this function if the plugin specifies a nonzero value for **dwSupportedSIMCount**. When called, the **pNetworkIdentity** argument should be NULL and the plugin is required to provide the list of all SIMs supported by the plugin. This function may also be called later on to identify SIMs that are associated with each hotspot network (at which time, the **pNetworkIdentity** will be non-NULL). The plugin must provide the list of supported SIMs. For more information, see [HS_PLUGIN_QUERY_SUPPORTED_SIMS](https://msdn.microsoft.com/library/windows/hardware/dn789368).

## Run time

As networks become visible, the hotspot plugin host queries the plugin for each network to determine if it is a hotspot network.

### HSPluginIsHotspotNetwork

The hotspot plugin host calls this function to determine if the specified network is a hotspot network. It passes identifying information about the network (SSID, authentication type, cipher) through a [HS_NETWORK_IDENTITY](https://msdn.microsoft.com/library/windows/hardware/dn789356) structure. The plugin must return an [eHS_NETWORK_STATE](https://msdn.microsoft.com/library/windows/hardware/dn756756) enumeration value that indicates the type of network. If it is a hotspot network, then information about the network is returned through a [HS_NETWORK_PROFILE](https://msdn.microsoft.com/library/windows/hardware/dn789357) structure. For more information, see [HS_PLUGIN_IS_HOTSPOT_NETWORK](https://msdn.microsoft.com/library/windows/hardware/dn789363).

### HsPluginQuerySupportedSIMs [Optional]

The hotspot plugin host calls this function if the plugin specifies the capabilities **HS\_FLAG\_CAPABILITY\_NETWORK\_AUTH\_HTTP** or **HS\_FLAG\_CAPABILITIES\_NETWORK\_AUTH\_EAP** in the *HS_NETWORK_PROFILE* argument of the call to [HS_PLUGIN_IS_HOTSPOT_NETWORK](https://msdn.microsoft.com/library/windows/hardware/dn789363). When called in this instance, the pNetworkIdentity argument should be non-NULL and the plugin must provide the list of SIMs supported for the network specified in pNetworkIdentity only. For more information, see [HS_PLUGIN_QUERY_SUPPORTED_SIMS](https://msdn.microsoft.com/library/windows/hardware/dn789368).

### HSPluginQueryCellularExceptionHosts [Optional]

The hotspot plugin host calls this function if the **dwNumCellularExceptions** field of the [HS_NETWORK_PROFILE](https://msdn.microsoft.com/library/windows/hardware/dn789357) structure, returned by the plugin, is set to a nonzero value. The plugin must return the list of cellular bearer hosts when called. For more information, see [HS_PLUGIN_QUERY_CELLULAR_EXCEPTION_HOSTS](https://msdn.microsoft.com/library/windows/hardware/dn789366).

## Connect time

When a network is deemed connectable, or the network is selected by the user, the following sequence of calls takes place:

### HSPluginPreConnectInit

The hotspot plugin host calls this function to notify the plugin that a connection to the hotspot network specified in the [HS_NETWORK_IDENTITY](https://msdn.microsoft.com/library/windows/hardware/dn789356) structure, returned by the plugin, is in progress. For more information, see [HS_PLUGIN_PRE_CONNECT_INIT](https://msdn.microsoft.com/library/windows/hardware/dn789364).

### HSPluginStartPostConnectAuth

When the L2 connection is complete, the hotspot plugin host calls this function to notify the plugin to start authentication. The plugin is provided the *pConnectContext*, *pNetworkIdentity*, and *pNetworkProfile* from the previous call to **HSPluginPreConnectInit**, but it is also provided a *dwConnectionId* and *pSIMData*. The plugin must store the Connection ID and use it when calling back the host’s **HSHostPostConnectAuthCompletion** handler to notify the OS of the authentication result, and also in the call to **HSHostSendUserMessage** if a message needs to be conveyed to the user. The **pSIMData** struct contains addition information about the SIM configuration that could be needed by the plugin during authentication. If the plugin returns Success, it must call **HSHostPostConnectAuthCompletion** within 5 minutes or the connection is disconnected.

## Disconnect and reset

When a network is disconnected, either explicitly by some user or device action or implicitly as a result of external factors, the following functions are called:

### HSPluginStopPostConnectAuth

The hotspot plugin host calls this function to terminate network authentication because the device is about to be disconnected from the network. For more information, see [HS_PLUGIN_STOP_POST_CONNECT_AUTH](https://msdn.microsoft.com/library/windows/hardware/dn789372).

### HSPluginDisconnectFromNetwork

The hotspot plugin host calls this function to inform the plugin that the device will be disconnected from the network. For more information, see [HS_PLUGIN_DISCONNECT_FROM_NETWORK](https://msdn.microsoft.com/library/windows/hardware/dn789361).

### HSPluginReset

The hotspot plugin host calls this function to reset the plugin to its initial (just loaded) state. For more information, see [HS_PLUGIN_RESET](https://msdn.microsoft.com/library/windows/hardware/dn789369).

## Periodic calls

The following functions are called periodically, depending on specific parameters set by the plugin:

### HSPluginSendKeepAlive [Optional]

The hotspot plugin host calls this function at the frequency specified in the **dwKeepAliveTimeMins** member of the [HS_NETWORK_PROFILE](https://msdn.microsoft.com/library/windows/hardware/dn789357) structure returned by the plugin. For more information, see [HS_PLUGIN_SEND_KEEP_ALIVE](https://msdn.microsoft.com/library/windows/hardware/dn789370).

### HSPluginCheckForUpdates [Optional]

The hotspot plugin host calls this function at the frequency specified in the **dwProfileUpdateTimeDays** member of the [HS_PLUGIN_PROFILE](https://msdn.microsoft.com/library/windows/hardware/dn789365) structure. 

## Unloading the plugin

### HSPluginDeinit

The hotspot plugin host calls this function to enable the plugin to flush any unsaved information and close any open handles before it is unloaded. The plugin will be provided the reason for the unload in the *UnloadReason* argument. For more information, see [HS_PLUGIN_DEINIT](https://msdn.microsoft.com/library/windows/hardware/dn789360).

## Plugin Installation package

THe plugin installation package should include the following:

### The Plugin DLL File

The DLL file must be signed and placed under **Programs\HotspotHost\\**<*ProviderName*>, where <*ProviderName*> is the name of the DLL provider. 

For information about signing the DLL, see [Sign binaries and packages](https://msdn.microsoft.com/library/windows/hardware/dn789217). 

There is no particular convention for naming the DLL file, so making sure the path to the file is correct in the registry is all that is required. For example, the registry information could be specified in the package as:

```xml
<RegKeys>
        <RegKey KeyName="$(hklm.software)\Microsoft\Windows Phone\HotspotOffload\Plugins\<ProviderName>">
          <RegValue Name="PluginRank" Type="REG_DWORD" Value="00000005" />
          <RegValue Name="PluginPath" Type="REG_SZ" Value="%SystemDrive%\Programs\HotspotHost\Orange\<ProviderName>\<HotspotPlugin.dll>" />
        </RegKey>
      </RegKeys>
```

### Registry configuration

The required registry settings are saved in a new entry created under: **HKEY_LOCAL_MACHINE\Software\Microsoft\Windows Phone\HotspotOffload\Plugins\\** *ProviderName*.

*ProviderName* must be unique to the plugin provider or Mobile Operator.

The following values must be saved under the registry key:

| Name | Type | Description |
| --- | --- | --- |
| PluginPath | [REG_SZ] | The name and full path to the DLL. |
| PluginRank | [REG_DWORD] | Any positive value between 1 and 250, inclusive (0 is reserved for Microsoft). A lower value represents a higher priority. If two plugins have the same rank, the hotspot service arbitrarily prioritizes one over another. |

### Data files that contain connection-specific information such as a list of SSIDs, encrypted credentials, etc. [Optional]

The data files should be saved under: `Data\SharedData\HotspotHost\Plugins\<ProviderName>`.

