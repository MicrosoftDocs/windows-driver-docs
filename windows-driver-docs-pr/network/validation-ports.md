---
title: Validation Ports
description: Validation Ports
ms.assetid: 67556275-EF02-4996-A3A2-E9D5D6FCD1AF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Validation Ports


Starting with NDIS 6.30 in Windows Server 2012, the extensible switch interface creates an operational port to host an extensible switch network adapter connection. Under certain conditions, the extensible switch interface creates a validation port before it creates the operational port for a Hyper-V child partition. The validation port is used to validate and verify settings for the operational port that will be connected to the extensible switch virtual machine (VM) network adapter of the child partition.

**Note**  In Hyper-V, a child partition is also known as a VM.

 

This validation port is created under the following conditions:

-   The VM is first created. Once the VM is powered on, the validation port is deleted and the operational port is created in its place.

-   The VM enters a saved state. When the VM is restored and powered on, the validation port is deleted and the operational port is created in its place.

    For more information, see [Hyper-V Extensible Switch Save and Restore Operations](hyper-v-extensible-switch-save-and-restore-operations.md).

-   The VM is stopped and powered down. Once the VM is powered on, the validation port is deleted and the operational port is created in its place.

-   The VM is being live migrated to another host computer. Once the VM is created and powered on in the new host computer, the validation port is deleted and the operational port is created in its place.

After the validation port is created, the extensible switch interface issues OID requests to download port policies for the port. Because these ports are created for policy validation and verification, such as when a VM is first configured, it is important that the validation that occurs is appropriate for configuration time rather than run time. Extensions should perform the following types of policy validation for these ports:

-   Syntax validation. This validation fails if the values are not properly formatted.

-   Range validation. This validation fails if the settings do not conform to the expected range of minimum and maximum values.

-   Applicability validation. This validation fails if the settings do not apply to the extensible switch. For example, a policy profile that defines an external network service-level agreement (SLA) would not apply to an extensible switch that does not have access to the external networking interface.

-   Conflict detection. The validation fails if the settings conflict with other settings that are already set on the same port.

When the extensible switch extension validates port and policy settings for a validation port, it must follow these guidelines:

-   Because the validation port is temporal, the extension must not validate and fail policy and configuration settings that cannot be currently satisfied by the extensible switch.

    For example, an extensible switch, which supports a maximum of 10 gigabits of bandwidth, may currently only have 1 gigabit of bandwidth available for reservation. The extension does not fail the validation of a port property that is reserving more than 1 gigabit of bandwidth. This kind of validation should instead occur when the operational port is created. This is because the settings that are being validated may still be applied to an operational port in which the bandwidth is available. This allows system administrators to initially configure VMs without being restricted by run-time constraints.

-   The extension must not allocate or reserve resources for the validation port. For example, bandwidth reservation settings on a validation port should not deduct from the available bandwidth of the extensible switch. Reservation should occur only when the operational port is created.

For more information on extensible switch operational ports, see [Operational Ports](operational-ports.md).

 

 





