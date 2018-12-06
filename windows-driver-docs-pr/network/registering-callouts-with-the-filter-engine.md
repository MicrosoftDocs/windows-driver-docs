---
title: Registering Callouts with the Filter Engine
description: Registering Callouts with the Filter Engine
ms.assetid: a5bade33-e3d1-4e1d-8503-51485097046e
keywords:
- Windows Filtering Platform callout drivers WDK , initializing
- callout drivers WDK Windows Filtering Platform , initializing
- initializing callout drivers WDK Windows Filtering Platform
- registering callouts WDK Windows Filtering Platform
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Callouts with the Filter Engine


After a callout driver has created a device object, it can then register its callouts with the filter engine. A callout driver can register its callouts with the filter engine at any time, even if the filter engine is currently not running. To register a callout with the filter engine, a callout driver calls the [**FwpsCalloutRegister0**](https://msdn.microsoft.com/library/windows/hardware/ff551140) function. For example:

```C++
// Prototypes for the callout's callout functions
VOID NTAPI
 ClassifyFn(
    IN const FWPS_INCOMING_VALUES0  *inFixedValues,
    IN const FWPS_INCOMING_METADATA_VALUES0  *inMetaValues,
    IN OUT VOID  *layerData,
    IN const FWPS_FILTER0  *filter,
    IN UINT64  flowContext,
    IN OUT FWPS_CLASSIFY_OUT0  *classifyOut
    );

NTSTATUS NTAPI
 NotifyFn(
 IN FWPS_CALLOUT_NOTIFY_TYPE notifyType,
    IN const GUID  *filterKey,
    IN const FWPS_FILTER0  *filter
    );

VOID NTAPI
 FlowDeleteFn(
    IN UINT16  layerId,
    IN UINT32  calloutId,
    IN UINT64  flowContext
    );

// Callout registration structure
const FWPS_CALLOUT0 Callout =
{
 { ... }, // GUID key identifying the callout
  0,       // Callout-specific flags (none set here)
 ClassifyFn,
 NotifyFn,
 FlowDeleteFn
};

// Variable for the run-time callout identifier
UINT32 CalloutId;

NTSTATUS
 DriverEntry(
    IN PDRIVER_OBJECT DriverObject,
    IN PUNICODE_STRING RegistryPath
    )
{
  PDEVICE_OBJECT deviceObject;
  NTSTATUS status;

  ...

 status =
 FwpsCalloutRegister0(
 deviceObject,
      &Callout,
      &CalloutId
      );

  ...

 return status;
}
```

If the call to the [**FwpsCalloutRegister0**](https://msdn.microsoft.com/library/windows/hardware/ff551140) function is successful, the variable pointed to by the last parameter contains the run-time identifier for the callout. This run-time identifier corresponds to the GUID that was specified for the callout key.

A single callout driver can implement more than one callout. If a callout driver implements more than one callout, it calls the [**FwpsCalloutRegister0**](https://msdn.microsoft.com/library/windows/hardware/ff551140) function one time for each callout that it supports to register each callout with the filter engine.

## Related topics


[classifyFn](https://msdn.microsoft.com/library/windows/hardware/ff544887)

 

 






