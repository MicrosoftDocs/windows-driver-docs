---
title: Querying WDDM Feature Support and Enablement
description: Describes DDIs that allow a user-mode or kernel-mode driver to determine whether a WDDM feature is supported and enabled.
keywords:
- WDDM, feature enabled
- WDDM, feature supported
ms.date: 04/05/2024
---

# Querying WDDM feature support and enablement

This article describes how to query the support and enablement of Windows Display Driver Model (WDDM) features. It describes:

* How user-mode and kernel-mode display drivers (UMD and KMD) can query the OS to determine whether a WDDM feature is supported and enabled on a system.
* How the OS can determine whether a driver supports a particular WDDM feature.

This feature querying mechanism is introduced starting in Windows 11, version 24H2 (WDDM 3.2).

## Overview of WDDM features

WDDM can be viewed as a collection of *features*, where a feature is a collection of WDDM APIs/DDIs that cover certain functionality.

A feature is identified by its *feature ID*, which is composed of a *category ID* and a *sub-ID* for the feature itself within the category.

Each feature known to the OS has associated state information to determine whether the feature is supported and/or enabled on the system. Some features can be *driver features*. A driver feature requires some level of support from the driver to be enabled. *Dxgkrnl* provides a handshaking mechanism to determine feature configuration. A registry key can override feature configuration on a per-feature, per-adapter basis.

Driver features can also have a [*feature interface*](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgkddi_feature_interface) that provides the driver's DDIs related to the feature. By supporting individual feature interfaces, we no longer need to rely on updating the main interfaces between the OS and KMD, which could previously only be expanded with updated WDDM versioning changes. This approach provides a more flexible means of backporting features to previous OSs or via Windows Moment releases without the need to define special support.

Each feature can have a list of dependencies that must also be supported as a prerequisite. Future features that require such dependencies will indicate their required dependencies in their documentation.

Features are versioned, and can have different interfaces or configurations for each supported version.

WDDM introduces a set of APIs to query a particular feature state. The APIs include:

* [**DXGK_FEATURE_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_feature_interface)
  * KMD can query for and use this interface to determine whether a particular feature is supported and enabled in the system after [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) is called.
  * This mechanism replaces the following existing DDIs:
    * [**DxgkCbIsFeatureEnabled**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_isfeatureenabled)
    * [**DxgkCbQueryFeatureSupport**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_queryfeaturesupport)

* [**DXGKDDI_FEATURE_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgkddi_feature_interface)
  * This mechanism allows the OS to query a feature interface from KMD.

* [**DxgkIsFeatureEnabled2**](/windows-hardware/drivers/ddi/d3dkmddi/nf-d3dkmddi-dxgkisfeatureenabled2)
  * This function is the entry point in the system-supplied *displib* library.
  * KMD can call **DxgkIsFeatureEnabled2** from its [**DriverEntry**](driverentry-of-display-miniport-driver.md) routine without [initializing *Dxgkrnl*](/windows-hardware/drivers/ddi/dispmprt/nf-dispmprt-dxgkinitialize) to determine whether the system has a particular feature enabled.

* [**D3DKMTIsFeatureEnabled**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtisfeatureenabled)
  * This user-mode API allows a user-mode module to determine whether a particular feature is enabled.

When a display miniport driver is loaded, the WDDM port driver queries all features that depend on driver support.

The driver can query the WDDM port driver for the supported features when it's loaded.

## WDDM feature definitions

A feature is identified by its *feature ID*, which is represented as a [**DXGK_FEATURE_ID**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_id) value. A **DXGK_FEATURE_ID** value has the following format:

* The feature's *category ID* is a [**DXGK_FEATURE_CATEGORY**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_category) value that identifies the category of the feature. It's stored in the upper 4 bits of **DXGK_FEATURE_ID**.
* The feature's *sub-ID*  that identifies the actual feature within the feature category. The sub-ID is stored in the bottom 28 bits of **DXGK_FEATURE_ID**.

When **DXGK_FEATURE_CATEGORY** is **DXGK_FEATURE_CATEGORY_DRIVER**, the feature's sub-ID is a [**DXGK_DRIVER_FEATURE**](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_driver_feature) value that identifies the actual feature.

### Global vs adapter features

Individual features correspond to either a global feature or an adapter-specific feature. A feature's documentation indicates whether the feature is a global feature. It's important to know this information when querying whether a feature is enabled, because an **hAdapter** parameter might be required to query the feature configuration specific to that adapter, or use the global database.

The following features are currently defined as global features:

* DXGK_FEATURE_GPUVAIOMMU

### Virtualization

For GPU-PV, the OS automatically negotiates feature support and enablement between the host and guest. The driver doesn't need to implement any special support for such queries.

### Dependencies

Each feature can specify a list of dependencies. These dependencies are tied to the definition of the feature itself, and are hardcoded at compile time by the OS.

For a particular feature to be enabled, all of its dependencies must also be enabled.

The following features currently have dependencies:

* DXGK_FEATURE_USER_MODE_SUBMISSION
* DXGK_FEATURE_HWSCH
* DXGK_FEATURE_NATIVE_FENCE

A feature's documentation specifies whether a feature has any dependencies that must also be enabled.

## Querying feature support from KMD

The OS uses a handshaking mechanism to determine whether both the OS and the driver support a feature. This mechanism allows the initial query for whether a feature is enabled to originate from any source (the OS/*Dxgkrnl*, KMD, UMD, Runtime, etc.), and still have the appropriate mechanisms for the OS and driver to negotiate feature support.

KMD needs to implement the [**DXGKDDI_FEATURE_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgkddi_feature_interface) interface in order for the port driver to query feature support. The interface GUID is GUID_WDDM_INTERFACE_FEATURE.

If the driver implements **DXGKDDI_FEATURE_INTERFACE**, it doesn't need to call [**DxgkCbQueryFeatureSupport**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_queryfeaturesupport) to enable a feature in the port driver ahead of time. It can instead query feature support on demand using its [**DXGKDDI_FEATURE_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgkddi_feature_interface)'s interface.

## Querying feature enablement

This section describes how a component checks whether a feature is enabled on the system. The [**DXGK_ISFEATUREENABLED_RESULT**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-dxgk_isfeatureenabled_result) structure defines the results of a feature query.

### User-mode query

A user-mode client calls [**D3DKMTIsFeatureEnabled**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtisfeatureenabled) to query whether a particular WDDM feature is enabled.

### Kernel-mode query

To obtain the callback for querying feature support, KMD needs to query the [**DxgkServicesFeature**](/windows-hardware/drivers/ddi/dispmprt/ne-dispmprt-dxgk_services) interface. To get this interface, KMD calls *Dxgkrnl*'s [**DxgkCbQueryServices**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_query_services) callback with **ServiceType** set to a **DXGK_SERVICES** value of **DxgkServicesFeature**, as shown in the following code snippet. KMD can call **DxgkCbQueryServices** once it gets the callback pointer in a call to its [**DxgkDdiStartDevice**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device).

  ```cpp
  DXGK_FEATURE_INTERFACE FeatureInterface = {};
  FeatureInterface.Size = sizeof(pDevExt->FeatureInterface);
  FeatureInterface.Version = DXGK_FEATURE_INTERFACE_VERSION_1;
  Status = DxgkInterface.DxgkCbQueryServices(DxgkInterface.DeviceHandle, DxgkServicesFeature, (PINTERFACE)&FeatureInterface);
  ```

## Checking for a feature before *Dxgkrnl* is initialized

**DxgkIsFeatureEnabled2** is defined in the display port driver's library (*displib.h*). As a result, KMD can call [**DxgkIsFeatureEnabled2**](/windows-hardware/drivers/ddi/d3dkmddi/nf-d3dkmddi-dxgkisfeatureenabled2) to check for the presence of a feature before *Dxgkrnl* is initialized.

Because this call is intended to be used at [**DriverEntry**](driverentry-of-display-miniport-driver.md), only a subset of global features can be queried through it. This subset currently includes:

* DXGK_FEATURE_GPUVAIOMMU

## Registry Overrides

You can override feature configurations in the registry during driver development and testing. This capability is useful to force a particular feature to be usable in a development environment when the default feature configuration might indicate it's unsupported.

A driver must not define any of these registry keys in their INF during driver installation. These keys are intended only for testing and development purposes, and not to broadly override a specific feature.

A driver's feature configuration is stored in the PNP software key for the adapter, under a ***XXXX*\\Features\\*YYYY*** key, where *XXXX* is the device identifier assigned by PnP when the device is installed and *YYYY* represents the [feature ID](/windows-hardware/drivers/ddi/d3dukmdt/ne-d3dukmdt-dxgk_feature_id). An example is ```HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000\Features\4```.

The following sections describe overrides that can be specified for a feature.

### Registry key name: Enabled

| Name | Type | Value | Description |
| ---- | ---- | ----- | ----------- |
| Enabled | DWORD | 0 (not supported) or 1 (supported). The default is feature-dependent. | Overrides OS support for the feature. |

Despite the name, this entry only overrides the OS-side *support* of a feature. It doesn't force the feature to always be enabled (that is, it doesn't guarantee that a call to IsFeatureEnabled(ID) returns **Enabled**=TRUE). Proper driver-side negotiation is still required for driver features.

### Registry key name: MinVersion

| Name | Type | Value | Description |
| ---- | ---- | ----- | ----------- |
| MinVersion | DWORD | Feature-dependent | Constrains the minimum supported version for this feature to be more restrictive than the default minimum version. |

This value can't be used to force the OS to support a version lower than the default minimum supported version (as this default minimum is chosen due to implementation support). Instead, this key can constrain the minimum supported version to a value higher than the default.

This configuration is useful to work around a bug that might be present in a specific version of the feature implementation.

If **MinVersion** is specified, **MaxVersion** must also be specified.

### Registry key name: MaxVersion

| Name | Type | Value | Description |
| ---- | ---- |------ | ----------- |
| MaxVersion | DWORD | Feature-dependent | Constrains the maximum supported version for this feature to be more restrictive than the default maximum version. |

This value can't be used to force the OS to support a version higher than the default maximum supported version (as this default maximum is chosen due to implementation support). Instead, this key can constrain the maximum supported version to a value lower than the default.

This configuration is particularly useful to work around a bug that might be present in a specific version of the feature implementation.

If **MaxVersion** is specified, **MinVersion** must also be specified.

### Registry key name: AllowExperimental

| Name | Type | Value | Description |
| ---- | ---- | ----- | ----------- |
| AllowExperimental | DWORD | 0 (experimental support isn't allowed) or 1 (supported). Default is branch-defined. | Forces the OS to allow experimental versions of this feature to be loaded, even if the build doesn't allow it by default. |

The OS typically defines experimental support. By default, experimental support is defined on a feature-by-feature basis, with a global override available on development builds (for example, internal developer builds always allow experimental support for all features, whereas prerelease builds might only allow support for specific features).

This value allows the OS definition to be overridden for a specific feature ID. It can even be used on release builds to bring up experimental driver support on an OS that supports the feature, but keep the feature disabled in a retail environment.

## Debugger extension: *dxgkdx*

The *dxgkdx* kernel debugger extension implements a ```!feature``` command that can query the state of various features.

The currently support commands (with example output) are:

```dbgcmd
!feature list

Lists features with descriptor information

2: kd> !dxgkdx.feature list

  Id  FeatureName                                       Supported  Version  VirtMode     Global  Driver
   0  HWSCH                                             Yes        1-1      Negotiate    -       X
   1  HWFLIPQUEUE                                       Yes        1-1      Negotiate    -       X
   2  LDA_GPUPV                                         Yes        1-1      Negotiate    -       X
   3  KMD_SIGNAL_CPU_EVENT                              Yes        1-1      Negotiate    -       X
   4  USER_MODE_SUBMISSION                              Yes        1-1      Negotiate    -       X
   5  SHARE_BACKING_STORE_WITH_KMD                      Yes        1-1      HostOnly     -       X
  32  PAGE_BASED_MEMORY_MANAGER                         No         1-1      Negotiate    -       X
  33  KERNEL_MODE_TESTING                               Yes        1-1      Negotiate    -       X
  34  64K_PT_DEMOTION_FIX                               Yes        1-1      DeferToHost  -       -
  35  GPUPV_PRESENT_HWQUEUE                             Yes        1-1      DeferToHost  -       -
  36  GPUVAIOMMU                                        Yes        1-1      None         X       -
  37  NATIVE_FENCE                                      Yes        1-1      Negotiate    -       X

```

```dbgcmd
!feature config

Lists the current configuration information for each feature. In most cases, this will be unspecified/default values if not overriden.

2: kd> !dxgkdx.feature config

  Id  FeatureName                                       Enabled Version  AllowExperimental
   0  HWSCH                                             --       --       -
   1  HWFLIPQUEUE                                       --       --       -
   2  LDA_GPUPV                                         --       --       -
   3  KMD_SIGNAL_CPU_EVENT                              --       --       -
   4  USER_MODE_SUBMISSION                              --       --       -
   5  SHARE_BACKING_STORE_WITH_KMD                      --       --       -
  32  PAGE_BASED_MEMORY_MANAGER                         --       --       -
  33  KERNEL_MODE_TESTING                               --       --       -
  34  64K_PT_DEMOTION_FIX                               --       --       -
  35  GPUPV_PRESENT_HWQUEUE                             --       --       -
  36  GPUVAIOMMU                                        --       --       -
  37  NATIVE_FENCE                                      --       --       -
```

```dbgcmd

!feature state

Lists the current state of each feature. Features that have bnot been queried will have an unknown state

2: kd> !dxgkdx.feature state

  Id  FeatureName                                       Enabled  Version  Driver  Config
   0  HWSCH                                             No       0        No      No    
   1  HWFLIPQUEUE                                       No       0        No      No    
   2  LDA_GPUPV                                         No       0        No      No    
   3  KMD_SIGNAL_CPU_EVENT                              Yes      1        Yes     Yes   
   4  USER_MODE_SUBMISSION                              No       0        No      No    
   5  SHARE_BACKING_STORE_WITH_KMD                      Unknown  --       --      --    
  32  PAGE_BASED_MEMORY_MANAGER                         No       0        No      No    
  33  KERNEL_MODE_TESTING                               No       0        No      No    
  34  64K_PT_DEMOTION_FIX                               Unknown  --       --      --    
  35  GPUPV_PRESENT_HWQUEUE                             Unknown  --       --      --    
  36  GPUVAIOMMU                                        Unknown  --       --      --    
  37  NATIVE_FENCE                                      No       0        No      No    
```

## Sample Implementation

For ease of support, a barebones sample implementation follows. Drivers can use this code as a starting point for their own implementation, and expand with additional features as necessary (for example, hooking up ways to override capabilities).

``` cpp

#include "precomp.h"

#pragma code_seg("PAGE")

#define VERSION_RANGE(Min, Max) Min, Max
#define DEFINE_FEATURE_INTERFACE(Name, Version, InterfaceStruct) InterfaceStruct Name##_Interface_##Version =
#define DEFINE_FEATURE_INTERFACE_TABLE(Name) const DRIVER_FEATURE_INTERFACE_TABLE_ENTRY Name##_InterfaceTable[] =
#define FEATURE_INTERFACE_ENTRY(Name, Version) { &Name##_Interface_##Version, sizeof(Name##_Interface_##Version) }
#define NO_FEATURE_INTERFACE { nullptr, 0 }
#define FEATURE_INTERFACE(Name, Version) { &Name##_Interface_##Version, sizeof(Name##_Interface_##Version) }
#define FEATURE_INTERFACE_TABLE(Name) { Name##_InterfaceTable, ARRAYSIZE(Name##_InterfaceTable) }
#define NO_FEATURE_INTERFACE_TABLE { nullptr, 0 }

struct DRIVER_FEATURE_INTERFACE_TABLE_ENTRY
{
    const void* Interface;
    SIZE_T InterfaceSize;
};

struct DRIVER_FEATURE_INTERFACE_TABLE
{
    const DRIVER_FEATURE_INTERFACE_TABLE_ENTRY* Entries;
    SIZE_T Count;
};

//
// Interfaces
//

DEFINE_FEATURE_INTERFACE(FEATURE_SAMPLE, 4, DXGKDDIINT_FEATURE_SAMPLE_4)
{
    DdiFeatureSample_AddValue,
};

DEFINE_FEATURE_INTERFACE(FEATURE_SAMPLE, 5, DXGKDDIINT_FEATURE_SAMPLE_5)
{
    DdiFeatureSample_AddValue,
    DdiFeatureSample_SubtractValue,
};

DEFINE_FEATURE_INTERFACE_TABLE(FEATURE_SAMPLE)
{
    NO_FEATURE_INTERFACE,                 // Version 3
    FEATURE_INTERFACE(FEATURE_SAMPLE, 4), // Version 4
    FEATURE_INTERFACE(FEATURE_SAMPLE, 5), // Version 5
};

static const DRIVER_FEATURE_INTERFACE_TABLE g_FeatureInterfaceTables[] =
{
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_HWSCH
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_HWFLIPQUEUE
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_LDA_GPUPV
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_KMD_SIGNAL_CPU_EVENT
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_USER_MODE_SUBMISSION
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_SHARE_BACKING_STORE_WITH_KMD
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved 
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    NO_FEATURE_INTERFACE_TABLE,              // Reserved
    FEATURE_INTERFACE_TABLE(FEATURE_SAMPLE), // DXGK_FEATURE_SAMPLE
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_PAGE_BASED_MEMORY_MANAGER
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_KERNEL_MODE_TESTING
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_64K_PT_DEMOTION_FIX
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_GPUPV_PRESENT_HWQUEUE
    NO_FEATURE_INTERFACE_TABLE,              // DXGK_FEATURE_NATIVE_FENCE
};
static_assert(ARRAYSIZE(g_FeatureInterfaceTables) == DXGK_FEATURE_MAX, "New feature must define an interface table");

#define VERSION_RANGE(Min, Max) Min, Max

//
// TODO: This table may be defined independently for each supported hardware or architecture,
// or may be completely overriden dynamically at runtime during DRIVER_ADAPTER::InitializeFeatureConfiguration
//
static const DRIVER_FEATURE_DESC g_FeatureDefaults[] =
{
//                                      SupportedOnConfig
//    VersionRange           Supported  |       Experimental  
//    |                      |          |       |
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_HWSCH
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_HWFLIPQUEUE
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_LDA_GPUPV
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_KMD_SIGNAL_CPU_EVENT
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_USER_MODE_SUBMISSION
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_SHARE_BACKING_STORE_WITH_KMD
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved 
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // Reserved
    { VERSION_RANGE(3, 5), { TRUE,      TRUE,   FALSE,   }, }, // DXGK_FEATURE_TEST_FEATURE_SAMPLE
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_PAGE_BASED_MEMORY_MANAGER
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_KERNEL_MODE_TESTING
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_64K_PT_DEMOTION_FIX
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_GPUPV_PRESENT_HWQUEUE
    { VERSION_RANGE(0, 0), { FALSE,     FALSE,  FALSE,   }, }, // DXGK_FEATURE_NATIVE_FENCE
};
static_assert(ARRAYSIZE(g_FeatureDefaults) == DXGK_FEATURE_MAX, "New feature requires a descriptor");

const DRIVER_FEATURE_DESC*
DRIVER_ADAPTER::GetFeatureDesc(
    DXGK_FEATURE_ID FeatureId
    ) const
{
    PAGED_CODE();

    if(FeatureId >= DXGK_FEATURE_MAX)
    {
        return nullptr;
    }

    return &m_FeatureDescs[FeatureId];
}

void
DRIVER_ADAPTER::InitializeFeatureConfiguration(
    )
{
    //
    // Choose correct default table to use here, or override manually below
    //
    static_assert(sizeof(DRIVER_ADAPTER::m_FeatureDescs) == sizeof(g_FeatureDefaults));
    memcpy(m_FeatureDescs, g_FeatureDefaults, sizeof(g_FeatureDefaults));
    
    //
    // Example overrides
    //

    //
    // While this is a sample feature and not tied to any architectural support, this is
    // an example of how a feature can be marked as supported by the driver in the table
    // above, and then dynamically enabled on this configuration here.
    //
    // The same can be done for hardware features, such as hardware scheduling
    //
    if(IsSampleFeatureSupportedOnThisGPU())
    {
        m_FeatureDescs[DXGK_FEATURE_TEST_FEATURE_SAMPLE].SupportedOnConfig = TRUE;
    }
}

NTSTATUS
DdiQueryFeatureSupport(
    IN_CONST_HANDLE                    hAdapter,
    INOUT_PDXGKARG_QUERYFEATURESUPPORT pArgs
    )
{
    PAGED_CODE();

    //
    // Start by assuming the feature is unsupported
    //
    pArgs->SupportedByDriver = FALSE;
    pArgs->SupportedOnCurrentConfig = FALSE;
    pArgs->MinSupportedVersion = 0;
    pArgs->MaxSupportedVersion = 0;

    DRIVER_ADAPTER* pAdapter = GetAdapterFromHandle(hAdapter);

    const DRIVER_FEATURE_DESC* pFeatureDesc = pAdapter->GetFeatureDesc(pArgs->FeatureId);

    if(pFeatureDesc == nullptr)
    {
        //
        // Unknown feature
        //
        return STATUS_INVALID_PARAMETER;
    }

    if(pFeatureDesc->Supported)
    {
        if(pFeatureDesc->Experimental == FALSE ||
           pArgs->AllowExperimental)
        {
            pArgs->SupportedByDriver = TRUE;
            pArgs->SupportedOnCurrentConfig = pFeatureDesc->SupportedOnConfig;

            pArgs->MinSupportedVersion = pFeatureDesc->MinSupportedVersion;
            pArgs->MaxSupportedVersion = pFeatureDesc->MaxSupportedVersion;
        }
    }

    return STATUS_SUCCESS;
}

NTSTATUS
DdiQueryFeatureInterface(
    IN_CONST_HANDLE                      hAdapter,
    INOUT_PDXGKARG_QUERYFEATUREINTERFACE pArgs
    )
{
    PAGED_CODE();

    DRIVER_ADAPTER* pAdapter = GetAdapterFromHandle(hAdapter);

    UINT16 InterfaceSize = pArgs->InterfaceSize;
    pArgs->InterfaceSize = 0;

    const DRIVER_FEATURE_DESC* pFeatureDesc = pAdapter->GetFeatureDesc(pArgs->FeatureId);

    if(pFeatureDesc == nullptr)
    {
        //
        // Unknown feature
        //
        return STATUS_INVALID_PARAMETER;
    }

    if(pFeatureDesc->Supported == FALSE)
    {
        //
        // Cannot query a feature interface for an unsupported feature.
        //
        return STATUS_UNSUCCESSFUL;
    }

    if(pArgs->Version < pFeatureDesc->MinSupportedVersion ||
       pArgs->Version > pFeatureDesc->MaxSupportedVersion)
    {
        //
        // Invalid feature version.
        //
        return STATUS_UNSUCCESSFUL;
    }

    const DRIVER_FEATURE_INTERFACE_TABLE* pInterfaceTable = &g_FeatureInterfaceTables[pArgs->FeatureId];
    if(pInterfaceTable->Entries == nullptr)
    {
        //
        // This feature does not have any interfaces. It's unclear why the driver is asking for it,
        // but the size should be zero and we will not return any data for it.
        //
        return STATUS_SUCCESS;
    }

    if((SIZE_T)(pArgs->Version - pFeatureDesc->MinSupportedVersion) >= pInterfaceTable->Count)
    {
        //
        // The interface table should have an entry for every supported version. This is
        // a bug in the OS, and the feature interface table must be updated for this feature!
        //
        NT_ASSERT(FALSE);

        //
        // Invalid feature version.
        //
        return STATUS_UNSUCCESSFUL;
    }

    UINT32 InterfaceTableIndex = pArgs->Version - pFeatureDesc->MinSupportedVersion;
    const DRIVER_FEATURE_INTERFACE_TABLE_ENTRY* pInterfaceEntry = &pInterfaceTable->Entries[InterfaceTableIndex];
    if(pInterfaceEntry->Interface == nullptr)
    {
        //
        // This feature does not have any interfaces. It's unclear why the OS is asking for one.
        //
        return STATUS_INVALID_PARAMETER;
    }

    if(InterfaceSize < pInterfaceEntry->InterfaceSize)
    {
        //
        // The driver-provided buffer is too small to store the interface for this feature and version
        //
        return STATUS_BUFFER_TOO_SMALL;
    }

    //
    // We have an interface!
    //
    RtlCopyMemory(pArgs->Interface, pInterfaceEntry->Interface, pInterfaceEntry->InterfaceSize);
    if(InterfaceSize != pInterfaceEntry->InterfaceSize)
    {
        //
        // Zero out remainder of interface in case the provided buffer was larger than
        // the actual interface. This may be done in cases where multiple interface versions
        // are supported simultaneously (e.g. in a unioned structure). Only the requested
        // interface should be valid.
        //
        RtlZeroMemory((BYTE*)pArgs->Interface + pInterfaceEntry->InterfaceSize, InterfaceSize - pInterfaceEntry->InterfaceSize);
    }

    //
    // Write back the interface size
    //
    pArgs->InterfaceSize = (UINT16)pInterfaceEntry->InterfaceSize;

    return STATUS_SUCCESS;
}

static void DdiReferenceFeatureInterfaceNop(PVOID pMiniportDeviceContext)
{
    PAGED_CODE();
}

//
// DRIVER_INITIALIZATION_DATA::DxgkDdiQueryInterface
//
NTSTATUS
DdiQueryInterface(
    IN_CONST_PVOID          pMiniportDeviceContext,
    IN_PQUERY_INTERFACE     pQueryInterface
    )
{
    DDI_FUNCTION();

    PAGED_CODE();

    if(pQueryInterface->Version == DXGK_FEATURE_INTERFACE_VERSION_1)
    {
        PDXGKDDI_FEATURE_INTERFACE Interface = (PDXGKDDI_FEATURE_INTERFACE)pQueryInterface->Interface;

        Interface->Version = DXGK_FEATURE_INTERFACE_VERSION_1;
        Interface->Context = pMiniportDeviceContext;
        Interface->Size = sizeof(DXGKDDI_FEATURE_INTERFACE);

        //
        // Returned interface shouldn't be larger than size provided for Interface
        //
        if (Interface->Size > pQueryInterface->Size)
        {
            return STATUS_BUFFER_TOO_SMALL;
        }

        Interface->InterfaceReference = DdiReferenceFeatureInterfaceNop;
        Interface->InterfaceDereference = DdiReferenceFeatureInterfaceNop;

        Interface->QueryFeatureSupport = DdiQueryFeatureSupport;
        Interface->QueryFeatureInterface = DdiQueryFeatureInterface;

        return STATUS_SUCCESS;
    }
    else
    {
        return STATUS_INVALID_PARAMETER;
    }
}

//
// These two functions act as hooks for when the OS doesn't support the feature functionality.
// If DxgkInterface.DxgkCbQueryServices(DxgkServicesFeature) returns a failure, it may mean
// we're running on an older OS, and we can fake the interface implementation using these
// functions instead.
//
// See DdiStartDevice sample code for how this is used
//
NTSTATUS
LegacyIsFeatureEnabled(
    IN_CONST_PVOID                     hDevice,
    INOUT_PDXGKARGCB_ISFEATUREENABLED2 pArgs
    )
{
    PAGED_CODE();

    DRIVER_ADAPTER* pAdapter = GetAdapterFromHandle(hAdapter);

    pArgs->Result = {};

    if (pAdapter->m_WddmVersion >= DXGKDDI_WDDMv2_9 &&
        pAdapter->m_DxgkInterface.Version >= DXGKDDI_INTERFACE_VERSION_WDDM2_9)
    {
        //
        // QueryFeatureSupport should be available.
        //
        DXGKARGCB_QUERYFEATURESUPPORT Args = {};
        Args.DeviceHandle = pAdapter->m_DxgkInterface.DeviceHandle;
        Args.FeatureId = pArgs->FeatureId;

        //
        // Example experimental status
        //

        /*
        switch(pArgs->FeatureId)
        {
            case DXGK_FEATURE_HWFLIPQUEUE:
            {
                Args.DriverSupportState = DXGK_FEATURE_SUPPORT_EXPERIMENTAL;
                break;
            }

            default:
            {
                Args.DriverSupportState = DXGK_FEATURE_SUPPORT_STABLE;
                break;
            }
        }
        */

        NTSTATUS Status = pAdapter->m_DxgkInterface.DxgkCbQueryFeatureSupport(&Args);
        if(NT_SUCCESS(Status))
        {
            if(Args.Enabled)
            {
                pArgs->Result.Enabled = Args.Enabled;
                pArgs->Result.Version = 1;
                pArgs->Result.SupportedByDriver = TRUE;
                pArgs->Result.SupportedOnCurrentConfig = TRUE;
            }
        }

        return Status;
    }
    else
    {
        return STATUS_NOT_SUPPORTED;
    }
}

//
// Sample code for DdiStartDevice
//
NTSTATUS
DdiStartDevice(
    IN_CONST_PVOID          pMiniportDeviceContext,
    IN_PDXGK_START_INFO     pDxgkStartInfo,
    IN_PDXGKRNL_INTERFACE   pDxgkInterface,
    OUT_PULONG              pNumberOfVideoPresentSources,
    OUT_PULONG              pNumberOfChildren
    )
{
    DRIVER_ADAPTER* pAdapter = GetAdapterFromHandle(hAdapter);

    ...

    //
    // Check fi the OS supports the feature interface.
    //
    pAdapter->m_FeatureInterface.Size = sizeof(pAdapter->m_FeatureInterface);
    pAdapter->m_FeatureInterface.Version = DXGK_FEATURE_INTERFACE_VERSION_1;

    Status = pAdapter->m_DxgkInterface.DxgkCbQueryServices(pAdapter->m_DxgkInterface.DeviceHandle, DxgkServicesFeature, (PINTERFACE)&pAdapter->m_FeatureInterface);

    if(!NT_SUCCESS(Status))
    {
        //
        // OS interface unavailable. This forwards calls to the Legacy functions defined above
        // when not available, which hard codes support for the handful of existing features
        // at the time (optionally going through DxgkCbQueryFeatureSupport).
        //
        // Doing this is optional, but may keep the driver code cleaner.
        //

        pAdapter->m_FeatureInterface.Context = pAdapter;
        pAdapter->m_FeatureInterface.InterfaceReference = nullptr;
        pAdapter->m_FeatureInterface.InterfaceDereference = nullptr;

        //
        // Use legacy function above.
        //
        pAdapter->m_FeatureInterface.IsFeatureEnabled = LegacyIsFeatureEnabled;

        //
        // QueryFeatureInterface is only used by the OS to query an interface for a feature,
        // but the OS doesn't support this. Any attempt to call this function implies
        // the driver is calling it themselves, which makes no sense.
        //
        pAdapter->m_FeatureInterface.QueryFeatureInterface = nullptr;

        Status = STATUS_SUCCESS;
    }
    
    Status = pAdapter->InitializeFeatureConfiguration();

    if(!NT_SUCCESS(Status))
    {
        goto cleanup;
    }

    ...
}

DRIVER_FEATURE_RESULT
DRIVER_ADAPTER::IsFeatureEnabled(
    DXGK_FEATURE_ID FeatureId
    )
{
    PAGED_CODE();

    DRIVER_FEATURE_RESULT Result = {};

    DXGKARGCB_ISFEATUREENABLED2 Args = {};
    Args.FeatureId = FeatureId;

    //
    // Will either call the OS, or the LegacyIsFeatureEnabled function above
    // depending on whether this is supported on the OS. 
    //
    if(NT_SUCCESS(FeatureInterface.IsFeatureEnabled(DxgkInterface.DeviceHandle, &Args)))
    {
        Result.Enabled = Args.Result.Enabled;
        Result.Version = Args.Result.Version;
    }

    return Result;
}
```

The following code implements the interfaces for the **FEATURE_SAMPLE** feature.

``` cpp
//
// This file implements the interfaces for the FEATURE_SAMPLE feature
//

#include "precomp.h"

//
// The OS supports 3 versions of the feature: 3, 4, and 5.
//
// - v3 has no interface
// - v4 has an interface that defines an "Add" function
// - v5 has an interface that defines both "Add" and "Subtract" functions
//
NTSTATUS
APIENTRY CALLBACK
DdiFeatureSample_AddValue(
    IN_CONST_HANDLE hAdapter,
    INOUT_PDXGKARG_FEATURE_SAMPLE_ADDVALUE pArgs
    )
{
    PAGED_CODE();

    DRIVER_ADAPTER* pAdapter = GetAdapterFromHandle(hAdapter);

    if(pAdapter->m_FeatureState.SampleFeatureVersion < 4)
    {
        //
        // Unexpected. This function should only be called for v4 and above of this feature
        //
        return STATUS_INVALID_PARAMETER;
    }

    DXGKARGCB_FEATURE_SAMPLE_GETVALUE GetValueArgs = {};

    NTSTATUS Status = pAdapter->m_FeatureState.SampleFeatureInterface.GetValue(pAdapter->m_DxgkInterface.DeviceHandle, &GetValueArgs);

    if(!NT_SUCCESS(Status))
    {
        return Status;
    }

    pArgs->OutputValue = pArgs->InputValue + GetValueArgs.Value;

    return STATUS_SUCCESS;
}

NTSTATUS
APIENTRY CALLBACK
DdiFeatureSample_SubtractValue(
    IN_CONST_HANDLE hAdapter,
    INOUT_PDXGKARG_FEATURE_SAMPLE_SUBTRACTVALUE pArgs
    )
{
    PAGED_CODE();

    DRIVER_ADAPTER* pAdapter = GetAdapterFromHandle(hAdapter);

    if(pAdapter->m_FeatureState.SampleFeatureVersion < 5)
    {
        //
        // Unexpected. This function should only be called for v5 and above of this feature
        //
        return STATUS_INVALID_PARAMETER;
    }

    DXGKARGCB_FEATURE_SAMPLE_GETVALUE GetValueArgs = {};

    NTSTATUS Status = pAdapter->m_FeatureState.SampleFeatureInterface.GetValue(pAdapter->m_DxgkInterface.DeviceHandle, &GetValueArgs);
    
    if(!NT_SUCCESS(Status))
    {
        return Status;
    }

    pArgs->OutputValue = pArgs->InputValue - GetValueArgs.Value;

    return STATUS_SUCCESS;
}
```
