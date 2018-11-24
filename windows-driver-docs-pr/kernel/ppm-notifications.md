---
title: Processor power management (PPM) notifications
description: Each processor power management (PPM) notification that the PEP's AcceptProcessorNotification callback routine receives is accompanied by a Notification parameter that indicates the type of notification, and a Data parameter that points to a data structure that contains the information for the specified notification type.
ms.assetid: 4BA89D0F-78F0-44DF-BC9B-0F9F3256CD59
keywords: [AcceptProcessorNotification callback]
ms.date: 01/17/2018
ms.localizationpriority: medium
---

# Processor power management (PPM) notifications
Each processor power management (PPM) notification that the PEP's AcceptProcessorNotification callback routine receives is accompanied by a Notification parameter that indicates the type of notification, and a Data parameter that points to a data structure that contains the information for the specified notification type.

In this call, the Notification parameter is set to a PEP_NOTIFY_PPM_XXX constant value that indicates the notification type. The Data parameter points to a PEP_PPM_XXX structure type that is associated with this notification type.

The following processor power management (PPM) notification IDs are used by the AcceptProcessorNotification callback routine.

## PEP_NOTIFY_PPM_QUERY_CAPABILITIES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_CAPABILITIES.

Data
A pointer to a PEP_PPM_QUERY_CAPABILITIES structure.
 informs the PEP that it is being queried for the power management capabilities of the PEP.

The Windows power management framework (PoFx) sends this notification when the PEP is queried for its power management capabilities. This happens at processor initialization time and will be sent for each processor in the system.

Platforms with x86/AMD64 processors must use ACPI interfaces for processor performance control.

To send a PEP_NOTIFY_PPM_QUERY_CAPABILITIES notification, PoFx calls the PEP's AcceptProcessorNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_PPM_QUERY_CAPABILITIES, and the Data parameter points to a PEP_PPM_QUERY_CAPABILITIES structure.

For a PEP_NOTIFY_PPM_QUERY_CAPABILITIES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_IDLE_STATES 
Notification
The value PEP_NOTIFY_PPM_QUERY_IDLE_STATES.

Data
A pointer to a PEP_PPM_QUERY_IDLE_STATES structure.
 Informs the PEP about idle states.

To send a PEP_NOTIFY_PPM_QUERY_IDLE_STATES notification, PoFx calls the PEP's AcceptProcessorNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_PPM_QUERY_IDLE_STATES, and the Data parameter points to a PEP_PPM_QUERY_IDLE_STATES structure.

For a PEP_NOTIFY_PPM_QUERY_IDLE_STATES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_IDLE_SELECT 
Notification
The value PEP_NOTIFY_PPM_IDLE_SELECT.

Data
A pointer to a PEP_PPM_IDLE_SELECT structure.
 Informs the PEP of idle select.

To send a PEP_NOTIFY_PPM_IDLE_SELECT notification, PoFx calls the PEP's AcceptProcessorNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_PPM_IDLE_SELECT, and the Data parameter points to a PEP_PPM_IDLE_SELECT structure.

For a PEP_NOTIFY_PPM_IDLE_SELECT notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_IDLE_CANCEL 
Notification
The value PEP_NOTIFY_PPM_IDLE_CANCEL.

Data
A pointer to a PEP_PPM_IDLE_CANCEL structure.
 Informs the PEP of a cancel action.

To send a PEP_NOTIFY_PPM_IDLE_CANCEL notification, PoFx calls the PEP's AcceptProcessorNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_PPM_IDLE_CANCEL, and the Data parameter points to a PEP_PPM_IDLE_CANCEL structure.

For a PEP_NOTIFY_PPM_IDLE_CANCEL notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_IDLE_EXECUTE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_IDLE_EXECUTE.

Data
A pointer to a PEP_PPM_IDLE_EXECUTE or PEP_PPM_IDLE_EXECUTE_V2 structure.
 Sent to the PEP to transition the current processor to the specified idle state.

The Windows power management framework (PoFx) sends this notification to the PEP to transition the current processor to the specified idle state. 

The PEP can prepare the hardware to enter the previously selected idle state, including notifying the OS of core system resources which may be affected by the sleep transition. Then it must execute the halt instruction to transition the processor to the idle state. Upon return from the idle state, the PEP must undo the hardware setup, including notifying the OS of core system resources which may have become active upon wake. If the PEP is unable to execute the processor (and platform) idle state, then it must return back an error status.

When using the coordinated idle state interface, the OS uses the PEP_PPM_IDLE_EXECUTE_V2 structure which includes the CoordinatedStateCount and CoordinatedState fields with the list of coordinated idle states that will be entered by the idle transition. The PlatformState field will specify the deepest platform coordinated idle state that's being entered, if any. 

When not using the coordinated idle state interface, the OS uses the PEP_PPM_IDLE_EXECUTE structure. 

For a PEP_NOTIFY_PPM_IDLE_EXECUTE notification, the AcceptProcessorNotification routine is called with interrupts disabled.
 
## PEP_NOTIFY_PPM_IDLE_COMPLETE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. 

Notification
The value PEP_NOTIFY_PPM_IDLE_COMPLETE.

Data
A pointer to a PEP_PPM_IDLE_COMPLETE or PEP_PPM_IDLE_COMPLETE_V2 structure..
 Informs the PEP that the current processor is waking up from a completed idle transition.

The Windows power management framework (PoFx) sends this notification when the current processor is waking up from a completed idle transition. If the platform was executing a platform idle transition, the first processor to wake will indicate the platform idle state that is being exited. Depending on the type of synchronization used in the platform idle transition, the first processor to wake from a platform idle state may not be the processor that entered the platform idle state. 

If the processor was executing a deep idle state, the PEP must not wait until it receives the complete notification to restore core context or notify the OS that core resources have been restored. The OS expects these resources to have been restored once the execute notification has completed. When the hypervisor is enabled, the PEP will only receive this notification upon exit from a platform idle state, and with the ProcessorState field set to PEP_PROCESSOR_IDLE_STATE_UNKNOWN. 

When using the coordinated idle state interface, the OS uses the PEP_PPM_IDLE_COMPLETE_V2 structure which includes the CoordinatedStateCount and CoordinatedState fields with the list of coordinated idle states that will be exited by the idle transition. The PlatformState field will specify the deepest platform coordinated idle state that's being exited, if any. Note that the set of coordinated idle states exited by this processor may be different from the set of coordinated idle states entered by it, if loose synchronization is used. 

When not using the coordinated idle state interface, the OS uses the PEP_PPM_IDLE_COMPLETE structure. 

For a PEP_NOTIFY_PPM_IDLE_COMPLETE notification, the AcceptProcessorNotification routine is called with interrupts disabled and is always executed on the target processor.
 
## PEP_NOTIFY_PPM_IS_PROCESSOR_HALTED 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_IS_PROCESSOR_HALTED.

Data
A pointer to a PEP_PPM_IS_PROCESSOR_HALTED structure.
 Sent to the PEP to determine if the specified processor is currently halted in its selected idle state.

The Windows power management framework (PoFx) sends this notification to the PEP to determine if the specified processor is currently halted in its selected idle state. The OS will use this notification to check if a secondary processor has fully completed the transition to idle when coordinating platform idle states. The PEP must guarantee the target processor has reached a state in which the platform idle transition can safely occur (e.g., by checking hardware registers to see if the core is halted). Once this notification indicates the processor is in an idle state, that processor must not wake up unless the OS explicitly requests it to do so. 

The PEP may receive this notification any time between the IDLE_SELECT and IDLE_COMPLETE notifications. It is guaranteed to receive this notification at most once during an idle transition. 

For a PEP_NOTIFY_PPM_IS_PROCESSOR_HALTED notification, the AcceptProcessorNotification routine is called at any IRQL and with interrupts disabled, at any IRQL, and is never executed on the target processor.

<= HIGH_LEVEL
 
## PEP_NOTIFY_PPM_INITIATE_WAKE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor.

Notification
The value PEP_NOTIFY_PPM_INITIATE_WAKE.

Data
A pointer to a structure.
 Sent to the PEP for a specified processor to initiate its wake up from a non-interruptible idle state.

The Windows power management framework (PoFx) sends this notification to the PEP for a specified processor to initiate its wake up from a non-interruptible idle state. The PEP must return the status of wake for the target processor using NeedInterruptForCompletion. It returns TRUE if the processor requires an interrupt to finish waking up from the idle state. In this case the PEP must ensure the target processor is interruptible upon return from handling this notification. If the target processor is already running and/or will eventually exit the idle state (and is in the process of doing so) without requiring any software generated interrupt, NeedInterruptForCompletion should be set to FALSE.


Note  The PEP will not receive this notification for the same processor concurrently.
 

For a PEP_NOTIFY_PPM_INITIATE_WAKE notification, the AcceptProcessorNotification routine is called at any IRQL, with interrupts disabled, and is never executed on the target processor.

<= HIGH_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_FEEDBACK_COUNTERS 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_FEEDBACK_COUNTERS.

Data
A pointer to a PEP_PPM_QUERY_FEEDBACK_COUNTERS structure.
 Informs the PEP that the PEP is being queried for the list of feedback counters that it supports.

The Windows power management framework (PoFx) sends this notification at processor initialization to query the PEP for the list of feedback counters that it supports.

For a PEP_NOTIFY_PPM_QUERY_FEEDBACK_COUNTERS notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_FEEDBACK_READ 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_FEEDBACK_READ.

Data
A pointer to a PEP_PPM_FEEDBACK_READ structure.
 Informs the PEP that it is being queried for a feedback counter's current value.

The Windows power management framework (PoFx) sends this notification when it wants to query a feedback counter's current value. 

This notification may be sent with interrupts disabled. If the counter's Affinitized field is set, this notification is executed on the target processor. Otherwise, this notification may be executed from any processor.

For a PEP_NOTIFY_PPM_FEEDBACK_READ notification, the AcceptProcessorNotification routine may be called at IRQL = DISPATCH_LEVEL.

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES.

Data
A pointer to a PEP_PPM_QUERY_PERF_CAPABILITIES structure.
 Informs the PEP that it is being queried for the performance ranges supported by the platform.

The Windows power management framework (PoFx) sends this notification at processor initialization to query the performance ranges supported by the platform. The DomainId and DomainMembers fields of the PEP_PPM_QUERY_PERF_CAPABILITIES structure are used to express performance state domains to the platform. Each processor is a member of exactly one performance state domain. The operating system will ensure that all processors in a performance domain change performance together. 

For a PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_PERF_CONSTRAINTS 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. 

Notification
The value PEP_NOTIFY_PPM_PERF_CONSTRAINTS.

Data
A pointer to a PEP_PPM_PERF_CONSTRAINTS structure.
 Informs the PEP that it is being queried for the current operating constraints of the processor.

The Windows power management framework (PoFx) sends this notification when it wants to inspect the current operating constraints of the processor. The PEP initiates a request for the OS to re-evaluate the perf constraints of the processor by executing a power control with the control code GUID_PPM_PERF_CONSTRAINT_CHANGE. The InBuffer and OutBuffer must be NULL. 

The PEP must wait until it receives a PEP_DPM_DEVICE_STARTED notification for a processor before it issues a power control transaction for the processor. 

For a PEP_NOTIFY_PPM_PERF_CONSTRAINTS notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_PERF_SET 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_PERF_SET.

Data
A pointer to a PEP_PPM_PERF_SET structure.
 Informs the PEP that the current operating performance of the processor should be changed.

The Windows power management framework (PoFx) sends this notification when it wants to change the current operating performance of the processor. This notification may be sent while executing on any processor.

For a PEP_NOTIFY_PPM_PERF_SET notification, the AcceptProcessorNotification routine is always called at IRQL = DISPATCH_LEVEL.

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_PARK_SELECTION 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_PARK_SELECTION.

Data
A pointer to a PEP_PPM_PARK_SELECTION structure.
 Informs the PEP that the OS would like it to select a preferred set of processor cores to park.

The Windows power management framework (PoFx) sends this notification to instruct the PEP to select a preferred set of cores to park.

The PEP_NOTIFY_PPM_PARK_SELECTION has been overloaded to perform two functions: 

Let the PEP select which processors (from the set of all processors in the system) should be parked, and which should be unparked. 
Let the PEP select which processors (from the set of all processors that are unparked) should receive interrupts, and which should not receive interrupts. 
Windows does not provide a means for the PEP to distinguish which of the two the OS is performing. As a result, when the PEP receives this notification with a given set of inputs (AdditionalUnparkedProcessors count and PoPreference), it should provide a consistent output (PepPreference) unless some external event causes a change in PEP preference. 

For a PEP_NOTIFY_PPM_PARK_SELECTION notification, the AcceptProcessorNotification routine is always called at IRQL = DISPATCH_LEVEL.

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_CST_STATES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_CST_STATES.

Data
A pointer to a PEP_PPM_CST_STATES structure.
 sent to the PEP to indicate the set of ACPI-defined C-states supported by the processor. 

The Windows power management framework (PoFx) sends this notification to the PEP to indicate the set of ACPI-defined C-states supported by the processor. This notification will be sent once before the first time the PEP receives PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2 notification for a processor, and again any time that processor receives a Notify(0x81) indicating the _CST object has changed.

For a PEP_NOTIFY_PPM_CST_STATES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES.

Data
A pointer to a PEP_PPM_QUERY_PLATFORM_STATES structure.
 Sent at processor initialization to query the number of platform idle states that the PEP supports.

The Windows power management framework (PoFx) sends this notification to the PEP at processor initialization to query the number of platform idle states that it supports. This notification is sent once upon boot. After returning a non-zero number of platform states, the PEP can then begin to select platform idle states during processor idle transitions.

For a PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_LP_SETTINGS 
Notification
The value PEP_NOTIFY_PPM_QUERY_LP_SETTINGS.

Data
A pointer to a PEP_PPM_QUERY_LP_SETTINGS structure.
 To send a PEP_NOTIFY_PPM_QUERY_LP_SETTINGS notification, PoFx calls the PEP's AcceptProcessorNotification callback routine. In this call, the Notification parameter value is PEP_NOTIFY_PPM_QUERY_LP_SETTINGS, and the Data parameter points to a PEP_PPM_QUERY_LP_SETTINGS structure.

For a PEP_NOTIFY_PPM_QUERY_LP_SETTINGS notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2.

Data
A pointer to a PEP_PPM_QUERY_IDLE_STATES_V2 structure.
 Used at processor initialization to query the list of idle states that the PEP supports.

The Windows power management framework (PoFx) sends this notification to the PEP at processor initialization to query the list of idle states that it supports. 

The Count member specifies the size of the idle state array. The processor driver will query for the number of idle states with PEP_NOTIFY_PPM_QUERY_CAPABILITIES before sending this notification. 

The PEP fills in the IdleStates array with information about each idle state that it supports. The idle states should be listed in order of decreasing power consumption/increasing transition cost. The PEP is not required to report the same list of idle states for each processor. 

For a PEP_NOTIFY_PPM_QUERY_IDLE_STATES_V2 notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE.

Data
A pointer to a PEP_PPM_QUERY_PLATFORM_STATE structure.
 Sent to the PEP to query the properties of a single platform idle state.

The Windows power management framework (PoFx) sends this notification at processor initialization to query the properties of a single platform idle state. 

The StateIndex parameter of the PEP_PPM_QUERY_PLATFORM_STATE structure specifies the index of the platform idle state being queried. The processor driver will query for the number of supported platform idle states with PEP_NOTIFY_PPM_QUERY_PLATFORM_STATES before sending this notification. The processor driver will then send one PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE notification for each platform idle state. The processor driver will wait to send this notification until after all processors have registered with the PEP. 

The PEP fills in State structure with information about the platform idle state. Platform idle states should be listed in order of decreasing power consumption/increasing transition cost. 

For a PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_TEST_IDLE_STATE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_TEST_IDLE_STATE.

Data
A pointer to a PEP_PPM_TEST_IDLE_STATE structure.
 Used to test whether the specified processor and platform idle state can be entered on the specified processor.

The Windows power management framework (PoFx) sends this notification to test whether the specified processor and platform idle state can be entered on the specified processor. If the idle state can be entered, the PEP fills in veto code PEP_IDLE_VETO_NONE and completes the idle transition. If the idle transition cannot be completed for some reason, the PEP fills in a non-zero veto code. 

Important  Veto codes in the range 0x80000000 to 0xffffffff are reserved for OS use and may not be used.
 

When this notification is sent, the OS has already validated that all constraints associated with the selected processor or platform idle state have been met, including device and processor constraints for a platform idle transition. 

This notification will be sent before the OS attempts to enter any processor or platform idle state, except for the processor idle state with index 0, which must always be enterable. Completing this notification with PEP_IDLE_VETO_NONE does not guarantee that the OS will enter the indicated idle state. This notification is sent with interrupts disabled. This notification is always executed on the target processor. 

For a PEP_NOTIFY_PPM_TEST_IDLE_STATE notification, the AcceptProcessorNotification routine is called with interrupts disabled.
 
## PEP_NOTIFY_PPM_IDLE_PRE_EXECUTE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_IDLE_PRE_EXECUTE.

Data
A pointer to a PEP_PPM_IDLE_EXECUTE or PEP_PPM_IDLE_EXECUTE_V2 structure.
 Sent to the PEP to prepare the system to transition to the specified idle state.

The Windows power management framework (PoFx) sends this notification to the PEP to prepare the system to transition to the specified idle state. Upon successful completion of this notification, the OS will transition the processor into idle by entering the associated C-state. If the PEP is unable to prepare the system to enter the processor (and platform) idle state, then it must return back an error status. 

When the hypervisor is enabled, the PEP will only receive this notification upon entry to a platform idle state, and with the ProcessorState field set to PEP_PROCESSOR_IDLE_STATE_UNKNOWN. 

When using the coordinated idle state interface, the OS uses the PEP_PPM_IDLE_EXECUTE_V2 structure which includes the CoordinatedStateCount and CoordinatedState fields with the list of coordinated idle states that will be entered by the idle transition. The PlatformState field will specify the deepest platform coordinated idle state that's being entered, if any. 

When not using the coordinated idle state interface, the OS uses the PEP_PPM_IDLE_EXECUTE structure. 

For a PEP_NOTIFY_PPM_IDLE_PRE_EXECUTE notification, the AcceptProcessorNotification routine is called with interrupts disabled and is always executed on the target processor.
 
## PEP_NOTIFY_PPM_UPDATE_PLATFORM_STATE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_UPDATE_PLATFORM_STATE.

Data
A pointer to a PEP_PPM_QUERY_PLATFORM_STATE structure.
 Informs the PEP that a processor has received Notify(0x81) to update the characteristics of a platform idle state.

The Windows power management framework (PoFx) sends this notification when a processor has received Notify(0x81) to update the characteristics of a platform idle state. This notification is sent once for each platform idle state. If the PEP does not accept the notification (i.e. returns FALSE from its AcceptProcessorNotification callback), then the prior definition of the platform idle state, from the most recently accepted PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE or PEP_NOTIFY_PPM_UPDATE_PLATFORM_STATE notification, is preserved. 

This notification uses the same Data buffer as the PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE notification. 

For a PEP_NOTIFY_PPM_UPDATE_PLATFORM_STATE notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE_RESIDENCIES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE_RESIDENCIES.

Data
A pointer to a PEP_PPM_PLATFORM_STATE_RESIDENCIES structure.
 Informs the PEP that it should capture the actual accumulated time spent in each platform idle state since boot.

The Windows power management framework (PoFx) sends this notification to the PEP to capture the actual accumulated time spent in each platform idle state since boot. As such, this query is only applicable to platforms where the underlying hardware may autonomously decide to enter a platform idle state different from that requested by the OS. The values returned are used for diagnostic purposes and identify when the OS's view of platform idle state residency differs significantly from what the platform actually achieved. 

Count specifies the number of elements in the States array, where the element index corresponds to platform idle state index. The PEP will fill each element with the matching state's actual residency and transition count. 


Note  The accumulated values captured by this query should correspond only to those periods where the PEP (or processor driver) actually executed a platform idle state transition. This will ensure that the comparison between OS calculated residency and actual residency is meaningful.
 

For a PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE_RESIDENCIES notification, the AcceptProcessorNotification routine can be called at any IRQL.
 
## PEP_NOTIFY_PPM_QUERY_VETO_REASONS 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_VETO_REASONS.

Data
A pointer to a PEP_PPM_QUERY_VETO_REASONS structure.
 Used to query the number of unique veto reasons that the PEP uses in the ProcessorIdleVeto and PlatformIdleVeto callbacks. 

The Windows power management framework (PoFx) sends this notification at processor initialization to query the number of unique veto reasons that the PEP uses in the ProcessorIdleVeto and PlatformIdleVeto callbacks. This notification is optional, and may be ignored by the PEP. 

If accepted, the PEP is allowed to use the veto reasons between 1 and VetoReasonCount, inclusive, to veto any processor, platform, or coordinated idle state. The PEP is not allowed to use veto reasons greater than VetoReasonCount. The OS will pre-allocate veto tracking structures, and when used with PEP_NOTIFY_PPM_ENUMERATE_BOOT_VETOES, guarantees that all processor, platform, and coordinated state veto callbacks will succeed.

If this notification is not accepted by the PEP, the PEP may use the ProcessorIdleVeto and PlatformIdleVeto callbacks with any legal veto reason. The OS does not guarantee that the callbacks will not fail due to allocation failures or other issues.

For a PEP_NOTIFY_PPM_QUERY_VETO_REASONS notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_VETO_REASON 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_VETO_REASON.

Data
A pointer to a PEP_PPM_QUERY_VETO_REASON structure.
 Sent to the PEP to query for information about a specific veto reason.

The Windows power management framework (PoFx) sends this notification at processor initialization to query for information about a specific veto reason. This notification is sent twice for each veto reason, once with a NULLName buffer to retrieve the allocation size needed for Name, and once with a non-NULLName buffer to fill in the contents of Name. The name should be a human-readable string indicating what condition this veto reason represents. Debugging tools such as WPA and the kernel debugger will display Name when diagnosing why an idle state was not entered. 

For a PEP_NOTIFY_PPM_QUERY_VETO_REASON notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_ENUMERATE_BOOT_VETOES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_ENUMERATE_BOOT_VETOES.

Data
The NULL pointer value.
 Informs the PEP that the OS is ready to accept calls to ProcessorIdleVeto or PlatformIdleVeto. 

The Windows power management framework (PoFx) sends this notification after processor initialization but before first idle entry to indicate that the OS is ready to accept calls to ProcessorIdleVeto or PlatformIdleVeto. The PEP may enumerate any boot-time vetoes in the context of this notification, and the OS guarantees that they will take effect before the first attempt to select a processor, platform, or coordinated idle state. This notification has no associated Data parameter. 

For a PEP_NOTIFY_PPM_ENUMERATE_BOOT_VETOES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_PARK_MASK 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_PARK_MASK.

Data
A pointer to a PEP_PPM_PARK_MASK structure.
 Informs the PEP of the current core parking mask.

The Windows power management framework (PoFx) sends this notification at runtime to inform the PEP of the current core parking mask.

For a PEP_NOTIFY_PPM_PARK_MASK notification, the AcceptProcessorNotification routine is called at IRQL = DISPATCH_LEVEL and may be sent while executing on any processor.

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_PARK_SELECTION_V2 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_PARK_SELECTION_V2.

Data
A pointer to a PEP_PPM_PARK_SELECTION_V2 structure.
 Informs the PEP that the OS would like it to select a preferred set of cores to park or steer interrupts away from. If this notification is not accepted, the OS will fall back to sending the PEP_NOTIFY_PPM_PARK_SELECTION notification.

When running its performance check algorithm, the OS may send the PEP_NOTIFY_PPM_PARK_SELECTION_V2 notification multiple times: zero or more times for each core efficiency class within each park domain, and zero or more times for interrupt steering. To assist the PEP in providing a consistent response to the OS for a performance check, the OS will supply the interrupt time based timestamp of the performance check evaluation that prompted the notification. All park selection notifications resulting from one performance check evaluation will have the same timestamp. Note that the remaining fields (Count, AdditionalUnparkedProcessors, EvaluationType, and Processors) may vary for notifications that are sent during the same performance check evaluation, the PEP cannot assume that they will remain the same. 

For a PEP_NOTIFY_PPM_PARK_SELECTION notification, the AcceptProcessorNotification routine is always called at IRQL = DISPATCH_LEVEL.

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_PERF_CHECK_COMPLETE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_PERF_CHECK_COMPLETE.

Data
A pointer to a PEP_PPM_PERF_CHECK_COMPLETE structure.
 Informs the PEP that the periodic performance check evaluation has completed.

The Windows power management framework (PoFx) sends this notification at runtime to notify the PEP that the periodic per check evaluation has completed.

For a PEP_NOTIFY_PPM_PERF_CHECK_COMPLETE notification, the AcceptProcessorNotification routine is called at IRQL = DISPATCH_LEVEL and may be sent while executing on any processor.

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_COORDINATED_DEPENDENCY 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_COORDINATED_DEPENDENCY.

Data
A pointer to a PEP_PPM_QUERY_COORDINATED_DEPENDENCY structure.
 Sent to the PEP to query for the dependencies of each coordinated idle state.

The Windows power management framework (PoFx) sends this notification at processor initialization to query the PEP for the dependencies of each coordinated idle state. The OS will allocate MaximumDependencySize elements for the Dependencies array. The PEP must fill in the number of elements of the array that were used in DependencySizeUsed.

If the dependency being expressed is on a processor, PEP fills in the TargetProcessor field with the POHANDLE of the target processor. The ExpectedState field then refers to the index of a processor idle state on the target processor. 

If the dependency being expressed is on other coordinated idle states, PEP fills in NULL for the TargetProcessor. The ExpectedState field then refers to the index of a coordinated idle state. 

Each dependency lists a menu of options the OS is allowed to use to satisfy the dependency. When going idle, the OS will attempt to satisfy the dependency by checking the conditions for each, from highest index to lowest index. If the conditions for a dependency are met, then the OS will consider the dependency met. If none of the conditions can be met, the dependency is not met and the coordinated idle state may not be entered.

For a PEP_NOTIFY_PPM_QUERY_COORDINATED_DEPENDENCY notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_COORDINATED_STATE_NAME 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_COORDINATED_STATE_NAME.

Data
A pointer to a PEP_PPM_QUERY_STATE_NAME structure.
 Sent to the PEP to query for information about a specific coordinated or platform idle state.

The Windows power management framework (PoFx) sends this notification at processor initialization to query the PEP for information about a specific coordinated or platform idle state. This notification is sent twice for each state, once with a NULL Name buffer to retrieve the allocation size needed for Name, and once with a non-NULL Name buffer to fill in the contents of Name. The name should be a human-readable string indicating the name of the coordinated idle state. Coordinated idle states should have unique names, except on multi-cluster systems, where the names of equivalent states on different clusters may be the same. Debugging tools such as WPA and the kernel debugger will display Name in diagnostics that refer to this coordinated/platform idle state.

For a PEP_NOTIFY_PPM_QUERY_COORDINATED_STATE_NAME notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_COORDINATED_STATES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_COORDINATED_STATES.

Data
A pointer to a PEP_PPM_QUERY_COORDINATED_STATES structure.
 Used at processor initialization to query for the properties of all coordinated idle states.

The Windows power management framework (PoFx) sends this notification to the PEP at processor initialization to query for the properties of all coordinated idle states. This notification is sent just before the PEP would have sent the PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE notification. If accepted, the PEP is using the coordinated idle state interface and will not receive any PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE notifications. If not accepted, the PEP is using the platform idle state interface and the OS will fall back to using the PEP_NOTIFY_PPM_QUERY_PLATFORM_STATE notification to query for coordinated idle states. 

The OS will wait to send this notification until after all processors have registered with the PEP. 

The PEP fills in the State structure with information about the coordinated idle states.

The order of coordinated idle states must follow the following rules: 

Two coordinated states that represent different power states for the same functional unit should be listed in order from lightest (most power consumption/least transition cost) to deepest (least power consumption/most transition cost). 
Coordinated idle states may only depend on other coordinated idle states with a lower index. 
There is not required order between two disjoint coordinated idle states (that is, two coordinated idle states that depend on disjoint sets of processors).

For a PEP_NOTIFY_PPM_QUERY_COORDINATED_STATES notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_PROCESSOR_STATE_NAME 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_PROCESSOR_STATE_NAME.

Data
A pointer to a PEP_PPM_QUERY_STATE_NAME structure.
 Sent to the PEP to query for information about a specific processor idle state.

The Windows power management framework (PoFx) sends this notification at processor initialization to query the PEP for information about a specific processor idle state. This notification is sent twice for each state, once with a NULL Name buffer to retrieve the allocation size needed for Name, and once with a non-NULL Name buffer to fill in the contents of Name. The name should be a human-readable string indicating the name of the coordinated idle state. Coordinated idle states should have unique names, except on multi-cluster systems, where the names of equivalent states on different clusters may be the same. Debugging tools such as WPA and the kernel debugger will display Name in diagnostics that refer to this coordinated/platform idle state.

For a PEP_NOTIFY_PPM_QUERY_PROCESSOR_STATE_NAME notification, the AcceptProcessorNotification routine is always called at IRQL = PASSIVE_LEVEL.

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_ENTER_SYSTEM_STATE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_ENTER_SYSTEM_STATE.

Data
A pointer to a PEP_PPM_ENTER_SYSTEM_STATE structure.
 PEP_NOTIFY_PPM_ENTER_SYSTEM_STATE is an optional notification that notifies the PEP that the system is about to enter a system power state. This notification is sent to all processors simultaneously after the system has completed all passive level work transitioning the processor to the system power state.  

This notification is sent at DISPATCH_LEVEL, with all processors at dispatch. This notification is always executed on the target processor. 

Note  The PEP must not queue any work from this notification. The processors will not process work items, DPCs, etc. after this notification has been sent. 
 

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_PERF_SET_STATE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_PERF_SET_STATE.

Data
A pointer to a PEP_PPM_PERF_SET_STATE structure.
 Used at runtime to set the current operating performance state of the processor. If the PEP has autonomous hardware capable of boosting/reducing performance without a performance set request, it should limit the requests from autonomous hardware based on the minimum performance state and/or maximum performance state, and target the desired performance state. Otherwise, it should run at exactly the desired performance state.  

This notification is sent at DISPATCH_LEVEL. If scheduler directed performance states are in use, the PEP must adhere to the restrictions in section 3.3.6 when processing this notification. It may be sent while executing on any processor. 

DISPATCH_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_DISCRETE_PERF_STATES.

Data
A pointer to a PEP_PPM_QUERY_DISCRETE_PERF_STATES structure.
 Used at processor initialization to query for the list of discrete performance states that the PEP supports, if the PEP_NOTIFY_PPM_QUERY_CAPABILITIES notification indicates support for discrete performance states.  

The performance state list should be ordered from fastest to slowest, with each performance state mapping to a distinct performance value. The performance state list should also include an entry that matches each performance value listed in the PEP_NOTIFY_PPM_QUERY_PERF_CAPABILITIES notification.  This notification is sent at PASSIVE_LEVEL. It may be sent while executing on any processor. 

PASSIVE_LEVEL
 
## PEP_NOTIFY_PPM_QUERY_DOMAIN_INFO 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_QUERY_DOMAIN_INFO.

Data
A pointer to a PEP_PPM_QUERY_DOMAIN_INFO structure.
 An optional notification that queries for information about a performance domain.  This notification is sent at PASSIVE_LEVEL. It may be sent while executing on any processor.

PASSIVE_LEVEL

  
## PEP_NOTIFY_PPM_RESUME_FROM_SYSTEM_STATE 
Handle
A PEPHANDLE structure containing the device handle of the PEP for the target processor. If the notification does not target a specific processor, this will be NULL.

Notification
The value PEP_NOTIFY_PPM_RESUME_FROM_SYSTEM_STATE.

Data
A pointer to a PEP_PPM_RESUME_FROM_SYSTEM_STATE structure.
 An optional notification that notifies the PEP that the system has just resumed from a system power state. This notification is sent to all processors simultaneously just before processors are released to resume passive level work.  This notification is sent at DISPATCH_LEVEL, with all processors at dispatch. This notification is always executed on the target processor. 

DISPATCH_LEVEL
 

