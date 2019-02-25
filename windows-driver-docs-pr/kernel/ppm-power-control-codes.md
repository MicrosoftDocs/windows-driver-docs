---
title: PPM power control codes
description: The power control codes described in this topic are used by platform extension plug-ins (PEPs). 
ms.assetid: 4BA89D0F-78F0-44DF-BC9B-0F9F3256CD59
keywords: [PPM power control codes]
ms.date: 01/17/2018
ms.localizationpriority: medium
---

# PPM power control codes

The power control codes described in this topic are used by platform extension plug-ins (PEPs). A power control request is similar to an I/O control request (IOCTL). Unlike an IOCTL, however, a power control request is sent directly to the Window power management framework (PoFx) and is not observed by other device drivers in the device stack.

The following are the PPM power control codes:

|Code |Syntax |Description |
|---|---|---|
|PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE|<p> // {38BD8901-AB20-4908-ABAA-AC34674BDFF3}</p><p>DEFINE_GUID(PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE, </p><p>0x38bd8901, 0xab20, 0x4908, 0xab, 0xaa, 0xac, 0x34, 0x67, 0x4b, 0xdf, 0xf3);</p>| Code is used by the PEP to query the Windows power management framework (PoFx) for information about the parking page assigned to a processor. <p>To determine the parking page for a processor, the platform extension plug-in (PEP) for this processor submits a PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE power control request to PoFx.</p> <p>To initiate this power control request, the PEP first calls the RequestWorker routine to inform PoFx that the PEP has a work item to submit. PoFx responds to this call by sending a PEP_DPM_WORK notification to the PEP. The PEP responds by submitting a power control work request for the parking page information. This request includes a PEP-allocated PEP_WORK_INFORMATION structure in which the WorkType member is set to PepWorkRequestPowerControl, and the PowerControl member points to a PEP-allocated PEP_WORK_POWER_CONTROL structure. The PowerControlCode member of the PEP_WORK_POWER_CONTROL structure is set to PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE. The InBuffer member of this structure must be NULL, and the OutBuffer member must point to a PEP-allocated PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure. In response to this power control request, PoFx writes the virtual and physical addresses of the parking page to the PEP_PPM_CONTEXT_QUERY_PARKING_PAGE structure.</p><p>The PEP_PPM_POWER_CONTROL_QUERY_PARKING_PAGE power control request is ARM-specific and is not supported for x86 and x64 processors. In an ARM multiprocessor system, a parking page is a 4-kilobyte block of memory that the operating system uses as a mailbox to control a processor that is starting up from an idle state. A PEP might use some part of the mailbox to store processor-specific context data. For more information, see the document titled "Multiprocessor Startup for ARM Platforms" at https://www.acpica.org/related-documents.</p>|
|GUID_PPM_PERF_CONSTRAINT_CHANGE|<p> // {29181FA1-4BF3-4c2e-B314-A6D226322B00}</p><p>DEFINE_GUID(GUID_PPM_PERF_CONSTRAINT_CHANGE,</p><p>0x29181fa1, 0x4bf3, 0x4c2e, 0xb3, 0x14, 0xa6, 0xd2, 0x26, 0x32, 0x2b, 0x0);</p>|Code is used by the PEP to notify the Windows power management framework (PoFx) that the processor's performance limits must change to accommodate external constraints (power budgeting, thermal constraints, power source, and so on). <p>No input or output buffer is used with this control code.</p><p>To initiate this power control request, the PEP first calls the RequestWorker routine to inform PoFx that the PEP has a work item to submit. PoFx responds to this call by sending a PEP_DPM_WORK notification to the PEP. The PEP responds by submitting a power control work request for a performance constraint change. This request includes a PEP-allocated PEP_WORK_INFORMATION structure in which the WorkType member is set to PepWorkRequestPowerControl, and the PowerControl member points to a PEP-allocated PEP_WORK_POWER_CONTROL structure. The PowerControlCode member of the PEP_WORK_POWER_CONTROL structure is set to GUID_PPM_PERF_CONSTRAINT_CHANGE. Both the InBuffer and OutBuffer members of this structure must be NULL. In response to this power control request, PoFx will send a PEP_NOTIFY_PPM_PERF_CONSTRAINTS notification to the PEP to get the new processor performance limits.</p>
 

 

