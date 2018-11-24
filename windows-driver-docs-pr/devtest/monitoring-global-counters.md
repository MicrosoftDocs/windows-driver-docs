---
title: Monitoring Global Counters
description: Monitoring Global Counters
ms.assetid: ca8f2b87-bb62-4389-bd59-1ed8ef6ac730
keywords:
- global counters WDK Driver Verifier
- Driver Verifier WDK , counters
- statistics WDK Driver Verifier
- counters WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitoring Global Counters


## <span id="ddk_monitoring_global_counters_tools"></span><span id="DDK_MONITORING_GLOBAL_COUNTERS_TOOLS"></span>


*Global counters* are statistics that monitor some of the actions that Driver Verifier performs on drivers. These statistics are drawn from all drivers being verified.

Global counters can be viewed by using the [**Verifier Command Line**](verifier-command-line.md), or by using Driver Verifier Manager. There are two versions of Driver Verifier Manager -- one for [Windows 2000](driver-verifier-manager--windows-2000-.md) and one for [Windows XP and later](driver-verifier-manager--windows-xp-and-later-.md).

### <span id="verifier_command_line"></span><span id="VERIFIER_COMMAND_LINE"></span>Verifier Command Line

To view global counters, use the **verifier /query** command. This will show both global counters and [individual counters](monitoring-individual-counters.md).

Global counters are also included in Driver Verifier [log files](creating-log-files.md).

### <span id="driver_verifier_manager__windows_2000_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_2000_"></span>Driver Verifier Manager (Windows 2000)

To view global counters, select the **Global Counters** tab. This tab includes almost all of the global counters. (However, the **Not Tracked Allocations** counter is on the **Pool Tracking** screen, and the 95% special pool alert is on the **Driver Status** screen, as described immediately below.)

### <span id="driver_verifier_manager__windows_xp_and_later_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_XP_AND_LATER_"></span>Driver Verifier Manager (Windows XP and later)

To view global counters, start Driver Verifier Manager and select the **Display information about the currently verified drivers** task. Then press **Next** twice.

### <span id="explanation_of_global_counters"></span><span id="EXPLANATION_OF_GLOBAL_COUNTERS"></span>Explanation of Global Counters

The following global counters monitor statistics related to the [Force IRQL Checking](force-irql-checking.md) option. These counters include actions performed since the last boot by all kernel-mode drivers that are currently being verified.

<span id="IRQL_Raises"></span><span id="irql_raises"></span><span id="IRQL_RAISES"></span>**IRQL Raises**  
The number of times verified drivers raised the IRQL.

<span id="Spinlocks_Acquired"></span><span id="spinlocks_acquired"></span><span id="SPINLOCKS_ACQUIRED"></span>**Spinlocks Acquired**  
The number of times verified drivers acquired spin locks.

<span id="Executions_Synchronized"></span><span id="executions_synchronized"></span><span id="EXECUTIONS_SYNCHRONIZED"></span>**Executions Synchronized**  
The number of times verified drivers synchronized the execution of a given routine with the ISR associated with a given interrupt object pointer.

<span id="Trims"></span><span id="trims"></span><span id="TRIMS"></span>**Trims**  
The number of times Driver Verifier trimmed pageable memory from the working set. (Note that this is the number of trimming passes made by Driver Verifier, not the number of pages trimmed.)

The following global counter monitors a statistic related to the [Low Resources Simulation](low-resources-simulation.md) option.

<span id="Faults_Injected"></span><span id="faults_injected"></span><span id="FAULTS_INJECTED"></span>**Faults Injected**  
The total number of resource allocations failed deliberately by Driver Verifier since the last boot.

The following global counters monitor statistics related to the [Special Pool](special-pool.md) option. These counters always reflect the allocations attempted since the last boot by all kernel-mode drivers that are currently being verified.

<span id="Pool_Allocations_Attempted"></span><span id="pool_allocations_attempted"></span><span id="POOL_ALLOCATIONS_ATTEMPTED"></span>**Pool Allocations Attempted**  
The total number of memory allocations attempted by these drivers.

<span id="Pool_Allocations_Succeeded"></span><span id="pool_allocations_succeeded"></span><span id="POOL_ALLOCATIONS_SUCCEEDED"></span>**Pool Allocations Succeeded**  
The number of allocation attempts that succeeded.

<span id="Pool_Allocations_Succeeded_in_Special_Pool"></span><span id="pool_allocations_succeeded_in_special_pool"></span><span id="POOL_ALLOCATIONS_SUCCEEDED_IN_SPECIAL_POOL"></span>**Pool Allocations Succeeded in Special Pool**  
The number of allocation attempts that succeeded, and were assigned from the special pool.

<span id="Pool_Allocations_Without_Tag"></span><span id="pool_allocations_without_tag"></span><span id="POOL_ALLOCATIONS_WITHOUT_TAG"></span>**Pool Allocations Without Tag**  
The number of times these drivers requested memory allocations but did not supply a pool tag. (Pool tags are always recommended for every allocation.)

<span id="Pool_Allocations_Failed"></span><span id="pool_allocations_failed"></span><span id="POOL_ALLOCATIONS_FAILED"></span>**Pool Allocations Failed**  
The number of allocation attempts that failed, due to lack of memory.

If the Special Pool feature is enabled, but less than 95% of all pool allocations have been assigned from the special pool, a warning will appear. In Windows XP and later, this warning will appear in a dialog box on the **Global Counters** screen. In Windows 2000, this warning will appear on the **Driver Status** screen.

The following global counter monitors a statistic related to the [Special Pool](special-pool.md) and [Pool Tracking](pool-tracking.md) options. It will always be zero if Pool Tracking is not active.

<span id="Pool_Allocations_Not_Tracked"></span><span id="pool_allocations_not_tracked"></span><span id="POOL_ALLOCATIONS_NOT_TRACKED"></span>**Pool Allocations Not Tracked**  
The number of untracked allocations from all drivers currently being verified. Allocations whose size is one page or larger are not tracked by Pool Tracking and cannot be allocated from the special pool. The [individual counters](monitoring-individual-counters.md) do not reflect these allocations. (In Windows 2000, this counter can be found on the **Pool Tracking** screen under the title **Not Tracked Allocations**.)

 

 





